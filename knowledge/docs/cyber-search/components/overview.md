# Search Common Components

| Component                  | Scale | Description                                        |  Cluster Address              | Metrics                   | External |
| -------------------------- | ----- |--------------------------------------------------- | --------------------------    | ------------------------  | -------- |
| Kafka                      | 1     | Data Entry                                         |                               |                           |          |
| Kafka Manager              | 1     | Kafka Explorer                                     |                               |                           |          |
| Elassandra                 | 1 - N | Data Back And Search                               | elassandra.search.svc:9042    |                           |          |
| Search Api                 | 1 - N | Api To Search Chain Entities                       | search-api.search.svc:80      | 8080:/actuator/metrics    |   y      |
| Search Api Docs            | 1 - N | Search Api Docs Based On Swagger                   | search-api-docs.search.svc:80 |                           |   y      |

![Basic Overview](images/architecture.png)

## Chains Components
- [Ethereum](ethereum-components.md)
- [Bitcoin](bitcoin-components.md)

## Kafka
[Kafka](https://kafka.apache.org/) is message queue used as main data entry. All raw data firstly goes into kafka, than 
 various services consume it to provide new functionality.
 
## Elassandra (Elastic + Cassandra)
[Elassandra](https://github.com/strapdata/elassandra) is used as main backend storage with linear growth fulltext-search
 index on source cassandra data.
 
## Search Api
Main search access endpoint. See [api calls documentations](http://docs.cybersearch.io).
