## Kafka
### Stop kafka and delete kafka data(cheat sheet)
```bash
docker stop fast-data-dev-search
docker rm fast-data-dev-search
```


## Elassandra
### Stop elassandra and delete elassandra data(cheat sheet)
```bash
docker stop elassandra-search
docker rm elassandra-search
```
### Get indices info
```bash
curl -XGET 'localhost:9200/_cat/indices?v&pretty'
```

## Chains
### Run parity node
```bash
sudo  docker run -d -p 8545:8545 --name parity_eth \
-v ${REPLACE_IT_BY_HOST_FOLDER}:/cyberdata parity/parity:stable \
--db-path /cyberdata --jsonrpc-hosts all --jsonrpc-interface all --jsonrpc-threads 4
```
### Run bitcoind node
```
docker run -d -p 8332:8332 --name bitcoind --restart always \
-v ${REPLACE_IT_BY_HOST_FOLDER}:/home/bitcoin/.bitcoin ruimarinho/bitcoin-core:0.15.1 \
-server -rest -txindex -rpcpassword=cyber -rpcuser=cyber -rpcallowip=0.0.0.0/0
```