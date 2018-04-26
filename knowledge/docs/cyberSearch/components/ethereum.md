# Ethereum Components

| Component                  | Scale | Description                                        |  Cluster Address              | Metrics                   | External |
| -------------------------- | ----- |--------------------------------------------------- | --------------------------    | ------------------------  | -------- |
| Ethereum Pump              | 1     | Ethereum Chain Data Kafka Pump                     |                               | 8080:/actuator/metrics    |          |
| Ethereum Cassandra Dump    | 1     | Dump Kafka Topics Into Cassandra                   |                               | 8080:/actuator/metrics    |          |
| Ethereum Contract Summary  | 1 - N | Calculates Contract Summaries (balances and etc)   |                               | 8080:/actuator/metrics    |          |

 
## Ethereum Pump
Pumps Ethereum raw data(block,tx,uncles) into Kafka.

## Ethereum Cassandra Dump
Consumes Ethereum raw data from Kafka topics, translate it into cassandra entities and store them into Elassandra.

## Ethereum Contract Summary 
Collects summary for each contract stored in Ethereum chain. Consumes Kafka topics and update data in Elassandra.