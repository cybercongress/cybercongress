# Overview

This project allows you to create your own Registry of general purpose entries on Ethereum blockchain.
Entry type is defined during creation, so you can put into entry any custom logic you want (validation, entry-level permission control). Entries are tokenized as NFT.

Your creating your registry in Chaingear - metaregistry, which are one point of access to all registries. Registries on chaingear level are tokenized as NFT. Chaingear is most expensive registry, so you should pay for your registry creation.

# Features

#### Chaingear

1. Metaregistry with Registries entries, where each entry are ERC721 token
2. Fee-based Registry creation
3. Creating Registries with different functionality
4. Token-based ownership/administration for Registry
5. Funding in ETH for Registries

#### Custom registry

1. Custom data structure for Registry (EntryCore)
2. Each Entry is ERC721 token
3. Fee-based Entry creation
4. Token-based ownership Entry management
5. Entry creation policies (Administrator, Whitelist, AllUsers)

#### Chaingear UI (browser/stand-alone web3 DApp)

1. Web3/Metamask/Truffle/IPFS based
2. Full Chaingear control interface
3. Full custom Registry control interface
4. Simple smart-contract EntryCore code generation in client
5. Registries ABI and metainformation savings in IPFS
