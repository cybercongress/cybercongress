# Components requirements

Resources requirements to run components in gcloud cluster

| Component                  | Min CPU | Max CPU  |  Min RAM  | Max RAM |
| -------------------------- | ------- |--------- | -------   | --------|
| Kafka Broker               | 1.5     | 2        | 10GB      | 10GB    |
| Kafka Exporter             | 0.1     | 0.2      | 1GB       | 2GB     |
| Kafka Manager              | 0.1     | 0.2      | 1GB       | 2GB     |
| Zoo Keeper                 | 0.1     | 0.2      | 1.25GB    | 1.25GB  |
| Elassandra                 | 3.5     | 3.5      | 55GB      | 55GB    |
| Grafana                    | 0.1     | 0.2      | 100MB     | 200MB   |
| Prometheus                 | 0.25    | 1        | 3GB       | 3GB     |
| Prometheus Operator        | 0.1     | 0.2      | 100MB     | 200MB   |
| Parity ETH                 | 3       | 3        | 15GB      | 20GB    |
| Parity ETC                 | 1       | 1.5      | 10GB      | 15GB    |
| ETH Pump                   | 1.5     | 3        | 5GB       | 6GB     |
| ETH Cassandra Dump         | 1.5     | 3        | 3.75GB    | 3.75GB  |
| ETH Contract Summary       | 1.5     | 3        | 3.75GB    | 3.75GB  |
| ETC Pump                   | 1.5     | 3        | 3.75GB    | 3.75GB  |
| ETC Cassandra Dump         | 1.5     | 3        | 3.75GB    | 3.75GB  |
| ETC Contract Summary       | 1.5     | 3        | 3.75GB    | 3.75GB  |
| Bitcoind                   | 2       | 3        | 20GB      | 30GB    |
| BTC Pump*                  | 2.5     | 2.5      | 22GB      | 25GB    |
| BTC Dump                   | 3       | 3        | 3.75GB    | 3.75GB  |
| BTC Contract Summary       | 1.5     | 3        | 3.75GB    | 3.75GB  |
| Search Api                 | 0.5     | 1        | 3.75GB    | 3.75GB  |
| Search Api Docs            | 0.1     | 0.2      | 100MB     | 200MB   |

\* - With cache size = 10GB
