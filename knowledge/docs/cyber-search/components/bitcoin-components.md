# Bitcoin Components

| Component                 | Scale | Description                                        |  Cluster Address              | Metrics                   | External |
| ------------------------- | ----- |--------------------------------------------------- | --------------------------    | ------------------------  | -------- |
| Bitcoin Pump              | 1     | Bitcoin Chain Data Kafka Pump                      |                               | 8080:/actuator/metrics    |          |
| Bitcoin Cassandra Dump    | 1     | Dump Kafka Topics Into Cassandra                   |                               | 8080:/actuator/metrics    |          |
| Bitcoin Contract Summary  | 1 - N | Calculates Contract Summaries (balances and etc)   |                               | 8080:/actuator/metrics    |          |

 
## Bitcoin Pump
Pumps Bitcoin raw data(block,tx,uncles) into Kafka.

## Bitcoin Cassandra Dump
Consumes Bitcoin raw data from Kafka topics, translate it into cassandra entities and store them into Elassandra.

## Bitcoin Contract Summary 
Collects summary for each contract stored in Bitcoin chain. Consumes Kafka topics and update data in Elassandra.