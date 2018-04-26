## Kafka
### Stop kafka and delete kafka data(cheat sheet)
```bash
docker stop fast-data-dev-markets
docker rm fast-data-dev-markets
```

## Elassandra
### Stop elassandra and delete elassandra data(cheat sheet)
```bash
docker stop elassandra-markets
docker rm elassandra-markets 
```

## Chains
### Run parity node(cheat sheet)
```bash
sudo  docker run -d -p 8545:8545 --name parity_eth \
-v ${REPLACE_IT_BY_HOST_FOLDER}:/cyberdata parity/parity:stable \
--db-path /cyberdata --jsonrpc-hosts all --jsonrpc-interface all --jsonrpc-threads 4
```