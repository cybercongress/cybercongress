# Cyb: web3 browser


## 0. Overview

Cyb is simply a [web3](cyb/docs/web3-vision.md) browser.

## 1. Principles

## Agent respect

In web3 this is the most fundamental principle. We focus on developers and advanced blockchain users who is able to work with private keys and transaction. But Cyb is also friendly for everyone who wants to interact with consensus computers in a web of third generation.

We respect agent attitude and principles. So we offer 3 clear custom types of user behavior:

- anonymous activity [no tracking at all]
- private activity [abstract ID + events tracking ]
- public activity [address + events tracking by web 3 provider]

By default all activity is anonymous. Others must be explicitly asks permissions.
For successful browser development application developers need to collect at least public and private data. Thus users of these 2 groups will be incentivized by giving nice perks from dapp developers.

## Contributions

As an open source project we are welcome for contributions. Gitcoin is an excellent instrument that we use for delegating tasks for community a processing payments for completed ones.

## Feature development

We have our vision of how to develop browser and what kind of features develop first. But we give an opportunity for community to decide and vote with tokens what kind of browser we need to see in near future. Our product [Chaingear](https://github.com/cybercongress/chaingear) is also made for this.

## Feedback and bug collection

We use user's feedback to make products better. So we provide options for bug reporting and feedback leaving on every page.

## 2. Cyb concepts

Browser shell consists of the following concepts:

- Main page
- Navigation bar
- State bar
- Search bar
- ID bar
- DApp bar
- Core DApps
- Notifications
- Transaction signer
- Root registry
- Permissions & limitations

Let us describe in details every concept.


## Main Page

Main page of the browser consists of three main parts:

- search bar, that provides all search functions
- "most use" tabs, which are based on popular account activity and are unique for every account
- links of Congress' products, which are useful to contributors

## Navigation bar

In web3 all data has a definite state, so it become easier to navigate through it and make UX better.  

Navigation bar in Cyb is based on such elements as:

- back button - returns user to the previous state of web3 agent
- DURA section - provides easy access to certain state of web3 agent
- forward button - brings user to the future state
- favorites button - pin liked web3 objects  

As a knowledge graph, (cyberd)[cyberd doc] can analyze user's activity and make predictions of user behavior. Thus we can implement the "forward" button.

## State bar

To be sure that you are working with actual state browser needs to manage connection to web3 providers.

Currently we use Ethereum, IPFS, and Cyber nodes. Browser can show sync state with that nodes, display connection state (local, remote, no connection) and give an ability for user to chose own web3 provider.

## Search bar

Search bar is used to browse inside blockchains, IPFS and DApps. It [web3 vision doc](cyb/docs/web3-vision.md) we describe concepts of web3 browsing in details.

## ID bar

ID bar consists of account information, user logo, wallet, notifications and settings.

Account info - account logo + address.
Wallet button - link on wallet DApp.
Notifications - for displaying all pending transactions and web3 events.
Settings - for managing connection to IPFS, Ethereum and Cyber nodes (local or remote).

## DApp bar

DApp bar is a place where user can quickly get access to most used web3 objects. User can pin such objects by clicking on button "favorite" on navigation bar and then it will appear in DApp bar.

## Core Dapps

For good initial experience we develop core browser DApps such as:

- Ethereum wallet
- Cyberd search app
- Ethereum node status
- Help app
- App store
- Contract development
- Transaction queue
- DApp method permissions

These apps are delivered with every browser build.  

## Transaction signer

This feature allows users to sign single transactions or lists of transactions and brings web3 UX to the whole new level. Browser use own app for signing transactions so user can be always sure that transaction details are valid. Thus we decrease probability of phishing. Also browser has it's own key for signing big lists of transactions.

## Permissions & limitations

Web3 apps should strictly limited in computational resources. We describe detailed specifications [here](cyb/docs/dapp-guidelines.md).

## Root registry

Root registry of Cyb is a hard mix between top-level domains and file extensions.

Programming languages:
500 (200) (domains of language developers) https://gist.github.com/aymen-mouelhi/82c93fbcd25f091f2c13faa5e0d61760

Common programs:
500 (100) (domains of app developers) https://fileinfo.com/filetypes/common https://github.com/dyne/file-extension-list https://www.computerhope.com/issues/ch001789.htm

Top english words:
1000 (300) (grants, competitions. community feedback) https://github.com/first20hours/google-10000-english/blob/master/google-10000-english-no-swears.txt

Tokens:
1000 (100) (domain based distribution) https://coinmarketcap.com/

Tlds:
1000 (100) Write a program that is able to display web2 sites. Map all iana tlds to this programm https://en.wikipedia.org/wiki/List_of_Internet_top-level_domains http://data.iana.org/TLD/tlds-alpha-by-domain.txt










There are two main parts of browser:

1. Shell, which alows:

- deploy and manage Dapps for users
- manage sync state of nodes: IPFS, Ethereum and Cyber
- manage user's account data (sign transactions, create custom feed)

2. DApps, which:

- provide full user experience in web3
- can be available through IPFS
