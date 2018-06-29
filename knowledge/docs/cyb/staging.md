
### Staging server

To avoid conflicts with other services on the same ports, we run our services on the following ports:

    cyber-ui :32500
    chaingear-api :32600
    cyber-search-api :32700
    cyber-markets-api :32800

Staging runs 4 **components**:

- [cyber-ui](https://github.com/cyberFund/cyber-ui)
- [cyber-search](https://github.com/cyberFund/cyber-search)
- [cyber-markets](https://github.com/cyberFund/cyber-markets)
- [chaingear](https://github.com/cyberFund/chaingear)

Each component is composed from different **containers**. Some containers are shared to save resources.

### Server setup

This is only needed to be done once.

1. SSH to staging server. Make sure you're in `docker` group:

       $ groups
       anatoli docker wheel cyber

2. Checkout `cyber-ui` repo with staging setup:

       $ git clone https://github.com/cyberFund/cyber-ui

#### Update running containers

Update running containers:

       $ cd cyber-ui && git pull
       $ ./devops/staging/up.sh

This uses `docker-compose` to start containers from DockerHub. It doesn't rebuild them.

#### Rebuilding

TODO: Move stuff out of CircleCI configs into build scripts + conventions.

