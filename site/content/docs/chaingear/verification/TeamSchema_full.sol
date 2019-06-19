pragma solidity 0.4.25;

// File: contracts/common/ISchema.sol

interface ISchema {

    function createEntry() external;
    function deleteEntry(uint256) external;
}

// File: contracts/common/IDatabase.sol

interface IDatabase {
    
    function createEntry() external payable returns (uint256);
    function auth(uint256, address) external;
    function deleteEntry(uint256) external;
    function fundEntry(uint256) external payable;
    function claimEntryFunds(uint256, uint256) external;
    function updateEntryCreationFee(uint256) external;
    function updateDatabaseDescription(string) external;
    function addDatabaseTag(bytes32) external;
    function updateDatabaseTag(uint8, bytes32) external;
    function removeDatabaseTag(uint8) external;
    function readEntryMeta(uint256) external view returns (address, address, uint256, uint256, uint256, uint256);
    function getChaingearID() external view returns (uint256);
    function getEntriesIDs() external view returns (uint256[]);
    function getIndexByID(uint256) external view returns (uint256);
    function getEntryCreationFee() external view returns (uint256);
    function getEntriesStorage() external view returns (address);
    function getSchemaDefinition() external view returns (string);
    function getDatabaseBalance() external view returns (uint256);
    function getDatabaseDescription() external view returns (string);
    function getDatabaseTags() external view returns (bytes32[]);
    function getDatabaseSafe() external view returns (address);
    function getSafeBalance() external view returns (uint256);
    function getDatabaseInitStatus() external view returns (bool);
    function transferAdminRights(address) external;
    function transferOwnership(address) external;
    function getAdmin() external view returns (address);
    function getPaused() external view returns (bool);
}

// File: openzeppelin-solidity/contracts/ownership/Ownable.sol

/**
 * @title Ownable
 * @dev The Ownable contract has an owner address, and provides basic authorization control
 * functions, this simplifies the implementation of "user permissions".
 */
contract Ownable {
  address public owner;


  event OwnershipRenounced(address indexed previousOwner);
  event OwnershipTransferred(
    address indexed previousOwner,
    address indexed newOwner
  );


  /**
   * @dev The Ownable constructor sets the original `owner` of the contract to the sender
   * account.
   */
  constructor() public {
    owner = msg.sender;
  }

  /**
   * @dev Throws if called by any account other than the owner.
   */
  modifier onlyOwner() {
    require(msg.sender == owner);
    _;
  }

  /**
   * @dev Allows the current owner to relinquish control of the contract.
   * @notice Renouncing to ownership will leave the contract without an owner.
   * It will not be possible to call the functions with the `onlyOwner`
   * modifier anymore.
   */
  function renounceOwnership() public onlyOwner {
    emit OwnershipRenounced(owner);
    owner = address(0);
  }

  /**
   * @dev Allows the current owner to transfer control of the contract to a newOwner.
   * @param _newOwner The address to transfer ownership to.
   */
  function transferOwnership(address _newOwner) public onlyOwner {
    _transferOwnership(_newOwner);
  }

  /**
   * @dev Transfers control of the contract to a newOwner.
   * @param _newOwner The address to transfer ownership to.
   */
  function _transferOwnership(address _newOwner) internal {
    require(_newOwner != address(0));
    emit OwnershipTransferred(owner, _newOwner);
    owner = _newOwner;
  }
}

// File: openzeppelin-solidity/contracts/introspection/ERC165.sol

/**
 * @title ERC165
 * @dev https://github.com/ethereum/EIPs/blob/master/EIPS/eip-165.md
 */
interface ERC165 {

  /**
   * @notice Query if a contract implements an interface
   * @param _interfaceId The interface identifier, as specified in ERC-165
   * @dev Interface identification is specified in ERC-165. This function
   * uses less than 30,000 gas.
   */
  function supportsInterface(bytes4 _interfaceId)
    external
    view
    returns (bool);
}

// File: openzeppelin-solidity/contracts/introspection/SupportsInterfaceWithLookup.sol

/**
 * @title SupportsInterfaceWithLookup
 * @author Matt Condon (@shrugs)
 * @dev Implements ERC165 using a lookup table.
 */
contract SupportsInterfaceWithLookup is ERC165 {

  bytes4 public constant InterfaceId_ERC165 = 0x01ffc9a7;
  /**
   * 0x01ffc9a7 ===
   *   bytes4(keccak256('supportsInterface(bytes4)'))
   */

  /**
   * @dev a mapping of interface id to whether or not it's supported
   */
  mapping(bytes4 => bool) internal supportedInterfaces;

  /**
   * @dev A contract implementing SupportsInterfaceWithLookup
   * implement ERC165 itself
   */
  constructor()
    public
  {
    _registerInterface(InterfaceId_ERC165);
  }

  /**
   * @dev implement supportsInterface(bytes4) using a lookup table
   */
  function supportsInterface(bytes4 _interfaceId)
    external
    view
    returns (bool)
  {
    return supportedInterfaces[_interfaceId];
  }

  /**
   * @dev private method for registering an interface
   */
  function _registerInterface(bytes4 _interfaceId)
    internal
  {
    require(_interfaceId != 0xffffffff);
    supportedInterfaces[_interfaceId] = true;
  }
}

// File: contracts/schemas/TeamSchema.sol

contract TeamSchema is ISchema, Ownable, SupportsInterfaceWithLookup {
    
    bytes4 constant internal INTERFACE_SCHEMA_ID = 0x153366ed;

    struct Entry {
        string  name;
        address gitcoin;
        address payouts;
        string  github;
        string  telegram;
        string  keybase;
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
            gitcoin:    address(0),
            payouts:    address(0),
            github:     "",
            telegram:   "",
            keybase:    ""
        }));

        entries.push(m);
    }
    
    function readEntry(uint256 _entryID)
        external
        view
        returns (
            string,
            address,
            address,
            string,
            string,
            string
        )
    {
        uint256 entryIndex = database.getIndexByID(_entryID);
        return (
            entries[entryIndex].name,
            entries[entryIndex].gitcoin,
            entries[entryIndex].payouts,
            entries[entryIndex].github,
            entries[entryIndex].telegram,
            entries[entryIndex].keybase
        );
    }

    function updateEntry(
        uint256 _entryID,
        string  _name,
        address _gitcoin,
        address _payouts,
        string  _github,
        string  _telegram,
        string  _keybase
    )
        external
    {
        database.auth(_entryID, msg.sender);
        
        uint256 entryIndex = database.getIndexByID(_entryID);
            
        Entry memory m = (Entry(
        {
            name:       _name,
            gitcoin:    _gitcoin,
            payouts:    _payouts,
            github:     _github,
            telegram:   _telegram,
            keybase:    _keybase
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
