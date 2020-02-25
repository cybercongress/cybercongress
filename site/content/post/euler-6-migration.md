---
date: 2020-02-24
url: euler-6-migration
title: 'State migration proccess from euler-5 -> euler-6'
author: serejandmyself
---

> Summary: Currently we have at least one blocking error to continue the Game of Links on top of the euler-5 network: a bandwidth limiting bug which removes the ability to correctly load the network. According to the outlined launch protocol of euler-5, we have to act and relaunch the network.

Due to the blocking error described in [#309](https://github.com/cybercongress/congress/issues/309), we shall activate the [crisis protocol](https://github.com/cybercongress/congress/blob/master/site/content/post/game-of-links.md#crisis-protocol) and migrate from euler 5 -> euler-6.

The migration will include:

- A rewritten storage for using the latest SDK features (such as IAVL with in-memory data, which periodically flushes to disk. This was introduced in SDK 0.38.0 for high I/O performing chain, such as ours)
- During calculation, we now catch NaN values and assign zero values to them
- Bandwidth consumption during linking is fixed and now consumes/regenerates energy as should
- The whole chain upgraded to the latest SDK: 0.38.1
- CosmWasm integration (smart-contracts!)
- On-chain upgrades! This will allow us to upgrade the chain via governance with (almost) zero-time downtime

You may follow the [project board for migration here](https://github.com/cybercongress/cyberd/projects/6).

## News by @litvintech
Since the launch of Euler-5 in December, I was fully concentrated on code polishing and preparation of the cyber~Foundation setup ceremony. Huge progress with this. We are almost finished with the ceremony. Also, huge progress with the cyber.page application, which will be released in weeks to come, and will have an awesome set of new features.

But today, I mostly want to describe the progress made with the chain and make some announcements.

January started with signals from validators on failed node reload in 25% of cases. @mrlp4 quickly helped me to collect data with which I started debugging these cases. It's a medium-high impact issue. During this, we continued to support validators that had this problem and continuously provided them with the latest chain backups to allow them ASAP relaunch.

I found that the roots of the issue lay with our custom storage for links, which we developed for the first Euler release. At the time we decided to use custom storage, as the cosmos-SDK storage was pretty slow for our use case.

Debugging in a decentralized environment, i.e. blockchains, is a pretty complex thing. But looking ahead I’ll say that we dealt with all the issues efficiently. During the debugging of storage, I found an issue with rank calculation, which doesn't lead to halts, but produces results not specified by the protocol.

As you know, we are computing a token-weighted page rank: cyber~Rank. All the cyberlinks are stored permanently with the account that made these cyberlinks. The aggregation of all weights between given objects (CIDs), is the sum of the current account balances, which made the cyberlinks between these objects. Transfer of tokens affects weights of the produced cyberlinks of an agent. Therefore, rank values - change.

The case I found, was when an agent (subject) transfers their full balance from their account to another account, and there is only one cyberlink between two CIDs (made only by this agent). This results in zero aggregate sum of weight and produces a NaN (Not-a-Number) value when division happens inside the rank algorithm. The issue is in both, GPU (production) and CPU (local development, cross-testing) rank code.

We also found an issue with the consumption of bandwidth during linking. It was produced during last-minute featuring before Euler-5 launch. The issue leads to fast bandwidth regeneration as if it was consumed for linking.

All of this is now solved, and plenty of other new features are introduced in the new release!

## State migration process by @SaveTheAles
To update the chain we plan to implement the following migration process. (Read the [full internal proposal here](https://github.com/cybercongress/launch-kit/blob/0.1.0/migrations/e-6%20migration_proposal.md)).

4 major things should be taken into account:

- Cyberlinks made by an agent
- Karma of an agent
- Precommits by a validator
- The stake of a validator

Given the circumstances, an agents' karma was compromised by the bug described by @litvintech, so there is no sense to migrate karma values between testnets.

The solution is in migrating cyberlinks. It is possible to export all of the cyberlinks made by an agent to an IPLD-like structure and add an opportunity for the agents to make their cyberlinks again in the new testnet, with one single transaction. In other words: in the new testnet, the agents can get their links from the previous testnet by a query to an IPLD structure, generate a transaction with all their previously made cyberlinks, sign it and broadcast it to the new network using their ledger via the [cyber.page app](https://cyber.page/pocket) or manually, via [CLI](https://cybercongress.ai/docs/cyberd/ultimate-commands-guide/).

This lets us cover two of the migration points: cyberlinks and karma. **The weakness of that method is that anyone can relink all the previously made cyberlinks before the original discoverers.**

The migration of the precommits is complex. To avoid any additional changes in the distribution, we will save the state of the precommits in [a .csv file](https://github.com/cybercongress/launch-kit/tree/0.1.0/game_rewards_calculations) at a certain block height and use it for the Game of Links recalculations after the Game. Thus, we can avoid major changes in the distribution and make the migration a smoother process.

The stake of the validators should be burned. The complexity of changing distribution parameters is much higher than the error of the final stake results. This means that the accounts in euler-6 genesis file will be the same as those of euler-5.

Additionally, we are now able to test the `genesis ceremony` and hold parameters discussion. The `genesis ceremony`  is the process of signing the genesis file by validators who want to participate in the initial transaction of the network. Validators can sign the Genesis before the launch and start validating from the first block. The [launch-kit repo](https://github.com/cybercongress/launch-kit) is now ready for newcomers and it seems possible to do this now.

The workflow should be fairly easy:

1. Announce network halt at a given block height
2. Export precommits and cyberlinks on a given block
3. Import the required UI for cyber.page to migrate cyberlinks
4. Create a guide for importing cyberlinks via the CLI 
4. Generate Genesis
5. [Genesis ceremony](https://github.com/cybercongress/launch-kit/blob/0.1.0/gen_txs/README.md)
6. Relaunch

Comments and ideas are welcome in [309](https://github.com/cybercongress/congress/issues/309).
