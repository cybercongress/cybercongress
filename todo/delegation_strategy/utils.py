import requests
import pandas as pd
import base64
import bech32
import os
import shutil


from tqdm import tqdm
from cyberpy._wallet import address_to_address
from config import LCD_API, BLACK_LIST, JAILED_WINDOW, NUMBER_OF_JAILS_FOR_KICKOFF, DELEGATOR_ADDRESS
from calculations import get_cost_optimization, get_cost_optimization_endorsement, get_decentralization,\
    get_decentralization_endorsement, get_confidence, get_confidence_endorsement, get_reliability,\
    get_reliability_endorsement, get_superintelligence, get_superintelligence_endorsement
from tx import get_unsigned_txs


def b64_to_cons(cons):
    cons = bytes(cons, 'utf-8')
    cons = base64.b64decode(cons)
    five_bit_r = bech32.convertbits(cons, 8, 5)
    return bech32.bech32_encode('bostromvalconspub', five_bit_r)


def get_validators():
    url = LCD_API + '/cosmos/staking/v1beta1/validators?pagination.limit=1000'
    res = requests.get(url).json()['validators']
    height_url = LCD_API + '/cosmos/base/tendermint/v1beta1/blocks/latest'
    min_height = int(requests.get(height_url).json()['block']['header']['height']) - JAILED_WINDOW
    result = [
        (
            validator['description']['moniker'],
            validator['operator_address'],
            int(validator['tokens']),
            float(validator['delegator_shares']),
            float(validator['commission']['commission_rates']['rate']),
            get_self_delegation(validator['operator_address'], int(validator['tokens'])),
            get_power(validator['operator_address']),
            get_jailed_times(validator['operator_address'], min_height),
            get_jailed_times(validator['operator_address'], 2),
            validator['jailed']
        ) for validator in tqdm(res)]
    return pd.DataFrame(result, columns=[
        'moniker',
        'operator_address',
        'staked',
        'delegator_shares',
        'greed',
        'ownership',
        'power',
        'jailed_times_100_000',
        'jailed_times_all',
        'isjailed',
    ])


def get_self_delegation(validator_address: str, tokens: int):
    delegator_address = address_to_address(validator_address, 'bostrom')
    url = LCD_API + f'/cosmos/staking/v1beta1/validators/{validator_address}/delegations/{delegator_address}'
    try:
        delegated = int(requests.get(url).json()['delegation_response']['balance']['amount'])
        delegation_share = delegated / tokens
    except KeyError as e:
        print(e, url)
        delegation_share = 0
    return delegation_share


def get_jailed_times(address: str, min_height: int) -> int:
    url = LCD_API + f'/txs?message.action=%2Fcosmos.slashing.v1beta1.MsgUnjail&message.sender={address}&limit=1000&tx.minheight={min_height}'
    res = requests.get(url).json()
    if 'txs' in res.keys():
        return len(res['txs'])
    else:
        return 0


def get_power(validator_address: str):
    address = address_to_address(validator_address, 'bostrom')
    url = LCD_API + f"/cosmos/bank/v1beta1/balances/{address}"
    try:
        balances = requests.get(url).json()['balances']
    except KeyError as e:
        print(e, url)
        balances = []
    milliampere = list(filter(lambda balance: balance['denom'] == 'milliampere', balances))
    millivolt = list(filter(lambda balance: balance['denom'] == 'millivolt', balances))
    if milliampere == [] or millivolt == []:
        power = 0
    else:
        milliampere = int(milliampere[0]['amount']) / 1000
        millivolt = int(millivolt[0]['amount']) / 1000
        power = milliampere * millivolt
    return power


def processor():
    validators_df = get_validators()
    validators_df['validator_rank'] = validators_df['staked'].rank(ascending=False)
    validators_df = validators_df.drop(validators_df[validators_df['isjailed'] == True].index)
    validators_df = validators_df.drop(validators_df[validators_df['jailed_times_100_000'] > NUMBER_OF_JAILS_FOR_KICKOFF].index)
    validators_df = validators_df[~validators_df['operator_address'].isin(BLACK_LIST)]
    validators_df = validators_df.reset_index(drop=True)
    validators_df['cost_optimization'] = validators_df.apply(lambda x: get_cost_optimization(x['greed']), axis=1)
    validators_df['cost_endorsement'] = validators_df.apply(
        lambda x: get_cost_optimization_endorsement(x['cost_optimization'], validators_df['cost_optimization'].sum()), axis=1)
    validators_df['decentralization'] = validators_df.apply(
        lambda x: get_decentralization(x['validator_rank']), axis=1)
    validators_df['decentralization_endorsement'] = validators_df.apply(
        lambda x: get_decentralization_endorsement(x['decentralization'], validators_df['decentralization'].sum()), axis=1)
    validators_df['confidence'] = validators_df.apply(
        lambda x: get_confidence(x['ownership']), axis=1)
    validators_df['confidence_endorsement'] = validators_df.apply(
        lambda x: get_confidence_endorsement(x['confidence'], validators_df['confidence'].sum()), axis=1)
    validators_df['superintelligence'] = validators_df.apply(
        lambda x: get_superintelligence(x['power']), axis=1)
    validators_df['superintelligence_endorsement'] = validators_df.apply(
        lambda x: get_superintelligence_endorsement(x['superintelligence'], validators_df['superintelligence'].sum()), axis=1)
    validators_df['reliability'] = validators_df.apply(
        lambda x: get_reliability(x['jailed_times_100_000'], x['staked'], x['delegator_shares']), axis=1)
    validators_df['reliability_endorsement'] = validators_df.apply(
        lambda x: get_reliability_endorsement(x['reliability'], validators_df['reliability'].sum()), axis=1)
    validators_df['total'] = validators_df['cost_endorsement'] + validators_df['decentralization_endorsement'] + \
                         validators_df['confidence_endorsement'] + validators_df['reliability_endorsement'] + \
                         validators_df['superintelligence_endorsement']
    validators_df = validators_df.sort_values(by=['total'], ascending=False).reset_index(drop=True)
    validators_df.to_csv('./delegation_strategy.csv', index=False)
    validators_df = validators_df.sort_values(by=['total']).reset_index(drop=True)
    try:
        shutil.rmtree('./txs')
    except OSError as e:
        print("Error: %s : %s" % ('./txs', e.strerror))
    os.mkdir('./txs')
    get_unsigned_txs(DELEGATOR_ADDRESS, validators_df)