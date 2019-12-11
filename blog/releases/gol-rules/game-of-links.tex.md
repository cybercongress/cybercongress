# Game of Links rules

Welcome to the Game of Links - the `euler-5` incentivized testnet for the `cyber` network launch. The Game of Links organized by cyber\~Congress. The main goal of participants is to win as much as possible tokens from cyber\~Congress and its seed investors.

## Intro

Game of Links starts with `euler-5` launch and ends when a snapshot of the network which is produced after the Game of Links Final. Based on the snapshot Genesis of `cyber` network will be computed independently by every validator who will decide to be a part of Genesis. Key idea of the Game of Links is to establish starting value of relevance in the knowledge graph because its crucual for getting quality search results from the inception of the network. So all disciplines are integral part of preparition and testing network before mainnet.

Goals:

- Public incentivized testing of [cyberd](https://github.com/cybercongress/cyberd) and [ethereum contracts](https://github.com/cybercongress/aragon-claim-app) before mainnet
- Demonstrating search with an experimental knowledge graph filled with useful cyberlinks
- Up to 6% CYB distribution for validators who will participate in pre-genesis takeoff donations depending on the amount of donated ATOMs
- Up to 4% CYB distribution for participants of 6 disciplines depending on how much participants win from cyber•Congress

> **! Important**

In `euler-5` testnet we'll use special named `EUL` tokens against liquid `CYB` in mainnet and `GOL` tokens against `THC` governmence tokens. EUL tokens have minor value as they serve the basis for rewards calculation during the game. GOL tokens have also tiny value as they will allow to gain EUL during the game if vested. Non-vested GOL tokens not have any value. GOL tokens serve (1) as a means to provide incentivized testing of ethereum contracts and (2) in order to protect faucet from spam. DO NOT spend significant funds for buying GOL during Test of Thrones & test~Auction and EUL over the counter. We'll burn GOL after `euler-5` testnet as well as reset accounts in `euler` experimental networks series. All ETHs and ATOMs sent to faucet during the Game of Links are donated to cyber\~Congress because it's cool.

The distribution in the Genesis file of `euler-5` will be the following:

![euler-5-distribution](euler-5_distribution.png)

| Group | Amount EUL |
| --- | ---: |
| Takeoff donations | 100,000,000,000,000 |
| gifts to Ethereum, Cosmos and Urbit communitites | 100,000,000,000,000 |
| Euler-4 validators | 20,000,000,000,000 |
| GOL stakers | 20,000,000,000,000 |
| test of Thrones in Atoms | 1,000,000,000,000 |

Total Genesis supply is 231,000,000,000,000 EULs or 231 TEULs.

The distribution across GOL stakers will be:

![euler-5-GOL-distribution](euler-5_GOL_distribution.png)

| Group | Amount EUL |
| --- | ---: |
| test\~Auction | 6,000,000,000,000 |
| cyber\~Congress | 3,000,000,000,000 |
| Test of Thrones in ETH | 1,000,000,000,000 |

> **! Important**

We can not guaranty that everything will goes as expected. Software can be vulnerable. So if something goes wrong cyber•Congress as organiser **has the full power** of deciding whether the game must be restarted **without any rewards** or restarted with **partial rewards** depending on circumstances. In this case we are going to count community opinion though. Please read carefully [launch protocol]() in which we defined the rules of faults handling. More details about crisis protocol [here](inside link).

In order to remove confusion here is the comparison table of the names for the stuff that will happen.

| during `euler-5` testnet | during `cyber` mainnet |
| --- | --- |
| Test of Thrones | Game of Thrones |
| test\~Auction | cyber\~Auction |
| GOL token  | THC token |
| EUL token  | CYB token |
| Takeoff funding | not applicable|

We believe that such measures will help reduce risks associated with the usage of Aragon contracts, Aragon plugins, cyberd software and multisig accounts involved. Thanks for understanding.

## How to participate in the Game

There is no face control or KYC for joining the Game. You just need a tool for playing and tokens. You can join the Game as:

- Validator. [Set up]() your own node and start validation.
- Great Web Agent. The builder of Great Web. Migrate the content from web2 to the Great Web or create yours, and make it searchable. You can link your content with [browser extension](), [web app](), and with [CLI]().
- Developer. Create things and claim your rewards by community pool spend proposal.

How to get tokens?

- **Gifts**. There are 100 TEULs allocated as a gift to Cosmos, Ethereum and Urbtit communities. This is 43.3% of `euler-5` Genesis supply. You can check your balance using `cyberdcli`, cyber.page app, cyb-virus extension just by adding your address (cyber.page) for checking, or by importing your private key (for ethereum), or seed phrase (for cosmos) to CLI and extension. Also, you can use Ledger device at [cyber.page](cyber.page) app and CLI. The gifting rules defined in the [whitepaper](). The gifting mechanism is implemented in [launch kit]() repo.

- **Faucet**. We want to test the production auction app in `euler-5` and this is a great opportunity for creating faucet based on this app. You can buy GOL tokens and claim EULs for playing. We expect a low price for it, so you can fill your stake by Szhabos and uAtoms.

- **Takeoff round**. You can get tokens if you will participate in takeoff round. There are 100 TEULs allocated for takeoff round participators in `euler-5`. It will distributed at the end of takeoff round and this is 43,3% of Genesis supply, so it should be hot in the end.

- **Be a validator**. You can earn tokens through inflation as a validator. The `euler-4` validators will get 20 TEULs in `euler-5` for their support.

## Provision of the Game

The Game will start with `euler-5` network launch and contract deployment.

The takeoff donation will start after approving the government proposal of takeoff donation start and will last until 1 of 2 control events happens:

-  90 days will be passed after the takeoff funding start
-  600,000 ATOMs well be donated

After the end of the takeoff donation, we will distribute test EUL tokens for participators of the takeoff. This will start the final round of the Game of Links.

At this time will come key gamers with significant stakes and make a powerful impact on the Game results.

The final round will be playing for 21 days after EULs distribution.

## Takeoff funding and disciplines incentives

Takeoff funding has 3 key goals:
- bootstrapping genesis validator set
- definition of allocation for cyber\~Congress participants
- definition of allocation to Game of Links participants

The Game result and distribution significantly influenced by the Takeoff donation results. If 600k ATOM is raised during takeoff round 10% of CYB will be distributed. The logic is the following: the more amount raised the more rewards game of stakes acquire. The following criteria form a basis for payouts in the Game of Links. Participants, which want to get CYBs in Genesis file of mainnet but cannot play, can donate ATOMs, therefore, increasing the percentage of payouts for other participants and for themselves. The following formula define allocation for takeoff donors. 

$$ formula $$ 

![takeoff-distribution](takeoff_distribution.png)

The development of the project has been done thanks to investments of 10 people. ~3200 ETH has been spent during 3 years of development. For that at least 4% CYB is allocated for them by means of THC from cyber•Congress allocation. In order to protect seed investors their share will be defined based on the amount raised during takeoff round. In essence, the funding round curve (green curve) defines the allocation of up to 6% CYB for takeoff participants. If takeoff round get 600k ATOMs than seed investors (orange curve) get 4% of CYB by the means of THC and takeoff participants get 6% of CYB directly. If zero amount will be raised remaining CYB allocated to cyber\~Congress and distribute to seed investors, cyber\~Congress and inventors proportionally.





![game-of-links-distribution](GOL_distribution.png)

| Group | Amount CYB (up to) |
| --- | ---: |
| takeoff funding | 60,000,000,000,000 |
|*disciplines*||
| relevance | 15,000,000,000,000 |
| load | 6,000,000,000,000 |
| delegation | 5,000,000,000,000 |
| full validator set | 5,000,000,000,000 |
| lifetime | 2,000,000,000,000 |
| community pool | 2,000,000,000,000 |
| *other* ||
| `euler-4` rewards | 5,000,000,000,000 |


## Type of disciplines

There are six disciplines for playing in the Game of Links of two types:

Depended on takeoff funding:
-  The relevance of links submitted
-  A bandwidth load of every participant
-  Amount of delegated to validators
-  Life summary of every validator

Independent on takeoff funding:
- full validator set
- community pool

There are no limits in disciplines quantity participation. By all means.
You can set up your own validator to get a reward for validator's uptime or you can link CIDs  and load network bandwidth. You can create a promotion around your validator and collect stakes from users. You can do all of those things together. Just play and monitor the results.

## Full validator set
If the set of validators will increase up to 100 and this amount can last during 10000 blocks we will allocate an additional 2 TCYB to validators who take part in genesis evenly. If this amount will increase to 146 under the same conditions we will allocate additional 3 TCYB.

## `euler-4` rewards
Thanks for helping our early validators in `euler-4` testnet. They're running their nodes for the year for the Great future 

## Community pool

2 TCYB allocated to the community pool in `cyber` networkd. During euler-5 we expect from community some experiments with governance. All governance decisions of testnet will be migrated to mainnet.

## Lifetime summary of every validator

The easiest discipline. You need just set up your validator and monitor its lifetime. The lifetime means validators blocks precommits.

> Important! Your validator should be in the set of active validators! Watch your stake!

By following formula calculated each validator reward in the block *n* if precommit was and 600,000 ATOMs collected:

$$r_{n}=\frac{\frac{1}{block_{max}}\cdot 2\ TCYB}{V_{n}}$$

The *r* is reward for vlidator at block *n*, the $block_{max}$ is the latest block of the Game, and *V* the amount of validators on block *n*.

We need to divide the allocated supply to the sum of blocks in the Game period and to the sum of precommits in the current block.

For example, if you have an active validator from the start of the Game of Links till the end without any block missing and other validators do the same way and it funded 600,000 ATOMs on the Auction you will get
$$ R = \frac{2\ TCYB}{146} \approx 13.7\ GCYB$$
in the Genesis file of `cyber` network.

## A bandwidth load of every participant

Easy too. According to our resource credits model, there are no transaction fees. We use bandwidth. The user bandwidth value is the ability of users to send messages, make links and do transactions.

Each message type has assigned bandwidth cost. For this discipline we're using ONLY bandwidth spend to linking.

All bandwidth spending data available at ? RPC/LCD. After the game 6 TCYBs will be distributed to players addresses according to their weight coefficient, other words according to how much they spent. It decreases if the network has a low load and increase if high between 0.01 and inf.

The network has desirable bandwidth in 24 h, so if current bandwidth equals this value it means normal, and the multiplier parameter is 1.00. In other cases, the multiplier is correcting for uploading or downloading the network.

The multiplier value recalculates every minute according to network load last 24 h window. You can always find it on the Game monitors.

User bandwidth depends on its stake as:

$$ bandwidth_{user} = \frac{stake_{user}}{supply_{current}} \cdot bandwidth_{desirable}$$

The genesis $bandwidth_{desirable}$ param available at [launch-kit](https://github.com/cybercongress/launch-kit/tree/0.1.0/params) repo.

User's reward in case 600,000 ATOMs donated calculating next way:

$$ reward_{user} = \frac{bandwidthSpent_{user}}{bandwidthSpent_{all}}\cdot6\ TCYB $$

## Amount of delegated to validators

Validators can earn a reputation in their lifetime rate and infrastructure. It's somekind of promoting their services in early community. We'll allocate up to 5 TCYBs proportionally staked tokens on validators at the last block in the Game. If 600,000 ATOMs will be donated every validator will get:

$$ revard_{validator} = \frac{staked_{validator}}{staked_{all}}\cdot 5\ TCYB $$

## The relevance of links submitted

The most interesting part of the Game. Users can link everything that they believe important for the future web.

There are up to 15 TCYBs allocated for the top 1000 CIDs and top 10 agents linked with that CIDs.

CYBs will be distributed by top 1000 CID proportionally it ranks. In case 600,000 ATOMs donated:

$$  = \frac{rank_{CID}}{rank_{top1000}}\cdot 15\ TCYB $$

Then rewards will be distributed between 10 Agents in submitting link order by a power law:

$$\sum\limits_{i=1}^{10}\frac{a}{i}=reward_{CID} $$

This way we can calculate allocation to the top one CID with Euler's method for the sum of harmonic series like:

$$a\sum\limits_{i=1}^{10}\frac{1}{i}=reward_{CID} \Rightarrow$$
$$a=\frac{reward_{CID}}{\sum\limits_{i=1}^{10}\frac{1}{i}}=\frac{reward_{CID}}{\ln i+\gamma+\epsilon_{i}}$$

Where $\gamma$ is Euler–Mascheroni constant =0.57721..., $\epsilon_{i}\sim\frac{1}{2i}$ .

> Notice! Only available for reading hashes take part in the Game. Make sure that your content pinned and responded.

## Conclusion