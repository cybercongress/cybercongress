# A vision for web3
@xhipster @asadovka

## Introduction

Originally an idea of web3 was inspired by Gavin Wood http://gavwood.com/web3lt.html

Proplems of web2:

- Monopolization of traffic by tech companies (gates, servers)
- Monopolization of resources by tech companies (computing power, datacenters)
- Monopolization of broadband sources such as ISP providers

Problematics is defined by video [need to transcript].

Original protocols of the Internet such as TCP/IP, DNS, URL and HTTPS brought a web into the point there it is now. Along with all benefits they has created they brought more problem into the table. Globality being a key property of the the web since inception is under real threat. Speed of connections degrade with network grow and from ubiquitous government interventions into privacy and security of web users. One property, not obvious in the beginning, become really important with everyday usage of the Internet: its ability to exchange permanent hyperlinks thus they would not break after time have pass. Reliance on one at a time internet service provider architecture allow governments censor packets is the last straw in conventional web stack for every engineer who is concerned about the future of our children. Other properties while being not so critical are very desirable: offline and real-time. Average internet user being offline must have ability to work with the state it has and after acquiring connection being able to sync with global state and continue verify state's validity in realtime while having connection. Now this properties offered on app level while such properties must be integrated into lower level protocols.

## Properties

- Simple
- Fast
- Global
- Secure
- Private
- Permanent
- Offline
- Realtime
- Meshready

### Mesh ready

Current internet paradigm is based on 1 internet provider paradigm. That is basicaly a bad shit, because in general even if you have 2 or more internet connection like wifi and lte your device and/or operation system don't allow you to get the full possibilities of connectivity enforcing you to use only one connection at a time. Another major bad shit in current internet architecture is that your device is treated as leech by default. Every device keeps data necessary to being useful for surround devices. Huge portion of our network traffic goes not from origin server but from isp cache. That means that changing a paradigm we can get to very different topology where our neighbours are our web3 providers. 

## Roles
- Agents
- Dapps
- Web3 provider

### Web3 providers

Any neigbour node can be web3 provider

### Dapps

Any content hash is dapp

### Agents

Agents are dapps who can change it's state using signed transaction.

### Contracts

Contracts are agents who don't have will.

## Key concepts

- content addressing
- digital signatures
- consensus computing

### Content adrreses

To understand why they so important we need to understand a difference in foundational concept of Web3 and web3

Web2: Where => what-how. Instead of location based paradigm is based on content addressing paradigm. Key point is that we do not need to have knowledge of location such as domain name in order to link to an object

Web3: What => How. Register with simple map between input and hash of an app. If no input return self

### Digital signatures

Saying that any particular blockchain or even all blockchains altogether is web3 is like saying that databases is world wide web. Yes databases technology contributed to a development of www, but without several protocols this databases would not become interconnected through billions of web sites. That is, in order to implement a vision of full web3 potential we need to find drop-in replacement for IP, TCP, HTTPS and DNS. None of currently deployed blockchain technologies don't have necessary properties to directly replace dinosaurs. I would say that distributed ledger technology ...

### Consensus computers

A notion of consensus computers is ... 

## DURA

Distributed Unified Resource Address

```
[local-handler]://[content-address].[root-registry-name]//[app-navigation]
```

### Local handler
cyb:// - is local handler that every os can handle. Being fully optional it can be very important in the very begining of web3
The most important part in this expression is the dot

### Content address
```
cyb://QmQLXHs7K98JNQdWrBB2cQLJahPhmupbDjRuH1b9ibmwVa.ipfs//files/explorer
```

### Root registry

Current state of DNS root management is outdated. The most bad thing is that we still must to trust the most important things in our lives to strange organizations such as ICANN, IANA

...Our proposal is that different browser software can choose

We can ask ourselves why after 40 years of ubiquitous computer moment we are still don't have simple common knowledge about what file extensions must be used with what software?

Our proposal is a concept of a root register. Structure of root register is a simple map between short name and ipfs hash of a program that is being triggered:

```
com:QmQLXHs7K98JNQdWrBB2cQLJahPhmupbDjRuH1b9ibmwVa google.com
io:QmQLXHs7K98JNQdWrBB2cQLJahPhmupbDjRuH1b9ibmwVa
exe:QmQLXHs7K98JNQdWrBB2cQLJahPhmupbDjRuH1b9ibmwVa
pdf:QmQLXHs7K98JNQdWrBB2cQLJahPhmupbDjRuH1b9ibmwVa
```
A name must be letter, number or hypen


Purpose of root register is to reach some very basic os and network agnostic agreement about what extensions with what programs must be used. Of corse the problem with such registry is that it must be somehow and somewhere maintained.

### Three rules of root registry

1. Software vendors must compete for a better root registry
2. Software vendors must add setting with a change of a root registry
3. Users of browsers and operation systems must have ability to overwrite maps

One of the implementation is a [cyb](QmQLXHs7K98JNQdWrBB2cQLJahPhmupbDjRuH1b9ibmwVa.md) root registry

### App navigation

Traditionally its up to developers is how to structure navigation within an app. We believe that in dapp movement we 


### Root keyword
- . is the thing

Examples:
- cybernode.ai 0x1ec498ae753774989b7fd3ac6f84054385bb98d21e98ef5d524a9e77c941cf51.ethtx
- cybernode.eth

New approach for paths in web3:
- local file paths ~~versus~~ are global paths. Merge filesystem paths and internet paths
- thinking how to get resource, not where. file extensions and 1 level tlds are the same things
- right segment explains how to parse left segment. Maps in chaingear.

### DURA Extensions

A lot of cool stuff can be implemented using extensions. Extension is any symbol that adds predictable an logical behavior for parsing and rendering of requests.

Examples:
- local paths
- connection links
- CID stuff
- URL parameters

Key principle is that semantics is programmable and can be delivered from distributed network

### Where extension

Keyword:
- under / left part is local path

Examples:
/https/cybernode.ai
/ethereum/cybersearch.et

Need to extend global paths to local paths

- under right is state

### Linkchain or cyberlink extension

Keyword:
- at @

Examples:
xhipster.eth@cybetfund.ai

Need to find link between two entries

## On censorship resistance
    - writing data (medium, EOS)
    - reading data (gitcoin)

## Reference

https://multicoin.capital/2018/07/10/the-web3-stack/

https://blockchainhub.net/web3-decentralized-web/

https://avc.com/2018/07/the-web-3-stack/

https://blog.stephantual.com/web-3-0-revisited-part-one-across-chains-and-across-protocols-4282b01054c5

Worth to note that this links covers some aspects but do note catch the whole thing. 

https://tools.ietf.org/search/rfc6454
http://127.0.0.1:8080/ipfs/QmR7GSQM93Cx5eAg6a6yRzNde1FQv7uL6X1o4k7zrJa3LX/ipfs.draft3.pdf
Not good

https://github.com/bitcoin/bips/blob/master/bip-0122.mediawiki

ERC 190 Package manager

https://github.com/ethpm/ethpm-spec/blob/v1.0.0/release-lockfile.spec.md

https://github.com/ethereum/EIPs/issues/190
