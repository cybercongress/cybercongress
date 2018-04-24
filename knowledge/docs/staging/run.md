## Port mapping

Ports that are not accessible from internet. Use ssh forwarding.

* 8332 - chain btc
* 18332 - chain bth
* 8545 - chain eth
* 18545 - chain etc


* 2181 - zookeper
* 9092 - kafka
* 9042 - elassandra search
* 9043 - elassandra markets
* 9200 - elastic rest search
* 9201 - elastic rest markets
* 9300 - elastic transport search
* 9301 - elastic transport markets


Ports open for internet.

* 32001 - portainer
* 32002 - grafana (monitoring)
* 32500 - browser-ui
* 32600 - chaingear 1.0 api
* 32800 - markets rest api
* 32801 - markets stream api
* 32901 - search api


## Docker data


## Run chains
Chains should be run manually once and ideally should not require addition work. To run chains, execute:
```
sudo bash /cyberdata/cybernode/chains/up.sh
```

## Run portainer.io
Run once
```
docker run -d -p 32001:9000 --name portainer --restart always \
-v /var/run/docker.sock:/var/run/docker.sock \
-v /cyberdata/portainer:/data portainer/portainer
```

## Run components

```
sudo bash /cyberdata/cybernode/up.browser.sh
sudo bash /cyberdata/cybernode/up.chaingear.sh
sudo bash /cyberdata/cybernode/up.ethereum.index.sh
sudo bash /cyberdata/cybernode/up.search.api.sh
```
Then go into each `kafka`, `elassandra` and run
```
docker-compose up -d
```

To access `monitoring` dashboard, run `docker-compose up -d`
in `monitoring` as well.
