---
date: 2019-02-04
url: ultimate-validator-guide
title: 'Ultimate cyberd validator setup. Testnet: Euler-1.'
author: savetheales
---

# What is this?

The cyberd is a public Delegated Proof-of-Stake (DPoS) protocol based on Tendermint Byzantine Fault-Tolerant consensus, meaning that a validator's weight is determined by the amount of staking tokens bonded as collateral. These tokens can be staked directly by the validator or delegated to them by token holders. The weight (i.e. total stake) of a validator determines whether or not it is an active validator, and also how frequently this node will have to propose a block and how much revenue it will obtain.

# Validators

The maximum number of validators is 146. If the number of active validators is less than 146 all of them take a part of signing blocks. If more - the top 146 with staked tokens will, in a active validators set.

# Validators requirements

Rank calculation on a cyberd is benefit GPU computation. They are easy to parallelize, which is why it is best to use GPU.

Minimal requirements for the next two weeks (until the middle of February):

```
CPU: 4 cores
RAM: 16 GB
SSD: 256 GB
Connection: 100Mb, Fiber, Stable and low-latency connection
GPU: GeForce 1070-1080, CUDA
Software: Docker, Ubuntu 16.04/18.04 LTS
```
Recommended requirements:

```
CPU: 6 cores
RAM: 64 GB
SSD: 512 GB
Connection: 100Mb, Fiber, Stable and low-latency connection
GPU: GeForce 1070-1080, CUDA
Software: Docker, Ubuntu 16.04/18.04 LTS
```

# Validator setup

## Third-party software

