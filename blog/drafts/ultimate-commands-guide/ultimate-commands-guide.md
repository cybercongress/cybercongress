# Ultimate validator maintenance guide. Testnet: Euler-1.

<operator_address> you can take from
`docker exec -ti cyberd cyberdcli query staking validators --trust-node=true`


show all validators
`docker exec cyberd cyberdcli query staking validators --trust-node=true`

show chain status
`docker exec cyberd cyberdcli status --indent`

show address information
`docker exec cyberd cyberdcli keys show <your_key_name>`

Show account balance, pubkey in 16, account number and sequence
`docker exec cyberd cyberdcli query account <your_account_address>`

distribution params
`docker exec -ti cyberd cyberdcli query distr params`

the amount of outstanding rewards
`docker exec -ti cyberd cyberdcli query distr outstanding-rewards`

the amount of commission
`docker exec -ti cyberd cyberdcli query distr commission <validator_address>`

distribution delegator rewards
`docker exec -ti cyberd cyberdcli query distr rewards <delegator_address> <validator_address>`

return delegator shares with current validator
`docker exec -ti cyberd cyberdcli query staking delegation <delegator_address> <validator_address>`

return all delegations made from one delegator
`docker exec -ti cyberd cyberdcli query staking delegations <delegator_address>`

state of your validator
`docker exec -ti cyberd cyberdcli query staking validator <validator_address>`

return all delegations to one validator
`docker exec -ti cyberd cyberdcli query staking delegations-to <validator_address>`

return all unbonding delegatations from a validator
`docker exec -ti cyberd cyberdcli query staking unbonding-delegations-from <validator_address>`

staking params
`docker exec -ti cyberd cyberdcli query staking params`

staking pool
`docker exec -ti cyberd cyberdcli query staking pool`

send tokens
`docker exec cyberd cyberdcli tx send --from=<your_key_name> --account-number=<account_number> --amount=<amount>cyb --sequence=<sequence> --trust-node --chain-id=<testnet_chain_id>`

??? withdraw rewards for either a delegation or a validator
`docker exec -ti cyberd cyberdcli tx distr withdraw-rewards --from=<your_key_name> --account-number=<account_number> --sequence=<sequence> --trust-node --chain-id=<testnet_chain_id>`

??? change the default withdraw address for rewards associated with an address
`docker exec -ti cyberd cyberdcli tx distr set-withdraw-addr <your_new_address> --from=<your_key_name> --account-number=<account_number> --sequence=<sequence> --trust-node --chain-id=<testnet_chain_id>`

cyber1hmkqhy8ygl6tnl5g8tc503rwrmmrkjcq4878e0
cybervaloper1hmkqhy8ygl6tnl5g8tc503rwrmmrkjcq4xvhhf

AccountNumber: 62310
  Sequence:      2







???
docker exec -ti cyberd cyberdcli query distr slashes
docker exec -ti cyberd cyberdcli query staking unbonding-delegation
docker exec -ti cyberd cyberdcli query staking unbonding-delegations
docker exec -ti cyberd cyberdcli query staking redelegation
docker exec -ti cyberd cyberdcli query staking redelegations
docker exec -ti cyberd cyberdcli query staking redelegations-from
