# Cyb: web3 browser

@xhipster @asadovka

Concept. Definitions are work in progress.

[Current implementation](https://github.com/cybercongress/cyb) is not in comply with spec yet

## Abstract

Cyb is a friendly software robot who helps you explore the universes. Put it simply it just a [web3](cyb://QmXHiEVCFTN8hda93qZN6ay5bXJ1ZkaLCV68AefXPs1pXg.ipfs) browser. At the very beginning cyb is focusing on developers and advanced blockchain users who are able to work with private keys and transactions. But we see how Cyb becomes friendly for everyone who wants to interact with consensus computers in a web of the third generation. This new web is designed to free developers from outdated things such as html and v8. So developers can use any markup, execution and rendering engine they wish. That is why we don't focus on implementation of mentioned things. Instead this paper discuss implementation agnostic concepts of browser that are simple enough to be adopted by web3 developers. Initially we design Cyb for conventional desktop browsing. But suggested concepts can be easily used for mobile, voice, vr and robotics implementations.

## Introduction

Current state of web3 experience is non satisfactory. Still [we did not meet](cyb/docs/comparison.md) any piece of software that is able to deliver deep, emotional web3 experience. So we decide to bring to the table one contender that strictly follows web3 principles defined by ourselves ;-) In a rush for this passion we define the following web3 apps which we believe together implement the full web3 vision in the context of a browsing for web3 agents and app developers:

- `.main`: main page for every joe
- `.path`: navigation bar and its backend
- `.connect`: connection manager and state widget
- `.keys`: keystore interface and id widget
- `.cyber`: cyberd node manager and app for link chains
- `.pins`: favourites backend and application bar
- `.sign`: phishing resistant signer for messages and transactions with scheduler
- `.crr`: cyb root registry
- `.cyb`: origianl web3 appstore
- `.access`: permission manager that respects agents' resources
- `.feed`: notification backend and feed app
- `.ipfs`: ipfs node manager and agent experience
- `.eth`: ethereum node manager + ens resolver
- `.wallet`: universal wallet ux
- `.help`: cyb educational library and feedback mechanism
- `.dev`: web3 development tool with support of contracts
- `.cg`: all the things chaingearable
- `.settings`: cyb settings

All this apps are considered as core apps and are included in every Cyb distribution. Let us describe in details every app as a pure concept.

## .main

Purpose of the `main` app is to make agent happier in a moment it returns for surfing and between experiences. Main page of the browser consists of three main elements:

- search bar: provides all search functions
- relevance bar: the most relevant cyberlinks for a particular agent
- footer: cyberlinks to ecosystem resources which are important for education and contribution

## .path

Navigation bar in Cyb is based on the following elements:

- back button - returns user to the previous state of web3 agent
- search bar - provides direct access to certain state
- star button - allow users to pin cyberlinks
- forward button - brings user to the future state based on Cyb prediction

Search bar is used to browse web3. With the help of DURA with knowledge of application involved (<content-address>.<app>) it can get content across different content addressing protocols such as IPFS, DAT, SWARM, and inside blockchains, tangles and DAGs thus forming heterogeneous environment of web3. In [web3 vision doc](cyb/docs/web3-vision.md) we describe in details a concept of web3 browsing based on DURA specs.

That is, in web3 appending "dot" works very different in comparison with web2. Dot is literally a search query to a particular app that also has a content address in heterogeneous network. All symbols after "dot" make a map with content address of an app in root registry, and all data before "dot" is a query parameter to an app.

```
<illustration>
```

For example:

`.help` query will open Cyb help app. `chaingear.help` will open `chaingear` info page in the `help` app. Query without "dot" will be automatically redirected to search in cyberd (Note: queries without dot is synonym to `<your-query>.cyber`).

Empty query always leads to the main page. `.` query returns a root registry that is being used by default in Cyb.

```
<api-definition>
```

All cyberlinks that was requested by agent can be accessed using `path` app that is integral part of Cyb experience.

## .connect

In web3 all data has the state, so it become easier to navigate through it and make agent experience better. To be sure that you are working with actual state Cyb needs to manage connection to web3 providers.

Our purpose is to build web3 browser that is agnostic from addressing, identity and consensus protocols. But currently we use ipfs, parity-light and cyberd nodes to show off possible experience at early stage of web3 development without necessity to connect to web3 provider at all (be your own web3 provider) for basic needs such as popular static content surfing and simple transfers of tokens.

```
<illustration>
```

Cyb is hiding all complexities of web3 connections under one colorful indicator that range from green to red. Ideally it works like indicator of internet connection we all used to see in smartphones.  Connection indicator cyberlinked to a `connect` app that is integral part of id bar. It gives an ability for an agent to understand status of connections and chose web3 providers.

```
<api-definition>
```

Ultimate purpose of `connect` is to remove necessity of agents to manually switch between networks. Agent do not need to think about switching across networks. It is a goal of app developers and browser vendors to define an approach that allow seamless interaction during web3 experience with all network magic happens underneath. Cyb is developing in a way that allow async interactions with several peer-to-peer networks in an app context.

## .keys

Purpose of id bar is to enable the concept of identity. Using identity an agent is able to authenticate messages and sign transactions in web3. Cyb assumes that an agent interacting with web3 is using active identity, but offers ability to change id of a signed transaction during signing.

Agent understand which id is active using identicon. Cyb computes unique and deterministic identicons for every id, but offer agent to set any identicon for local pleasure. Clicking on id bar allow agent to choose active identity from a `keys` app.

```
<illustration>
```

Keys app is inherent component of id bar and embedded in Cyb. This app allows to store cryptographic secrets. Think of it as lastpass you don't need to trust that is able to compute different addresses, one time passwords and signatures in the context of an app.

The following convention is used for `keys`:

```
id: String,
chainId: Number
keystore: Promise <String>
mnemonic: String
derivationPath?: Promise <String>
otherAddresses: Array <String>
privateKey: String
publicKey: Promise <String>
type: String
subtype: String
```

The following API is being used to programmatically interact with id bar:

```
setDefaultId(addressIndex: Number): Promise <Boolean>
sign(transactionObject: Object): Promise <String>
signMessage(messageObject: Object): Promise <String>
verifyMessage(verificationObject: Object): Promise <Boolean>
```

## .cyber

It happens then agent knows some content address but have no idea in which network it can be retrieved as well as what app can deal with it. That is why Cyb has default integration with cyber [CYBER] protocol. Cyb append `.cyber` app for all request without a dot. `.cyber` is an app that has simple interface to cyberd, which returns prediction of related cyberlinks thus agent can get required resource directly through peer-to-peer network. Cyb has a setting of default search engine, thus an agent can plug a search she wants.

```
<api-definition>
```

## .pins

App bar is a place where user can quickly get access to most used web3 objects. User can pin such objects by clicking on button "favourite" on navigation bar and then it will appear in app bar. Cyberlink manager is an attached app that allow agents to group and tag pins.

## .sign

`.sign` allows users to sign messages and transactions in a way that brings web3 experience to the whole new level.

Browser use embedded app for signing transactions so user can be always sure that transaction details are valid. In a web2 there is no inherent mechanism to be sure that overlay of an app is produced by a browser and not an app itself. Cyb solves this problem deterministically generating background and sound of overlay window in a way that an underlying app cannot know the seed for generating desired sound and visual pattern. The user need to remember its unique pattern once to safely interacting with different apps including not so trusted.

Another problem we are approach to solve with `.sign` is deferred transactions. Cyb has its own address for which an agent can delegate some rights. Using this API app developer can create a logic that allow create and execute complex sequences of transactions client side. Since inception of Ethereum we sign thousands of transactions and miss even more. That is why we believe this feature is critical for awesome web3 experience.

## .crr

According to [3 rules of root registry]() every developer can deliver best possible experience for their agents. That is why we want to mix the best from every word in our worlds in our implementation of root registry. To bring better user experience about 3k of records will be cybersquatted to align interests of existing app developers and agents who look for a beautiful, simple and trustful experience.

`.crr` is a potpourri of the most well known concepts consolidated under one namespace! Let me introduce what is included in the shake:

- [programming languages](https://gist.github.com/aymen-mouelhi/82c93fbcd25f091f2c13faa5e0d61760): up to 200 names
- [common programs](https://fileinfo.com/filetypes/common): up to 100 names
- [tokens](https://coinmarketcap.com/): Up to 1k names
- [top-level domains](https://en.wikipedia.org/wiki/List_of_Internet_top-level_domains): up to 300 names
- [top english words](https://github.com/first20hours/google-10000-english/blob/master/google-10000-english-no-swears.txt): up to 1k names
- [utf symbols](https://www.compart.com/en/unicode/category/So): up to 300 names

Initially cyber•Congress will own all this cybersquatted records. In order to improve probability of adoption of `.crr` cyber•Congres will distribute this names to original app developers based on proof of dns mechanism. That is, names for programming languages, common programs, tokens and top-level domains will be distributed based on a proof of dns according to verified registry produced by cyber•Congress.

Top english words and utf symbols will be distributed using competitions, grants and awards produced by cyber•Congress.

Initially unregistered names in `.crr` will be distributed under flat fee for cyb root registry owner in Chaingear. We are going to start from 1 ETH for every name and will see will it be enough to protect from abusive squatting or not. It is possible that we will switch to auction form of distribution in a future.

## .cyb

Extension over `.crr`.

Added fields: logo, tagline, manifest, meta, code, crr.

As result it become suitable to be an app store for browser. Appstore treats pinned apps as installed if at leas one permission is granted.

## .access

Permission management is of paramount importance in the process of safe application distribution. We want to improve upon 3 critical aspects of permission management in web:

- app authentication
- resource management
- dynamic permissions

*App authentication* is hard in web2. You need somehow know the origin and this is practically hard in a face of government level adversaries, than you must compute hash of received file and compare it with a file hash received from origin. Due to practical complexity nobody do that. In web3 if you know that address is correct authentication is done automagically. That is why browser can easily verify that permission is granted for expected app and not malicious.

*Resource management* was not in place. In web2 all permission systems was primarily build around a concept of granting access to a particular data which browser has access to. While this approach find itself useful it just not enough to run any application from untrusted developers. Computing resources has fundamental value now, thus must be carefully managed and metered. In web3 its weird that any untrusted app can eat all resources of a machine in no time. Moreover, if an application is executed in a sandbox all we need to feel ourselves safe (in addition to authenticated permissions) is ensure that app do not eat more resources than expected. Libraries that help app developers to mine some proof-of-work algorithms using visitor machine become ubiquitous. Practically that means that in addition to shity ads web2 users will experience even more worse web experience: greedy, slow and battery consuming apps are coming. The answer to this upcoming problem in a browser permission system which is able to produce bounds on apps consumption of fundamental resources such as cpu, gpu, ram, storage and broadband. We believe that resource management must be in the core of web3 application engine. We are currently doing research on how that can be implemented: containerisation seems to be low hanging fruit that can be embedded right into web experience.

*Permission affordances*. Current permission systems are static in a sense that browser provide limited set of predefined apis. Cookies, location, camera, microphone, sound and notifications: that is very limited set of things browsers can afford. Permissions of a third party developers are not native for a browsers either. Browser just don't care about what data with which apps agent want to share. We ask ourselves what if a browser can ask apps what kind of permissions they can provide thus exposing this permission system to any other apps? We believe this approach will allow web3 developers provide experience inaccessible for previous architectures.

## .feed

Notification panel displaying all pending transactions and web3 events corresponding to certain account.
Settings button leads to settings page where user can manage connection to IPFS, Ethereum and Cyber nodes (local or remote ways).

## .ipfs

This app is a third party app developed by IPFS Shipyard. This is very basic app for interacting with ipfs.

## .eth

Simple app which ger DURI requests and route requests to ethereum node (contracts, transactions and blocks). Else resolve ENS.

## .wallet

We believe that transfer of tokens is very basic experience in a web3 thus want to provide embedded in browser wallet app as soon as possible. Thus we consider either to develop our own bicycle or partner with some 3d party wallet developer.

## .dev

Developers experience is critical for the whole web3 adoption. This app helps to develop and publish web3 apps.

## .cg

[Chaingear](https://github.com/cybercongress/chaingear) is an app that help developers create ethereum based CRUD databases. We believe it will help developers to adopt web3 easier the same they MySQL helped to site developers in the very beginning of web.

## .help

Help is a two way help application. Using this app cyb helps agents to use itself. Using `.help` agents help Cyb evolve.

As an open source project we are welcome for contributions. Gitcoin is an excellent instrument that we use for delegating tasks for community a processing payments for completed ones.

We have our vision of how to develop browser and what kind of features develop first. But we give an opportunity for community to decide and vote with tokens what kind of browser we need to see in near future. Our product [Chaingear](https://github.com/cybercongress/chaingear) is also made for this.

We use user's feedback to make products better. So we provide options for bug reporting and feedback leaving on every page.

## .settings

Cyb settings

## Saga on privacy and anonymity

...

## On censorship resistance

...
