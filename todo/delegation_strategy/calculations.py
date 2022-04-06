import math
from config import ALLOCATION, COST_OPTIMIZATION, DECENTRALIZATION, CONFIDENCE, RELIABILITY, SUPERINTELLIGENCE


def get_cost_optimization(commission: float):
    if commission <= 0.05:
        return int(8000 * commission)
    else:
        return int(math.ceil(1 / (commission ** 2)))


def get_cost_optimization_endorsement(cost_optimization, cost_optimization_sum):
    return int((cost_optimization / cost_optimization_sum) * ALLOCATION * COST_OPTIMIZATION)


def get_decentralization(rank, sum_rank):
    return rank / sum_rank


def get_decentralization_endorsement(rank_share):
    return int(rank_share * ALLOCATION * DECENTRALIZATION)


def get_confidence(ownership, ownership_sum):
    return ownership / ownership_sum


def get_confidence_endorsement(confidence):
    return int(confidence * ALLOCATION * CONFIDENCE)


def get_reliability(pre_commits, jails, staked, delegator_shares):
    tokens_bluring = delegator_shares / staked
    tokens_bluring_points = (tokens_bluring ** 3) * 100
    pre_commits_points = ((pre_commits / 100) ** 2) * 100
    jails_points = (1 / 2 ** jails) * 100
    if jails_points < 0.0009765625:
        jails_points = 0.0
    return tokens_bluring_points + pre_commits_points + jails_points


def get_reliability_endorsement(reliability, reliability_sum):
    return int((reliability / reliability_sum) * ALLOCATION * RELIABILITY)


def get_superintelligence(power, power_sum):
    return power / power_sum


def get_superintelligence_endorsement(superintelligence):
    return int(superintelligence * ALLOCATION * SUPERINTELLIGENCE)