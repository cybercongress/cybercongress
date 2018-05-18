# Components requirements

Resources requirements to run components in gcloud cluster

| Component                  | Min CPU | Max CPU  |  Min RAM  | Max RAM |
| -------------------------- | ------- |--------- | -------   | --------|
| Kafka Broker               | 1.5     | 2        | 15GB      | 20GB    |
| Kafka Exporter             | 0.1     | 0.2      | 1GB       | 2GB     |
| Kafka Manager              | 0.1     | 0.2      | 1GB       | 2GB     |
| Zoo Keeper                 | 0.1     | 0.2      | 2GB       | 4GB     |
| Elassandra                 | 2       | 2.5      | 20GB      | 25GB    |
| Grafana                    | 0.1     | 0.2      | 100MB     | 200MB   |
| Prometheus                 | 0.25    | 0.5      | 500MB     | 1000MB  |
| Prometheus Operator        | 0.1     | 0.2      | 100MB     | 200MB   |
| Parity ETH                 | 1.5     | 2        | 15GB      | 20GB    |
| Parity ETC                 | 1       | 1.5      | 10GB      | 15GB    |
| ETH Pump                   | 1.5     | 2        | 2.5GB     | 3GB     |
| ETH Cassandra Dump         | 1.5     | 2        | 2.5GB     | 3GB     |
| ETH Contract Summary       | 1.5     | 2        | 2.5GB     | 3GB     |
| ETC Pump                   | 1.5     | 2        | 2.5GB     | 3GB     |
| ETC Cassandra Dump         | 1.5     | 2        | 2.5GB     | 3GB     |
| ETC Contract Summary       | 1.5     | 2        | 2.5GB     | 3GB     |
| Bitcoind                   | 2       | 3        | 20GB      | 30GB    |
| BTC Pump*                  | 1.5     | 2        | 10GB      | 12GB    |
| BTC Dump                   | 1.5     | 2        | 2.5GB     | 3GB     |
| BTC Contract Summary       | 1.5     | 2        | 2.5GB     | 3GB     |
| Search Api                 | 0.5     | 1        | 1.5GB     | 2GB     |
| Search Api Docs            | 0.1     | 0.2      | 100MB     | 200MB   |

\* - With cache size = 4GB