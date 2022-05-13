# Supply API

The API service for `total_supply` and `circulation_supply`

## Total supply API

The amount of BOOT from the following [enpoint](https://lcd.bostrom.cybernode.ai/cosmos/bank/v1beta1/supply/boot)


## Circulation supply API

The amount of BOOT token from the following [enpoint](https://lcd.bostrom.cybernode.ai/cosmos/bank/v1beta1/supply/boot) excluding:

1. Staked tokens ([link](https://lcd.bostrom.cybernode.ai/cosmos/staking/v1beta1/pool))
2. Gift [account](https://lcd.bostrom.cybernode.ai/cosmos/bank/v1beta1/balances/bostrom1qs9w7ry45axfxjgxa4jmuhjthzfvj78sxh5p6e/boot)
3. The Great Web foundation multisig [account](https://lcd.bostrom.cybernode.ai/cosmos/bank/v1beta1/balances/bostrom1ha4pw9w2qgc2ce9jwfrwrmaft5fneus58nqwev/boot)
4. Community [pool](https://lcd.bostrom.cybernode.ai/cosmos/distribution/v1beta1/community_pool)