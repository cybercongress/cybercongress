## Intro

Euler-6 is the latest current cyber network testnet of the incoming Euler series. Testnets, especially incentivized one, gives the playground to the community to battle-test protocol and their implementation. 

Blockchain development is hard in many perspectives. Software which runs in a decentralized environment has a lot of failure points. This software has bugs, and the continuous process of finding and fixing them  is the part of development. 

During Euler-1/2/3/4/5 a lot of bugs were found and repaired by the core team and community that required the chain restart  or  launch a new network. 

Thanks to the Upgrade module introduced by the Regen team, tested in a series of Regen network testnets and then merged to Cosmos-SDK in 38 release, now we have an option for repairing and adding features without necessity to restart* the whole network from genesis.

*Onchain upgrades though have some limitations of using especially for things like storage and encoding

On block 195180 of euler-6, we detected consensus failure on a couple validators nodes which fortunately did not kill (or “layed down”) the network  with liveness fault, but was an alarm signal to start network  strange behavior diagnostics.

Our team started data collecting about node faulty behaviour from the community reports and found a 1-line bug, which was the cause of those problems.

In this post, we’ll describe the meaning and the fix of the bug, and how to fix the network with zero-downtime using an upgrade module and coordination between validators. 

## Bug

On cyber's knowledge graph account balances are used for cyber~Rank calculation. Accounts balances consist of bonded and non-bonded stake. All balances are written and read from storage according to default functionality of Cosmos-SDK. To calculate CIDs rank in the knowledge graph we need fast access to weights of cyberlinks, which are current accounts balances. For this purpose a special wrapper-module was implemented on top of SDK's bank module . This module tracks changes in accounts balances each block and calls hooks to update in-memory balances index, which available to other modules (used in bandwidth and rank modules)

__Bug was here:__

```
func (k Keeper) DelegateCoins(ctx sdk.Context, delegatorAddr, moduleAccAddr sdk.AccAddress, amt sdk.Coins) error {
  err := k.Keeper.DelegateCoins(ctx, delegatorAddr, moduleAccAddr, amt)
  if err == nil {
--    k.onCoinsTransfer(ctx, nil, moduleAccAddr) <-- Delegator address not passed to hook
++    k.onCoinsTransfer(ctx, delegatorAddr, nil) <-- Fixed
    }
  return err
}
```

The above means that the chain did not track delegation actions correctly since the genesis: module balance change was tracked instead of delegator’s account balance.
That leads to incorrect rank calculation and impossibility for cyber nodes to restart when such a case occurs. All the details of the bug would be clarified below, as well as explanation how the network is functioning currently and what will upgrade fix.

## Deep Dive

Calculations in Cyber protocol and cyber~Rank are driven by consensus between validators. It means for such cases with incorrectly-tracked delegation all nodes using a current weight of account balance to calculate rank, which might be not correct for an account that recently committed cyberlinks to knowledge graph and performed delegations to validators. 

Issue come up when node operator attempts to restart the node and in-memory balance index is loaded directly from the current node storage state, which is different  compared to  all online nodes iteratively updated in-memory index. This leads to different application hash calculation (root hash of the Merkle Tree of cids rank values) and node failure.

__But:__

1. The wrapper-module collects only events of balance change. Actual balances updates for the in-memory index performed in end-block operation of the module. That means in the overall case we need to catch up not all events, but any event which triggers balance update for a given account in this block to keep things work.
2. Indexed balance of account consists of non-bonded stake plus cumulative sum of shares from all validators (shares used to calculate the delegators tokens portion in validator pool).
3. Delegations on validator which were newer jailed before would not cause overall balance change because non-bonded and bonded stake sums are equal before and after delegation, and token/shares exchange rate is 1\1 (read about [delegator shares](https://docs.cosmos.network/master/modules/staking/01_state.html#delegator-shares)). And untracked delegation action don't lead to balance index issue.
4. If the validator was jailed before the first delegation of a specific delegator, then the delegator will receive an amount of shares not equal to amount of delegated tokens because of the changed exchange rate of token/shares.
5. Only the first delegation to the validator leads to a problem. Because any next (after first) delegation to a specific validator triggers staking module rewards withdrawal and calls staking hook, which calls the bank module to send coins to the delegator. That leads to a new hook call to update the in-memory index balance. While fist delegation is not causing balance traction, withdraw causes balance updates up to the correct value.
6. All other balance change actions events process correctly by wrapper-module.

__To summarize:__

The issue appears if at least one account, which already created cyberlinks and committed them to the knowledge graph, performs its first delegation to a validator, which was jailed before, and doesn't process any other balance changing transaction for a given time. For that time in-memory index holds data with incorrect balances. However, when this happens during consensus between all online nodes, this does not trigger network faults but leads to impossibility to launch and sync node or calculate cyber~Rank on existing one, that would be equal to the current consensus state. During launch or restart, node restores in-memory balance index from current storage state unlike online nodes iteratively update index from catched-up actions.

## Tracking index variance

When the issue was diagnosed, we launched a special cyber node with an upgraded binary that allowed us to track any accounts that made transactions and compare their actual and indexed balances at each block end. Thus we were able to see when the index is “broken” and simply fix it by making send transactions for few tokens to the needed accounts.

Since the moment we discovered the issue,  we periodically made and published backups to allow validators, who caught this bug, to restore quickly.
These manual manipulations allowed us to support chain health and correct operation but it's time for the community to perform the upgrade and fix this issue permanently.

## Time to

Euler-6 network passed 1.3M blocks and attracted more than 20 validators - heroes fighting for freedom and uncensored access to relevant information across the whole Great Web. 
As a community, we are ready to perform first online onchain upgrade to repair chain and protocol work. This will be a huge professional milestone for validators as well as for community maturity in solving common project tasks.

## About the upgrade process

During Euler-6 launch preparation, we published node setup documentation that describes how to configure node in the manner to be compatible with onchain upgrades. If the validator was following that guide during his node setup, minimal efforts would be required to upgrade successfully.
1. During few next days we will release a new cyber version with the needed patch
2. We will start educating and support process for validators
3. We will introduce a proposal to upgrade the network onto new version using network governance 
4. The upgrade proposal will be set to a specific height
5. During proposal voting period and before specified upgrade block validators would need to equip their nodes with new cyber's build
6. At the given height the network will stop at the same time at all nodes and attempt to launch with the new upgraded binary. As soon as all nodes would boot-up and the network would accumulate minimal required consensus power - block production will continue in the new healthy chain.


