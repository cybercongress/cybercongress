# The ELI-5 FAQ for Cyber 
> What is Cyber? How does it work? How to use it? 

This guide will, hopefully, answer these and many other questions in very simple terms.

If you want to help, then submitting more questions to this guide can be the best way to do so. To submit questions to this FAQ use [GitHub issues](https://github.com/cybercongress/congress/issues). If you don't have a GitHub account or you are unsure how to open an issue, simply tag `serejandmyself` in our [TG channel](https://t.me/fuckgoogle), and leave your question there.

You may skim through questions, of course, but I recommend you to `buckle up your seat belt` and read it all. The first section `Like google, but Cyber` explains everything you need to know to understand how Cyber works.

*But, first:*
## What is a FAQ?
A FAQ is a list of frequently asked question that tries to gather as much as possible information about the project in one place. The purpose of this is to to give the reader a basic overview of a specific subject, and if necessary, refer the reader to more detailed information. 

-------------------------------

## Table of content
- [Like google, but Cyber](https://github.com/cybercongress/congress/blob/master/ecosystem/ELI-5%20FAQ.md#like-google-but-cyber): What is cyber and what problem does it solve
- [Under the hood, part-1](https://github.com/cybercongress/congress/blob/master/ecosystem/ELI-5%20FAQ.md#under-the-hood-part-1): A very high-level explanation of what are blockchain and web3 technologies
- [How does Cyber work and how do I use it?](https://github.com/cybercongress/congress/blob/master/ecosystem/ELI-5%20FAQ.md#how-does-cyber-work-and-how-do-i-use-it): How can you use cyber and what are the basic incentives for you to do so
- [Under the hood, part-2](https://github.com/cybercongress/congress/blob/master/ecosystem/ELI-5%20FAQ.md#under-the-hood-part-2): How to validate Cyber, what is a knowledge graph, what are the distribution games, etc...
- [The philosophy behind Cyber](https://github.com/cybercongress/congress/blob/master/ecosystem/ELI-5%20FAQ.md#the-philosophy-behind-cyber): Why are we building Cyber?
- [Silly, yet, VIP questions](https://github.com/cybercongress/congress/blob/master/ecosystem/ELI-5%20FAQ.md#silly-yet-vip-questions): How does Cyber compare to others, how is Cyber safe from abuse and many other VIP things
- [Links](https://github.com/cybercongress/congress/blob/master/ecosystem/ELI-5%20FAQ.md#links): Some links to help you navigate around Cyber and get more insight on what has shaped it

---------------------------------

## Like google, but Cyber:
#### What is cyber?
*Simple answer:*<br>
Cyber is a decentralized google. It is an innovative search protocol that can provide provable answers to questions without an intermediary opinion. 

*Detailed answer:*<br>
Cyber is a brand new protocol (a procedure that helps computers to do things in a certain way) for adding and searching information onto a knowledge graph (a compilation of facts about something that provides meaning to the user). And rank this information. In other words, it's a decentralized google. 

This protocol exists thanks to such technology as blockchain and what is referred to, as content addressing (a way to locate information on the web using the content, rather than referring to its location, by such, avoiding censorship).

But why do we need a new way to search for things? Well, there are 2 reasons. One, we want to decentralize the service of the web. This is social media, search and even e-commerce, etc, which are all based around semantics (the meaning and the relation of words and objects). The problem is that the current semantical field, that we use every day, is built pretty much by one company, allowing it to sell data, provide users with misleading information and to effectively censor data. And here we come to Cybers second task, the creation of an open semantics field. 

Google is essentially a huge marketplace, where someone is searching for content and the other side provides this content. You can purchase most of googles services, but you cannot purchase the ability to search without bullshit and advertisement. Moreover, you cannot search for many things. The original vision of the internet was to share knowledge freely. Currently, this is not the case. We pay for academical papers, we cannot freely share information. Hence projects like WikiLeaks, arXiv.org, tor, etc exist. 

You may think of Cyber is a huge Wikipedia without censorship, which is at the moment, waiting to be filled with knowledge from the current web, by a transition to the new web. A web which you control. A web that is free of censorship. A web where the internet works for you and not the other way around.

But how does this all work and can this really be used for something rather than just search? Well, imagine a simple graph. This graph has an X-axis and a Y-axis. For now, let's label the X-axis `from` and the Y-axis `to`. Now imagine that you want to end up at any point of this graph. You need to fill in 2 bits of information. From and to. The from in our case is a search word that will identify the content. This is what shapes the semantics field.  The `to`, is the content itself. So far simple.

<img src="https://i.postimg.cc/VkbNs6vd/photo-2020-05-14-03-54-50.jpg" />

To make the content and the keyword immutable, we use what we call content identifiers. For now, we work with a technology called IPFS, which is, basically, a distributed p2p storage, where users can safely store and exchange data (but Cyber can work with any similar technology, DAT, GIT, Bitcoin, Ethereum, Swarm, etc). 

This means that to add anything to the graph, the users need to use IPFS hashes (hash is simply an encrypted pointer to a certain value that lets us make sure that what is pointed to is actually what is pointed to and not something else). Users use the 2 links to create what we call a cyberlink. A Cyberlink is exactly what is described above, a link between the X and the Y, where one thing is the keyword and the other is the content. 

There is no transactional fees in Cyber, this means that it doesn't cost anything to add information to the graph. But we need to limit spam, this is why Cyber uses an energy model. Where users have a certain amount of energy that they can spend over a certain period of time before it recharges. Just like your phone or tablet.

As this content gets added the graph is filled with more and more knowledge. Hence, the reference to Wikipedia. This knowledge needs to somehow be indexed and ranked. There is so no censorship in Cyber. All of the indexing and ranking is done with the help of a transparent mechanism that everyone knows of. This work is done by validators (a program or a computer that are responsible for checking the validity of something). The validators do so, by using their GPU's (literally - graphics cards). 

That content is dynamically ranked with the help of digital tokens and the current parameters of the networks load. This makes the rank dynamic (characterized by continuous change, activity, or progress) and, literally, alive. All these parameters can be changed by the users, as they are the stakeholders.

Because we use hashes and blockchain technology, we can root to the origin of the links and make sure that the content came from where it says it has. Basically, allowing for a simple provable mechanism.  

At first, this makes up for a perfect search engine, without a blackbox intermediary. But going back to our graph, we can imagine, that such a graph can be used in many cases. For example, unified semantics, because hashes don't care about what language was used by the person who added the content. Or autonomous robots, because they are built on simple ML algorithms, which are in turn based on semantics too. There are many use cases for this. But most importantly, this leaves us in control of our own data. Allowing us to decide what to do with it. Also, this helps us to create relevance between objects on the graph, without any opinions that are sold to us daily by different megacorps. 

##### Fun fact
On the topic of immutability and unified semantics. What is one of the most popular things that communication on the internet gave birth to? Emojis! They have become a separate language of their own, understood by anyone, regardless of race, gender, age, colour, whatever...

Have you ever tried Googling Emojis? It is an example of a language NOT understood by Google, but understood by Cyber thanks to its brand-new search architecture. Google can actually search one Emoji, but that brilliant machine does not understand when I do this:
🧑🏻‍🤝‍🧑🏽 👮 ☮️, `all lives matter` maybe?

Let's try [cyber.page](https://cyber.page/search/%F0%9F%A7%91%F0%9F%8F%BB%E2%80%8D%F0%9F%A4%9D%E2%80%8D%F0%9F%A7%91%F0%9F%8F%BD%20%F0%9F%91%AE%20%E2%98%AE%EF%B8%8F) - and...it works! Emoji is a language. It should be searchable!     

#### What problem are you solving?
Cyber solves the problem of opening up the centralised semantics field of the internet. It does so by shaping an open and accessible semantics field, created (and managed) by the users. This allows to design a trustless, provable and incentivized method of communication between users who provide content and those searching for it. Effectively removing censorship, blackbox intermediary opinions and opening the possibility for a provable, incentivized and a fairer method for anyone to build and use online tools that are built around semantics.

#### What is your mission?
Cyber is an innovative, general-purpose search mechanism for
obtaining answers.  Its mission is to create a universal search mechanism to:
(a) build an open semantic field of the internet with the help of blockchain technology and cyberlinks, and
(b) provide more resistance to web services through decentralization of its infrastructure

#### What's the value proposition?
Cyber can be defined as a smart, distributed computer. It can process, store and compute value in the form of providing answers to questions. At first glance, this might seem like a very primitive utility, suited, maximum, for an innovative browser. But that is far from the case. First of all, it is worth pointing out that Cyber provides useful computations! It is one of the first times in the history of blockchain technology where the computations done by the distributed computer have obvious and useful utility, not just to the end-user, but to the whole world. The forming of relevant and provable answers, that will shape an open semantics field.

An open semantics field lets you shape the internet differently. It allows users with interest in prosperity to receive more by using yesterdays' tools. It can make these instruments fairer, more efficient and more relevant. The basic idea is to create an Intercommunication Knowledge Protocol that can interact with everything that is defined by the user. Cyber can account for a large number of use-cases, like: unified semantics, autonomous robots, programmable semantics, personal assistants, language convergence, universal oracles, proof of location and much more. All of these cases are built on semantics. Even including naive cases like e-commerce, that can flourish fairly on local markets, thanks to a distributed, accessible knowledge graph. Queries can be delivered straight out of your personal browsing application. Answers can provide subjective relevance that is important at the time, at the place, to a particular community and/or projects.

Other cases, like social networks, prediction markets, offline search, etc are also possible but are less global, although can have more reach, based on consumer behaviour. The ability to create a Wikipedia without the censorship and blackbox intermediaries is astonishing. The idea of recreating search at its original vision, where you can search for academic papers, search inside of a social network, interact with your own search results, etc, is astonishing.

Cyber can be used for communication with your own database of knowledge. This means, that you control your data. This opens up a multi-billion dollar market of data selling to individuals, who now choose what to do with their data. Other, more far-fetched cases can exist. For example, if I am a trader that searches and trades, I produce metadata I can interact with locally. It can help me to answer where my trades went wrong (with the help of analysing that data of course). 

Cyber can create local, subjective oracles of data that can be sold. If we provide cyber with the ability to work with second layer semantics (emotions), it can re-create a local, subjective happiness mechanism. Or count the risk of something happening, based on the local semantics field. Of course, this is all up to the users. Cyber allows deleting the boundary between the content provider, the content receiver, the service provider and the service receiver.

#### What cyber is NOT?
Cyber is not the new internet. It is a tool that can help to shape and to decentralize (distribute the power of authority) the services of the new, Great Web. 

Cyber is not a commercial product. It is an instrument if you wish, or a tool, that anyone can use. That said, Cyber allows for several ways for its participants to earn rewards and Cyber is a technology that belongs to its users.

---------------------------------

## Under the hood, part-1:
To understand Cyber, you might want to understand the technology it's using. This is a brief overview. For more information, check the [homestead guide](https://github.com/cybercongress/congress/blob/master/ecosystem/Cyber%20Homestead%20doc.md#technical-questions-in-plain-terms)

#### What is a blockchain?
A blockchain is a distributed ledger, to which independent participants write, and read from it, information. It is protected from malicious attacks (such as creating an entry which shouldn't be there) due to its distributed nature. The ledger is distributed across computers, which are in agreement one with another at any point of a given time (past or present). All the transactions on the ledger are auditable to anyone and transparent. This allows the participants to make sure that there is nothing shady happening in the background. Usually, data in blockchains is structured with the help of a Merkle tree or a Directed Acyclic Graph (more commonly knows as a DAG, which in very basic terms, is just a different way of structuring data). 

#### What is web3?
Web3 is the next evolutionary step in the development of the web. A step that takes away from centralisation of search and social services and away from things that are depended on a single functioning unit (have a central source of authority). It is a step that desires to see involved counterparties and applications communicate directly one with another. In agreement with each other, whilst also, motivate users for their behaviour. And as a result, achieve a safer routing of data and packets (information exchange) on the web.

Often, you might notice the term `Great Web` in our documents. For us, The Great Web is a much better-suited name for the more common term `web3`.

#### What is IPFS?
IPFS is a peer-to-peer (directly connected between two users) protocol, that is designed to make the web faster, safer, and more open. IPFS makes it possible to spread across high volumes of data and keeps every version of your files. IPFS makes it simple to set up networks for mirroring data. This means that data is pretty much immutable or if you may - everlasting.

IPFS helps to further distribute the web amongst peers (users). It enables constant availability — with or without internet connectivity. You can share and view files, manage large chunks of data, build applications, etc. 

#### Why use this technology?
To create a safer, trustless and a censorship-free environment, where no 1 entity, actually, `owns` the technology. To create an environment free of bureaucracy, underwater obstacles, etc. An environment in which the stakeholders govern and manage the technology as a collective mind.

#### Why should I care?
First of all, you shouldn't! It is up to you to decide what you care about and what you don't. However, if you care about our future being less centralized, less authoritative and fairer, then it makes sense to decentralise the services of the technology that binds us all together. Of course, I am referring to the internet. 

-------------------------------

## How does Cyber work and how do I use it?
#### How do I use Cyber?
Our main app, [cyber.page](https://cyber.page/), allows you to search for content on the knowledge graph and create cyberlinks. It also lets you participate in the governance of Cyber, sends tokens, take part in our gamified mechanics and explore all the other possibilities of the protocol. For now, searching is as simple as googling. However, the creatin of cyberlink via the app requires a [Ledger](https://www.ledger.com/). 

To learn how to use cyber.page and the other tools described below, please use these [step-by-step guides](https://github.com/cybercongress/congress/blob/master/ecosystem/Cyber%20Homestead%20doc.md#connecting-to-cyber). 

cyb~Virus is an extension for Chrome and Firefox that allows you to create cyberlinks by downloading content into IPFS with a few simple clicks. It also acts like a wallet, i.e. like [Metamask](https://metamask.io/).

There are several other, [community-maintained tools](https://github.com/cybercongress/congress/blob/master/ecosystem/Cyber%20Homestead%20doc.md#community-maintained-profiles-and-tools) that you may want to check out.

#### What is a cyberlink?
Cyberlink is a link between 2 IPFS hashes. Where one hash points to the keyword that makes the content searchable. And the second hash points to the content itself. A cyberlink allows us to pinpoint a specific location on the graph. [Take a look](https://cyber.page/graph) at how things look inside of a graph!

#### How do I create a cyberlink?
You can create a cyberlink by providing 2 pieces of what makes it up. A `from` part, which is the keyword. And the `to` part, which is the content. Both are content identifiers, which are, currently, IPFS hashes. We recommend using [cyber.page](https://cyber.page/) to create one. Learn how-to.

If you don't have a Ledger device, please use one of [the other tools](https://github.com/cybercongress/congress/blob/master/ecosystem/Cyber%20Homestead%20doc.md#connecting-to-cyber). 

#### Are transactions free?
Yes. Cyber uses what we call an [`energy` model](https://github.com/cybercongress/congress/blob/master/ecosystem/Cyber%20Homestead%20doc.md#advanced-explanation). This acts as a spam protection mechanism and makes transacting free. Your energy regenerates get used when you create a transaction and regenerates after some time. 

Transactions in Cyber shape the semantics field. 

#### How many tokens do I need to use it?
This depends on the current parameters of the networks load, which can be checked [here](https://cyber.page/network/euler/parameters). Generally, this is a very low amount. bare in mind, that you don't actually spend any tokens, you just freeze them to prove your intention.  

#### Where can I get tokens?
Tokens can be obtained in several ways. One is by claiming a gift that was intended for ETH, ATOM and Urbit users. Learn how-to [here](https://github.com/cybercongress/congress/blob/master/ecosystem/Cyber%20Homestead%20doc.md#claiming-the-gift).

Another way is to use [our faucet](https://cyber.page/gol/faucet). We recommend to check out [this guide](https://cybercongress.ai/how-to-get-eul-tokens-if-you-have-none/). 

When you have tokens, enjoy playing the [Game of Links](https://cyber.page/gol) to obtain even more tokens.

#### What is a CID?
A [CID](https://github.com/cybercongress/congress/blob/master/ecosystem/Cyber%20Homestead%20doc.md#glossary) is a content identificator. In our case, it is also an [IPFS hash](https://github.com/cybercongress/congress/blob/master/ecosystem/Cyber%20Homestead%20doc.md#glossary). That means its a something that represents (or rather - points to) a specific file/piece of data within the IPFS database.

#### How many tokens do you have?
There are 2 tokens. 

[CYB](https://github.com/cybercongress/congress/blob/master/ecosystem): the token of our network, which has 3 primary uses: (1) staking (securing the network and receiving rewards), (2) bandwidth limiting for submitting links (energy), and (3) expression of intentions for indexing and ranking the content. 

There are  1 000 000 000 000 000 CYB (one Peta CYB or 1 PCYB). There is currently no such thing as the maximum amount of CYB tokens, this is due to the continuous inflation paid to the network validators.

[THC](https://github.com/cybercongress/congress/blob/master/ecosystem): an Ethereum ERC-20 compatible token has utility value in the form of control over [cyber\~Foundation](https://github.com/cybercongress/cyber-foundation) (an Aragon DAO) and the ETH from the [auction](https://github.com/cybercongress/congress/blob/master/ecosystem/Cyber%20Homestead%20doc.md#cyberauction-or-auction) proceeds.

One of the core values of THC, is the ability to be able to receive CYB tokens (1 to 1) for anyone staking THC during cyber\~Auction. Prior to Genesis cyber~Congress has minted 750 000 000 000 000 THC (seven hundred and fifty Tera THC).

The third, non-transferable, and non-tradable token, is called [Karma](https://github.com/cybercongress/congress/blob/master/ecosystem/Cyber%20Homestead%20doc.md#general-questions). Karma can be thought of as a token, but it's closer to your reputation. Karma points are gained by users when they create cyberlinks.

#### Why do you have 2 tokens?
1) There is no technical possibility to create 2 tokens with such features using 1 network

2) It allows us to create 2 independent, yet, connected entities. One that acts as a fund governed and managed by the users in ETH. And the second as the main utility token of the network

#### What is the [allocation breakdown](https://github.com/cybercongress/launch-kit/tree/0.1.0/distribution)?
CYB tokens breakdown, initial supply: 1,000,000,000,000,000:
- cyber~Congress*: 6% of CYB
- cyber\~FundClassic: 3% of CYB (a fund to help growing the ecosytem)
- Seed donors*: 4% of CYB
- Inventors of the protocol*: 2% of CYB
- Gift allocated to over 1 million addresses: 10% of CYB
- Other public allocation: 75% of CYB
* These groups get THC tokens and can [vest them](https://cyber.page/gol/faucet/vest) to receive CYB

THC tokens breakdown (governance tokens), total supply: 750,000,000,000:
- 20% cyber~Congress team + inventors + seed donors + development fund (which IF vested gain the max. above CYB allocation)
- 80% Public allocation

#### Is the inflation endless?
The inflation parameters are defined by [governance](https://cyber.page/governance).

#### Why IPFS/Cosmos and how do you use them?
Cyber uses IPFS as the current backbone, where users store content and where users perform the search. Think about IPFS for cyber, as of the fridge, and cyber is the lightbulb inside of it. Users use IPFS to store and publish content and files. cyber lets users rank, index and find it. If there was no lightbulb, how would you find food in the fridge during those hungry nights?

[IPFS](https://ipfs.io/) is revolutionary. It is the first protocol that created content-based addressing, which allowed cyber to build cyberlinks on top of it and change the way we search for information. In the future, we plan to use any other protocol that is capable of creating a cyberlink (DAT, GIT, Swarm, Bitcoin, Ether, etc).

[Cosmos](https://cosmos.network/) provides the consensus mechanism for cyber. We use Tendermint as an engine that helps the network to reach agreement on its current state, perform transactions on the blockchain, validate search results, etc. (1) When we started to build Cosmos was already in mainnet. (2) Cosmos has [IBC](), a protocol that allows for data transfer between sovereign blockchains. (3) We share the decentralized, non-monolithic philosophy that Cosmos preaches. (4) The security of Tendermint and Cosmos-SDK is top-notch.

#### What other technologies do you use?
Cyber strives to be chain-agnostic. This means we will use [any trustless and censors free technology](https://github.com/cybercongress/congress/blob/master/ecosystem/Cyber%20Homestead%20doc.md#the-manifest) that can help us to achieve results. 

Currently, we use [CUDA](https://developer.nvidia.com/cuda-zone) for computing [the rank](https://github.com/cybercongress/congress/blob/master/ecosystem/Cyber%20Homestead%20doc.md#glossary). [Aragon](https://aragon.org/network/) for shaping our DAO's. [Go](https://golang.org/) and [React](https://reactjs.org/) as the main programing languages. We also use [Ethereum](https://ethereum.org/) for [cyber~Foundation](https://github.com/cybercongress/cyber-foundation). 

#### What can cyber be used for?
Cyber has several [use-cases](https://github.com/cybercongress/congress/blob/master/ecosystem/Cyber%20Homestead%20doc.md#usecases), all built around semantics and its incentivized use. Such uses account for [search-engines](https://cyber.page/), [web-3 browsers](https://github.com/cybercongress/cyb), oracles, data markets, prediction markets, language convergence, unified semantics, autonomous robots, SEO instruments, providing web services, etc.

#### What are the incentives for using Cyber?
There are 4 types of users that we outline, each with its separate interests:

- [Evangelists](https://cyber.page/evangelism): They are building a social knowledge graph by attracting others to the protocol. For this, they receive rewards from the [community pool](https://cyber.page/governance) and a share of the [donated ATOM](https://cyber.page/gol/takeoff)
- Users: [The masters](https://github.com/cybercongress/congress/blob/master/ecosystem/Cyber%20Homestead%20doc.md#using-cyber-the-very-basics-of-becoming-a-master) of the protocol. The obvious interest is the ability to receive a reward if they [delegate](https://github.com/cybercongress/congress/blob/master/ecosystem/Cyber%20Homestead%20doc.md#picking-honey) CYB and the ability to receive payouts from both, the CYB community pool and the ETH pot under [their control](https://github.com/cybercongress/cyber-foundation) in the form of THC. Their other values include the ability to interact with the protocol and to [share](https://cyber.page/search/god) and [search](https://cyber.page) for knowledge
- Validators (and developers): [The heroes](https://github.com/cybercongress/congress/blob/master/ecosystem/Cyber%20Homestead%20doc.md#nut_and_bolt-section-subtitle-mama-im-an-engineer) of the protocol. They manage [the infrastructure](https://cybercongress.ai/docs/cyberd/run_validator/) and make sure the computer works as should without cheating (they, of course, provide cryptographic profs to this). As long as they stake tokens they receive inflation rewards. They too can receive money from the community pool. They are most likely to develop different tools for users that can be monetized. E.G. simple oracle or crawling tools. This helps them to build their reputation to attract more delegations from which they charge a commission
- Large donors: The large shareholders. Their interest is the [overall use](https://github.com/cybercongress/congress/blob/master/ecosystem/Cyber%20Homestead%20doc.md#usecases) of the protocol and its prosperity. They have the same incentive as the users, but with a larger game at stake

#### Who does Cyber belong to?
Cyber does not belong to anyone. Yes, it launched by [cyber~Congress](https://mainnet.aragon.org/#/cybercongress/), the DAO that launches Cyber and [transitions](https://cybercongress.ai/euler-ceremony/) the `power` to [cyber\~Foundation](https://github.com/cybercongress/cyber-foundation), the main governing DAO. 

Cyber does not have KYC, jurisdictions, CEO's or other fairytale creatures.

#### How can I take part in Cyber?
You can take part by playing [the Game of Links](https://cyber.page/gol), by becoming [an ambassador](https://cyber.page/evangelism), by participating in [the takeoff](https://cyber.page/gol/takeoff), by filling Cyber [with cyberlinks](https://cyber.page/search/help), by helping to [secure the network](https://cybercongress.ai/docs/cyberd/run_validator/) and by being part of [the community](https://github.com/cybercongress/congress/blob/master/ecosystem/Cyber%20Homestead%20doc.md#cyberecosystem).

#### Who are heroes and masters?
This is part of [our subculture](https://github.com/cybercongress/congress/blob/master/ecosystem/Cyber%20Homestead%20doc.md#subculture). Heroes are the validators that secure Cyber. Masters are the users that build the Great Web.

#### When are you going to launch a mainnet?
This is heavily depending on the testing of every single bit of our protocol. Currently, this date is set for the 3rd quarter of 2020. However, you can already [use Cyber](https://cyber.page/). All of the knowledge from the testnet will be transitioned to the mainnet.

#### Do you have a chat / a forum / a blog?
[We have a TG chat](https://t.me/fuckgoogle). [A forum](http://ai.cybercongress.ai/). [And a blog](https://cybercongress.ai/post). We also have [numerous](https://github.com/cybercongress/congress/blob/master/ecosystem/Cyber%20Homestead%20doc.md#public-profiles) other communication channels.

--------------------------------------

## Under the hood, part-2
#### What is a knowledge graph?
Knowledge graphs are a compilation of facts and information that provide meaning to a specific search result. I.E. if you search for Bitcoin, you might see a box on the side of the search results with lots of data about Bitcoin, what it is, where to get some, etc. This is essentially, the work of a [knowledge graph](https://en.wikipedia.org/wiki/Knowledge_Graph). Currently, knowledge graphs use data from Wikipedia, Wikidata and other sources (which almost all, belong to google).

#### Who are [cyber~Congress](https://github.com/cybercongress/congress/blob/master/ecosystem/Cyber%20Homestead%20doc.md#the-cybercongress-dao-and-its-role)?
cyber\~Congress is a [DAO](https://mainnet.aragon.org/#/cybercongress). Its role is to launch Cyber, create the initial allocation and to work on Cyber as one of the community participants.

#### What is [cyber~Foundation](https://github.com/cybercongress/cyber-foundation)?
cyber\~Foundation is a [DAO](https://mainnet.aragon.org/#/eulerfoundation/0xfc3849b9711f69ddb677facff0cd6755a981a1f0/). Its role is to govern Cyber, act as an independent, non-jurisdiction based entity, in charge of its own money. A foundation that has no borders. 

#### How is content ranked in cyber?
You might be surprised to learn that our ranking mechanism is based on no other, but the original idea of [PageRank](https://en.wikipedia.org/wiki/PageRank)! The differences are that our mechanism mixes into the pot economical incentives in the form of digital tokens and bandwidth. This makes it [`Sybil-resistant`](https://en.wikipedia.org/wiki/Sybil_attack).

#### How do you calculate the rank?
The [rank](https://github.com/cybercongress/congress/blob/master/ecosystem/Cyber%20Homestead%20doc.md#advanced-explanation) is a dynamic property. It is calculated using incoming weights of the links, outgoing weight of the links and the current network load. It is recalculated by validators every block to form the current shape of the intentions of the users. This mechanism can be changed via governance.

#### How to become a validator?
You need to set up a node. The best place to start is [here](https://github.com/cybercongress/congress/blob/master/ecosystem/validators/onboarding.md).

#### What are the incentives of becoming a validator?
- You can use your cards to take part in computing the knowledge graph and be a part of an interesting project
- You will be receiving rewards for running a validator, just like in Cosmos (ATOM)
- You will be eligible to build your reputation in the system and can participate in governance during the mainnet
- You can receive a commission from delegators on the mainnet
- You can take part in forming the knowledge graph of the new Great Web
- Become a web3 provider

#### What are the distribution games?
The [distribution games](https://github.com/cybercongress/congress/blob/master/ecosystem/Cyber%20Homestead%20doc.md#the-distribution-games-in-detail) is our achieving the best possible initial allocation, testing the network and creating a decentralized launch. 

There are 2 parts to this process. The [Game of Links](https://cyber.page/gol) for initial believers and validators and [cyber\~Auction](https://github.com/cybercongress/congress/blob/master/ecosystem/Cyber%20Homestead%20doc.md#cyberauction-or-auction) for making sure cyber\~Foundation can be an independent entity.  

#### What are EUL and GOL tokens?
EUL is the test name of CYB. And GOL is the test name of THC. Both are the testing versions of our mainnet tokens.

#### What about crawlers and indexing?
Crawlers are needed to migrate content from the current web to the Great web. Check out the [crawler section](https://github.com/cybercongress/congress/blob/master/ecosystem/Cyber%20Homestead%20doc.md#crawlers).

#### How is this AI related?
First, what is [AI](https://en.wikipedia.org/wiki/Artificial_intelligence)? AI is the intelligence demonstrated by a machine. This doesn't necessarily mean that the machine must be from the year 12255 (by then, it will probably be a world of machines as it is).

In its essence cyber is a huge distributed consensus computer, it is a dynamic protocol that is influenced by different machines and users simultaneously. It learns from actions. It can prune things that are irrelevant to it. It can prove the relevance of any two existing objects that are known to it.

#### I heard I can use my Ledger device, really?
Yes! You should. A ledger is a hardware wallet and its possible to sign transactions in Cyber straight out of your Ledger device. By the way, it is also possible to set up a validator node with a [Ledger device](https://github.com/cybercongress/cyberd/blob/0.1.5/docs/Validator%20launch%20with%20Tendermint%20KMS%20%2B%20Ledger.md).

-------------------------------------

## The philosophy behind Cyber:
#### What problem are you trying to solve?
We are trying to solve the problem of data centralization and data censorship. Which in other words, is decentralization of common knowledge (assuming that data is the new knowledge, and that we are moving into the digital age). 

#### Why are you doing this?
Each person should be able to control their own data, their identity, their knowledge. The universe can become a better place if our children live in a digital environment where they are in charge of their actions.

#### What's wrong with google?
google is a brilliant idea. We do not deny this. But google is the rebel that has overthrown the dictator and became the dictator itself. google uses you to shape the essence and the fundamentals of communications between everyone and everything. Whilst at it, google doesn't care for anyone and will make money on your action and your behalf.

It should be noted, that by this question I am attempting not just at google, but at all the mega-digital corporations. Feel free to check out what this can lead to in the shape of [Cambridge Analityca](https://en.wikipedia.org/wiki/Cambridge_Analytica). If this case is too much to take in or too "loud" for you, feel free to watch some episodes of Black Mirror to see how digital control can "break" society.

#### Why now?
Because we are almost done with post-industrialism. We are slowly and surely moving into the digital realm. One can deny or accept this. Now is the time to either have the tools that will help us to shape the matrix the way we want to shape it or give those powers away to someone to control all aspects of our lives.

#### Why search?
Search is a global mechanism that is globally understood by everyone, regardless of language, race, age, etc. It is somewhat a basic instinct (searching for food to survive, etc). In the digital realm with the help of search, we gain answers to our questions, which we always ask. Search helps us to build a model around any subject that is of interest to us. With the use of search, we can build databases, which can lead to a great number of useful instruments (on these later).

#### Aren't there other, more important problems to solve?
There probably are. But we decided to focus on this because we understand how to achieve the required result. There are probably more problems and questions to be solved (like hunger, wars, ecology, etc). Our tool can help to play a role in solving if not all, but some of these.

#### Aren't there other things out there that solve this?
There is a lot of awesome, open-source technology on the market that can commit to making a change in the world. Most of the technology we use is not something we invented (although the code itself is written from scratch!). They are technologies that have existed previously and are awesome at doing what they do. Our software is a combination of existing technologies, protocols and our own work that has arisen from this. It is specifically targeted at fixing what is broken.

#### How are users/developers/others benefit from using such a system in comparison to google, etc?
<img src="https://i.postimg.cc/7hX2GbQC/cyber.png" />

#### Why do you need consensus within Cyber?
A consensus is required for nodes to agree on the current state of the ledger at any given point of time. This is needed to achieve security, transparency, immutability and decentralization. 

#### What is your take on: privacy/censorship/routing?
We believe that privacy should be a fundamental right. As of now, the protocol is pseudo-private (just like Bitcoin is). I.E. you know which hash linked something and with what weight, but you don't know the real name of the user. With that, we are planning to implement full privacy into the protocol. 

We are strongly discouraged by any censorship and view it as a sin against any living and/or thinking organism. 

Routing should be always permitted. Transactions should always be permitted to pass. Otherwise, this is censorship. 

#### Do you not think that the motto #fuckgoogle is offensive?
No, because fucking is not about pain, it's about pleasure! In all honesty, censorship killed more people over the course of history, than swearing did.

---------------------------------

## Silly, yet, VIP questions:
#### Why Cyber?
We like that name. That's one reason. We have been using this name throughout our projects for the past 6 - 7 years. 

Cyber refers to anything that is very smart. The meaning is rooted from the word `cybernetics` (check out this article on [Wikipedia](https://en.wikipedia.org/wiki/Cybernetics#Subdivisions_of_the_field)) - a science which describes the behaviour of dynamic systems with feedback loops.

In popular culture, it has become a partial synonym to all the crazy sci-fi things out there. Like the cyber-track by Elon Musk and co. Cyber refers to cyberspace. Space free from centralized, human influence and bureaucracy. It is the Andromeda of freedom. The last frontier...

#### How is cyberlink different to a hyperlink?
Cyberlink are the fundamental building blocks of the Great Web. Cyberlinks help to interconnect data the same way [hyperlinks](https://en.wikipedia.org/wiki/Hyperlink) help interconnect servers on the web we are all used to. The differences between cyberlinks and hyperlinks are in the way what you link, how you link and where you store the link:

|                           | Hyperlink                          | Cyberlink                      |
|---------------------------|------------------------------------|--------------------------------|
| What you link             | From one server to another server  | From one file to another file  |
| How you link              | Embed link in a webpage            | Sign a transaction             |
| Where you store the link  | Private server                     | Public blockchain              |
| Example                   | [google](https://google.com)       | [cyber](https://cyber.page/network/euler/tx/08F9514853A59EB063ACF4D80D62B48B863834124386B1D473E488344D38EA80) |

Currently, there are trillions of hyperlinks in existance, but so far [less than a million cyberlinks](https://cyber.page/brain/knowledge) have been created. Changing the way we create links, gives you and the world superpowers and provide features which are impossible with hyperlinks in web-2:

|                | Hyperlink        | Cyberlink                      |
|----------------|------------------|--------------------------------|
| Beneficiaries  | Server owners    | Content creators               |
| Index yourself | Impossible       | Just cyber it (yes)!                 |
| Censorship     | Trivial          | Impossible (if you store the file) |
| Offline        | Impossible       | Yes (if you store the file)        |
| Broken links   | A matter of time | Impossible (if you store the file) |

#### Is linking that important?
Yes! Hyperlinks shape the internet. They have built it. We base our knowledge, our political, economic and educational decisions on the internet. We learn from google. google is our father, teacher, source of knowledge, social life, etc. But, how can we trust the internet if it was shaped by something that itself is untrusted? Well, we can't. Cyberlinks, on the other hand, are trusted and backed by a provable and an auditable mechanism that anyone can check. This means that with the aid of cyberlinks we can, no less, but create a trusted model of all the information in the universe!

#### How are pages included or excluded from the index?
Pages are added to the index (the word index is about all the information stored on the knowledge graph in the blockchain) when someone submits a CID or creates a cyberlink. This is a transaction. Transactions are checked by validators (the computers that make sure you have the balance to submit a transaction) and added to the knowledge graph, which is then accessed by someone who queries the database. 

Pages are not excluded from the index in any way. 

#### So is there any censorship?
Nope... Not on the protocol level. Not on the database level. Not on the consensus level. Every transaction should and must be routed (passed to its destination whatever it may be).

#### So what do you do with those who break the law?
If we obscure from the question of what is the law and by whom it is determined, then:

There are no bad intentions in wanting to find the answer to something. You might not know something is `bad` until you know what it is. We are born `Tabula Rasa`, a clean sheet. The answer itself might indeed contain information that someone might see as `bad` or `inappropriate`. This is not something we can control. We do not produce the information, we provide the tool to search through it and obtain it. 

It can be assumed that in the future, someone will build applications on top of cyber and might want to filter out information on the application level (the results that the end-users sees and interacts with). This is not encouraged, but indeed, is up to the developer. We will never do something like this. Regardless if this happens or not, the protocol will NOT be censored and that information will be accessible. 

This will create a competition between developers to pass the truth to the users.

#### So who has the power?
No one or rather everyone. Our idea is to design a tool where everyone feels equal. With that said, this can defiantly act like a competitive instrument. Someone who posses more tokens can link content (and hence rank it) with more weight at any given moment. However, the amount of tokens in possession does not influence Cybers virtue. On the contrary, someone submitting a link with a higher weight does a good job for the whole protocol. The stronger the knowledge graph is, the more valuation it has, the better everyone feels. 

#### So whoever is richer will always stay on top, right?
Someone who ranks content with a higher value will see his content ranked higher at a certain point of time. That is obvious. With that, he does not have an indexation preference. Here, the principle: first come - first served, will always function. If you were first to index something, then you indexed it before someone else did. It is hard to comprehend at first, but the only way to abuse the protocol is to perform a 51% attack. And even then, just like any other blockchain, it will, probably, fork itself out.

With that, the search is dynamic. If I rank a content then it is relevant to me here and now. If I am not interested in it, then I have stopped ranking it. Older ranks will dilute with time. But, apart from my weight, the rank depends on the weight of incoming and outgoing ranks. And those ranks depend on their incoming and outgoing ranks... This makes it a never endless game, where simply because I have more tokens, might not be enough for me to always end up on top. 

A comparison to [wisdom of the crowd](https://en.wikipedia.org/wiki/Wisdom_of_the_crowd) can be made, where the collective opinion has a larger weight than that of a single entity.

#### How is the search algorithm safe from abuse?
This is one of the easiest and the most complicated questions we get asked. Several things prevent abuse. (1) The consensus mechanism (the more nodes, the better), (2) the resource credit model (an economic spam protection mechanism), (3) the thing is, is that the network belongs to the users, governed by the users and is utilized by the users. They are the sole beneficiaries of the network. If you attempt to abuse the search mechanism, the only thing you can abuse is yourself. The network will stay where it stands. This is a difficult concept to grasp, but this is the reality of things for web3.

#### Why open-source?
Because open-source technology is the future way of communication between projects, users and developers. Open-source doesn't stop at referencing to technological progress. Open-source is a new way to collaborate. It allows people to freely change, commit to and modify ideas. And as a result, help progress and innovation at a higher temp and in a more secure manner.

#### Is this P2P?
Not exactly. It is in the sense that users are interacting peer to peer with their computers, without a company in the middle. However, technically a blockchain is also an intermediary. What's good, is that you don't need to trust a blockchain thanks to how it functions.

#### What is the difference between Cyber and P2P search engines like YACY?
[YACY](https://yacy.net/en/) (and other P2P similar mechanisms) have plenty of years of work behind their backs, which cyber (still) hasn't. YACY is pure P2P, cyber isn't. It has a blockchain between the users. Also those years of work which YACY and the others have, kind of proven that they don't work. Otherwise, we would not be making cyber.

#### How does this compare to TOR?
Tor is not a search protocol. Tor is a highly efficient privacy instrument. Tor does not provide economic incentives. Tor doesn't use the blockchain. Tor does not answer questions. we see Tor as an instrument that we could provide a search protocol for. We hope that Tor can implement cyber on an application-level one day.

#### Do you have a White Paper?
[Yes, we do](https://ipfs.io/ipfs/QmQ1Vong13MDNxixDyUdjniqqEj8sjuNEBYMyhQU4gQgq3). You are welcome to read it. It can also be manually compiled, with the help of Xelatex, from [this repository](https://github.com/cybercongress/cyber).

#### Have you tested this? Does it work?
Yes, we have. There have been numerous private and public testnets. In fact, as of now, we are still testing and improving the protocol. It already works. [Use it](https://cyber.page/)!

#### Can I use it on web2 (normal browsers/phone, etc)
Depends. You can certainly view and download IPFS hashes via gateways to your phone/web2, etc. We presume that in the future people [will be building](https://github.com/cybercongress/congress/blob/master/ecosystem/Cyber%20Homestead%20doc.md#community-maintained-profiles-and-tools) some kind of bridge between what we do and web2. But we do not see this is a task and shall not work on it. People should move to web3.

#### Are you Satoshi?
We wish... And we don't. We wish we were so smart and to have the knowledge of whomever Satoshi was/were/ is/are... We do not wish because knowing who Satoshi is, would destroy the whole idea of Satoshi.

#### Why are you so geeky?
Why not? Geeky is the new cool. Geeks are awesome. If you didn't notice the world has been ruled by Geeks since the Microsoft made it to the top. In the last century, geeks have been all around us. From Facebook to google.

#### Is this an ICO?
The projects receive donations from users who wish to donate them and participate in the distribution games. In exchange they receive tokens. The process can be referred to as an initial community offering. Which is the process where the community understands the value of the proposed idea and decides to donate towards its development for its own benefit.

#### Is this religious?
Yes. By all means, it is. It is the most anti-religious techno-religion in the wild.

#### How do you plan to take over the world/internet?
By showcasing and awesome product and with the help of the community behind it. Of course, those are loud words. But our product is [working](https://cyber.page/). The idea has proved to be functioning and has a proved and a cemented market demand. We are experimenting, but we are an experienced team. We have the knowledge, the understanding and the passion to drive this product forward. In combination with the product itself, the code, the community, the donations, the DAO, and everything else, it will either happen (the taking over)... or it won't. Either way, we will do everything to make this happen!

#### What is your main target audience?
Our main TA are internet users. We plan to concentrate on developers, IPFS users, crypto maniacs and like-minded people at the beginning. We then, want to concentrate on younger generations. We firmly believe that they can grasp what we do (including our values) better than anyone else.

#### Can I copy what you do?
Go ahead. Seriously. We are open-source for a reason. You may copy, modify, do as you please. Our license agreement is: `Don’t believe, don’t fear, don’t ask.`

If you plan to fork the protocol, then eventually, we will meet each other with the help of IBC or other instruments of the free market. If you plan to fork the client, then this is another way of scaling Cyber. Feel free to fork it and build something on top of Cyber, for example, a targeted knowledge graph.

----------------------------

## Links
- [Our White Paper](https://ipfs.io/ipfs/QmQ1Vong13MDNxixDyUdjniqqEj8sjuNEBYMyhQU4gQgq3)
- [cyber.page](https://cyber.page/)
- [Homestead documentation](https://github.com/cybercongress/congress/blob/master/ecosystem/Cyber%20Homestead%20doc.md)
- [cyber~Ecosystem development paper](https://github.com/cybercongress/congress/blob/master/ecosystem/cyber~Ecosystem%20development%20paper.md)
- [Validator onboarding guide](https://github.com/cybercongress/congress/blob/master/ecosystem/ELI-5%20FAQ.md)
- [Our twitter](https://mobile.twitter.com/cyber_devs)
- [Our Telegram](https://t.me/fuckgoogle)
- [Our forum](https://ai.cybercongress.ai/)
- [IPFS docs](https://docs.ipfs.io/)
- [Urbit docs](https://urbit.org/docs/)
- [Bitcoin White Paper](https://bitcoin.org/bitcoin.pdf)
- [Cosmos intro](https://cosmos.network/intro)
- [ETH wiki](https://github.com/ethereum/wiki/wiki/What-is-Ethereum)
- [Aragon website](https://aragon.org/)
- [Cypherpunk manifesto](https://www.activism.net/cypherpunk/manifesto.html)

-------------------------
