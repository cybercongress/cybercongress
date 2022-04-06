import requests
import pandas as pd
import base64
import bech32


from tqdm import tqdm
from cyberpy._wallet import address_to_address
from config import LCD_API, GRAPHQL_API, HEADERS
from calculations import get_cost_optimization, get_cost_optimization_endorsement, get_decentralization,\
    get_decentralization_endorsement, get_confidence, get_confidence_endorsement, get_reliability,\
    get_reliability_endorsement, get_superintelligence, get_superintelligence_endorsement



def b64_to_cons(cons):
    cons = bytes(cons, 'utf-8')
    cons = base64.b64decode(cons)
    five_bit_r = bech32.convertbits(cons, 8, 5)
    return bech32.bech32_encode('bostromvalconspub', five_bit_r)


def run_query(query):  # A simple function to use requests.post to make the API call. Note the json= section.
    request = requests.post(GRAPHQL_API, json={'query': query}, headers=HEADERS)
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception("Query failed to run by returning code of {}. {}".format(request.status_code, query))


def get_precommits():
    query = '''{
                  pre_commits_total {
                    consensus_pubkey
                    pre_commits
                  }
                }'''
    result = run_query(query)['data']['pre_commits_total']
    res =  [(x['consensus_pubkey'], x['pre_commits']) for x in result]
    return pd.DataFrame(res, columns=['consensus_pubkey', 'pre_commits'])


def get_validators():
    url = LCD_API + '/cosmos/staking/v1beta1/validators'
    res = requests.get(url).json()['validators']
    result = [
        (
            validator['description']['moniker'],
            validator['operator_address'],
            address_to_address(validator['operator_address'], 'bostrom'),
            b64_to_cons(validator['consensus_pubkey']['key']),
            int(validator['tokens']),
            float(validator['delegator_shares']),
            float(validator['commission']['commission_rates']['rate']),
            get_self_delegation(address_to_address(validator['operator_address'], 'bostrom'), validator['operator_address']),
            get_jailed_times(validator['operator_address'])
        ) for validator in tqdm(res)]
    return pd.DataFrame(result, columns=[
        'moniker',
        'operator_address',
        'address',
        'consensus_pubkey',
        'staked',
        'delegator_shares',
        'greed',
        'ownership',
        'jailed_times'
    ])


def get_self_delegation(delegator_address: str, validator_address: str):
    url = LCD_API + f'/cosmos/staking/v1beta1/validators/{validator_address}/delegations/{delegator_address}'
    try:
        delegated = int(requests.get(url).json()['delegation_response']['balance']['amount'])
    except KeyError as e:
        print(e, url)
        delegated = 0
    url = LCD_API + f'/cosmos/bank/v1beta1/balances/{delegator_address}/boot'
    try:
        balance = int(requests.get(url).json()['balance']['amount'])
    except KeyError as e:
        print(e, url)
        balance = 0
    if balance == 0:
        return 0
    url = LCD_API + f'/cosmos/staking/v1beta1/delegations/{delegator_address}'
    try:
        res = requests.get(url).json()['delegation_responses']
        delegations = sum([int(delegation['balance']['amount']) for delegation in res])
    except KeyError as e:
        print(e, url)
        delegations = 0
    if balance + delegations == 0:
        return 0
    return delegated / (balance + delegations)


def get_jailed_times(address: str) -> int:
    url = LCD_API + f'/txs?message.action=%2Fcosmos.slashing.v1beta1.MsgUnjail&message.sender={address}&limit=1000'
    res = requests.get(url).json()
    if 'txs' in res.keys():
        return len(res['txs'])
    else:
        return 0


def get_power(df):
    power = []
    for index, row in tqdm(df.iterrows()):
        url = LCD_API + f"/cosmos/bank/v1beta1/balances/{row['address']}"
        balances = requests.get(url).json()['balances']
        milliampere = list(filter(lambda balance: balance['denom'] == 'milliampere', balances))
        millivolt = list(filter(lambda balance: balance['denom'] == 'millivolt', balances))
        if milliampere == [] or millivolt == []:
            milliampere = 0
            millivolt = 0
        else:
            milliampere = int(milliampere[0]['amount']) / 1000
            millivolt = int(millivolt[0]['amount']) / 1000
        power.append(milliampere * millivolt)
    return power


def processor():
    validators_df = get_validators()
    precommits_df = get_precommits()
    result_df = validators_df.merge(precommits_df, on='consensus_pubkey', how='outer')
    result_df['pre_commits'] = result_df['pre_commits'].fillna(0.0)
    result_df['power'] = get_power(result_df)
    result_df['validator_rank'] = result_df['staked'].rank(ascending=False)
    result_df['cost_optimization'] = result_df.apply(lambda x: get_cost_optimization(x['greed']), axis=1)
    result_df['cost_endorsement'] = result_df.apply(
        lambda x: get_cost_optimization_endorsement(x['cost_optimization'], result_df['cost_optimization'].sum()), axis=1)
    result_df['decentralization'] = result_df.apply(
        lambda x: get_decentralization(x['validator_rank'], result_df['validator_rank'].sum()), axis=1)
    result_df['decentralization_endorsement'] = result_df.apply(
        lambda x: get_decentralization_endorsement(x['decentralization']), axis=1)
    result_df['confidence'] = result_df.apply(
        lambda x: get_confidence(x['ownership'], result_df['ownership'].sum()), axis=1)
    result_df['confidence_endorsement'] = result_df.apply(
        lambda x: get_confidence_endorsement(x['confidence']), axis=1)
    result_df['reliability'] = result_df.apply(
        lambda x: get_reliability(x['pre_commits'], x['jailed_times'], x['staked'], x['delegator_shares']), axis=1)
    result_df['reliability_endorsement'] = result_df.apply(
        lambda x: get_reliability_endorsement(x['reliability'], result_df['reliability'].sum()), axis=1)
    result_df['superintelligence'] = result_df.apply(
        lambda x: get_superintelligence(x['power'], result_df['power'].sum()), axis=1)
    result_df['superintelligence_endorsement'] = result_df.apply(
        lambda x: get_superintelligence_endorsement(x['superintelligence']), axis=1)
    result_df['total'] = result_df['cost_endorsement'] + result_df['decentralization_endorsement'] + \
                         result_df['confidence_endorsement'] + result_df['reliability_endorsement'] + \
                         result_df['superintelligence_endorsement']
    result_df = result_df.sort_values(by=['total'], ascending=False)
    result_df.to_csv('./delegation_strategy.csv', index=False)