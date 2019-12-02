sequenceDiagram
    Congress fund->>Gitcoin fund: ETH allocated to gitcoin during sprint
    Note over Congress fund,Gitcoin fund: Calculate ETH amount for sprint
    Gitcoin fund->>Team member: % of ETH sprint amount according to prepared gitcoin issues
    Note over Gitcoin fund,Team member: Calculate weighting factors for each member
    Team member->>Issue fund: Fund issues as per members wish
    Issue fund-->>Congress fund: Accumulate funded issues and make a forecast
