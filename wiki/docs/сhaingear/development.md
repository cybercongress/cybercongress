# Configuring, development and deploying

##### Development environment
Recommending to use [Remix Ethereum Online IDE](remix.ethereum.org)  or [desktop electron-based Remix IDE](https://github.com/horizon-games/remix-app)

PS: to import to IDE open-zeppelin contacts change imports this way:
```js
import "github.com/openZeppelin/zeppelin-solidity/contracts/ownership/Ownable.sol";
```

##### Truffle + Ganache workflow

Install Ganache (with UI) from [latest release](https://github.com/trufflesuite/ganache/releases) or npm package =>

```bash
npm install -g ganache-cli
```

Configure development config in truffle.js and launch Ganache (configure them too if needed) and:
```bash
ganache-cli -p 7545 (in first tab/or run UI-client)
truffle migrate --network development --reset (in second tab)
truffle console --network development (in second tab)
```

##### Creating new registry/CRU entries (truffle console way/no Remix IDE)
```bash
var chaingear = Chaingear.at(Chaingear.address)

var beneficiaries = []
var shares = []
var buildingFee = 100000
var gas = 10000000

chaingear.registerRegistry("V1", beneficiaries, shares, "BlockchainRegistry", "BLR", {value: 100000, gas: 10000000})
var registryAddress = chaingear.registryInfo.call(0)
var registry = Registry.at('insert_registry_address_here')
registry.initializeRegistry("IPFS_HASH", EntryCore.bytecode)
registry.createEntry()
var entryCoreAddress = registry.getEntriesStorage()
var entryCore = EntryCore.at('insert_entry_core_address_here')
entryCore.updateEntry(0, '0xa2f0dde51cb715f9cc7c12763fef90270bd50f70', 256, -127,"helloworld")
entryCore.entryInfo(0)
// --->>>
[ '0xa2f0dde51cb715f9cc7c12763fef90270bd50f70',
  BigNumber { s: 1, e: 2, c: [ 256 ] },
  BigNumber { s: -1, e: 2, c: [ 127 ] },
  'helloworld' ]
```

##### Linting:

```bash
npm install -g solium

solium -d contracts
```

##### Testing:

```bash
truffle test
```
PS: script will run separate tests flow for each file, also produce gas report. Temp solution, for while we don't fix problem with tests falls when running for all files at one time what in truffle by default.

##### Deploying (for example kovan):

```bash
parity ui --chain=kovan

truffle migrate --network=kovan
```
PS: approve transaction in parity ui (http://127.0.0.1:8180/)

#####(Optional) Build contract in file:

```bash
truffle-flattener contracts/registry/Registry.sol > Registry_full.sol
```
