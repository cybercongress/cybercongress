search# Block 2. Iceland

## Priorities
1. cyberd whitepaper + PoC
2. cyb release
3. Get 100 ETH from chaingear
4. №1 organization on Gitcoin
5. Launch community reports and fill blog with 20 posts with overall 1000 subscribers

## cyberd
@hleb-albau @arturalbov @litvintech @xhipster @asadovka @vstavetsky
Example of [good workflow](http://tezos.gitlab.io/betanet/#the-networks):
- `zeronet`: nightly builds of the team, no guaranties
- `alphanet`: test network, tokens has now value, hence faucet
- `betanet`: developer network, token has low value
- `cybernet`: user network, token has value

These  workflow can activates only after when initial protocol and consensus technology will be stabilized. Until the following stage of development reached master branch is zeronet.

## Epics

### Rank research
Main goal is to analyze existing ranks on real Ethereum and Bitcoin transactions in terms of time and predictability of transactions.

### Whitepaper 0.2

Happens if consensus reached around intended protocol for alphanet. After that define whitepaper as WIP. All proofs and explanations can be not finalized.

### Link Chain PoC | Zeronet

We need to reach zeronet because we want:
- Test and develop browser PoC
- Research around semantics and link chains
- Research around link prediction on real life data
- Test algorithms of ranking and payouts
- Load testing and simulation
- Start distribution during development
- Win time for more research around consensus algorithms

### Distribution

- Compute SpringRank for Ethereum (Link is tx, weight is amount)
- Create initial genesis for our network
- Importing Ethereum keys to application. Computing addresses in ipfs and cyber
- Singing messages and transactions using imported keys

### Explorer

Must work in cyb and standalone.
The following view must be developed:
- Graph explorer. Watch incoming and outcoming links.
- Stats monitor. Like steemdb.com
- Blocks
- Txs

### Semantics research
- Define a concept of link chains
- Common block semantics
- Common transaction semantics
- Common contract semantics
- Write guide for application developers on semantic programming of web3 app
- Develop semantics for chaingear

### Load testing
- transfer our cybernode's dataset to IPFS hashes and load them with semantic

### Simulation
Create tool for fast evaluating protocol with different params and users behavior
- Simulate users and their search/linking (params)
- Simulate ranking (params)
- Simulate payouts (params)

## cyb PoC release
@asadovka @vstavetsky @volga @pechalka
Merge into Parity. Purpose is functionality of Atom
- specification / whitepaper (web3 vision)
- duri vision / web3 application guidelines
- permission layer
- feed and notification system
- address book and keystore
- tx states
- identity providers
- bookmarks
- history
- app store
- submit to app store
- apm integration

## chaingear
@litvintech @hleb-albau @pechalka
Feature freeze. Go to mainnet ASAP. Need to implement Gitcoin + Chaingear strategy. Improve upon the concept of Creator Curated registries and CRUD ERC.
- master audit
- deploy to mainnet
- launch registry of apps
- launch registries for integrations prioritization (chains, exchanges, metaprotocols, roadmap/proxy-to-gitcoin)

## cyber-markets
Freeze current code. Gitcoin + Chaingear strategy.
Purpose: compute price from tx data by general purpose algorithm.
Community roadmap:
- 0x 1.0 integration
- 0x 2.0 integration
- Bancor integration
- search conversion paths
- ipfs integration
- cyber-search integration

## cyber-search
Freeze current code. Gitcoin + Chaingear strategy.
- there are money came from? Research around
- How to outsource computation? SONM testdrive

Community roadmap:
- the more transactions the better
- balances
- ERC-20, ENS, ERC-721 parsers

## cybernode
Freeze current code. Gitcoin + Chaingear strategy.
- cyberd integration
- IPFS cluster ingtegration (pins for searched items)

Community roadmap:
- core
- API calls reward based on channels
- "compatible" containers
- permissions for fundamental resources
- permissions for features

## cyb-js
Bring IPFS to Ethereum
- IPFS
- CYBER
- Ethereum
- permissions

## Community
- Twitter/Reddit/Steem/Telegram
- 20 articles from team
- 1000 devs-subscribers
- 20 gitcoin's contributors
- partnerships

## Gitcoin N1 strategy
- Organize repos/tasks for contributors
- Finalize/formalize/clearify roadmap for contributors
- 30k+ $ for founties

## CYB apps with partnerships
contracts:
- augur
- gitcoin
- decentraland
- radar-relay
- maker
- galt
- robonomics
- academy
- 0x
- sonm

non-contracts:
- ipfs
- myetherwallet
- metamask
- swarm
