---
project: cyb
---
# DURA: a missing piece for "The Great Web"

[@xhipster](0x7C4401aE98F12eF6de39aE24cf9fc51f80EBa16B)
[cyberCongress](https://github.com/cybercongress)

## Abstract

Originally an [idea of web3](http://gavwood.com/web3lt.html) was inspired by Gavin Wood in 2014. A vision of Gavin was around 4 implementable concepts: content addressing, cryptographic identities, consensus computing and browsers. In parallel an idea of [Interplanetary File System](https://ipfs.io/ipfs/QmV9tSDx9UiPeWExXEeH6aoDvmihvx6jD5eLb4jbTaKGps) has been developed by Juan Benet. IPFS creates a foundation for web3: a system of content addressing and cryptographic identities. Since 2014 consensus computing has suffered insanely rapid development so one more missing piece is also in place. Still missing piece is a web3 browsing. Some projects such as Metamask has demonstrated a taste of web3. But one critical component in terms of browsing is just not there. URL scheme is outdated in terms of desired web3 properties and needs a drop in replacement. In this paper we propose DURA scheme aka Distributed Unified Resource Address as drop in replacement for URLs based on desired properties of "The Great Web" some of them has been defined in an article [An idea of decentralized search for web3](https://steemit.com/web3/@hipster/an-idea-of-decentralized-search-for-web3-ce860d61defe5est). DURA is being implemented in web3 browser [Cyb](/cyb.md). We believe DURA is a dump enough scheme (your captain) which can bring up basic consensus across web3 browser vendors due to simplicity, openness and protocol agnostic approach.

## Introduction

Current state of DNS root management is outdated. The most bad thing is that we still must to trust the most important things in our lives to strange organizations such as ICANN, IANA.

We can ask ourselves why after 40 years of ubiquitous computer movement we still don't have simple common knowledge about what file extensions must be used with what software?

Distributed Unified Resource Address or put simply DURA is a more simpler and trustful scheme then the scheme which has been used in a conventional web. In it's root it doesn't requires central authorities such as ICANN. Also, proposed approach do not depends on any blockchain based registry such as [ENS](https://docs.ens.domains/), [Chaingear](https://github.com/cybercongress/chaingear/blob/master/whitepaper.md) or [Handshake](https://handshake.org/files/handshake.txt) though. Only agents define which content type is being processed by which app. Using "Cascading Name Registries" technique the principle can be practical enough to become universal without harming a will of agents.

## DURA scheme

```
[protocol]://[query].[app]
```

We believe that a term `cyberlink` can be used for DURA links in order to differentiate with `hyperlinks` of previous internet architecture. Further we discuss some details of a proposed linking convention.

## Protocol

```
dura://
```

It is a local handler that every os can handle. Being fully optional it can be very important in the very beginning of web3. If a browser do not know the protocol handler of a link it can look up the handler in a root registry.

## Query

```
dura://QmQLXHs7K98JNQdWrBB2cQLJahPhmupbDjRuH1b9ibmwVa
```

If a browser is able to understand in which network she can resolve this particular content hash it can resolve it without much ado. Though we expect that IPFS will be not the only system and it become practically hard to say with 100% certainty whether given hash is ipfs hash or swarm or torrent or some other address type. That is there the concept of a root registry came into the game. In some sense it serves as an alternative to a self describing scheme used in CIDs. In some sense it is not, as it offers visually more sound links for agents. We believe that the root registry and self description concepts are complementary to each other.

## App

The key in our proposal is a concept of a root register. Structure of root register is a simple map between short name and ipfs hash of a program that is being triggered:

```
com:QmQLXHs7K98JNQdWrBB2cQLJahPhmupbDjRuH1b9ibmwVa
io:QmQLXHs7K98JNQdWrBB2cQLJahPhmupbDjRuH1b9ibmwVa
exe:QmQLXHs7K98JNQdWrBB2cQLJahPhmupbDjRuH1b9ibmwVa
pdf:QmQLXHs7K98JNQdWrBB2cQLJahPhmupbDjRuH1b9ibmwVa
eth:QmQLXHs7K98JNQdWrBB2cQLJahPhmupbDjRuH1b9ibmwVa
```

A name must be letter, number or hypen.

Purpose of a root register is bring to reach some very basic os and network agnostic agreement about what extensions with what programs must be used. Of course the problem with such registry is that it must be somehow and somewhere maintained.

```
dura://QmQLXHs7K98JNQdWrBB2cQLJahPhmupbDjRuH1b9ibmwVa.ipfs
```

This is an example of full DURA link that is able get hash of `ipfs` app in a root registry, than throw predicate into this app and get a desired resource from a peer to peer network.

## Implementation in browsers

1. Software vendors must compete for a better root registry.
2. Software vendors must add setting with a change of a root registry.
3. Agents of browsers and operation systems must have ability to overwrite maps for local pleasure.

One of the implementation is a [cyb](QmQLXHs7K98JNQdWrBB2cQLJahPhmupbDjRuH1b9ibmwVa.md) root registry

Cascading name registries

## DURA extensions

A lot of cool stuff can be implemented using extensions. Extension is any symbol that adds predictable and logical behavior for parsing and rendering of requests.

The following extensions can demonstrate the flexibility of an approach:

- app navigation
- app state
- local paths
- link chains
- URL parameters

Key principle is that semantics is programmable and can be delivered from a distributed network using symbols that has been registered in a root registry.

## App navigation

Traditionally it is up to developers how to structure navigation within an app.

Keyword:
- `/` after the main body

Example:
cybernode.ai/dashboard

## App state

It can be useful to have simple convention on how to reflect state of an app on a particular block.

Keyword:
- `!`

Example:
cybernode.ai/dashboard!1567485

## Local paths

Dura can be easily extended with conventional requirement of pointing to a certain place in a current device directory structure:

Keyword:
- `/` before the main body

Examples:
/users/xhipster/cybernode.ai
/ethereum/cybersearch.eth

## Link chains

Keyword:
- `@` between DURA statements

Example:
xhipster.eth@cybercongress.ai

## Key-value parameters

Keywords:
- `?` start of kv params
- `&` start of kv clause
- `=` denote key and value

Example:
- page?name=ferret&color=purple

## Reference

1. [Idea of web3](http://gavwood.com/web3lt.html)
2. [Interplanetary File System](https://ipfs.io/ipfs/QmV9tSDx9UiPeWExXEeH6aoDvmihvx6jD5eLb4jbTaKGps)
3. [Cyb](https://github.com/cybercongress/cyb/blob/dev/docs/cyb.md)
