# Contracts Overview

### /chaingear
- **_Chaingear_** allows any user to create his own registry. Building fee is collecting by new registry creation. All builded registries are tokenized with ERC721 NFT token standard and saved in Chaingear metaregistry with registry metainformation. Creator of registry may transfer tokenized ownership of registry and destroy registry with token burning. Chaingear supports multiple benefitiaries witch have access to collected fees.

  ###### depends on:
    - _ERC721Token_
    - _SplitPaymentChangeable_
    - _ChaingearCore_
    - _Registry (int)_


- **_ChaingearCore_** holds general logic of Chaingear. Allows change chaingear's metainformation, amount of registration fee, set registry creator contract.

  ###### depends on:
    - _RegistryBase_
    - _IPFSeable_
    - _Destructible_
    - _Pausable_
    - _RegistryCreator (int)_


- **_RegistryBase_** holds struct of data with describes registry metainformation which associated with token, views function for registry metainformation.

- **_RegistryCreator_** contains the bytecode of current version of Registry. This bytecode used by Chaingear for Registry Creation. Registry Creator address can be changed in Chaingear by it's owner. Creation function can be only called by setted out chaingear address.

  ###### depends on:
    - _Registry_
    - _Ownable_

### /common
- [Seriality](https://github.com/pouladzade/Seriality) is a library for serializing and de-serializing all the Solidity types in a very efficient way which mostly written in solidity-assembly.

- **_IPFSeable_** contains logic which allows view and save links to CID in IPFS with ABI, source code and contract metainformation. Inherited by Chaingear and Registry.

  ###### depends on:
    - _Ownable_


- **_RegistySafe_** allows inherited contract transfer ETHs to safe and client claim from safe, accounting logic holded by inherited contract. Inherited by Chaingear and Registry.

  ###### depends on:
    - _Ownable_
    - _Destructible_


- **_SplitPaymentChangeable_** allows add beneficiaries to contract (addresses and shares amount) and change payee address. Beneficiaries can claim ETHs from contract proportionally to their shares. Inherited by Chaingear and Registry.

  ###### depends on:
    - _Ownable_
    - [_SplitPayment_](https://zeppelin-solidity/blob/master/contracts/payment/SplitPayment.sol)

### /registry
- **_Chaingeareable_** holds basic logic of Registry as registry basic information, balance and fees amount. Contains getters and setters for registry name, desciption, tags, entry base address.

  ###### depends on:
    - _IPFSeable_
    - _RegistryAccessControl_


- **_EntryBase_** base for _EntryCore_. Holds entry metainformation and interfaces of functions (**C** _R_ **UD**) which should be implemented in _EntryCore_.

- **_EntryCore_** partilly codegenerated contract where registry creator setup their custom entry structure and setters/getters. _EntryCore_ then goes to Registry constructor as bytecode, where _EntryCore_ contract creates. Registry goes as owner of contract (and acts as proxy) with entries creating, transfering and deleting.

  ###### depends on:
    - _EntryBase_
    - _Ownable_
    - _Seriality_


- **_Registry_** contract witch tokenize entries as NFT tokens via ERC721 standard. Users can create entries with structure described in _EntryCore_ sent serialized params according to entry access policy. Also users can fund entries with ETHs which send to _RegistrySafe_ where owner of entry can claim funds.

  ###### depends on:
    - _Chaingeareable_
    - _ERC721Token_
    - _SplitPaymentChangeable_
    - _EntryBase (int)_


- **_RegistryAccessControl_** holds logic of controlling registry and accessing to entries creation. Policy options to entries creation are OnlyCreator, Whitelist, AllUsers. Chaingear acts as owner of registry and creator of registry acts of creator with separated policies to Registry functions.

  ###### depends on:
    - _Ownable_
    - _Destructible_
