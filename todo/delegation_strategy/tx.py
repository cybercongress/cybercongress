import json
from config import MSGS_IN_TX, GAS_LIMIT, MEMO


def get_tx(messages: list, memo: str, gas_limit: int):
    return {
        "body": {
            "messages": messages,
            "memo": memo,
            "timeout_height": "0",
            "extension_options": [],
            "non_critical_extension_options": []
        },
        "auth_info": {
            "signer_infos": [],
            "fee": {
                "amount": [],
                "gas_limit": str(gas_limit),
                "payer": "",
                "granter": ""
            }
        },
        "signatures": []
    }


def get_msg(delegator_address: str, validator_address: str, amount: int):
    return {
                "@type": "/cosmos.staking.v1beta1.MsgDelegate",
                "delegator_address": delegator_address,
                "validator_address": validator_address,
                "amount": {
                    "denom": "boot",
                    "amount": str(amount)
                }
            }


def get_unsigned_tx(delegator_address: str, validator_addresses: list, amounts: list):
    msgs = []
    for validator_address, amount in zip(validator_addresses, amounts):
        msg = get_msg(delegator_address, validator_address, amount)
        msgs.append(msg)
    return get_tx(msgs, MEMO, GAS_LIMIT)


def get_unsigned_txs(delegator_address: str, df):
    counter = df.shape[0] // MSGS_IN_TX + 1
    c = 0
    for i in range(counter):
        tx = get_unsigned_tx(delegator_address, df[c: c + MSGS_IN_TX].operator_address.to_list(),  df[c: c + MSGS_IN_TX].total.to_list())
        if tx['body']['messages'] == []:
            continue
        else:
            with open(f"./txs/unsigned_{i}.json", "w") as fp:
                json.dump(tx, fp, indent=4)
            c += MSGS_IN_TX