Cyberd main distribution unit is a [docker](https://www.docker.com/) container. All images are located in default [Dockerhub registry](https://hub.docker.com/r/cyberd/cyberd/).  In order to access GPU from the container, Nvidia drivers version **410+** and [Nvidia docker runtime](https://github.com/NVIDIA/nvidia-docker) should be installed on the host system. For a great user experience, we propose you use [portainer](https://portainer.io) - docker containers manager. You can skip any subsection of this if you already had and configured the necessary software.

#### Docker installation

1. Update the apt package index:

```bash
sudo apt-get update
```

2. Install packages to allow apt to use a repository over HTTPS:

```bash
sudo apt-get install \
     apt-transport-https \
     ca-certificates \
     curl \
     gnupg-agent \
     software-properties-common
```

> May require `curl` installation `apt-get install curl`

3. Add Docker’s official GPG key:

```bash
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
```

```bash
sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"
```

4. Update the apt package index.

```bash
sudo apt-get update
```

5. Install the latest version of Docker CE and containerd, or go to the next step to install a specific version:

```bash
sudo apt-get install docker-ce docker-ce-cli containerd.io
```

If you don’t want to preface the docker command with sudo, create a Unix group called docker and add users to it. When the Docker daemon starts, it creates a Unix socket accessible by members of the docker group.

6. Create the docker group.

```bash
sudo groupadd docker
```

7. Add your user to the docker group.

```bash
sudo usermod -aG docker $USER
```
8. Reboot the system for the changes to take effect.

#### Portainer installation

1. Before installing Portainer, download the Portainer image from the DockerHub using the docker pull command below.

```bash
docker pull portainer/portainer
```

2. Now run Portainer using the simple docker command below.

```bash
docker run -d --restart always -p 9000:9000 -v /var/run/docker.sock:/var/run/docker.sock portainer/portainer
```

3. Open your browser and go to:

```bash
localhost:9000
```

![](portainer_start.png)

4. Set password, chose `local` tab and click `connect`. All containers will be available at the `containers` tab.

#### Nvidia drivers installation

1. To proceed first add the `ppa:graphics-drivers/ppa` repository into your system:

```bash
sudo add-apt-repository ppa:graphics-drivers/ppa
```

```bash
sudo apt update
```

2. Next, identify your graphic card model and recommended driver:

```bash
ubuntu-drivers devices
```
You should see something like this:

```bash
== /sys/devices/pci0000:00/0000:00:01.0/0000:01:00.0 ==
modalias : pci:v000010DEd00001BA1sv00001462sd000011E4bc03sc00i00
vendor   : NVIDIA Corporation
model    : GP104M [GeForce GTX 1070 Mobile]
driver   : nvidia-driver-390 - third-party free
driver   : nvidia-driver-410 - third-party free
driver   : nvidia-driver-396 - third-party free
driver   : nvidia-driver-415 - third-party free recommended
driver   : xserver-xorg-video-nouveau - distro free builtin
```
3. We need **410+** drivers release. As we see v415 is recommended. The command below will install the recommended version of drivers.

```bash
sudo ubuntu-drivers autoinstall
```

Drivers will install within approximately 10 minutes.

```bash
DKMS: install completed.
Setting up libxdamage1:i386 (1:1.1.4-3) ...
Setting up libxext6:i386 (2:1.3.3-1) ...
Setting up libxfixes3:i386 (1:5.0.3-1) ...
Setting up libnvidia-decode-415:i386 (415.27-0ubuntu0~gpu18.04.1) ...
Setting up build-essential (12.4ubuntu1) ...
Setting up libnvidia-gl-415:i386 (415.27-0ubuntu0~gpu18.04.1) ...
Setting up libnvidia-encode-415:i386 (415.27-0ubuntu0~gpu18.04.1) ...
Setting up nvidia-driver-415 (415.27-0ubuntu0~gpu18.04.1) ...
Setting up libxxf86vm1:i386 (1:1.1.4-1) ...
Setting up libglx-mesa0:i386 (18.0.5-0ubuntu0~18.04.1) ...
Setting up libglx0:i386 (1.0.0-2ubuntu2.2) ...
Setting up libgl1:i386 (1.0.0-2ubuntu2.2) ...
Setting up libnvidia-ifr1-415:i386 (415.27-0ubuntu0~gpu18.04.1) ...
Setting up libnvidia-fbc1-415:i386 (415.27-0ubuntu0~gpu18.04.1) ...
Processing triggers for libc-bin (2.27-3ubuntu1) ...
Processing triggers for initramfs-tools (0.130ubuntu3.1) ...
update-initramfs: Generating /boot/initrd.img-4.15.0-45-generic
```

4. Reboot the system for the changes to take effect.

5. Check installed drivers

```bash
nvidia-smi
```
You should see this:

```
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 415.27       Driver Version: 415.27       CUDA Version: 10.0     |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|===============================+======================+======================|
|   0  GeForce GTX 1070    Off  | 00000000:01:00.0  On |                  N/A |
| N/A   54C    P0    36W /  N/A |    445MiB /  8117MiB |      0%      Default |
+-------------------------------+----------------------+----------------------+

+-----------------------------------------------------------------------------+
| Processes:                                                       GPU Memory |
|  GPU       PID   Type   Process name                             Usage      |
|=============================================================================|
|    0       882      G   /usr/lib/xorg/Xorg                           302MiB |
|    0      1046      G   /usr/bin/gnome-shell                         139MiB |
+-----------------------------------------------------------------------------+
```

### Install Nvidia container runtime for docker

1. Add the package repositories

```bash
curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | \
    sudo apt-key add -
```

```bash
distribution=$(. /etc/os-release;echo $ID$VERSION_ID)
```

```bash
curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | \
   sudo tee /etc/apt/sources.list.d/nvidia-docker.list
```

You should see this:

```
deb https://nvidia.github.io/libnvidia-container/ubuntu18.04/$(ARCH) /
deb https://nvidia.github.io/nvidia-container-runtime/ubuntu18.04/$(ARCH) /
deb https://nvidia.github.io/nvidia-docker/ubuntu18.04/$(ARCH) /
```

3. Install nvidia-docker2 and reload the Docker daemon configuration

```bash
sudo apt-get update
```

```bash
sudo apt-get install -y nvidia-docker2
```

```bash
sudo pkill -SIGHUP dockerd
```

4. Test nvidia-smi with the latest official CUDA image

```bash
docker run --runtime=nvidia --rm nvidia/cuda:10.0-base nvidia-smi
```

Output logs must should coincide as earlier:

```
Unable to find image 'nvidia/cuda:10.0-base' locally
10.0-base: Pulling from nvidia/cuda
38e2e6cd5626: Pull complete
705054bc3f5b: Pull complete
c7051e069564: Pull complete
7308e914506c: Pull complete
5260e5fce42c: Pull complete
8e2b19e62adb: Pull complete
Digest: sha256:625491db7e15efcc78a529d3a2e41b77ffb5b002015983fdf90bf28955277d68
Status: Downloaded newer image for nvidia/cuda:10.0-base
Fri Feb  1 05:41:12 2019       
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 415.27       Driver Version: 415.27       CUDA Version: 10.0     |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|===============================+======================+======================|
|   0  GeForce GTX 1070    Off  | 00000000:01:00.0  On |                  N/A |
| N/A   55C    P0    31W /  N/A |    445MiB /  8117MiB |     38%      Default |
+-------------------------------+----------------------+----------------------+

+-----------------------------------------------------------------------------+
| Processes:                                                       GPU Memory |
|  GPU       PID   Type   Process name                             Usage      |
|=============================================================================|
+-----------------------------------------------------------------------------+
```

Your machine is ready to launch fullnode.

## Cyberd fullnode launching

1. Create folders for keys and data storing where you want:

``` bash
mkdir cyberd
mkdir cyberdcli
```

2. Run fullnode

```bash
docker run -d --name=cyberd --restart always --runtime=nvidia  -p 26656:26656 -p 26657:26657 -p 26660:26660  -v /<path_to_cyberd>/cyberd:/root/.cyberd  -v /<path_to_cyberdcli>/cyberdcli:/root/.cyberdcli  cyberd/cyberd:euler-1
```
3. After successful container pulling and launch, run to check if your node is connected to the testnet:

```bash
docker exec cyberd cyberdcli status
```
The possible output looks like this:
```
{"node_info":{"protocol_version":{"p2p":"6","block":"9","app":"0"},"id":"93b776d3eb3f3ce9d9bda7164bc8af3acacff7b6","listen_addr":"tcp://0.0.0.0:26656","network":"euler-1","version":"0.29.1","channels":"4020212223303800","moniker":"anonymous","other":{"tx_index":"on","rpc_address":"tcp://0.0.0.0:26657"}},"sync_info":{"latest_block_hash":"686B4E65415D4E56D3B406153C965C0897D0CE27004E9CABF65064B6A0ED4240","latest_app_hash":"0A1F6D260945FD6E926785F07D41049B8060C60A132F5BA49DD54F7B1C5B2522","latest_block_height":"45533","latest_block_time":"2019-02-01T09:49:19.771375108Z","catching_up":false},"validator_info":{"address":"66098853CF3B61C4313DD487BA21EDF8DECACDF0","pub_key":{"type":"tendermint/PubKeyEd25519","value":"uZrCCdZTJoHE1/v+EvhtZufJgA3zAm1bN4uZA3RyvoY="},"voting_power":"0"}}
```
Your node has started to sync. The syncing process can be seen in the terminal. Open a new tab and run the following command:

```bash
docker logs cyberd --follow
```

Or go to `localhost:9000` and open logs at cyberd container:

![](cyberd_logs.jpg)

Syncing has started. Syncing time depends on your internet bandwidth, connection and blockchain height. As at 2019/02/03 syncing time approximately 15-20 minutes. Once you see in the logs that blocks are syncing for 1 second, your node is synced.

Additional information available by API endpoint at `localhost:26657`

f.e. the number of active validators is available here `localhost:26657/validators`

## Validator start
After your node successfully synced you can run validator.

#### Prepare stake address

If you already have an address with CYB and know your seed phrase or private key just restore it onto your local keystore.
```bash
docker exec -ti cyberd cyberdcli keys add <your_key_name> --recover
docker exec cyberd cyberdcli keys show <your_key_name>
```

If you have been lucky enought and your Ethereum address has been included in genesis you can import ethereum private key

> Please, do not import high value Ethereum accounts. This cannot be safe! Cyberd software is a new software and is not battle tested yet.

```bash
docker exec -ti cyberd cyberdcli keys add import_private <your_key_name>
docker exec cyberd cyberdcli keys show <your_key_name>
```

If you want to create new acccount use the command below.
Also, you should send coins to that address to bind them later during validator submitting.

```bash
docker exec -ti cyberd cyberdcli keys add <your_key_name>
docker exec cyberd cyberdcli keys show <your_key_name>
```

**<your_key_name>** is any name you pick to represent this key pair.
You have to refer to this <your_key_name> later when you use the keys to sign transactions.
It will ask you to enter your password twice to encrypt the key.
You also need to enter your password when you use your key to sign any transaction.

The command returns the address, public key and a seed phrase which you can use to
recover your account if you forget your password later.
Keep the seed phrase in a safe place in case you have to use it.

The address showing here is your account address. Let’s call this **<your_account_address>**.
It stores your assets.

#### Send create validator transaction

Validators are actors on the network committing new blocks by submitting their votes.
It refers to the node itself, not a single person or a single account.
Therefore, the public key here is referring to the node public key,
not the public key of the address you have just created.

To get the node public key, run the following command:

```bash
docker exec cyberd cyberd tendermint show-validator
```

It will return a bech32 public key. Let’s call it **<your_node_pubkey>**.
The next step is to declare a validator candidate.
The validator candidate is the account which stakes the coins.
So, the validator candidate is an account this time.
To declare a validator candidate, run the following command adjusting stake amount and other fields.

```bash
docker exec -ti cyberd cyberdcli tx staking create-validator \
  --amount=10000000cyb \
  --pubkey=<your_node_pubkey> \
  --moniker=<your_node_nickname> \
  --trust-node \
  --from=<your_key_name> \
  --commission-rate="0.10" \
  --commission-max-rate="0.20" \
  --commission-max-change-rate="0.01" \
  --chain-id=euler-1
```

#### Verify that you are validating

```bash
docker exec -ti cyberd cyberdcli query staking validators --trust-node=true
```

If you see your `<your_node_nickname>` with status `Bonded` and Jailed `false` everything must be good. You are validating the network.

# Maintenance of validator

#### jailing

If your validator goes under slashing conditions it first goes to jail. After this event the operator must unjail it manually.

```bash
docker exec -ti cyberd cyberdcli tx slashing unjail --from=<your_key_name> --chain-id=euler-1
```

#### Upgrading of validator

Updating is as easy as pulling the new docker container and launching it again

```bash
docker stop cyberd
docker rm cyberd
docker pull cyberd/cyberd:<testnet_chain_id>

docker run -d --name=cyberd --restart always --runtime=nvidia \
 -p 26656:26656 -p 26657:26657 -p 26660:26660 \
 -v /root/cyberd:/root/.cyberd \
 -v /root/cyberdcli:/root/.cyberdcli \
 cyberd/cyberd:euler-1
```

Don't forget to unjail if you were jailed during an update.

The rank calculation has a linear relationship between GPU memory usage and links quantity. A number of links is indefinitely increasing, but the potential of vertical scaling is limited.

Understanding this, we are looking for solutions to calculate the same amount of links with fewer capacity.

# Call to you, validator

For now it is the time and opportunity to go up against blackbox search engines. Obviously, a cryptoeconomic approach can change beneficiaries in this game effectively removing possible sybil attack vectors and removing the necessity to make a decision on example crawling and meaning extraction from one entity to the whole world. Learning a sybil-resistant model will probably lead to orders of magnitude with more predictive results.

At 2019/02/04 there 9 active validators and 1 jailed. This is enough to support net, but this is not enough for quality growth. We are looking for validators. Join us!

# Connect to us, #fuckgoogle

Subscribe at [Steemit](https://steemit.com/@cybercongress), [Reddit](https://www.reddit.com/r/cybercongress/), [Twitter](https://twitter.com/cyber_devs), [Telegram channel](https://t.me/cybercongress) and join our community in [@fuckgoogle](https://t.me/fuckgoogle)
