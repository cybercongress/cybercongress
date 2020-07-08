---
date: 2020-07-01
url: cycle-upgrade
title: 'Cycle upgrade'
author: litvintech
---

## Intro

Euler-6 is the latest incentivized test network of the Euler series. Test networks, especially incentivized once, can provide a playground for the community to battle-test protocols and their implementations.

Blockchain development is difficult from many perspectives. Software which runs in a decentralized environment has a lot of failure points. This software has bugs. And the continuous process of finding and fixing them is part of the development.

During Euler 1-5 a lot of bugs were found and fixed by the cyber\~Congress team and by community members. These fixes required to restart the chain or to relaunch the network.

Thanks to the upgrade module and [service](https://github.com/regen-network/cosmosd) introduced by the Regen Network team (which was tested in a series of Regen Network testnets and then merged into one of the latest Cosmos-SDK releases), we have the option for repairing and adding features without the necessity to restart* the network from genesis.

*Onchain upgrades do have some limitations, especially with regards to things like storage and encoding.

On block #195180 of Euler-6, we detected consensus failure from a couple of validators nodes, which fortunately did not kill the network with a liveness fault, but became an alarm signal to start the diagnostic of this strange behaviour.

The cyber\~Congress team started to collect data about the faulty behaviour of nodes coming from community reports and found a 1-line bug, which was the cause of these problems*.

*There is a possibly of another complicated bug which leads to the same problem, but we are addressing the issues one by one.

In this post, we’ll describe it's meaning and the fix for it. How to fix the network with zero-downtime using the upgrade module, and coordination between validators.

## The Bug

On Cyber's knowledge graph account balances are used for calculating cyber~Rank. Accounts balances consist of bonded and non-bonded stakes. All of the balances are written and read from the storage according to the default functionality of Cosmos-SDK. To calculate the CID of the ranks on the knowledge graph we require fast access to the weights of cyberlinks, which are, basically the current accounts balances. For this purpose, a special wrapper-module was implemented on top of SDK's bank module. This module tracks changes in accounts balances every single block, and calls hooks to update the in-memory balances index (on block's end), which is available to other modules (used in bandwidth and rank modules).

__The bug was here:__

```go
func (k Keeper) DelegateCoins(ctx sdk.Context, delegatorAddr, moduleAccAddr sdk.AccAddress, amt sdk.Coins) error {
  err := k.Keeper.DelegateCoins(ctx, delegatorAddr, moduleAccAddr, amt)
  if err == nil {
--    k.onCoinsTransfer(ctx, nil, moduleAccAddr) <-- Delegator address not passed to hook
++    k.onCoinsTransfer(ctx, delegatorAddr, nil) <-- Fixed
    }
  return err
}
```

This means that the chain did not track delegation actions correctly from genesis. Change in the module balance was tracked instead of changes on the delegator’s account balance.

That lead to incorrect rank calculations and the impossibility for nodes to restart when such a case occurred. All the details of the bug will be clarified below, as well as, an explanation of how the network is still functioning and what will the upgrade fix.

## Deep dive

Calculations within the Cyber protocol and those of cyber~Rank are driven by consensus between validators. This means that for cases with incorrectly-tracked delegations, all of the nodes that are online calculate the ranks using incorrect values for a certain period of time. 

The issue arises when a node operator attempts to restart their node, and the in-memory balance index is loaded and restored directly from the current storage state, which is, of course, different when compared to all the online nodes, iteratively updated the in-memory index. This leads to a different hash calculation of the application (the root hash of the Merkle Tree of CID rank values) and, essentially - node failure.

__But:__

1. The wrapper-module only collects the events with a balance change. Actual balance updates for the in-memory index are performed on the end-block side operation of the module. This means that we don't need to catch up on all of the events, but only to events, which trigger balance update for a given account on this block to keep things working
2. Indexed balance of an account consists of non-bonded stake plus of the cumulative sum of all shares from all validators (shares are used to calculate the portion of the delegators tokens in the validator pool)
3. Delegations to a validator that has never been jailed would not cause overall balance change because non-bonded and bonded stake sums are equal before and after delegation. Token/shares exchange rate is 1/1 (read about [delegator shares](https://docs.cosmos.network/master/modules/staking/01_state.html#delegator-shares)). And untracked delegation actions don't lead to balance index issues
4. If the validator was jailed before their first delegation from a delegator, then the delegator will receive a number of shares, which is unequal to the amount of the delegated tokens, because of the changed exchange rate of token/shares
5. Only the first delegation to a validator leads to a problem. Any further delegations to a specific validator trigger the staking module reward withdrawals and calls for the staking hook, which calls the bank module to send coins to the delegator. This leads to a new hook call to update the in-memory index balance. While the first delegation does not cause balance traction, withdrawal causes balance updates to the correct value
6. All other actions with regards to balance change events are processed correctly by the wrapper-module

__To summarize:__

The issue appears when at least one account, which has already created some cyberlinks and committed them to the knowledge graph, performs its first delegation to a validator, which was jailed before and doesn't process any other balance changing transactions for a given time. During this time, the in-memory index holds data with an incorrect balance for this account (or for a couple of accounts). However, when this happens when there is consensus between all online nodes, the issue does not trigger a network fault, but rather, leads to the impossibility to launch and sync the node or to calculate cyber~Rank values, that will be equal to the current consensus state. During launch or restart, the node restores the in-memory balance index from the current storage, unlike the online nodes, iteratively, it updates the index from a cached-up state.

The difference between a wrong balance and the actual balance is tiny, but it still leads to changes in the weights of cyberlinks, ranks values and consequently, the consensus application hash (the root hash of Merkle Tree of the rank values). This means that from the genesis of the Euler-6 network until a successful fix, we will have periods when it will not be possible to stop and then to re-launch a node. This is because the actual state of the application and the consensus state is different. Only when these states are the same it becomes possible to re-launch the node successfully.

## Tracking index variance

When the issue was first identified we launched a special node with an upgraded binary that allowed us to track any accounts that made transactions and compare* their actual and indexed balances on the end of each block. Thus, we were able to see when the index was “broken” and simply fix it by making a `send transactions` with a few tokens to the required accounts.

*At peak there were a maximum of 5 accounts with an issue like this.

Since the moment we discovered the issue we regularly made and published backups (on blocks with no variance) to allow validators that caught this bug to restore promptly.

These manual manipulations allowed us to support chain health and correct operation but it's time for the community to perform the upgrade and fix this issue permanently.

## Time to

Euler-6 network passed 1.3M blocks and attracted more than 21 heroes (validators) fighting for freedom and the uncensored access to relevant information across the Great Web.

As a community, we are ready to perform our first on-chain upgrade to repair the work of the network and the protocol. This will be a huge professional milestone for validators, as well as, for the community. Maturity in solving common tasks associated with the project.

## About the upgrade process

During preparations for the launch of Euler-6, we published documents that describe how to configure a node in a way, so it would be compatible with on-chain upgrades. If validators were following these guides during their setup process, minimal efforts will be required to upgrade successfully.

1. During the next few days, we will release a new version of Cyberd with the required patch
2. We will start to support the upgrade process for validators
3. We will introduce a proposal to upgrade the network onto a new version using the current on-chain governance
4. The upgrade proposal will be set to a specific block height
5. During the voting period of the proposal and before the specified upgrade, validators will need to equip their nodes with a new build of Cyberd 
6. At the given height, the network will stop at the same time for all nodes and will attempt to launch with the new upgraded binary. As soon as all the nodes will boot-up and the network will accumulate the minimal required consensus power, the block production will continue from a clean slate
