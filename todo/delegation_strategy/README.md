# Delegation strategy for cyber~congress

That toolkit provides a delegation strategy for `bostrom` heroes from cyber~congress multisig. 

The aim is to build strong heroes set by endorsing their stake with cyber~congress power. According to cyber~congress values, decentralization, confidence, reliability, and superintelligence will be encouraged. Also, additional delegations from cyber~congress will help cover maintaining validators running costs.

That toolkit should help distribute multisig tokens in the correct way and to automatize the delegation/redelegation/unbonding processes.

The result of that tool execution is a pivot table with all calculations in detail and unsigned transaction files for signing and broadcasting.

## Criteria

The allocation of the delegation strategy programm is 92 TBOOT.

```python
ALLOCATION = 92_000_000_000_000
```

***Cost optimization.***

Each hero decides which commission he wants to grab from their delegators. This mechanics provides resources for heroes to maintain their nodes in a high-reliability way. But, some heroes skip this simple rule and keep zero-fee validators online for some kind of advertisement. On the other hand, some of the validators increase their commission rates up to 100%. Both of these cases are not encouraged. After some investigation and experience with other networks, the optimal parameter was found. This is 5% of the commission rate. This way, the distribution function for cost endorsement will be:

```python
def get_cost_optimization_endorsement(
        cost_optimization,
        cost_optimization_sum,
        cost_strategy,
        cost_strategy_sum
        ):
    cost_optimization_share = cost_optimization / cost_optimization_sum
    cost_strategy_share = cost_strategy / cost_strategy_sum
    return int((cost_optimization_share + cost_strategy_share) * 0.5 * ALLOCATION * COST_OPTIMIZATION)
```

where:
`COST_OPTIMIZATION` = 0.3
`cost_optimization_sum` is the sum of `cost_optimization` for all heroes,
`cost_strategy_sum` is the sum of `cost_strategy` for all heroes
`cost_optimization` is:

```python
def get_cost_optimization(commission: float):
    if commission <= 0.05:
        return int(8000 * commission)
    else:
        return int(math.ceil(1 / (commission ** 2)))
```
That function is linear rising from zero to 400 points (the maximum for that criterion) and then falling as reverse quadratic.

The `cost_strategy` is :

```python
def get_possible_cost_strategy(commission_rate_change: float):
    return 101.01 - 101.01 * commission_rate_change
```

***Decentralization.***

This criterion is necessary in order to discourage the formation of cartels in the network, as well as to protect the network from attack vectors associated with poor decentralization. Due to this criterion, the result of the tool will be a little blurry in favor of decentralization.

The idea is ranking validators descending by staked tokens and give them weighted points:

```python
def get_decentralization(rank, sum_rank):
    return rank / sum_rank
```

And then distribute tokens:

```python
def get_decentralization_endorsement(rank_share):
    return int(rank_share * ALLOCATION * DECENTRALIZATION)
```

where `DECENTRALIZATION` = 0.25

***Confidence.***

The hero's confidence shows the relationship between the tokens that the hero has delegated to himself and the tokens that the hero owns. If the hero is not ready to put tokens on the validator he supports, then his confidence level is low. That is why only those heroes who believe in themselves will be encouraged.

```python
def get_confidence(ownership, ownership_sum):
    return ownership / ownership_sum
```

And the distribution is:

```python
def get_confidence_endorsement(confidence):
    return int(confidence * ALLOCATION * CONFIDENCE)
```

where `CONFIDENCE` = 0.2

***Reliability.***

The most complex criterion. It should help to understand the sustainability of the hero node set-up. 

Here the subcriteria will be defined:
- pre commits
- jails
- tokens blurring

`pre commits` is a ratio between validators pre commits distinct on the block since the first signed block as a hero and amount of blocks since that time. This subcriterion is calculated for the whole hero's lifetime.

`jails` is the amount of `unjail` transactions from the hero. In other words, this subcriterion is about how many times the validator was jailed for some kind of misbehavior.

`tokens blurring` is the ratio between `staked` and `delegator_shares` tokens. It shows how many tokens validator lost cause of slashing. 

The sum of the normed of that subcriteria is formed reliability criteria:

```python
def get_reliability(pre_commits, jails, staked, delegator_shares):
    tokens_bluring = delegator_shares / staked
    tokens_bluring_points = (tokens_bluring ** 3) * 100
    pre_commits_points = ((pre_commits / 100) ** 2) * 100
    jails_points = (1 / 2 ** jails) * 100
    if jails_points < 0.0009765625:
        jails_points = 0.0
    return tokens_bluring_points + pre_commits_points + jails_points
```

The tokens loss is very serious misconduct. If the validator didn't lose anything the `tokens_bluring` will be equal to 1. The cube function is defined for that criterion. The same schema for `pre commits`, but with a quadratic function. And halving schema for jails.

The distribution is:

```python
def get_reliability_endorsement(reliability, reliability_sum):
    return int((reliability / reliability_sum) * ALLOCATION * RELIABILITY)
```

where `RELIABILITY` = 0.15

***Superintelligence.***

This criterion shows the power of the hero or the product of Volts and Amperes owned by the validator.

```python
def get_superintelligence(power, power_sum):
    return power / power_sum
```

The distribution is:

```python
def get_superintelligence_endorsement(superintelligence):
    return int(superintelligence * ALLOCATION * SUPERINTELLIGENCE)
```

where `SUPERINTELLIGENCE` is 0.1

## Black list

In that list heroes who announced of quitting are placed.

## Usage (python3 required)

0. Install requirements

```bash
pip3 install -r requirements.txt
```

1. Fill `config.py`

2. Run script

```bash
python3 main.py
```

The result of the script execution is .csv file with pivot table

## Example calculations

[here](./delegation_strategy.csv) the result of script execition for 2022-04-27 