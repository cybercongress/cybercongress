---
date: 2020-04-21
url: launch-kit-guide
title: 'An awesome tool-kit for launching Cosmos-SDK and Tendermint-based projects'
author: serejandmyself
---

### TL;DR 
As a team, we have over 5 years of experience launching blockchain-related products and projects. One of our core principles is decentralization and transparency, hence we work in a 100% open-source manner. This not only relates to code, but to our documentation, organisation process and so on.

Another core principle that we follow is trying to deliver tools for others as we progress. To counter both of these principles we would like to share a launch-kit that was prepared by our team for the launch of [cyber](https://cyber.page/) (which is still ongoing). 

This tool kit includes various tools, build by ourselves or forked and modified from other awesome projects. Primarily these are tools for distribution params, conversion and exporting tools and tools for compiling the Genesis of your project. This post will overview the [launch-kit repository](https://github.com/cybercongress/launch-kit) and our suggested workflow for teams starting their own projects on [Cosmos](https://cosmos.network/). 

### The toolkit, Cyber and Cosmos 
To save a long story, here is the [awesome tool-kit](https://github.com/cybercongress/launch-kit) repository. 

[Cyber](https://github.com/cybercongress/go-cyber) is a decentralized google for provable and relevant answers. Its mission is to create an open semantics field of the internet, make knowledge accessible to anyone and to decentralize the services of the internet with the use of blockchain technology. You can use the slick [cyber.page](https://cyber.page/) to interact with cyber. 

To understand the toolkit fully, you should be aware that cyber made a real big accent on its distribution params. Our goal is to achieve the best possible distribution by using a distribution process, that consists of [several games](https://github.com/cybercongress/congress/blob/master/ecosystem/Cyber%20Homestead%20doc.md#the-distribution-games-in-detail) and [a gift to specific communities](https://github.com/cybercongress/congress/blob/master/ecosystem/Cyber%20Homestead%20doc.md#the-gift). Our other big accent is on governance and [community governed DAOs](https://github.com/cybercongress/congress/blob/master/ecosystem/Cyber%20Homestead%20doc.md#cybermetagalaxy). 

[Cosmos](https://cosmos.network/) is the internet of blockchains. According to its [intro](https://cosmos.network/intro), it is a decentralized network of independent parallel blockchains, each powered by consensus algorithms like [Tendermint](https://cosmos.network/intro#what-is-tendermint-core-and-the-abci) consensus. Tendermint and Cosmos-SDK are probably the most advanced tools that let you build your own blockchain. In fact, most of the work below was inspired by [The launch of Cosmos](https://github.com/cosmos/launch). 

### Who can use this toolkit? 
The toolkit is primarily addressed at 2 different groups: 

- Developers that want to launch their chain using Tendermint and/or Cosmos-SDK 
- Cybers heroes and masters, wanting to make sure that cyber launched as it says it did 

Of course, anyone is welcome to use it for any other purposes. 

### What's inside the toolkit 
Before we move on to the workflow and why you should use it, let’s examine what [this toolkit](https://github.com/cybercongress/launch-kit) contains: 

- [`Cosmos gift tool`](https://github.com/cybercongress/launch-kit/tree/0.1.0/cosmos_gift_tool): Takes Cosmos addresses on certain block height and pulls their balance 
- [`Cyber address converter`](https://github.com/cybercongress/launch-kit/tree/0.1.0/cyber_address_converter): Converts ETH and Cosmos addresses to Cyber addresses. For Cosmos addresses, we change the prefix and postfix, which is fairly simple. For ETH, we cannot calculate the address directly. We need to pull the pub keys. Pub keys are pulled only if there are any outgoing tx's for the specified address (and it's not a contract). We then proceed to use the pub keys and converts them to Cyber addresses 
- [`Cyberlink exporter`](https://github.com/cybercongress/launch-kit/tree/0.1.0/cyberlink_exporter): For migrating links between Cyber chains. Exports links from graph QL according to the subjects. In other words, it goes to the graph QL and collects unique links of an account. 
- [`Distribution`](https://github.com/cybercongress/launch-kit/tree/0.1.0/distribution): Contains files that make up the genesis. Shows what goes where 
- [`ETH gift tool`](https://github.com/cybercongress/launch-kit/tree/0.1.0/ethereum_gift_tool): ETH gift tool 
- [`Game reward calculations`](https://github.com/cybercongress/launch-kit/tree/0.1.0/game_rewards_calculations): Still in the making. Calculates rewards for Cybers incentivized game 
- [`Gen_tx`](https://github.com/cybercongress/launch-kit/tree/0.1.0/gen_txs): Genesis transactions. A process that describes the genesis ceremony and for it, we use the: 
- [`Genesis generator tool`](https://github.com/cybercongress/launch-kit/tree/0.1.0/genesis_generator_tool): It takes all the files, params, distribution, gifts, and gives out a .json file. This .json is used for the genesis ceremony at the Genesis block 
- [`Lifetime rewards tool`](https://github.com/cybercongress/launch-kit/tree/0.1.0/lifetime_rewards_tool): Calculates rewards for validators per their precommits on a certain chain-id 
- [`Urbit gift tool`](https://github.com/cybercongress/launch-kit/tree/0.1.0/urbit_gift_tool): Not consistent for the time being. A gift tool for Urbit addresses 
- [`Diagram of flow`](https://github.com/cybercongress/launch-kit/blob/0.1.0/pic/protocol.png): A diagram to help you understand our flow better and to plan your own flow 
- [`Crisis protocol`](https://github.com/cybercongress/launch-kit/blob/0.1.0/README.md#crisis-protocol): What to do in case of a failure 

### Why should you use this toolkit and how it can save you time? 
This is an excellent question. Well, we do have the answers, but I will assume that if you are coming to use it, you should already have some answers for yourself. If you are still unsure, let me try to explain why you should use this toolkit and how it can save you time! 

PoS-based chains have initial distribution trouble. If PoW chains kinda solve the issue: you burn some electricity (do an action) and receive a reward for it by securing the chain and helping it to communicate, then in PoS, the initial distribution is kinda left unravelled. 

We believe that the initial distribution of the project is uber important. Even if this distribution changes later, the initial stakeholders should be strong hands that are committed to the distribution. Obviously, it should be as fair as possible and include as many actors as possible. 

We took the biggest developers project out there (Ethereum), the most promising and our native project (Cosmos) and (probably) the most technologically advanced project (in the world) -Urbit. We gifted 10% of our supply to these projects to increase traction and to improve distribution. Hence, our gifting and converting tools. 

But this is just one step. Inspired by the [Game of Stakes](https://github.com/cosmos/game-of-stakes) we created our own [set of distribution games](https://github.com/cybercongress/congress/blob/master/ecosystem/Cyber%20Homestead%20doc.md#the-distribution-games-in-detail) to help us to achieve the best process tat targets 3 different user groups: believers, validators (infrastructure) and speculators. The kit contains a lot of numbers in the [`distribution` section](https://github.com/cybercongress/launch-kit/tree/0.1.0/distribution), check them out to get a better understanding of the distribution. 

There are other steps to this, and I suggest you check out [our docs](https://github.com/cybercongress/congress/blob/master/ecosystem/Cyber%20Homestead%20doc.md#moneybag-section-subtitle-beep-beep-beep) to understand the economics behind cyber. Which isn't simple and is designed like that for several reasons: 

- Achieving the best possible initial distribution 
- Protecting the economy at its infancy from dumps 
- Utilizing the utility of the protocol and providing agents with non-zero at stake incentives 

Distribution is important, but another important part that will save you time and money in the long term is using these tools to provide transparency. A good description of the launch process can help to make it clear, transparent and for users that will govern the protocol, make sure that you did not cheat. The launch protocol contains the so-called [`point of truth`](https://github.com/cybercongress/launch-kit#points-of-truth), which fix the most important steps on the flow diagram with an IPFS hash that can be checked by anyone wishing to do so. 

The tools provided by the kit can be recreated, forked, customized to your own needs and be used for planning an even more amazing distribution. 

The kit should be used at 3 different stages of your planning: 

1) Before the launch: Look at the flow diagram, some clusters let you understand what to do and how. They warn you of possible danger zones and let you know what you should do at this stage. For example, create a Genesis file with the distribution params, pick the communities you want to target, let the community discuss these params, decide on them and finally create a genesis file for the [launch ceremony](https://cybercongress.ai/genesis-ceremony/) 
2) During the launch: We can use the kit to launch any of our applications, count the hashes of files tor your own `points of truth`, plan proposals, DAOs, etc 
3) After the launch: The kit can provide a tool to calculate rewards if your launch included similar incentivized processes and of course serve as a basis to build your own kit 

### The DAOs and the governance 
We believe that technology does not require CEOs, CMOs and other fairy tale creatures. A good tech can live on its own. Blockchain helps to govern that tech and for shareholders to be represented. In other words, allows the tech to become independent of unnecessary bureaucratic hassle and other bingo-bullshit. 

In the flow diagram, we describe the creation of the community DAO, the launch of the initialization of roles, contracts, etc. For this post, I will not go into detail about how to do this, as we have already created a huge workflow for this specific purpose. 

You can find everything that you need in [this intro post](https://cybercongress.ai/euler-ceremony/), [cyber~Foundationrepostory](https://github.com/cybercongress/cyber-foundation) and our [awesome guide of how to create one DAO with another DAO](https://github.com/cybercongress/cyber-foundation/blob/master/euler-foundation/foundation.md) and supply it with the necessary tools (the guide will walk you through each tool and how to set it up). 

INSERT SMALLER VERSION OF WORKFLOW DIAGRAM ALES

### Flow for devs 
Now that we finally understand what the kit includes, why we should use it and what benefits it can give, here is a short workflow we would like to suggest for devs and hackers (of course, you are welcome to change anything, this is just a suggestion): 

1) Develop your distribution: Plan the Genesis file. Decide which communities you will attract and why. Think about the economics of your project. What percentage you want to give to what actors and for what reasons. As an example, you can view our [distribution directory](https://github.com/cybercongress/launch-kit/blob/0.1.0/distribution/README.md) 
2) Fill in the .json files, `cyber_distribution.json` and `manual_distribution.json` 
3) Decide on the params of the network with your community. Set the values up inside the `network_genesis.json`. You can use our [params folder](https://github.com/cybercongress/launch-kit/blob/0.1.0/params/README.md) 
4) Select the tools that you want and don't forget to format them per your own requirements, they should match your economy! If you have used any gifting tools, you will need to create a .csv file and use our [`converter` tool](https://github.com/cybercongress/launch-kit/blob/0.1.0/cyber_address_converter/README.md). If you're doing the distribution yourself, you will need our [`genesis generator` tool](https://github.com/cybercongress/launch-kit/blob/0.1.0/genesis-generator-tool/README.md) 
5) When everything is prepared, move it to `genesis-generator-tool/data` and use the same tool as above 
6) Run [a Genesis ceremony](https://cybercongress.ai/genesis-ceremony/) 
7) Launch [your DAO](https://github.com/cybercongress/cyber-foundation) and [governance](https://cyber.page/governance) 

### Links that may help you 
- [Our Homestead doc](https://github.com/cybercongress/congress/blob/master/ecosystem/Cyber%20Homestead%20doc.md): explains what goes where and who is who 
- [Our forum](https://cybercongress.ai/post/) for any questions
- [Game of Links](https://cybercongress.ai/game-of-links/) rules 

You are welcome to ask questions in our [TG chat](https://t.me/fuckgoogle) or open an issue in [this repository](https://github.com/cybercongress/launch-kit/issues) regarding anything in this post.
