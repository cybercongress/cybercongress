

## Current chains nodes tables
| App              | data path                     |  port        |  current size |
| ---------------  | ----------------------------- | ------------ | ------------- |
| parity           | /cyberdata/parity             | 34545        | 174 gb        |
| parity-kovan     | /cyberdata/parity-kovan       | 34645        |  30 gb        |


## Local forwarding port for chains

```
ssh -L 8545:localhost:34545 -L 8546:localhost:34546 earth@earth.cybernode.ai -p 33324
```

## Commands used to run chain and live probe

### Parity 
Run:
```
docker run -d  -p 34546:8546 -p 34545:8545 -v /cyberdata/parity:/cyberdata \
-v  /home/earth/.local/share/io.parity.ethereum/jsonrpc.ipc:/home/parity/.local/share/io.parity.ethereum/jsonrpc.ipc \
--name parity --restart always --ipc=host parity/parity:stable \
--db-compaction ssd --unsafe-expose --db-path /cyberdata --tracing=on --fat-db=on
```
Probe:
```
curl -X POST -H "Content-Type: application/json" \
--data '{"jsonrpc":"2.0","method":"eth_getBlockByNumber","params":["0x1", true],"id":1}'\
 http://127.0.0.1:34545
```

### Parity --chain kovan
Run:
```
docker run -d  -p 34646:8546 -p 34645:8545 -v /cyberdata/parity:/cyberdata \
-v  /home/earth/.local/share/io.parity.ethereum/jsonrpc.ipc:/home/parity/.local/share/io.parity.ethereum/jsonrpc.ipc \
--name parity-kovan --restart always --ipc=host parity/parity:stable \
--db-compaction ssd --unsafe-expose --db-path /cyberdata --tracing=on --fat-db=on --chain kovan
```
Probe:
```
curl -X POST -H "Content-Type: application/json" \
--data '{"jsonrpc":"2.0","method":"eth_getBlockByNumber","params":["0x1", true],"id":1}' \
http://127.0.0.1:34645
```
