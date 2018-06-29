# Configuring, development and deploying

##### Deploy contract:

```
parity ui --chain=kovan

truffle migrate --network=kovan
```

PS: approve transaction in parity ui (http://127.0.0.1:8180/)

Build contract in file:

```
truffle-flattener contracts/common/Chaingeareable.sol >> app/src/Chaingeareable.sol
```

##### Linting:

```
npm install -g solium

solium -d contracts
```

##### Development environment
Recommending to use [Remix Ethereum Online IDE](remix.ethereum.org)  or [desktop electron-based Remix IDE](https://github.com/horizon-games/remix-app)

PS: to import to IDE open-zeppelin contacts follow this:
```
import "github.com/openZeppelin/zeppelin-solidity/contracts/ownership/Ownable.sol";
```

##### Truffle + Ganache workflow

Install Ganache from [latest release](https://github.com/trufflesuite/ganache/releases), then =>

```
npm install -g ganache-cli
```

Configure development config in truffle.js and launch Ganache (configure them too if needed) and:
```
ganache-cli -p 7545 (in first tab)
truffle migrate --network development --reset (in second tab)
truffle console --network development (in second tab)
```

##### Create new registry
```
var chaingear = Chaingear.at(Chaingear.address)

var beneficiaries = []
var shares = []
var buildingFee = 1000000
var gas = 10000000

chaingear.registerRegistry(beneficiaries, shares, "BlockchainRegistry", "BLR", "", EntryCore.bytecode, {value: buildingFee, gas: 10000000})
```
