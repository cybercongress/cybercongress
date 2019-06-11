#!/usr/bin/env bash
truffle-flattener ../../contracts/databases/DatabaseV1.sol > DatabaseV1_full.sol
truffle-flattener ../../contracts/chaingear/Chaingear.sol > Chaingear_full.sol
truffle-flattener ../../contracts/schemas/TeamSchema.sol > TeamSchema_full.sol
truffle-flattener ../../contracts/builders/DatabaseBuilderV1.sol > Builder_full.sol
