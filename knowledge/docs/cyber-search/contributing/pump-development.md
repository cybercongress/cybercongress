# Pump Development Guide

To develop your own chain pump you have two deal with two modules:
* common
* pumps

## Some explanations

To describe single chain in our system we're using following scheme.

Every chain has `ChainFamily`. For example `BITCOIN, ETHEREUM` families.

`ChainFamily` has it's own set of entities like `TX, BLOCK, UNCLE` and default url of chain node.

Next, chain has a name. Chain name used everywhere in modules. Kafka topics, Cassandra keyspaces, API endpoints
will be based on chain name. By default chain name is equal to `ChainFamily`. For example if you have  `ChainFamily == BITCOIN`
and you not specifying a chain name it will be set to `BITCOIN`. Main goal of chain name is to separate forks
of one chain that have the same structure. For example  `BITCOIN` and `BITCOIN_CASH` or `ETHEREUM` and `ETHEREUM_CLASSIC`. 

So as far as you can understand single chain pump is chain pump for specific `ChainFamily`
## Adding models to common module

First of all you have to put models representing your blockchain entities in common module.
They should be placed in `fund.cyber.search.model.{your_chain_family_name}` package.
This models will be used to transfer your blockchain data among our microservices (using Kafka).

After doing so put description of your chain family to `ChainFamily` enum.
You could find it in `fund.cyber.search.model.chains.ChainInfo.kt` file. Description includes following info:

* `defaultNodeUrl` - default URL of blockchain node to connect for data.
* `entityTypes` - map of blockchain entities types (from `fund.cyber.search.model.chains.ChainEntity` enum) to their class representation.

If you can't find needed entity type in `fund.cyber.search.model.chains.ChainEntity` enum you have to add it by your own.
## Developing pump

Now you're ready to write pump for your chain family. Note that this pump is suitable only for block based chains.

We're using Spring Boot (https://projects.spring.io/spring-boot/). So you also should be familiar with spring beans, spring dependency injection and spring configuration.

### Creating gradle module
To start with, create new Gradle submodule with name of your chain in `pumps` module. Include your module in `pumps/build.gradle` and in `settings.gradle`.

Example of `pumps/build.gradle` file with your module:

```groovy
project(":pumps:common") {

    apply plugin: "io.spring.dependency-management"
    jar.archiveName = "common-pumps"

    dependencies {
        ...
    }
}

...

project(":pumps:{your_module_name}") {

    apply plugin: "org.springframework.boot"

    dependencies {

        compile project(":pumps:common")

        //your module dependencies
    }
}

...
```
Example of `settings.gradle` file:
```groovy
include "common"
include "common-kafka"
include "cassandra-service"

...

include "pumps:common"
include "pumps:bitcoin"
include "pumps:ethereum"
include "pumps:{your_chain_name}"

...
```

All classes should be placed under `fund.cyber.pump.{your_chain_name}` package (except main class).

### Creating spring boot main class

The next step is creating spring boot main class. It should be placed in your module under `fund.cyber` package.

Example of main class:
```kotlin
@SpringBootApplication(exclude = [KafkaAutoConfiguration::class])
class BitcoinPumpApplication {

    companion object {
        @JvmStatic
        fun main(args: Array<String>) {

            val application = SpringApplication(BitcoinPumpApplication::class.java)
            application.runPump(args)
        }
    }
}
```

### Default spring beans in context
After spring context start you'll have few already configured beans in context that you could inject in your module classes:

* `org.springframework.retry.support.RetryTemplate` - Spring Retry template for retrying failed operations.
* `io.micrometer.core.instrument.MeterRegistry` - bean for monitoring.
* `fund.cyber.search.model.chains.ChainInfo` - bean with all needed properties of running chain.

```kotlin
class ChainInfo(
    val family: ChainFamily,
    val name: String = "",
    val nodeUrl: String = family.defaultNodeUrl
) {

    val fullName
        get() = family.name + if (name.isEmpty()) "" else "_$name"

    val entityTypes
        get() = family.entityTypes.keys

    fun entityClassByType(type: ChainEntityType) = family.entityTypes[type]
}
```

`ChainInfo` bean constructed from environment properties at start:
* `CHAIN_FAMILY` - chain family name (matches `ChainFamily` enum). For example `CHAIN_FAMILY=BITCOIN`. **Required option**.
* `CHAIN_NAME` - name of your specific chain. **Not necessary**. By default equals to `CHAIN_FAMILY`.
All kafka topic will be named accordingly. For example `CHAIN_NAME=BITCOIN_CASH` then a topic name will be `BITCOIN_CASH_TX_PUMP`.
* `CHAIN_NODE_URL` - URL of node running your chain. **Not necessary**. By default will be equal to one that described in your `ChainFamily`.

