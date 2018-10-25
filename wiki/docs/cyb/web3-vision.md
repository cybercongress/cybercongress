# DURA: a missing piece for web3

[@xhipster](https://keybase.io/21xhipster)
[cyberCongress](https://github.com/cybercongress)

Early draft for web3 summit. Looking for [a feedback](https://github.com/cybercongress/cyb).

## Abstract

Originally an [idea of web3](http://gavwood.com/web3lt.html) was inspired by Gavin Wood in 2014. A vision of Gavin was around 4 implementable concepts: content addressing, cryptographic identities, consensus computing and browsers. In parallel an idea of Interplanetary File System has been developed by Juan Benet. IPFS creates a foundation for web3: a system of content addressing and cryptographic identities. Since 2014 consensus computing has suffered insanely rapid development so one more missing piece is also in place. Still missing piece is a web3 browsing. Some projects such as Metamask has demonstrated a taste of web3. But one critical component in terms of browsing is just not there. URL scheme is outdated in terms of desired web3 properties and needs a drop in replacement. In this paper firstly we discuss necessary properties that we expect from web3. Based on this analysis we propose DURA scheme aka Distributed Unified Resource Address as drop in replacement for URLs that is being implemented in web3 browser [Cyb](/cyb.md). We believe DURA is a dump enough scheme (your captain) which can bring up basic consensus across web3 browser vendors due to simplicity, openness and protocol agnostic approach.

## Introduction

[Conventional protocols](https://tools.ietf.org/search/rfc6454) of the Internet such as TCP/IP, DNS, HTTPS and URL brought a web into the point there it is now. Along with all benefits they has created this protocols brought more problem into the table. Globality being a key property of the the web since inception is under real threat. Speed of connections degrade with network growth and from ubiquitous government interventions into privacy and security of web users. One property, not obvious in the beginning, become really important with everyday usage of the Internet: its ability to exchange permanent hyperlinks thus they would not break after time have pass. Reliance on one at a time internet service provider architecture allow governments censor packets. This fact is the last straw in conventional web stack for every engineer who is concerned about the future of our children. Other properties while being not so critical are very desirable: offline and real-time. Average internet user being offline must have ability to work with the state it has and after acquiring connection being able to sync with global state and continue verify state's validity in realtime while having connection. Now this properties offered on app level while such properties must be integrated into lower level protocols: into
very core of web3.

## Speed

Usability researches state that interactions that do not make sense in 100 milliseconds are considered as slow by an agent. Achieving such instant speeds is nearly impossible in the current stack of protocols. The following generation of the web must enable instant responses user requests. Necessity for lookup a location of resource using remote machine is an obvious bottleneck for reaching desired properties.

## Globality

Current internet is starting to split into regions mutually inaccessible for each other. China is de facto such a region. Some countries are very close to joining the club. It is of paramount importance that web3 would remain global even in the face of government level adversaries.

## Security

Current web applications are still in its infancy in term of permission abilities. Security of web apps is a very complicated topic. But one thing is obvious: it is hard to setup a secure system with third party apps without built in authentication system of the code being run on client machine. Current system of mutable resource location based on certificate authorities can not be safe by design.

## Permanent

We are all experience broken links. IPFS has immunity to this issue. As long as you keep a file anybody can access it using globally defined immutable in time address of this file computed from the file itself.

### Mesh ready

Current internet paradigm is based on 1 internet provider paradigm. That is basically a bad shit, because in general even if you have 2 or more internet connection like wifi and lte your device and/or operation system don't allow you to get the full possibilities of connectivity enforcing you to use only one connection at a time. Another major bad shit in current internet architecture is that your device is treated as leech by default. Every device keeps data necessary to being useful for surround devices. Huge portion of our network traffic goes not from origin server but from ISP cache. That means that changing a paradigm we can get to very different topology where our neighbors are our web3 providers.

## Verifiability

...

## Privacy and Anonymity

...

## Offline

...

## Realtime

...

## Roles

In a web of the third generation roles are not like in a web2. There is no clear split on users, internet providers and sites. Key difference is such that interactions can happen truly peer to peer the one can be sovereign enough to be their own internet.

- Apps. Any content hash can be an app if it is known how to parse it.
- Agents. An app can become an agent if she can prove that she exist by digital signature.
- Providers. Any agent that is able to serve content can be web3 provider.

## Content addresses

To understand why they so important we need to understand a difference in foundational concept of web2 and web3.

*Web2: Where => What-How*: You must know resource location on a particular server to retrieve it.

*Web3: What => How*: Instead of location based paradigm web3 is based on the content addressing paradigm. Key point is that we do not need to have knowledge of resource location in order to link to an object. In a web3 the answer to the *How* is either local or blockchain based registry with simple map between input address and address of an app.

## Cryptographic identities

...

## Consensus computers

There are some very exhaustive articles [around](https://multicoin.capital/2018/07/10/the-web3-stack/) [the topic](https://blockchainhub.net/web3-decentralized-web/) of [web3](https://avc.com/2018/07/the-web-3-stack/) which are really about consensus computing part of it.

Worth to note that saying that any particular blockchain or even all blockchains altogether is web3 is like saying that databases is world wide web. Yes databases technology contributed to a development of www, but without several protocols this databases would not become interconnected through billions of web sites. Remember that in order to implement a vision of full web3 potential we need to find drop in replacement for every piece of current protocol stack: IP, TCP, HTTPS, DNS and URL. None of currently deployed blockchain technologies don't have necessary properties to directly replace dinosaurs. I would say that distributed ledger technology is a better database stack for the upcoming web.

## DURA scheme

Distributed Unified Resource Address or put simply DURA is a more simpler and trustful scheme that has been used in a conventional web. It doesn't requires central authorities such as ICANN or others:

```
[local-handler]://[content-address].[root-registry-app]/[app-navigation]
```

We believe that a term `cyberlink` can be used for DURA links in order to differentiate with `hyperlinks` of previous internet architecture.

## Local handler

```
dura://
```

It is a local handler that every os can handle. Being fully optional it can be very important in the very beginning of web3.


## Content address

```
dura://QmQLXHs7K98JNQdWrBB2cQLJahPhmupbDjRuH1b9ibmwVa
```

If a browser is able to understand in which network she can resolve this particular content hash it can resolve it without much ado. Though we expect that IPFS will be not the only system and it become practically hard to say with 100% certainty whether given hash is ipfs hash or swarm or torrent or some other address type. That is there the concept of a root registry came into the game. In some sense it serves as an alternative to a self describing scheme used in CIDs. In some sense its not as it offer visually more sound links for agents. We believe that the root registry and self description concepts are complementary to each other.

## Root registry

Current state of DNS root management is outdated. The most bad thing is that we still must to trust the most important things in our lives to strange organizations such as ICANN, IANA.

We can ask ourselves why after 40 years of ubiquitous computer movement we still don't have simple common knowledge about what file extensions must be used with what software?

Our proposal is a concept of a root register. Structure of root register is a simple map between short name and ipfs hash of a program that is being triggered:

```
com:QmQLXHs7K98JNQdWrBB2cQLJahPhmupbDjRuH1b9ibmwVa
io:QmQLXHs7K98JNQdWrBB2cQLJahPhmupbDjRuH1b9ibmwVa
exe:QmQLXHs7K98JNQdWrBB2cQLJahPhmupbDjRuH1b9ibmwVa
pdf:QmQLXHs7K98JNQdWrBB2cQLJahPhmupbDjRuH1b9ibmwVa
eth:QmQLXHs7K98JNQdWrBB2cQLJahPhmupbDjRuH1b9ibmwVa
```

A name must be letter, number or hypen.

Purpose of a root register is to reach some very basic os and network agnostic agreement about what extensions with what programs must be used. Of course the problem with such registry is that it must be somehow and somewhere maintained.

## Three rules of a root registry

1. Software vendors must compete for a better root registry.
2. Software vendors must add setting with a change of a root registry.
3. Agents of browsers and operation systems must have ability to overwrite maps for local pleasure.

One of the implementation is a [cyb](QmQLXHs7K98JNQdWrBB2cQLJahPhmupbDjRuH1b9ibmwVa.md) root registry

## Root registry app

```
cyb://QmQLXHs7K98JNQdWrBB2cQLJahPhmupbDjRuH1b9ibmwVa.ipfs
```

This is an example of full DURA link that is able get hash of `ipfs` app in a root registry, than throw predicate into this app and get a desired resource from a peer to peer network.

```
Note: need to add real case of ipfs DURA app being used in Cyb.
Note: need to add real case on how web2 link can be resolved using DURA approach.
```

## App navigation

Traditionally its up to developers how to structure navigation within an app. But we believe that some scheme will be invented to differentiate statefull and stateless links as it is very important for

## DURA extensions

A lot of cool stuff can be implemented using extensions. Extension is any symbol that adds predictable an logical behavior for parsing and rendering of requests.

Examples:
- local paths
- connection links
- URL parameters

Key principle is that semantics is programmable and can be delivered from a distributed network using symbols that has been registered in a root registry.

## Where extension

Keyword:
- `/` before content address is a local path

Examples:
/users/xhipster/cybernode.ai
/ethereum/cybersearch.eth

## Linkchain extension

Keyword:
- `@` between DURA statements

Examples:
xhipster.eth@cybercongress.ai

Need to find cyberlinks between two cyberlinks.

## Reference

...
