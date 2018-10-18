# Cyb: web3 browser

@xhipster @asadovka

## Overview

Cyb is simply a [web3](cyb/docs/web3-vision.md) browser.

## Principle of respect to agent

In web3 this is the most fundamental principle. We focus on developers and advanced blockchain users who are able to work with private keys and transaction. But Cyb is also friendly for everyone who wants to interact with consensus computers in a web of third generation.

We respect agent's attitude and principles. So we offer 3 clear custom types of user behavior:

- anonymous activity [no tracking at all]
- private activity [abstract ID + events tracking ]
- public activity [address + events tracking by web 3 provider]

By default all activity is anonymous. Others must be explicitly ask permissions.
For successful browser development app developers need to collect at least public and private data. So users of these 2 groups will be incentivized by giving nice perks from app developers.

## Cyb concepts

Browser shell consists of the following concepts:

- Main page
- Navigation bar
- State bar
- Search bar
- ID bar
- App bar
- Core apps
- Notifications
- Transaction signer
- Root registry
- Permissions

Let us describe in details every concept.

## Main Page

Main page of the browser consists of three main elements:

- search bar: provides all search functions
- relevance bar: the most relevant cyberlinks for a particular agent
- footer: cyberlinks to ecosystem resources which are important for education and contribution

## Navigation bar

Navigation bar in Cyb is based on the following elements:

- back button - returns user to the previous state of web3 agent
- search bar - provides easy access to certain state of web3 agent
- favorites button - pin cyberlinks
- forward button - brings user to the future state based on Cyb prediction

Search bar is used to browse inside blockchains, IPFS and фpps. It [web3 vision doc](cyb/docs/web3-vision.md) we describe concepts of web3 browsing in details using DURA specs.

We add "dot" to search query to manage type of search. All data after "dot" corresponds to App, and all data before "dot" is a query parameter.

For example:

".help" query will open Help App. "chaingear.help" will open Chaingear info page in Help App. Query without "dot" will be automatically redirected to search in cyberd (Note: you can also search in cyberd by typing "$yourquery$.cyber").

Empty query always leads to the main page.

## State bar

In web3 all data has the state, so it become easier to navigate through it and make UX better. To be sure that you are working with actual state browser needs to manage connection to web3 providers.

Our purpose is to build web3 browser that is agnostic from addressing, identity and consensus protocols. But currently we use ipfs, parity-light and cyberd nodes to show off possible experience at early stage without necessity to connect to web3 provider at all (be your own web3 provider) for basic needs such as popular static content surfing and simple transfers of tokens.

Cyb is hiding all complexities of web3 connections under one colorful indicator that range from green to red. Ideally it works like indicator of internet connection we use to in smartphones. Clicking on this indicator give an ability for agent to understand status of connection and chose own web3 provider.

## ID bar

ID bar consists of account information, user logo, wallet, notifications and settings.

Account panel consists of generated address logo and address hash itself. We support multiple accounts so there is an ability to switch quickly between them right from the account panel.
Wallet button simply leads to our Wallet App.
Notification panel displays all pending transactions and web3 events corresponding to certain account.
Settings button leads to settings page where user can manage connection to ipfs, parity and cyberd nodes (local or remote ways).

## App bar

App bar is a place where user can quickly get access to most used web3 objects. User can pin such objects by clicking on button "favorite" on navigation bar and then it will appear in App bar.

## Core apps

For good initial experience we develop core browser apps such as:

- App store
- Cyberd search app
- Ethereum wallet
- Parity node status
- Help app
- Contract development tool
- Signer with transaction queue
- Permission manager

These apps are delivered with every browser build.

## Transaction signer

This feature allows users to sign single transactions or lists of transactions and brings web3 UX to the whole new level. Browser use own app for signing transactions so user can be always sure that transaction details are valid. Thus we decrease probability of phishing to zero. Also browser has it's own key for signing big lists of transactions.

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

## Permissions

Web3 apps should strictly limited in computational resources. We describe detailed specifications [here](cyb/docs/dapp-guidelines.md).

## Contributions

As an open source project we are welcome for contributions. Gitcoin is an excellent instrument that we use for delegating tasks for community a processing payments for completed ones.

## Feature development

We have our vision of how to develop browser and what kind of features develop first. But we give an opportunity for community to decide and vote with tokens what kind of browser we need to see in near future. Our product [Chaingear](https://github.com/cybercongress/chaingear) is also made for this.

## Feedback and bug collection

We use user's feedback to make products better. So we provide options for bug reporting and feedback leaving on every page.
