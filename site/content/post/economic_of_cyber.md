---
date: 2019-07-17
url: economic_of_cyber
title: 'Introduction to cyberd economy'
author: savetheales
---
# Introduction to cyberd economy

![cyberd](https://ipfs.io/ipfs/QmejVRS9irYb6eXGDZNM9YEuFyb3a5jn4EWh3MRC3LVRij)

`Cyberd` or interplanetary search engine & knowledge consensus computer is [cosmos-sdk](https://github.com/cosmos/cosmos-sdk) based blockchain implementation of `cyber` protocol with unique property of creating relations between IPFS CIDs and storing them as the knowledge graph with weighted ranks. To understand the economic structure of `cyberd` we should look closely at the:
- key principles of the cyberd
- basic incentives for all different participants
- the possible influence of these principles on their behavior

## Key principles of the cyberd

`cyberd` is an application-specific blockchain or Cosmos Zone with sovereign economics and specification. `Cyberd` represents a knowledge graph as a weighted graph of directed links between content addresses or content identifications or CIDs.

Like a Cosmos ecosystem, `cyberd` utilizes Tendermint - practical Byzantine fault tolerance (PBFT) consensus mechanism. It means that finalizing blocks depends on 2/3 plus one quorum of all validators agreed on the current state of the network in order to reach the consensus.

## Basic incentives for all different participants

For `cyberd`, there are 146 possible validators, who are responsible for proposing new blocks and validating transactions. This number will constant until they're ready to increase it or decrease with a government proposal. If there are more validators then the right to participate in consensus will have participants with a higher amount of CYBs bonded.

`Cyberd` validators have the highest impact on network security. They must actively participate in governance and are required to vote on every proposal.

This group have enough knowledge and resources to maintain infrastructure and are interested in generating maximum long-term gains from CYB inflation and validation commission. That is why validators care about healthy and sustainable ecosystem development. They should act in interests of their delegators if they want to keep them loyal and increase the voting power in the long term. There're no transaction or message fees in `cyberd` instead it have resource credits, in `cyberd` it calls bandwidth (about this later).

And the primary responsibility of validators is continuous rank recalculation in knowledge graph. Every 100 blocks in depends on linker stake, the rank value is assigned to the link and all weights are recalculated by validators GPUs.

Delegators group consists of CYB token holders who have not enough skills or resources to run and maintain the infrastructure but still want to increase the network security and earn a share of the inflationary reward by bonding tokens to the validators. It boosts the voting power of validator and the frequency of being chosen as block proposer. In fact, by bonding CYB to validator delegators choose one of the pillars of the blockchain so their choice is very important and affects the level of decentralization.
Delegators are eligible for inflation reward as well but they have to pay commission, which varies within existing validators. There is no way for validators to steal bonded tokens but there are still other risks related to choosing the validator. Decisions based solely on a low commission rate is not always the best decision for delegators.

If we compare cyberd network with some search engine, users are consumers and service providers. Developers, entrepreneurs, SEO, buyers, and searchers who want to utilize the advantages of a decentralized search engine. Here we're can understand the true value of `CYB` tokens. `Cyberd` refused to the transaction or message fees in favor of resource credits as a method of decreasing network load. The main goal of that model is to reduce daily network growth to given constant, say less than 3gb per day. In `cyberd` resource credits named **bandwidth**. The user bandwidth value is the ability of users to send messages, make links and do transactions. More bandwidth points, more opportunities. Bandwidth price depends on the network load, namely, the less network load, the cheaper bandwidth price. At the current `cyberd` set up general messages costs:

| Type of transaction | Cost in BP |
| ------------- |:-------------:|
| Link|  K * 100 |
| NonLink | 5 \* K * 100 |
| Send | 3 \* K * 100 |

**K** is the price coefficient. It's calculated as the ratio of current network load and maximum network load. This coefficient recalculated every minute. The minimal value of **K** is `0.01`. **BP** it's a user's bandwidth points. Full user bandwidth recovering goes in 24h.

![bandwidth](https://ipfs.io/ipfs/QmYHfqb6ThrtnWcyVsPy8JQGEWunhwKnJiaJUdTemXrUmj)
<p align="center">Decreasing bandwidth value with sending transaction or linking. No commission</p>

The activity of this group measures the overall value of the network and can have a significant impact on demand for the token.

## Economic structure and reward distribution

Cyberd economy relies on the inflationary approach. The target annual inflation rate represents the percentage from total supply that is changing each block. If the total bonded stake is less than `66%` of the total CYB supply, the inflation rate will slightly increase until it reaches a maximum of `20%` or the total bonded stake climbs higher than `66%`. In this case, the annual inflation will decrease to `7%` depending on CYBs participating in bonding. New tokens incentivize participants to secure the network. The more tokens locked via staking the higher the threshold for initiating a successful attack.

The inflation speed calculates every minute so that reach its maximum or minimum in one year.

![rewards distribution](https://ipfs.io/ipfs/QmPgUhSGaE4NTHJ6UA2YtR4E7xfwVPBXkiJQejWMShvjj5)

Block reward distributing amongst all validators proportionally to their voting power. This reward is paid in CYBs.

Represents a percentage from both streams of revenue that delegators pay to a validator. Delegators reward streams are the same as for validators less the commission percentage.

## The possible influence of these principles on their behavior

In some circumstances occurs slashing of bonded CYBs. Penalties should increase the responsibility level of participants who are directly involved in decisions associated with network security. Validators have no control over delegator’s stake but if such an event happens both parties lose a percentage of their tokens. This is in order to prevent misbehavior and negligence from validators and bring incentives to delegators to diversify amongst them, perform proper due diligence and choose wisely.

- The first reason a stake can be slashed is double-signing a block. This means that a malicious node is broadcasting two blocks with different content for the same height. The penalty for that is currently set at 20% and the validator who is responsible for that drops out of validators set. All CYBs enter an unbonding (the process of undelegating CYBs from validator) period that lasts for 21 days and within this period the stake will not earn provisions and transaction fees.

- If a validator fails to sign more than 70% blocks in a window of 1800 blocks due to inactivity, 0.1% of the bonded CYBs will be lost and the validator will be jailed without allowance to participate in consensus and be eligible for rewards during the unjail transaction.

If slashing happens, it decreases stake and leads to fewer CYBs paid as a reward.

## Conclusion

Here is a brief explanation of how economic goes in `cyberd` at the current moment. This is not a final economic decision, also, it can be changed after euler-5 and mainnet. Moreover, it can be changed with governance. General specs values are very similar to Cosmos Hub ecosystem, but it has key differences, such us resource credits, for example. Before you decide validator for staking make sure that it has security and fault tolerance node :)
