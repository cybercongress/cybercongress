Tha main purpose of this document is to describe requirements and the structure of cyb and apps for MVP.

# Project description

Cyber browser - an entrance point to start working with blockchains.

# Requirements

## 1. Common functional requirements

- Integration with Metamask
- IPFS integration
- Prefered type of data structure - tables

## 2. Common non-functional requirements

- Simple and attractive design
- Intuitive UI
- Adaptive design for mobile devices
- Display IPFS hash for all objects
- All hashes should be easy to copy

## 3. System requirements

- less than 1 second for loading page
- less than 3 seconds for loading all data
- Web version of browser (React)
- Desktop version (Electron + React)
- Mobile web version

# Browser structure:


# 0 Shell.

Search bar, App bar, State bar, Context bar.


### 0.1 Search (Path) bar

Top of the page

- search in existing list of apps
- search in blockchain explorer app
- search in token monitor app
- search path

### 0.2 App bar:

Left menu

- list of installed apps (4 blockchain explorers, chaingear, token monitor)
- add/delete app  

### 0.3 State bar:

- desync state
- metamask instelled state (Y/N)
- tx processing state

### 0.4 Context bar:

- account logo
- account address
- account balance

settings:

- language
- location
- currency (USD/ETH/BTC)
- activity type (private/anonymous/public)


USE CASES:

- no metamask - install metamask
- non auth user- log in metamask
- auth user - account logo



## 1. Main Page

**Purpose:** accent the user's attention on all browser apps. 

**Design & UI features:** simple and attractive design, hints to start usage of cyber products.

There is a status text below search panel which describes technical information about cyber.Search products:

**_Search in 134 M transactions in 2 blockchain systems with 135 parsed tokens. Database size : 369 GBs_** 

Where:

1. Transactions [number] - number of all indexed transactions from all blockchains connected to Cybernode. 
2. Blockchain systems [number] - all blockchains processed by Cybernode.
3. Tokens [numger] - all unique tokens from all blockchains indexed. 
4. Database size [number + Gb] - size of Cassandra (index) database.

There are 3 main widgets below the status string describing the cryptoeconomy, registers and portfolio. Their apperance depends on user type:

1. User without Metamask

- Total market cap [billions of USD] - is a summ of all token capitalizations, valuated in USD. 

    _**Call to action:** install Metamask and transit to tokens page_.
  
- Chaingear registers [number] - number of created registers in Chaingear.

    _**Call to action:** install Metamask and transit to Chaingear page_.
  
- Apps [number] - number of browser apps.

    _**Call to action:** deploy app_.

2. User with Metamask (no activities in system)

- Total market cap [billions of USD] - is a summ of all token capitalizations, valuated in USD. 

    _**Call to action:** transit to tokens page_.
  
- Chaingear registers [number] - number of created registers in Chaingear.

    _**Call to action:** transit to Chaingear page, hint to create register or record_.
  
- Apps [number] - number of browser apps.

    _**Call to action:** deploy app_.

3. User with Metamask (no activities in system)

- Total market cap [billions of USD] - is a summ of all token capitalizations, valuated in USD. 

    _**Call to action:** transit to tokens page_.
  
- Chaingear registers [number] - number of created registers/records in Chaingear.

    _**Call to action:** Chaingear page_.
  
- Apps [number] - number of browser apps.

    _**Call to action:** deploy app_.


