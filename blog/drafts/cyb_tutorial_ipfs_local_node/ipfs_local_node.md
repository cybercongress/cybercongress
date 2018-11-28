# How to add custom ipfs node to your Cyb

by [@savetheales](cyb://0x00CA47db1BE92C1072e973fd8DC4A082f7d70214.eth)

[← Previous post](https://steemit.com/web3/@savetheales/how-to-open-ipfs-link-using-cyb)

Hey everyone! Today we'll take the glorious step into adulthood! The greatest level of Cyb using is taking 3 greenlights at right side of footer ;)

![](1.png)

The thing is Cyb use color indication to show your connection. Yellow one if you have connection to remote node, red one if you have no connection and the green one if you have your local node.

So today we intend to add local IPFS node to our Cyb.


1. IPFS installing

First of all we need to install and initiate IPFS node. If you made it already you can skip this section.

The easiest way to install IPFS is [homebrew](https://docs.brew.sh/Installation). All you need is just write in your terminal

`brew install ipfs`,

 and than make

 `ipfs init`.

Another ways you can explore [here](https://docs.ipfs.io/introduction/install/), but I recommend you homebrew :)

Just for test you can write

`ipfs cat /ipfs/QmYwAPJzv5CZsnA625s3Xf2nemtYgPpHdWEz79ojWnPbdG/readme`

and if you see following text everything is alright. ;)

![result](2.png)

2. Start IPFS daemon

So it's time to going online. Write in your terminal

`ipfs daemon`

wait few seconds and you should to see

![daemon](3.png)

Good job!

3. The last stage is adding local IPFS node to Cyb.

    3.1 So download [latest release](https://github.com/cybercongress/cyb/releases) for your platform.

    3.2 Type in search field `settings.cyb` and press `Enter`. You should see something like this:
    ![result](4.png)

    `settings.cyb` means that you open settings app in Cyb. As well as `Qm.....Dvd.ipfs` you open ipfs hash with app `.ipfs`.

    3.3 Now you see addresses of your nodes connections. As default you connect to our nodes. So let's solve this mistake. Put this `http://127.0.0.1:8080` at IPFS node filed and press `update`. If all right you must see:

    ![](5.png)

Awesome!!! Now you use your local IPFS node at Cyb!
Welcome to your adult life!

In the next post we will import account from Metamask  to Cyb;)

**Subscribe for our blogs:**

Steemit https://steemit.com/@cybercongress

Reddit https://www.reddit.com/r/cybercongress/

Twitter https://twitter.com/cyber_devs

Telegram channel https://t.me/cybercongress

devChat https://t.me/fuckgoogle

[← Previous post](https://steemit.com/web3/@savetheales/how-to-open-ipfs-link-using-cyb)
