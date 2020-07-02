---
date: 2020-07-01
url: cycle-upgrade
title: 'Cycle upgrade'
author: litvintech
---

## Intro

Euler-6 is the latest incentivized test network of the Euler series. Test networks, especially incentivized once, provide a playground to the community to battle-test protocols and their implementations.

Blockchain development is difficult from many perspectives. Software which runs in a decentralized environment has a lot of failure points. This software has bugs, and the continuous process of finding and fixing them is part of the development.

During Euler 1-5 a lot of bugs were found and repaired by the cyber\~Congress team and community members. These fixes required to restart the chain or to launch a new network.

Thanks to the upgrade module introduced by the Regen Network team, tested in a series of Regen network testnets and then merged into one of the latest Cosmos-SDK releases, we now have an option for repairing and adding features without the necessity to restart* the whole network from genesis.

*Onchain upgrades do have some limitations, especially for things like storage and encoding.

On block # 195180 of Euler-6, we detected consensus failure for a couple of validators nodes, which fortunately did not kill the network with a liveness fault, but it was an alarm signal to start the diagnostic of the strange behaviour.

The cyber\~Congress team started to collect data about the faulty behaviour of nodes coming from community reports and found a 1-line bug, which was the cause of these problems.

In this post, we’ll describe it's meaning and the fix for the bug. How to fix the network with zero-downtime using an upgrade module and coordination between validators.

## Bug

Account balances on Cyber's knowledge graph are used for calculating cyber~Rank. Accounts balances consist of bonded and non-bonded stake. All balances are written and read from the storage, according to the default functionality of Cosmos-SDK. To calculate CID ranks on the knowledge graph, we need fast access to the weights of cyberlinks, which are, basically - current accounts balances. For this purpose, a special wrapper-module was implemented on top of SDK's bank module. This module tracks changes in the accounts balances, every single block, and calls hooks to update the in-memory balances index, which is available to other modules (used in bandwidth and rank modules).

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

This means that the chain did not track the delegation actions correctly from the genesis: change in the module balance was tracked instead of changes on the delegator’s account balance.

That leads to incorrect rank calculation and impossibility for cyber nodes to restart when such a case occurs. All the details of the bug will be clarified below, as well as an explanation of how the network is functioning currently and what will the upgrade fix.

## Deep Dive

Calculations within Cyber protocol and of cyber~Rank are driven by consensus between validators. It means that for cases with incorrectly-tracked delegations, all nodes that use the current weight of account balances to calculate rank, which might be not correct for an account that recently committed cyberlinks to knowledge graph and performed delegations to validators.

An issue comes up when a node operator attempts to restart the node and the in-memory balance index is loaded directly from the current node storage state, which is, of course, different when compared to all the online nodes, iteratively updated the in-memory index. This leads to a different hash calcualtion of the application (root hash of the Merkle Tree of CIDs rank values) and, essentilay - node failure.

__But:__

1. The wrapper-module collects only the events of balance change. Actual balance updates for the in-memory index are performed on the end-block operation of the module. That means that in the overall case, we dont need to catch up on all events, but on any event, which triggers a balance update for a given account on this block to keep things working
2. Indexed balance of an account consists of non-bonded stake plus of the cumulative sum of all shares from all validators (shares are used to calculate the portion of the delegators tokens in the validator pool)
3. Delegations to a validator that is newly jailed would not cause overall balance change because non-bonded and bonded stake sums are equal before and after delegation, and token/shares exchange rate is 1\1 (read about [delegator shares](https://docs.cosmos.network/master/modules/staking/01_state.html#delegator-shares)). And untracked delegation actions don't lead to balance index issues
4. If the validator was jailed before the first delegation from a specific delegator, then the delegator will receive an amount of shares not equal to the amount of delegated tokens because of the changed exchange rate of token/shares
5. Only the first delegation to a validator leads to a problem. Because any further delegations to a specific validator triggers staking module rewards withdrawal and calls staking hook, which calls the bank module to send coins to the delegator. That leads to a new hook call to update the in-memory index balance. While fist delegation is not causing balance traction, withdraw causes balance updates up to the correct value
6. All other actions with regards to balance change events, process correctly by the wrapper-module

__To summarize:__

The issue appears when at least one account, which already created cyberlinks and committed them to the knowledge graph, performs its first delegation to a validator, which was jailed before, and doesn't process any other balance changing transaction for a given time. During this time, the in-memory index holds data with incorrect balances. However, when this happens where there is consensus between all nodes that are online, the issue does not trigger network fault, but leads to the impossibility to launch and sync a node or to calculate cyber~Rank that will be equal to the current consensus state. During launch or restart, the node restores the in-memory balance index from the current storage, unlike the nodes that are online, iteratively, it updates the index from catched-up state.

## Tracking index variance

When the issue was discovered, we launched a special node with an upgraded binary that allowed us to track any accounts that made transactions and compare their actual and indexed balances on each blocks end. Thus, we were able to see when the index is “broken” and simply fix it by making `send transactions` with a few tokens to the needed accounts.

Since the moment we discovered the issue,  we periodically made and published backups to allow validators, who caught this bug, to restore quickly.

These manual manipulations allowed us to support chain health and correct operation but it's time for the community to perform the upgrade and fix this issue permanently.

## Time to

Euler-6 network passed 1.3M blocks and attracted more than 21 heroes (validaotrs) fighting for freedom and uncensored access to relevant information across the Great Web.

As a community, we are ready to perform the first online / onchain upgrade to repair the work of the network and the protocol. This will be a huge professional milestone for validators, as well as, for community maturity in solving common tasks related to the project.

## About the upgrade process

During preperations for the launch of Euler-6, we published documents for node setup, that describe how to configure a node in a manner to be compatible with onchain upgrades. If validators were following that guide during their setup proccess, minimal efforts would be required to upgrade successfully.

1. During the next few days, we will release a new version of Cyberd with the required patch
2. We will start to support the upgrade process for validators
3. We will introduce a proposal to upgrade the network onto a new version using the current network governance
4. The upgrade proposal will be set to a specific block height
5. During the voting period of the proposal and before the specified upgrade, validators will need to equip their nodes with a new build of Cyberd 
6. At the given height, the network will stop on the same time for all nodes and will attempt to launch with the new upgraded binary. As soon as all nodes will boot-up and the network will accumulate the minimal required consensus power, the block production will continue clean and healthy 
