#!/usr/bin/env bash
truffle-flattener ../../contracts/chaingear/Chaingear.sol > Chaingear_full.sol
solgraph Chaingear_full.sol > chaingear_full.dot
dot -Tpng chaingear_full.dot -o chaingear_full.png

truffle-flattener ../../contracts/databases/DatabaseV1.sol > DatabaseV1_full.sol
solgraph DatabaseV1_full.sol > databasev1_full.dot
dot -Tpng databasev1_full.dot -o databasev1_full.png

solgraph ../../contracts/databases/DatabaseV1.sol > databasev1.dot
dot -Tpng databasev1.dot -o databasev1.png

solgraph ../../contracts/chaingear/Chaingear.sol > chaingear.dot
dot -Tpng chaingear.dot -o chaingear.png