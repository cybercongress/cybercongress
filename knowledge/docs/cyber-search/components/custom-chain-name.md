# Custom Chain Name

You have an ability to run our services with custom chain name based on supported chain families.
It may be needed if you have your own custom chain and you want API endpoints, Kafka topic names and Cassandra keyspaces to use your chain name.
Currently we're supporting `BITCOIN` and `ETHEREUM` chain families.

To make it work you need to define `CHAIN_NAME` environment variable along with `CHAIN_FAMILY`.
Also you may need to define your chain node url in PUMP by setting `CHAIN_NODE_URL` environment variable.

For example if you want to index `ETHEREUM` based chain called `MY_PRECIOUS`.
You have to use following config in all services (`CHAIN_NODE_URL` is necessary only for PUMP service):

```groovy
CHAIN_FAMILY = ETHEREUM
CHAIN_NAME = MY_PRECIOUS
CHAIN_NODE_URL = https://my_precious_node_url:port
```

Then all Kafka topics will be named as `MY_PRECIOUS_TX_PUMP`,`MY_PRECIOUS_BLOCK_PUMP`,`MY_PRECIOUS_UNCLE_PUMP`. Cassandra keyspace will be named `my_precious`.
And all API url will be build like this `http://localhost:8080/my_precious/block/42` and etc.