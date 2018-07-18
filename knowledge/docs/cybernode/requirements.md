# Requirements

For near future(1.0 release) cybernode will act as a helping tool around docker images to instantiate p2p systems and app around them. For the first release, we consider to do next:

```bash

1) cybernode settings
   cybernode help
   
2) cybernode status   

3) cybernode chains ethereum|ethereum_kovan|ethereum_classic start (--light --autostartup)
   cybernode chains ethereum stop

   cybernode chains bitcoin help
   cybernode chains bitcoin start (--autostartup)
   cybernode chains bitcoin stop
   
   cybernode chains status
   cybernide chains help

4) cybernode p2p ipfs start (--autostartup)
   cybernode p2p ipfs stop

5) cybernode apps|platforms cyb start
   cybernode apps|platforms cyb stop
```

## First run initialization

For first run of cybernode, user should specify where to store data for applications:
```bash
cybernode.data.location=~/.cybernode/data
```
By default, all cybernode configs|state will be stored in **~/.cybernode** path. Nonchangeble.

Research:
- [] Path autocompletion?

## `cybernode chains` subcomands
User shoud be able to run chains with specified options.
Research:
- [] UI for chains
- [] Light clients for chains

## `cybernode p2p` subcomands
User shoud be able to run p2p systems with specified options.
Research:
- [] Key pair managment if chain reuqired

## `apps|platforms` subcomands
User should be able to run DApps. Each DApp also have dependencies on p2p or chains entities. This subcommand should start only missing entities.

## `cybernode status`
Should display to user cybernode running|stopped entities.
Also should be available for all subcommands.

## `cybernode help`
Should display help message to the user.
Also should be available for all subcommands.

## `cybernode settings`
Should print current settings.

Research:
- [] Possible solutions for autocomplete for MacOS, Linux systems
- [] Language and framework for CLI
- [] Package distribution for various platforms(brew, npm, deb etc)
- [] Initial Message??
