# Cassandra Service

## Usage of cassandra-service Module

Сassandra service module could be used in two ways:

1. With specifying `CHAIN_FAMILY` environment variable
2. Without specifying `CHAIN_FAMILY` environment variable

### Specifying `CHAIN_FAMILY`

When you're specifying `CHAIN_FAMILY` environment variable cassandra-service module will work in the context of one keyspace based on this family.
For example if `CHAIN_FAMILY=BITCOIN` it will create `bitcoin` keyspace if it doesn't exists and do all migrations for this keyspace if they're not applied.
In spring context only repositories beans related to this keyspace will be available 

All of the cassandra work handled by `CassandraRepositoriesConfiguration` and it specific inheritor.

This kind of interaction with cassandra-service used in dumps and contract summaries modules.

### Without `CHAIN_FAMILY`

Without specifying `CHAIN_FAMILY` environment variable cassandra-service module will act like this:

1. It will run no migrations and creations of keyspaces
2. It will look on available keyspaces in current cassandra database based on `SearchRepositoriesConfiguration` inheritors
 and if they're exists it will initialize all repositories beans for this keyspaces and put them into spring context. 

This is useful when you want to interact with all of available keyspaces and indicies.
For example in search-api module we need all of repositories beans to build requests.