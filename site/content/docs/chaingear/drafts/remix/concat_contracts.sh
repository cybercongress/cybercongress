#!/usr/bin/env bash
truffle-flattener ../../contracts/databases/DatabaseV1.sol ../../contracts/chaingear/Chaingear.sol ../../contracts/schemas/TeamSchema.sol ../../contracts/builders/DatabaseBuilderV1.sol > contracts_full.sol
