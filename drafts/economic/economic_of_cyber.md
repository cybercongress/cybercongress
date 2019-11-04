# Introduction to the cyberd economy

![cyberd](cyberd.png)

`Cyberd` or the interplanetary search engine & knowledge consensus computer - is a [cosmos-SDK](https://github.com/cosmos/cosmos-sdk) based blockchain-implementation of the `cyber` protocol. It posses the unique property of being able to create meaningful relations between IPFS CIDs and storing them as a knowledge graph along with their weighted ranks. To understand the economic structure of `cyberd` we need to look closely at the following:
- the key principles of cyberd
- basic incentives for different participants
- possible influences of those principles on the participants' behaviour

## The key principles of cyberd

`cyberd` is an application-specific blockchain or a Cosmos Zone with sovereign economics and specification. `Cyberd` represents a knowledge graph as a weighted graph of directed links between content addresses or content identifications or CIDs.

Just like the Cosmos ecosystem, `cyberd` utilizes Tendermint - a practical Byzantine fault tolerance (PBFT) consensus mechanism. It means that finalizing blocks depends on the `2/3 plus one quorum` in between all validators having to agree on the current state of the network to reach consensus.

## Basic incentives for different participants

`Cyberd` has 146 validators who are responsible for proposing new blocks and validating transactions. This number will remain constant until it is ready to be increased or decreased via a governance proposal. As the number of validators grows, then the right to participate in the consensus will see participants with a higher amount of CYB tokens bonded.

`Cyberd` validators have the highest impact on network security. They should actively participate in governance and are expected to vote on every proposal.

They have enough knowledge and resources to maintain the infrastructure and are interested in generating maximum long-term gains from CYB token inflation and validation commissions. This is why validators care about a healthy and a sustainable development within the ecosystem. They should act in the interest of their delegators if they want to keep them loyal and increase their voting power in the long term. There are no transaction or message fees in `cyberd`. Instead, there is a system called: resource credits (in `cyberd` its called - bandwidth).

The primary responsibility of validators is the continuous ranking and recalculation of the knowledge graph. Every 100 blocks, depending on the weight staked behind the links, the rank value is assigned to the links and all of the weights are recalculated by the validators GPUs.

The delegator group is formed out of CYB token holders who do not have enough skills or resources to run and maintain the necessary infrastructure, but still, want to increase the network security and earn a share of the inflationary reward by bonding tokens to the validators. This boosts the voting power of validators and the frequency of being chosen as a block proposer. In fact, by bonding CYB tokens to validators, the delegators decide on one of the pillars of blockchains. Their choice is very important and affects the level of decentralization in the system. Delegators are also eligible to inflationary reward, but they have to pay commission, which varies amongst existing validators. There is no way for validators to steal the bonded tokens, but there are still other risks involved that are related to choosing a validator. Decisions based solely on a low commission rate is not always the best decision for delegators.

If we compare the cyberd network with other search engines, then the users are the consumers and the service providers. Developers, entrepreneurs, SEO, buyers, and searchers who want to utilize the advantages of a decentralized search engine. Here we can understand the true value of `CYB` tokens. `Cyberd` declined transactional or message fees in favour of resource credits as a method of decreasing network load. The main goal of that model is to reduce daily network growth to a given constant, say less than 3GB per day. In `cyberd` resource credits are called **bandwidth**. The value of a users bandwidth - is the ability of users to send messages, make links and to transact. The more bandwidth points, the more opportunities. Bandwidth price depends on the network load, namely, the less the network load is - the cheaper the bandwidth price. In the current `cyberd` set up, the general messages costs are:

| Type of transaction | Cost in BP |
| ------------- |:-------------:|
| Link|  K * 100 |
| NonLink | 5 \* K * 100 |
| Send | 3 \* K * 100 |

**K** is the price coefficient. It's calculated as the ratio of the current network load and the maximum network load. This coefficient is recalculated every minute. The minimal value of **K** is `0.01`. **BP** is the users' bandwidth points. Bandwidth recovers fully within a period of 24h.

![bandwidth](Bandwidth.png)
<p align="center">Decreasing bandwidth value with sending transaction or linking. No commission</p>

The activity of this group measures the overall value of the network and can have a significant impact on demand for the token.

## Economic structure and reward distribution

Like the economy and reward distribution within Cosmos Hub, `cyberd` relies on inflationary approach. Unlike in Cosmos, the inflation in `cyberd` constantly strives to ~7%. It's achieved by tuning the `TokensPerBlock` parameter during the genesis setup. Given that the network has 1-second target block time and ~7% target inflation the starting parameter will be 50 MCYB.

There is one fundamental stream of revenue for validators - inflation.

![rewards distribution](distr.png)

Block rewards are distributed amongst all validators proportionally to their voting power. This reward is paid in CYB tokens.

Represents a percentage from both streams of the revenue that delegators pay to a validator. The delegators reward streams are the same as the validators streams, minus the percentage of the commission.

## Possible influences of those principles on the participants' behaviour

In some circumstances, the slashing of bonded CYB tokens can occur. Penalties should increase the responsibility level of participants who are directly involved in decision making associated with network security. Validators have no control over delegators stake, but if such an event happens both parties lose a percentage of their tokens. This is to prevent misbehaviour and negligence from validators and bring incentives to delegators to diversify amongst them, perform proper due diligence and choose wisely.

- The first reason a stake can be slashed is double-signing a block. This means that a malicious node is broadcasting two blocks with different content at the same height. Currently, the penalty for this is set at 20%, and the validator who is responsible for that drops out of the validator set. All CYB tokens enter an unbonding (the process of undelegating CYB tokens from a validator) period, that lasts for 21 days. Within this period the stake will not earn any provisions and/or transaction fees.

- If a validator fails to sign more than 70% blocks in a window of 1800 blocks due to inactivity, 0.1% of the bonded CYB tokens will be lost and the validator will be jailed without allowance to participate in the consensus. They will also not be eligible for rewards during the unjail transaction.

When slashing happens, it decreases stake and leads to fewer CYB tokens paid as rewards.

## Conclusion

This is a brief explanation of how economics currently function within `cyberd`. This is not the final decision on economics. It can also be changed after euler-5 and after mainnet. Besides, it will always be open to change via governance proposals. The general spec values are very similar to those of the Cosmos Hub ecosystem, but, it has some key differences, such as: resource credits. Before you decide to run a validator for staking, please make sure that it is a secure and a fault-tolerant node :)
