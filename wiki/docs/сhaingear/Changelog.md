# Changelog

All major changes of chaingear will be documented in this file.

## Sprint 9:

**1. Started frontend migration to new architecture (spring 9 - initialial relealse contracts's epic)**

**2. Changed architecture:**
- Splitting Registry creation in two stages - creation (in Chaingear) and post-initialization with EntryCore's bytecode (in Registry via admin/token holder)
- Splitting Entry creation in two states - creation/deletion in Registry (with token minting/burning) and updating/reading in EntryCore

**3. Improved policies:**
- Improved policies for Chaingear
- Improved policies for Registry

**3. Added advanced tests:**
- Improved and added more tests to Chaingear (Registry Creation, Chaingear Settings, policies)
- Improved and added more tests to Registry (EntryCore initialization, CRUD, policies, Registry settings)

**4. Initial gas estimation:**
- First meaningfull estimates of gas consumption for Chaingear creation, Registry creation, Registry initialization (with user generated EntryCore bytecode), Entry adding

**5. Refactoring:**
- Policies refactoring

**5. Improved documentation:**
- Improved NatSpec

**6. Iceboxing after Research and Refactoring:**
- Funding of Chaingear registries
- Funding of Registry entries

## Sprint 7-8:

**1. Initial frontend with Web3 and Metamask/Truffle integration**

**2. Created initial version of contract of Chaingear/Registry**

**3. Initial research/integration of ERC721 to tokenize registries/entries in Chaingear/Registry**

**4. Initial realization of policies for Chaingear/Registry** 

**5. Initial research/realization of cross-linking Registries tokens in Chaingear with side Registries smart-contracts**
