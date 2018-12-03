# How to add custom ETH node to your Cyb

![pic](0.png)

by [@savetheales](https://cyb//0x00CA47db1BE92C1072e973fd8DC4A082f7d70214.eth)

[← Previous post](https://steemit.com/web3/@savetheales/how-to-add-custom-ipfs-node-to-your-cyb)

ToC:

[1. How to open ipfs link using Cyb](https://steemit.com/web3/@savetheales/how-to-open-ipfs-link-using-cyb)

[2. How to add custom ipfs node to your Cyb](https://steemit.com/web3/@savetheales/how-to-add-custom-ipfs-node-to-your-cyb)

Hi! As we know from [previous post](https://steemit.com/web3/@savetheales/how-to-add-custom-ipfs-node-to-your-cyb) we need 3 greenlights on the right side of footer. Today we'll add ETH node to Cyb. We'll use Parity node for example, but you can try geth node if you feel strong enough.

### Installing Parity-node

The easiest way to install stable version of Parity is [Homebrew](https://brew.sh/) by following command:

`brew tap paritytech/paritytech`

`brew install parity`

Additional methods you can explore [here](https://wiki.parity.io/Setup), but I still recommend you [Homebrew](https://brew.sh/) :)

### Syncing

After successful installing run:

`parity --jsonrpc-cors="all" --jsonrpc-apis="all" --jsonrpc-interface=all`

this command start syncing Parity. Actually node is available for using at port

`http://127.0.0.1:8545`

After syncing I reccomend you launch Parity with Homebrew by following command:
>not ready

`brew services start parity`

It's launch Parity in background mode.



### Adding port to Cyb

Launch Cyb, latest version you can download [here](https://github.com/cybercongress/cyb/releases) if you still not have :) . Type `settings.cyb` in a search field or click on a gear in top right side.

You need to insert this port `http://127.0.0.1:8545` opposite `ETH NODE` like this:

![result](1.png)

That it ;)

Now you run your own node and use it with Cyb ;)

2 of 3, move on! ;)

![result](2.png)

Subscribe at [Steemit](https://steemit.com/@cybercongress), [Reddit](https://www.reddit.com/r/cybercongress/), [Twitter](https://twitter.com/cyber_devs), [Telegram channel](https://t.me/cybercongress) and join to our community in [@fuckgoogle](https://t.me/fuckgoogle)

[← Previous post](https://steemit.com/web3/@savetheales/how-to-add-custom-ipfs-node-to-your-cyb)
