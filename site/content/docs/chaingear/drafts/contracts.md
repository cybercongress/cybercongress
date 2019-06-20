# Contracts Overview

## Design rationale

Main design principle goes from ERC721 NFT tokenization of Databases (in Chaingear/Database of databases) and Entries (in custom user's Database). 

In reason of Databases tokenization in Chaingear which allows token holder acts as administrator of their Databases, Chaingear acts to Database as owner, which sets token holder as administrator on creation phase, changes administrator when holder transfers token to another user, and transfers ownership when user unregister Database in Chaingear, giving them full control to contract. Database deep-linked to Chaingear database token. In other words, token ownership means control of Database. Also, Chaingear supports multiple Database Builders (fabrics of databases of given type), and allows Chaingear owners provide different kind and versioning of Databases.

In reason of providing user functionality to describe their custom database data structures/schema and CRUD operations, the user creates their custom smart-contract, which implements the ISchema interface. This contract acts as inner storage, defines schema, and Database acts them on token operations (creating and deleting). A user may deploy erroneous or vulnerable Schema contract, but this should not crash Chaingear-Database NFT-token logic and Database inner entry NFT-logic too. Even if this happens Database crashing should not affect Chaingear/metadatabase contract. We proceed from the premise that the creator of the database (administrator) is positive and it does not make sense for them to break his database by initializing it with an incorrect contract.

This brings us to tokenized (**C** _RU_ **D**) operations (and inner in Schema) in Database and public (_C_ **R** _UD_) plus tokenized (_CR_ **U** _D_) Storage operation.

## Chaingear inheritance 
![chaingear_inheritance](mermaid/contracts-chaingear_inheritance.svg)

## Database inheritance
![database_inheritance](mermaid/contracts-database_inheritance.svg)

### /chaingear
- **_Chaingear_** allows any user to create his own database. 
1. Building fee is collecting by new database creation. 
2. All builded databases are tokenized with ERC721 NFT token standard and saved in Chaingear metadatabase with db metainformation. 
3. Creator of database may transfer tokenized ownership of database and destroy database with token burning. 
4. Tokenized databases Entries may collect funds by users and Database's owner may claim them. 
5. Chaingear supports multiple benefitiaries witch have access to collected fees from databases creation. 
6. Also allows for owner add multiple database builders contracts based their on versioning or/and functionality.

### /builders
- **_DatabaseBuilder_** contains the code of specified version of Database. This code used by Chaingear for Database creation and deploy process. DatabaseBuilder should be added with specified version and description to Chaingear database's builders inner list. Chaingear contract should be added as allowed caller to DatabaseBuilder with reason to allow creation calls only by Chaingear contact.

### /common
- **_Safe_** allows creator contract transfer ETHs to them and claim from, accounting logic holded by owner contract.

- **_IChaingear_**
- **_IDatabase_**
- **_IDatabaseBuilder_**
- **_ISchema_**
 

### /databases
- **_Database_** contract witch tokenize entries as NFT tokens via ERC721 standard. Users can create tokenized empty entries according to entry access policy setted in Database. Database provides tokenized (**C** _RU_ **D**) actions, after creation of token and empty database object, user should initialize them (_CR_ **U** _D_) in Storage. Also users can fund entries with ETHs which send to _DatabaseSafe_ with which owner of entry token can claim funds.

- **_DatabaseAccessControl_** holds logic of controlling database and accessing to entries creation. Policy options to entries creation are OnlyAdministrator, Whitelist, AllUsers. Chaingear acts as owner of Database and creator of database acts of administrator with separated policies to Database functions.

### /schemas
- **_Schema_** partially code-generated contract where database creator setup their custom entry structure and setters/getters. _Schema_ then initializes in Database by their creator (as admin) and completes Database setup process. Provides public (_C_ **RU** _D_) actions for users and inner (**C** _RU_ **D**) tokenized actions for Database.  Database goes as owner of contract (and acts as proxy) with entries creating, token-based transferring and deleting.

#### EntryInterface interface (should be implemented in user EntryCore contract)
```js
interface ISchema {

    function createEntry() external;
    function deleteEntry(uint256) external;
}
```

#### Example Schema
```js
pragma solidity 0.4.25;

import "../common/ISchema.sol";
import "../common/IDatabase.sol";
import "openzeppelin-solidity/contracts/ownership/Ownable.sol";
import "openzeppelin-solidity/contracts/introspection/SupportsInterfaceWithLookup.sol";


contract Schema is ISchema, Ownable, SupportsInterfaceWithLookup {
    
    bytes4 constant internal INTERFACE_SCHEMA_ID = 0x153366ed;

    struct Entry {
        string name;
        string manifest;
        string extension;
        string content;
        string logo;
    }
    
    Entry[] public entries;
    
    IDatabase internal database;
    
    constructor()
        public
    {
        _registerInterface(INTERFACE_SCHEMA_ID);
        database = IDatabase(owner);
    }
    
    function() external {} 
    
    function createEntry()
        external
        onlyOwner
    {
        Entry memory m = (Entry(
        {
            name:       "",
            manifest:   "",
            extension:  "",
            content:    "",
            logo:       ""
        }));

        entries.push(m);
    }
    
    function readEntry(uint256 _entryID)
        external
        view
        returns (
            string,
            string,
            string,
            string,
            string
        )
    {
        uint256 entryIndex = database.getIndexByID(_entryID);
        return (
            entries[entryIndex].name,
            entries[entryIndex].manifest,
            entries[entryIndex].extension,
            entries[entryIndex].content,
            entries[entryIndex].logo
        );
    }

    function updateEntry(
        uint256 _entryID,
        string  _name,
        string  _manifest,
        string  _extension,
        string  _content,
        string  _logo
    )
        external
    {
        database.auth(_entryID, msg.sender);
        
        uint256 entryIndex = database.getIndexByID(_entryID);
            
        Entry memory m = (Entry(
        {
            name:       _name,
            manifest:   _manifest,
            extension:  _extension,
            content:    _content,
            logo:       _logo
        }));
        entries[entryIndex] = m;
    }

    function deleteEntry(uint256 _entryIndex)
        external
        onlyOwner
    {        
        uint256 lastEntryIndex = entries.length - 1;
        Entry memory lastEntry = entries[lastEntryIndex];
        
        entries[_entryIndex] = lastEntry;
        delete entries[lastEntryIndex];
        entries.length--;
    }
    
}

```
    