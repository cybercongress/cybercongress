---
project: js-cosmos
---
## Install
```
npm install git://github.com/cybercongress/cosmos-js.git#cosmos-builder --save
```

# RPC server calling

## Usage example for Cosmos-sdk RPC
```$js
import CosmosSdkRpc from 'cosmos-js/dist/rpc/cosmosSdkRpc';
const constants = require('cosmos-js/dist/constants/cosmos');

const cosmosRpc = new CosmosSdkRpc('https://lcd-do-not-abuse.cosmostation.io', constants);

const fromAddress = 'cosmos1adfp4t779mz5mqkp774l4d0umm2x9v4s42prxw';
const fromPrivateKey = 'a5b1305ebf29997a8a180b8bf322bc27b226e8cd00e243887e2129839c36bb2d';

const toAddress = 'cosmos14mgwf74me9jneaj7pxna873ufrqdwzes2vt4kl';
const amount = 1;

cosmosRpc
  .transfer(
    {
      address: fromAddress,
      privateKey: fromPrivateKey,
    },
    toAddress,
    amount
  )

  .then(res => {
    console.log('res', res);
  })

```

## Usage example for CyberD RPC

```$js

import CyberDRpc from 'cosmos-js/dist/rpc/cyberdRpc';

const constants = require('cosmos-js/dist/constants/cyberd');

const cyberdRpc = new CyberDRpc('http://93.125.26.210:34657', constants);

const fromAddress = 'cyber1adfp4t779mz5mqkp774l4d0umm2x9v4sjpxt05';
const fromPrivateKey = 'a5b1305ebf29997a8a180b8bf322bc27b226e8cd00e243887e2129839c36bb2d';

const toAddress = 'cyber14mgwf74me9jneaj7pxna873ufrqdwzesd8val9';
const amount = 1;

cyberdRpc
  .transfer(
    {
      address: fromAddress,
      privateKey: fromPrivateKey,
    },
    toAddress,
    amount
  )

  .then(res => {
    console.log('res', res);
  });
```

# Custom builder definition

You might need use cosmos-sdk builder but with some custom RPC methods or with changes 
in transaction structure.

In this case - better to define your own builder that extends some exist builder 
like CosmosSdkBuilder.

For creating custom request - need to define js-amino type first of your custom message:

```$js
const { TypeFactory, Types } = require('js-amino');

const CustomMessage = TypeFactory.create('CustomMessage', [
  {
    name: 'custom_address',
    type: Types.String,
  },
  {
    name: 'custom_amount',
    type: Types.String,
  },
]);
```

Then - you can use this CustomMessage for build custom request.

```$js
import CosmosSdkBuilder from 'cosmos-js/dist/builders/cosmosSdkBuilder';
import CosmosCodec from 'cosmos-js/dist/codec';

class MyCustomChainBuilder extends CosmosSdkBuilder {
  constructor() {
    super();
    // redefine codec for clear parent types and use only new types if you need
    this.codec = new CosmosCodec();
    this.codec.registerConcrete(new CustomMessage(), 'my-custom-chain/custom-message', {});
  }
  
  myCustomRequest(sendOptions) {
    const msg = new CustomMessage(sendOptions.customAddress, sendOptions.customAmount);
    return this.abstractRequest(sendOptions, msg);
  }
}
```

Then - you can build your request manually:
```$js
const requestData = {
  account: {
    address: keyPair.address,
    publicKey: keyPair.publicKey,
    privateKey: keyPair.privateKey,
    accountNumber: 0,
    sequence: 0,
  },
  chainId: 'euler-4',
  customAddress: 'my-custom-address',
  customAmount: '999',
  fee: {
    denom: '',
    amount: '0',
  },
  memo: ''
};

const customChainBuilder = new MyCustomChainBuilder();

const txRequest = customChainBuilder.myCustomRequest(requestData);

console.log('you can send result json to server:', txRequest.json);
console.log('or you can send result hex to server:', txRequest.hex);
```

Its already signed tx and converted to suitable for RPC server format.

If your RPC server takes non-standart data structures in Fee or Signature - you can
redefine `sendRequest`, `getResultTx`, `getFee`, `getSignature`, `getSignature`, 
`signMessageJson` methods for write specific logic or data structure.

By this way - all your custom transactions will follow the same specific rules that 
defined in these methods.

You can see the example in [cyberDBuilder.js](./src/builders/cyberDBuilder.js).

# Custom RPC definition

For definition method for sending your custom transaction to rpc server - you can
create custom rpc class:
```$js
import CosmosSdkRpc from 'cosmos-js/dist/rpc/cosmosSdkRpc';

class MyCustomChainRpc extends CosmosSdkRpc {
  constructor(rpc, constants) {
    super(rpc, constants);
    this.cosmosBuilder = new MyCustomChainBuilder();
  }
  
  async executeCustomRequest(txOptions, customAddress, customAmount) {
    const options = await this.prepareOptions(txOptions, {
      // for using inside myCustomRequest
      customAddress,
      customAmount,
      // you can also redefine fee for example
      fee: {
        denom: 'uatom',
        amount: '500',
      }
    });

    // calling previously defined myCustomRequest
    const txRequest = this.cosmosBuilder.myCustomRequest(options);
    
    // sending to server
    return this.handleResponse(axios.post(`${this.rpc}/txs`, {
       tx: JSON.parse(txRequest.json),
       mode: 'sync',
    }));
  }
}
```
Then use `MyCustomChainRpc` like this:
```$js
const myCustomChainRpc = new MyCustomChainRpc('http://rpc.server', new NetConfig('customprefix', 'custompubprefix'));

myCustomChainRpc.executeCustomRequest(
    {privateKey: 'a5b1305ebf29997a8a180b8bf322bc27b226e8cd00e243887e2129839c36bb2d'}, 
    'my-custom-address', 
    '999'
).then(res => {
    console.log('res', res);
});
```
