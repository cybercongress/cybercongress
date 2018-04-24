Mars is our `staging` server. You may reuse its config for your own.

## Current Mars storage setup

| Name      | Type  |  Size   | LABEL     |  Mapping                      |
| --------- | ----- | ------- |---------- |------------------------------ |
| nvme0n1p1 | ssd   | 1 tb    | SDD1      | /cyberdata/ssd1tb             |
| nvme2n1p1 | ssd   | 500 gb  | SDD2      | /cyberdata/ssd05tb            |
| sdc1      | hdd   | 3.5 tb  | HDD3      | /cyberdata/elassandra-markets |
| sdb1      | hdd   | 3.5 tb  | HDD2      | /cyberdata/elassandra-search  | 
| sda1      | hdd   | 3.5 tb  | HDD1      | /backupsData                  |
| sdd1      | hdd   | 3.5 tb  | cyberdata | /cyberdata                    |

### `/cyberdata` contents

* ***/cyberdata/portainer/*** - portainer data directory
* ***/cyberdata/cybernode/*** - clone of repo https://github.com/cyberFund/cybernode

## Useful commands

Format partition:
```
sudo mkfs -t ext4 -L SSD1 /dev/nvme0n1p1
sudo mkfs -t ext4 -L SSD2 /dev/nvme2n1p1
```
/etc/fstab addition lines:
```
LABEL=cyberdata /cyberdata ext4 defaults 0 0
LABEL=SSD2 /cyberdata/ssd05tb ext4 nofail 0 0
LABEL=SSD1 /cyberdata/ssd1tb ext4 nofail 0 0
LABEL=HDD1 /backupsData ext4 defaults 0 0
LABEL=HDD2 /cyberdata/elassandra-search ext4 defaults 0 0 
LABEL=HDD3 /cyberdata/elassandra-markets ext4 defaults 0 0 
```
Copy data:
```
sudo cp -R --verbose /backupsData/chain/eth/eth /cyberdata/ssd05tb/eth/
sudo cp -R --verbose /cyberdata/bitcoind /cyberdata/ssd05tb/bitcoind/
```

