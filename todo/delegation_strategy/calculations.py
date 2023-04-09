import math
from config import ALLOCATION, COST_OPTIMIZATION, DECENTRALIZATION, CONFIDENCE, RELIABILITY, SUPERINTELLIGENCE


def get_cost_optimization(commission: float):
    if 0.01 <= commission <= 0.10:
        return 1 / (commission**2)
    else:
        return 0


def get_cost_optimization_endorsement(
        cost_optimization,
        cost_optimization_sum,
        ):
    return int(cost_optimization / cost_optimization_sum * ALLOCATION * COST_OPTIMIZATION)


def get_decentralization(rank):
    return rank


def get_decentralization_endorsement(decentralization, decentralization_sum):
    return int((decentralization / decentralization_sum) * ALLOCATION * DECENTRALIZATION)


def get_confidence(ownership):
    return 1 - (1 / (1e-32 ** (-ownership)))


def get_confidence_endorsement(confidence, confidence_sum):
    return int((confidence / confidence_sum) * ALLOCATION * CONFIDENCE)


def get_reliability(jails, staked, delegator_shares):
    tokens_bluring = staked / delegator_shares
    if tokens_bluring == 1 and jails == 0:
        return 3
    else:
        return 1 / 2 ** jails + tokens_bluring ** 2


def get_reliability_endorsement(reliability, reliability_sum):
    return int((reliability / reliability_sum) * ALLOCATION * RELIABILITY)


def get_superintelligence(power):
    return math.log10(power + 1)


def get_superintelligence_endorsement(superintelligence, superintelligence_sum):
    return int((superintelligence / superintelligence_sum) * ALLOCATION * SUPERINTELLIGENCE)
