from flask import Flask
import requests


app = Flask(__name__)


@app.route('/total_supply', methods=['GET'])
def total_supply():
    global SUPPLY
    try:
        supply = int(requests.get('https://lcd.bostrom.cybernode.ai/cosmos/bank/v1beta1/supply/boot').json()['amount']['amount'])
        SUPPLY = supply
    except Exception:
        supply = SUPPLY.copy()
    return str(supply)


@app.route('/circulating_supply', methods=['GET'])
def circulating_supply():
    global C_SUPPLY
    try:
        supply = int(requests.get('https://lcd.bostrom.cybernode.ai/cosmos/bank/v1beta1/supply/boot').json()['amount']['amount'])
        # staked_supply = int(requests.get('https://lcd.bostrom.cybernode.ai/cosmos/staking/v1beta1/pool').json()['pool']['bonded_tokens'])
        gift_supply =  get_balance('bostrom1qs9w7ry45axfxjgxa4jmuhjthzfvj78sxh5p6e')
        # gw_foundation = int(requests.get(
        #     'https://lcd.bostrom.cybernode.ai/cosmos/bank/v1beta1/balances/bostrom1ha4pw9w2qgc2ce9jwfrwrmaft5fneus58nqwev/boot').json()[
        #                         'balance']['amount'])
        c_pool = get_c_pool()
        # c_supply = supply - staked_supply - gift_supply - c_pool - gw_foundation
        c_supply = supply - gift_supply
    except Exception:
        c_supply = C_SUPPLY.copy()
    return str(c_supply)


def get_c_pool():
    c_pool = requests.get('https://lcd.bostrom.cybernode.ai/cosmos/distribution/v1beta1/community_pool').json()['pool']
    return int(float([item for item in c_pool if item["denom"] == "boot"][0]['amount']))


def get_balance(address):
    gift_supply = requests.get(
        f'https://lcd.bostrom.cybernode.ai/cosmos/bank/v1beta1/balances/{address}').json()['balances']
    return int(float([item for item in gift_supply if item["denom"] == "boot"][0]['amount']))

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5002)