At the bottom of the page 5 project links are placed:
1. GitHub - GitHub repository of cyber.Congress [https://github.com/cybercongress]
2. Roadmap - roadmap for cyber.Search project [https://github.com/orgs/cybercongress/projects/1]
3. Cybernode - Cybernode stats page [cybersearch.live]
4. Dashboard - a link user's custom dashboard []
5. Knowledge - a link to knowledge database of cyber.Search project [cybersearch.io]

## 2. App list

**Purpose:** accent the user's attention on all browser apps. 

**Design & UI features:** simple and attractive design, hints to start usage of apps.

There is list of browser apps with categories (with brief overview):

1. Blockchain explorers - Search in 135 million transactions in 4 blockchains

- Ethereum Explorer
- Ethereum Classic explorer
- Bitcoin Explorer
- Bitcoin Cash explorer

2. Cybernomics - Watch and anayze 135 parsed tokens in 7 exchanges 

- Token Monitor
- Exchange Monitor
- Blockchain Monitor

3. Registers - Store your records in blockchains

- Chaingear

4. Accounting - Manage your cryptoassets

- Portfolio

There are 2 versions of apps:

- stable released apps
- developing apps

**Proposals:**

- donation button for developing apps
- install to App bar button (in app is not installed)

# Applications

1. Blockchain explorer

- Bitcoin
- Bitcoin Cash
- Ethereum
- Ethereum Classic




## 2. Search Results Page

**Purpose:** provide easy and quick functionality for working with blockchain search.

**Design & UI  features:** strictly logical UI, adaptive preferenses of filtration and sorting.

#### Objects of search.

There are 2 types of search provided by browser:
1. Global search (searching in whole ecosystem of indexed objects)
2. Context search (searching the data in certain pages)

There are 4 systems (blockchains) in which you can find data:

- Bitcoin
- Bitcoin Cash
- Ethereum
- Ethereum Classic

There are 4 types of objects that can be foung in listed systems:

1. Contracts
2. Transactions
3. Blocks
4. Uncle blocks

Objects can be found by entering next types of queries:

1. Full hash (address, block, uncle, transaction)
2. Number (block/uncle)

The search pannel in general should include next functions:
1. Global and local search (GitHub style)
2. Autocomplete function

#### Search results.

Left menu includes next hardcoded functions:

1. Display listed systems (blockchains)
2. Display listed objects

Search results in general are shown as a list of object preview. Each object preview its own structure:

1. Transaction:

- Time (finalization, or time of confirmation or "Mempool" status)
- Hash
- Value

2. Block + number

- Time of creation
- Hash
- Number of transactions


3. Uncle + number

- Time  of creation
- Hash
- Uncle position


4. Contract

- Time of creation
- Hash
- Value


Each preview has clickable hash string, that leads to block/uncle, contract or transaction page.

There is a infinite page scroll function on results page.

### 2.1 Contract Page

Currently browser shows 2 types of contract pages:

1. Ethereum (Ethereum Classic) contract page
2. Bitcoin (Bitcoin Cash) contract page

#### 2.1.1 Bitcoin contract

Displayed data:
- Robohash logo
- QR code of address hash

General

- UTC Time [date] - time of contract getting into blockchain
- Balance [number + currency] - BTC available to withdraw
- Hash [string] - hash of address

Cashflow

- Transactions [number] - number of transactions in contract
- Unconfirmed transactions [number] - number of transactions in mempool
- Accumulated income [number + currency] - received BTC
- Pending income [number + currency] - BTC in mempool transactions

Charts:

1. Valuation tab (Regular graph, all above zero):
- Valuation / Time - balance of contract on each period of time

2. Transactions tab (incoming tx - above zero, outcoming - below):
- Transactions / Time - activity of transactions by contract on each period of time

Transactions and blocks;

1. Transactions tab:

- UTC Time [date] - time of getting transaction to mempool
- Hash [string] - hash of transaction
- Block [number] - number of block
- Sender[number]- number of inputs
- Value[number + currency] - total input balance in BTC
- Receiver [number]- number of outputs
- Value [number + currency] - total output balance in BTC
- Fee [number + currency] - accumulated fees in BTC
- State [string] - "Confirmed", "Mempool", "Finalized"

2. Mined blocks (for miner address only):
- UTC Time [date] - time of block generation
- Block [number] - number of mined block
- Transactions [number] - number of transactions in mined block
- Reward [number + currency] - rewards for block in BTC

Code:
- bitcoin scripts

Actions:

1. Info by pointing:
- Time (UTC) - show age of transaction (current time minus mempool)
- Address - show label of address

2. Clicking
- Hash string - copy string in buffer
- Transaction row - expand transaction details (inputs and outputs)

3. Labeling
- labeling via button "label it"

#### 2.1.2 Ethereum contract

Displayed data:
- Robohash logo
- QR code of address hash

General:

- UTC Time [date] - time of contract getting into blockchain
- Balance [number + currency] - ETH available to withdraw
- Hash [string] - hash of address

Cashflow:

- Transactions [number] - number of transactions in contract
- Unconfirmed transactions [number] - number of transactions in mempool
- Accumulated income [number + currency] - received ETH
- Pending income [number + currency] - ETH in mempool transactions

Charts:

1. Valuation tab (Regular graph, all above zero):
- Valuation / Time - balance of contract on each period of time

2. Transactions tab (incoming tx - above zero, outcoming - below):
- Transactions / Time - activity of transactions by contract on each period of time

Transactions and blocks;

1. Transactions tab:
- UTC Time [date] - time of getting transaction to mempool
- Hash [string] - hash of transaction
- Block [number] - number of block
- Sender[hash]- hash of "from" address
- Receiver [hash]- hash of "to" address
- Value [number + currency] - tx value in ETH
- Fee [number + currency] - accumulated fees in ETH
- State [string] - "Confirmed", "Mempool", "Finalized"

4. Operations tab (if available):
- UTC Time [date] - time of getting transaction to mempool
- Type [string] - type of internal tx (call, delegate call, destroy, create)
- Sender[hash]- hash of "from" address
- Receiver [hash]- hash of "to" address
- Value [number + currency] - total input balance in ETH
- Gas used [number] - gas used
- Gas limit [number] - gas limit
- State [string] - "Failed", "Reverted", "Successful"

3. Tokens tab:
- Token [string] - token name
- Hash [string] - transaction hash
- Sender [number + currency] - sent tokens
- Receiver [number + currency] - received tokens
- Value [number + currency] - sent minus received tokens

4. Mined blocks tab (for miner address only):
- UTC Time [date] - time of block generation
- Block [number] - number of mined block
- Transactions [number] - number of transactions in mined block
- Reward [number + currency] - rewards for block in ETH

5. Mined uncles tab (if available):

- UTC Time [date] - time of block generation
- Hash [string] - uncle hash
- Block [number] - number of block with uncle
- Uncle [number] - number of mined uncle

- Reward [number + currency] - rewards for uncle in ETH

Code:

Contract code:
- Contract name [string] - name of contract
- Compiler version [string] - version of compiler
Source code - code of contract
ABI - contract ABI
Swarm code - link in ethereum swarm

Actions:

1. Info by pointing:
- Time  - show age of transaction (current time minus mempool)
- Address - show label of address

2. Clicking
- Hash string - copy string in buffer

3. Labeling
- labeling via button "label it"

### 2.2 Transaction Page

Currently browser shows 2 types of transaction pages:

1. Ethereum (Ethereum Classic) transaction page
2. Bitcoin (Bitcoin Cash) transaction page

#### 2.2.1 Bitcoin transaction

Displayed data:

General

- UTC Time [date] - time of getting transaction to mempool
- Hash [string] - hash of transaction
- Value [number + currency] - total transaction value in BTC
- State [string] - "Confirmed", "Mempool", "Finalized"

Blockchain specific

- Block [number] - number of block
- Size - [number + bytes] - size of transaction in bytes
- Confirmations [number] - number of confirmations (for confirmed or finalized transactions)
- Inputs [number] - number of input addresses
- Outputs [number] - number of output addresses

Fees

- Fee [number + currency] - accumulated fees in BTC
- Fee per byte [number + satoshi/Byte] - fee/size
- Fee per weight unit [number + satoshi/WU] - fee/weight unit

Address table. Headers:

- Senders [string]- input hashes:
- Value [number + currency] - input value in BTC
- Receivers [string]- output hashes:
- Value [number + currency] - output value in BTC

Transaction data:

- Input data [string] - input scripts
- Output data [string] - output scripts

Actions:

1. Info by pointing:
- Time (UTC) - show age of transaction (current time minus mempool)
- Confirmations - first confirmation time minus mempool time

2. Clicking
- Hash string - copy string in buffer

3. Labeling
- labeling via button "label it"

#### 2.2.2 Ethereum transaction

Displayed data:

General

- UTC Time [date] - time of getting transaction to mempool
- Hash [string] - hash of transaction
- Value [number + currency] - total transaction value in ETH
- State [string] - "Confirmed", "Mempool", "Finalized"

Blockchain specific

- Block [number] - number of block
- Nonce [number] - nonce of transaction
- Size - [number + bytes] - size of transaction in bytes
- Confirmations [number] - number of confirmations (for confirmed or finalized transactions)

Fees

- Fee [number + currency] - accumulated fees in ETH
- Gas price [number + wei] - price of gas
- Gas used [number] - used gas
- Gas limit [number] - limit of gas

Address table. Headers:

- Sender [string]- input hashes
- Receiver [string]- output hashes:
- Value [number + currency] - tx value in ETH

Transaction data:

- Input data [string] - hash
- Logs [string] - logs of transaction

Actions:

1. Info by pointing:
- Time - show age of transaction (current time minus mempool)
- Confirmations - first confirmation time minus mempool time

2. Clicking
- Hash string - copy string in buffer

3. Labeling
- labeling via button "label it"

### 2.3 Block Page

Currently browser shows 3 types of block pages:

1. Ethereum (Ethereum Classic) block page
2. Ethereum (Ethereum Classic) uncle block page
3. Bitcoin (Bitcoin Cash) block page

#### 2.3.1 Bitcoin block

Displayed data:

- Block number [number] (header of page)

General

- UTC Time [date] - time of block generation
- Hash [string] - hash of block
- Size [number + bytes] - size of block in bytes
- Nonce [string] - answer to PoW
- Transactions[number] - number of transactions in block

Blockchain specific

- Merkle root [string] - hash of merkle tree
- Version [number] - number of block

Mining

- Miner [string] - miner hash
- Difficulty [number] - mining difficulty

Rewards

- Static block reward [number + currency] - static reward for block mining in BTC
- Fees [number + currency] - accumulated fees in BTC
- Total blobk reward [number + currency] - sum of static reward and fees in BTC

Transaction table. Headers:

- UTC Time [date] - time of getting into block or confirmation minus time of getting into mempool
- Hash [string] - transaction hash
- Senders [number] - number in inputs
- Value [number + currency] - summ of all input values in BTC
- Receivers [number] - number in outputs
- Value [number + currency] - summ of all output values in BTC
- Fee [number + currency] - fees per transaction in BTC

Actions:

1. Info by pointing:
- Time (UTC) - show age of block (current time minus block generation time)
- Miner - show label of miner
- Total block reward - string "Static block reward + Fees"

2. Clicking
- Transaction table - expanding tx inputs and outputs by clicking on transaction row (like https://tradeblock.com/bitcoin/block/400000)
- Next & Previous buttons (top of the page)
- Hash string - copy string in buffer

#### 2.3.2 Ethereum block

Displayed data:

- Ethereum block number [number] (header of page)

General

- Time [date] - time of block generation
- Hash [string] - hash of block
- Size [number + bytes] - size of block in bytes
- Nonce [string] - answer to PoW
- Transactions [number] - number of transactions in block

Blockchain specific

- Sha3Uncles [string] - hash of uncles
- Extra Data [string] - extra mining date
- Uncles [number] - number of uncle blocks
- Gas used [number] - used gas
- Gas limit [number] - limit of gas

Mining

- Miner [string] - miner hash
- Difficulty [number] - mining difficulty

Rewards

- Static block reward [number + currency] - static reward for block mining in ETH
- Fees [number + currency] - accumulated fees in ETH
- Uncle inclusion rewards [number + currency] - rewards in ETH for uncle inclusion
- Total blobk reward [number + currency] - sum of static reward, fees and uncle inclusion

Transaction table. Headers:

- UTC Time [number + seconds] - time of getting into block or confirmation minus time of getting into mempool
- Hash [string] - transaction hash
- Sender [hash] - hash of input
- Receiver [hash] - hash of output
- Value [number + currency] - transaction value in ETH
- Fee [number + currency] - fees per transaction in ETH

Uncle table. Headers:

- Hash [string] - uncle hash
- Level [number] - uncle position
- Miner [hash] - hash of miner
- Reward [number + currency] - rewards of uncle

Actions:

1. Info by pointing:
- Time (UTC) - show age of block (current time minus block generation time)
- Extra - show converted hash
- Miner - show label of miner
- Gas used - 100% * (gas used / gas limit )
- Total block reward - string "Static block reward + Uncle block reward + Fees"

2. Clicking
- Next & Previous buttons (top of the page)
- Hash string - copy string in buffer

#### 2.3.3 Ethereum uncle block

Displayed data:

- Ethereum uncle block number [number] (header of page)
- Time [date] - time of block generation
- Hash [string] - hash of uncle block
- Parent block [number] - number of parent block
- Parent hash [string] - hash of parent block
- Level [number] - uncle position

- Miner [hash] - hash of miner

- Uncle inclusion rewards [number + currency] - rewards in ETH for uncle inclusion

Actions:

1. Info by pointing:
- Time - show age of block (current time minus block generation time)
- Miner - show label of miner

2. Clicking
- Next & Previous buttons (top of the page)
- Hash string - copy string in buffer





## 3. Blockchain Monitor

## 4. Token Monitor

Token Table:

Headers:

- Name [string] - token name
- Market cap [number + currency] - market cap of token (price * supply)
- Price [number + currency] - weightrd price of token
- Volume (24h) [number + currency] - 24h volume of token trades
- Supply [number + token ticker] - number of tokens
- Change (24h) [number + percent] - 24h chdnge of price
- Price graph (7d) [img] - weekly price change



## 5. Exchange Monitor

## 6. Chaingear

**Purpose:** provide easy integration with Chaingear.
**Design & UI  features:** simple UI, autoupdate register data, preview of changes.

All functionality is available after Metamask authorization.

Main functions of the page:

1. Watch and label created registers.
2. Create register
3. Edit register (entry)
3. Delete register
4. Transfer the rights of usage to another account
5. Upload content to register via IPFS
6. JSON import of custom fields
6. Real time calculation of registry creation costs
7. Data import from smart contract


## 8. Labels

## 9. Portfolio
