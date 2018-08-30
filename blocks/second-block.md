# Block 2. Iceland + Tolyatti

## `Main priorities`
1. cyberd whitepaper + PoC
2. cyb release
3. Get 100 ETH from chaingear
4. №1 organization on Gitcoin
5. Launch community reports and fill blog with 20 posts with overall 1000 subscribers

___________

## `cyberd`

@hleb-albau @arturalbov @litvintech @xhipster @asadovka @vstavetsky

Example of [good workflow](http://tezos.gitlab.io/betanet/#the-networks):
- `zeronet`: nightly builds of the team, no guaranties
- `alphanet`: test network, tokens has now value, hence faucet
- `betanet`: developer network, token has low value
- `cybernet`: user network, token has value

These  workflow can activates only after when initial protocol and consensus technology will be stabilized. Until the following stage of development reached master branch is zeronet.

## Epics:

### 1. Ranking research
Main goal is to analyze existing ranks on real Ethereum and Bitcoin transactions in terms of time and predictability of transactions.

### 2. Whitepaper 0.2

Happens if consensus reached around intended protocol for alphanet. After that define whitepaper as WIP. All proofs and explanations can be not finalized.

### 3. Link Chain PoC | Zeronet

We need to reach zeronet because we want:
- Test and develop browser PoC
- Research around semantics and link chains
- Research around link prediction on real life data
- Test algorithms of ranking and payouts
- Load testing and simulation
- Start distribution during development
- Win time for more research around consensus algorithms

### 4. Distribution

- Compute SpringRank for Ethereum (Link is tx, weight is amount)
- Create initial genesis for our network
- Importing Ethereum keys to application. Computing addresses in ipfs and cyber
- Singing messages and transactions using imported keys

### 5. Visual explorer

Must work in cyb and standalone.
The following views are of significant importance:
- Graph explorer. Watch incoming and outcoming links.
- Stats monitor. Like steemdb.com
- Blocks
- Txs

### 6. Semantics research
- Define a concept of link chains
- Common block semantics
- Common transaction semantics
- Common contract semantics
- Write guide for application developers on semantic programming of web3 app
- Develop semantics for chaingear

### 7. Load testing
- transfer our cybernode's dataset to IPFS hashes and load them with semantic

### 8. Simulation
Create tool for fast evaluating protocol with different params and users behavior
- Simulate users and their search/linking (params)
- Simulate ranking (params)
- Simulate payouts (params)

___________

## `cyb` PoC release

@asadovka @vstavetsky @volga @pechalka

Purpose is functionality of Atom

## Epics:

### 1. Merge into Parity
- offline launch
- ipfs browsing based on daemon inside
- offline state browsing
- Redesign search bar
- Apps left: wallet, node status
- Search results page logic (link if app used + ability to link)

### 2. Publish web3 browser vision
- whitepaper
- duri vision
- web3 application guidelines

### 3. Develop core dapps
dapp is _____
- app store
- submit to app store
- console (parity based)
- tx queue and states (parity based)
- develop contracts (parity based)
- feed and notification
- address book and keystore
- bookmarks
- history
- ipfs
- wallet
- messenger (pubsub, whisper)
- node status

### 4. Integrate dapps
- tokens
- chaingear
- myetherwallet
- metamask
- swarm
- augur
- gitcoin
- melonport
- decentraland
- radar-relay
- maker
- galt
- robonomics
- academy
- sonm

### 5. Paid browsing
- API's payment channels

### 6. Releasing/CI/CD

___________

## `chaingear`
@litvintech @hleb-albau @pechalka
**Feature freeze. Go to mainnet ASAP.**
- Need to implement Gitcoin + Chaingear strategy.
- Improve upon the concept of Creator Curated registries and CRUD ERC.

## Epics:

### 1. Master audit
- audit with 2+ different auditors

### 2. Deploy to mainnet
- deploy chaingear's contracts
- verification on etherscan

### 3. Launch registry of apps
- define registry structure

### 4. Launch registries for integrations prioritization
- chains
- exchanges
- metaprotocols
- roadmap/proxy-to-gitcoin

### 5. Community roadmap:
- continuous audit
- gas optimization

___________

## `cyber-search`
**Freeze current code, only cyberd integration. Gitcoin + Chaingear strategy.**
- There are money came from? Research around
- How to outsource computation? SONM testdrive

## Epics:

### 1. IPFS integration

### 2. crawler for cyberd
- connectors to cyberd/ipfs
- semantic indexing for cyberd

### 3. How to outsource computation?
- SONM testdrive

### 4. Community roadmap:
- new pumps/dumps
- balances calculation (+historical)
- ERC-20, ENS, ERC-721 parsers

___________

## `cybernode`

**Freeze features, only cyberd integration. Gitcoin + Chaingear strategy.**

## Epics:

### 1. cyberd integration
- launching
- monitor

### 2. IPFS cluster integration
- pins for searched items

### 3. API request/reward channels

### 4. Community roadmap:
- core
- "compatible" containers
- permissions for fundamental resources
- permissions for features

___________

## `cyb-js...`

Purpose: Bring search to IPFS and Ethereum

- IPFS
- CYBER
- Ethereum
- permissions

___________

## `cyber-markets`

**Freeze current code. Gitcoin + Chaingear strategy.**

Purpose: compute price from tx data by general purpose algorithm.

### Community roadmap:
- 0x 1.0 integration
- 0x 2.0 integration
- Bancor integration
- search conversion paths
- ipfs integration
- cyber-search integration

___________

## `Community`

## Epics:

### 1. Community Launch
- Twitter/Reddit/Steem/Telegram
- 20 articles from team
- 1000 devs-subscribers
- 20 gitcoin's contributors
- partnerships

### 2. Gitcoin N1 strategy
- Organize repos/tasks for contributors
- Finalize/formalize/clearify roadmap for contributors
- 30k+ $ for founties
