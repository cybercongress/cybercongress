# Ultimate validator maintenance guide. Testnet: Euler-1.


## Glossary
  **<your_key_name>**
  **<operator_address>**
## General commands

##### Show all validators

```bash
docker exec cyberd cyberdcli query staking validators --trust-node=true
```

##### Show chain status

```bash
docker exec cyberd cyberdcli status
  --indent
```

##### Distribution params
```bash
docker exec -cyberd cyberdcli query distr params
```

##### The amount of outstanding rewards
```bash
docker exec -ti cyberd cyberdcli query distr outstanding-rewards
```

##### Staking params
```bash
docker exec -ti cyberd cyberdcli query staking params
```

##### Staking pool
```bash
docker exec -ti cyberd cyberdcli query staking pool
```

## Account management

##### Show account information
```bash
docker exec cyberd cyberdcli keys show <your_key_name>
```

##### Show account balance, pubkey in 16, account number and sequence
```bash
docker exec cyberd cyberdcli query account <your_account_address>
```

##### Send tokens
```bash
docker exec cyberd cyberdcli tx send \
  --from=<your_key_name> \
  --to=<cyber_address_to_send_tokens> \
  --account-number=<account_number> \
  --amount=<amount>cyb \
  --sequence=<your_current_sequence> \
  --trust-node \
  --chain-id=<testnet_chain_id>
```

##### List existing keys
```bash
docker exec -ti cyberd cyberdcli keys list
```

##### Delete account from cybercli
```bash
docker exec -ti cyberd cyberdcli keys delete <key_name_to_remove>
```

##### Update account password
```bash
docker exec -ti cyberd cyberdcli keys update <your_key_name>
```

##### Linking content
```bash
docker exec -ti cyberd cyberdcli link
  --from=<your_key_name> \
  --account-number=<account_number> \
  --sequence=<your_current_sequence> \
  --cid-from=<key_phrase_to_link> \
  --cid-to=<kontent_that_you_want_to_link> \
  --trust-node \
  --chain-id=<testnet_chain_id>
```

## Validator commands

##### Get all validators
```bash
docker exec -ti cyberd cyberdcli query staking validators \
    --trust-node=true
```

##### The amount of commission
```bash
docker exec -ti cyberd cyberdcli query distr commission <validator_address>
```

##### State of current validator
```bash
docker exec -ti cyberd cyberdcli query staking validator <validator_address>
```

##### Return all delegations to validator
```bash
docker exec -ti cyberd cyberdcli query staking delegations-to <validator_address>
```

##### Edit an existing validator account
```bash
docker exec -ti cyberd cyberdcli tx staking edit-validator \
  --from=<your_key_name> \
  --account-number=<account_number> \
  --sequence=<your_current_sequence> \
  --commission-rate=<new_comission_rate_percentage> \
  --trust-node \
  --chain-id=<testnet_chain_id>
```

##### Unjail validator previously jailed for downtime
```bash
docker exec -ti cyberd cyberdcli tx slashing unjail
  --from=<your_key_name> \
  --account-number=<account_number> \
  --sequence=<your_current_sequence> \
  --trust-node \
  --chain-id=<testnet_chain_id>
```

## Delegator commands

##### Return distribution delegator rewards according current validator
```bash
docker exec -ti cyberd cyberdcli query distr rewards <delegator_address> <validator_address>
```

##### Return delegator shares with current validator
```bash
docker exec -ti cyberd cyberdcli query staking delegation <delegator_address> <validator_address>
```

##### Return all delegations made from one delegator
```bash
docker exec -ti cyberd cyberdcli query staking delegations <delegator_address>
```

##### Return all unbonding delegatations from a validator
```bash
docker exec -ti cyberd cyberdcli query staking unbonding-delegations-from <validator_address>
```

##### ??? withdraw rewards for either a delegation or a validator
```bash
docker exec -ti cyberd cyberdcli tx distr withdraw-rewards \
  --from=<your_key_name> \
  --account-number=<account_number> \
  --sequence=<your_current_sequence> \
  --trust-node \
  --chain-id=<testnet_chain_id>
```

##### ??? change the default withdraw address for rewards associated with an address
```bash
docker exec -ti cyberd cyberdcli tx distr set-withdraw-addr <your_new_address> \
  --from=<your_key_name> \
  --account-number=<account_number> \
  --sequence=<your_current_sequence> \
  --trust-node \
  --chain-id=<testnet_chain_id>
```

##### Delegate liquid tokens to a validator
```bash
docker exec -ti cyberd cyberdcli tx staking delegate \
  --from=<your_key_name> \
  --account-number=<account_number> \
  --sequence=<your_current_sequence> \
  --amount=<amount>cyb \
  --validator=<validator_address> \
  --trust-node \
  --chain-id=<testnet_chain_id>
```

##### ??? Redelegate illiquid tokens from one validator to another
```bash
docker exec -ti cyberd cyberdcli tx staking redelegate
  --from=<your_key_name> \
  --account-number=<account_number> \
  --sequence=<your_current_sequence> \
  --addr-validator-dest=<new_validator_address> \
  --addr-validator-source=<old_validator_address> \
  --shares-amount string
  --shares-fraction string
  --trust-node \
  --chain-id=<testnet_chain_id>
```

##### ??? unbond shares from a validator
```bash
docker exec -ti cyberd cyberdcli tx staking unbond
  --from=<your_key_name> \
  --account-number=<account_number> \
  --sequence=<your_current_sequence> \
  --shares-amount
  --shares-fraction
  --validator==<validator_address> \
  --trust-node \
  --chain-id=<testnet_chain_id>
```

cyber1hmkqhy8ygl6tnl5g8tc503rwrmmrkjcq4878e0
cybervaloper1hmkqhy8ygl6tnl5g8tc503rwrmmrkjcq4xvhhf

18075045310322.937748814370000000cyb
299738894.424487345540000000cyb

reward from one
docker exec -ti cyberd cyberdcli tx distr withdraw-rewards \
  --from=ales \
  --only-from-validator=cybervaloper1hmkqhy8ygl6tnl5g8tc503rwrmmrkjcq4xvhhf \
  --chain-id=euler-1

comission
docker exec -ti cyberd cyberdcli tx distr withdraw-rewards \
  --from=ales \
  --is-validator \
  --chain-id=euler-1

???
docker exec -ti cyberd cyberdcli query distr slashes BUG!!!
docker exec -ti cyberd cyberdcli query staking unbonding-delegation
docker exec -ti cyberd cyberdcli query staking unbonding-delegations
docker exec -ti cyberd cyberdcli query staking redelegation
docker exec -ti cyberd cyberdcli query staking redelegations
docker exec -ti cyberd cyberdcli query staking redelegations-from

docker exec -ti cyberd cyberdcli tx staking edit-validator \
  --from=ales \
  --website cybercongress.ai \
  --details trusted validator \
  --chain-id=euler-1
