sequenceDiagram
    Congress fund->>Gitcoin fund: ETH allocated to gitcoin at current sprint
    Note over Congress fund,Gitcoin fund: Calculate sprint ETH amount
    Gitcoin fund->>Team member: % of ETH sprint amount according to prepared gitcoin issues
    Note over Gitcoin fund,Team member: Calculate weighting factors for each member
    Team member->>Issue fund: Fund issue as member want
    Issue fund-->>Congress fund: Accumulate all funded issues and make forecast
