

## Current chains nodes tables
| App              | data path                     |  port        |   creds          |  current size |
| ---------------  | ----------------------------- | ------------ | ---------------- | ------------- |
| bitcoind - btc   | /cyberdata/ssd05tb/bitcoind   |  8332        | cyber:cyber      | 184 gb        |
| abc    -   bth   | /cyberdata/abc                | 18332        | bitcoin:password | 156 gb        |
| parity -   eth   | /cyberdata/ssd05tb/eth        |  8545        |                  | 56  gb        |
| parity -   eth_c | /cyberdata/ssd05tb/eth_c      | 18545        |                  | 5.3 gb        |


## Local forwarding port for chains

```
ssh -L 18332:localhost:18332 -L 8332:localhost:8332 \
-L 18545:localhost:18545 -L 8545:localhost:8545 \
mars@staging.cyber.fund  -p 33322
```

## Commands used to run chain and live probe

### Bitcoind  
Run:
```
sudo  docker run -d -p 8332:8332 --name bitcoind  --restart always \
-v /cyberdata/ssd05tb/bitcoind:/home/bitcoin/.bitcoin ruimarinho/bitcoin-core:0.15.1 \
-server -rest -txindex -rpcpassword=cyber -rpcuser=cyber -rpcallowip=0.0.0.0/0
```
Probe:
```
curl -X POST -H "Content-Type: application/json" \
--data '{"jsonrpc":"2.0","method":"getblockhash","params":[1],"id":1}' \
http://127.0.0.1:8332 -u cyber:cyber
```

### BitcoinABC
Run:
```
sudo  docker run -d -p 18332:8332 --name abc  --restart always 
-v /cyberdata/abc:/data zquestz/bitcoin-abc:0.16.1 bitcoind -server -rest
```
Probe:
```
curl -X POST -H "Content-Type: application/json" \
--data '{"jsonrpc":"2.0","method":"getblockhash","params":[1],"id":1}' \
http://127.0.0.1:18332 -u cyber:cyber
```  

### Parity 
Run:
```
sudo  docker run -d -p 8545:8545 --name parity_eth  --restart always \
-v /cyberdata/ssd05tb/eth:/cyberdata parity/parity:stable \
--db-path /cyberdata --jsonrpc-hosts all --jsonrpc-interface all --jsonrpc-threads 10
```
Probe:
```
curl -X POST -H "Content-Type: application/json" \
--data '{"jsonrpc":"2.0","method":"eth_getBlockByNumber","params":["0x1", true],"id":1}'\
 http://127.0.0.1:8545
```

### Parity --chain classic
Run:
```
sudo  docker run -d -p 18545:8545 --name parity_etc  --restart always \
-v /cyberdata/ssd05tb/eth_c:/cyberdata parity/parity:stable --db-path /cyberdata \
--jsonrpc-hosts all --jsonrpc-interface all --chain classic --jsonrpc-threads 10
```
Probe:
```
curl -X POST -H "Content-Type: application/json" \
--data '{"jsonrpc":"2.0","method":"eth_getBlockByNumber","params":["0x1", true],"id":1}' \
http://127.0.0.1:18545
```