### Implementing pump
To integrate your pump with our system you simply have to implement two interfaces:
* `fund.cyber.pump.common.node.BlockBundle`

```kotlin
/**
 * Blockchain block with all dependent entities. Should collect all entities in scope of one block.
 * For example: transactions, uncles, etc..
 */
interface BlockBundle {
    /**
     * Hash of the block
     */
    val hash: String
    /**
     * Hash of the parent block
     */
    val parentHash: String
    /**
     * Number of the block in blockchain
     */
    val number: Long
    /**
     * Size of the block in bytes
     */
    val blockSize: Int

    /**
     * Get dependent entity values list by entity type.
     *
     * @param chainEntityType type of entity (for example: [ChainEntityType.TX])
     * @return list of entity values (for example: transactions)
     */
    fun entitiesByType(chainEntityType: ChainEntityType): List<ChainEntity>
}
```

* `fund.cyber.pump.common.node.BlockchainInterface`
```kotlin
/**
 * Interface representing blockchain
 *
 * @param T block bundle of this blockchain
 */
interface BlockchainInterface<out T : BlockBundle> {
    /**
     * Get last number of the block in blockchain network.
     *
     * @return block number
     */
    fun lastNetworkBlock(): Long

    /**
     * Get [BlockBundle] by block number.
     *
     * @param number block number
     * @return block bundle
     */
    fun blockBundleByNumber(number: Long): T
}
```

Also you should define spring bean of `fund.cyber.pump.common.node.BlockchainInterface` implementation either by annotate it with `@Component` or defining `@Bean` in spring configuration.

For example:
```kotlin
@Component
class BitcoinBlockchainInterface(
        ...
) : BlockchainInterface<BitcoinBlockBundle> {

    private val downloadSpeedMonitor = monitoring.timer("pump_bundle_download")

    override fun lastNetworkBlock(): Long = bitcoinJsonRpcClient.getLastBlockNumber()

    override fun blockBundleByNumber(number: Long): BitcoinBlockBundle {
        return downloadSpeedMonitor.recordCallable {
            val block = bitcoinJsonRpcClient.getBlockByNumber(number)!!
            return@recordCallable rpcToBundleEntitiesConverter.convertToBundle(block)
        }
    }
}
```

So, as you can see, you're not care of what happening with data next and how to store it. All you need is just to tell `BlockBundle` how to map it's fields on entities and we'll take care of everything else.

Note that you should use `toSearchHashFormat()` extension function placed in `fund.cyber.api.common.Func.kt` on all fields in hex format when building your chain entities.

### Memory Pool Pump

You also could add memory pool pumping logic by simply implement `PoolInterface` interface

```kotlin
interface PoolInterface<T: PoolItem> {
    fun subscribePool(): Flowable<T>
}
``` 

It contains only one method that should return `io.reactivex.Flowable` of pool items.

### Create Dockerfile
Put Docker file in root folder of your module. Here is template of Dockerfile:
```
# Build Stage
# Container with application
FROM openjdk:8-jre-slim
COPY /build/libs /cyberapp/bin
ENTRYPOINT exec java $JAVA_OPTS -jar /cyberapp/bin/${your_chain_name}.jar
```

### Update CI

Finally, you should update `.circleci/config.yml` file with steps for building and pushing docker image.
* Add deploy job to `jobs` section. Template:
```
deploy_chain_pumps_${your_chain_name}_image:
     <<: *defaults
     steps:
       - attach_workspace:
           at: ~/build
       - setup_remote_docker:
           version: 17.11.0-ce
       - run:
           name: Build ${your_chain_name} Pump Image
           command: |
             docker build -t build/pump-${your_chain_name} -f ./pumps/${your_chain_name}/Dockerfile ./pumps/${your_chain_name}
             docker login -u $DOCKER_USER -p $DOCKER_PASS
             docker tag build/pump-${your_chain_name} cybernode/chain-pump-${your_chain_name}:$CIRCLE_TAG
             docker push cybernode/chain-pump-${your_chain_name}:$CIRCLE_TAG
             docker tag build/pump-${your_chain_name} cybernode/chain-pump-${your_chain_name}:latest
             docker push cybernode/chain-pump-${your_chain_name}:latest
```
* Add deploy job to `workflows.search_build.jobs` section. Template:
```
- deploy_chain_pumps_${your_chain_name}_image:
  <<: *release_filter
  requires:
    - build_project
```