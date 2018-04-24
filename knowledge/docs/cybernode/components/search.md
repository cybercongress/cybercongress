# Search Components

| Component                  | Scale | Description                                        |  Cluster Address              | Metrics                   | External |
| -------------------------- | ----- |--------------------------------------------------- | --------------------------    | ------------------------  | -------- |
| Kafka                      | 1     | Data Entry                                         |                               |                           |          |
| Kafka Manager              | 1     | Kafka Explorer                                     |                               |                           |          |
| Elassandra                 | 1 - N | Data Back And Search                               | elassandra.search.svc:9042    |                           |          |
| Ethereum Pump              | 1     | Ethereum Chain Data Kafka Pump                     |                               | 8080:/actuator/metrics    |          |
| Ethereum Cassandra Dump    | 1     | Dump Kafka Topics Into Cassandra                   |                               | 8080:/actuator/metrics    |          |
| Ethereum Contract Summary  | 1 - N | Calculates Contract Summaries (balances and etc)   |                               | 8080:/actuator/metrics    |          |
| Search Api                 | 1 - N | Api To Search Chain Entities                       | search-api.search.svc:80      | 8080:/actuator/metrics    |   y      |
| Search Api Docs            | 1 - N | Search Api Docs Based On Swagger                   | search-api-docs.search.svc:80 |                           |   y      |

![Basic Overview](/img/search/architecture.png)

## Kafka
[Kafka](https://kafka.apache.org/) is message queue used as main data entry. All raw data firstly goes into kafka, than 
 various services consume it to provide new functionality.
 
## Elassandra (Elastic + Cassandra)
[Elassandra](https://github.com/strapdata/elassandra) is used as main backend storage with linear growth fulltext-search
 index on source cassandra data.
 
## Ethereum Pump
Pumps Ethereum raw data(block,tx,uncles) into Kafka.

## Ethereum Cassandra Dump
Consumes Ethereum raw data from Kafka topics, translate it into cassandra entities and store them into Elassandra.

## Ethereum Contract Summary 
Collects summary for each contract stored in Ethereum chain. Consumes Kafka topics and update data in Elassandra.