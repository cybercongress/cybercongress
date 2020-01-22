---
date: 2020-01-22
url: cyber-reports
title: 'cyber~Wednesday Day 0'
author: serejandmyself
---

**cyber~Wednesday Day 0**

Welcome to the new bi-weekly report format from cyber!

As most of you know, previously we used to report weekly in our [TG channel](https://t.me/fuckgoogle) in an open format. But nothing lasts forever and its time to move to a new format. An asynchronous format that will:

- Eliminate the need for a monolithic team leader
- Make the report more interactive to the public
- Include more information from each full-time member of the team
- Be more efficient and creative than before

Last week, we outlined a [new set of guidelines](https://github.com/cybercongress/congress/blob/master/teams/team%20reports.md) for the reports. Each report will be a combined work from the team. It will be pushed to our GitHub and thereafter published for AMA (ask me anything) on the #fuckgoogle [TG channel](https://t.me/fuckgoogle). For now, questions from the community will be answered openly in the channel.

## Cyber bi-weekly report 2020.01.22

### @serejandmyself

DONE:

- Published several articles in crypto-related media (hackernoon, publish0x, bitcoinews and others)
- Created a [topic for mentions](https://ai.cybercongress.ai/t/mentions-of-the-beast-in-the-wild-any-links-that-mention-cyber-cyb-etc-are-a-fair-game/40) on the forum. Filled it with content
- Given several interviews (seen in the list)
- Had several mentions (IPFS and others)
- Taken part in [36c3](https://events.ccc.de/congress/2019/wiki/index.php/Main_Page)
- Given a [speech](https://www.youtube.com/watch?v=mc51zyflpa8) there
- Recorded an interview for [Monero talk](https://www.monerotalk.live/)
- Re-organised one of the ecosystem [main tasks](https://github.com/cybercongress/congress/issues/289)
- Started several new topics on different crypto-related forums. A full list can be seen [here](https://github.com/cybercongress/congress/tree/master/ecosystem/profiles)
- We also hit the [trending spot](https://www.reddit.com/r/privacytoolsIO/comments/en6qbn/data_is_the_new_gold_unfortunately_in_todays/) with some of our article on the privacytools subreddit, which was cool!
- The [ELI-5 FAQ](https://github.com/cybercongress/congress/blob/master/ecosystem/ELI-5%20FAQ.md) has been updated
- A few more new documents have been created, for example, the [gift FAQ](https://github.com/cybercongress/congress/blob/master/ecosystem/Gift%20FAQ%20and%20general%20gift%20information.md)
- Tested spreading out the news about the gift, but as that's not the main task right now, we stopped with that for the time being
- Contacted validators across the Cosmos ecosystem
- Converting miners from other ecosystems: [Grin](https://forum.grin.mw/t/a-shout-out-to-the-miners-of-grin-uncategorized-because-its-not-about-mining-grin-directly/6966) and the [Cortex mining](https://www.reddit.com/r/Cortex_Official/comments/erbuw3/off_topic_calling_out_to_cortex_miners/) 
- Gained frequent mentions in [TodayInCosomos](https://twitter.com/adriana_kalpa)
- Submitted [several PR's](https://github.com/serejandmyself) to list cyber on different GitHub awesome lists
- Submitted forms to websites like [cryptomiso](https://www.cryptomiso.com/)
- Talked with several players in the Cosmos ecosystem to gain awareness for cyber

TODO:

- Carry on work on forums, chats, SM, validators, partnerships 
- Submit to forklog hub, work with other media
- Carry on work on tasks according to the main [ecosystem development paper](https://github.com/cybercongress/congress/blob/master/ecosystem/cyber~Ecosystem%20development%20paper.md)


### @savetheales

DONE:

- Developed backend for cyber.page euler-5 gift checker as IPLD structure
- Provided concept for gift conversion on mongodb and flaks stack
- Provided concept for the Game of Links personal and overall monitors with currently won balances
- Continued to research backend stack for game monitors 

TODO:

- Backend for the game monitors with WebSockets.   

### @xhipster

DONE:

- Some advancement on [gift checker](https://cyber.page/#/search/0x002F9CaF40a444f20813DA783D152bdfAF42852F) feature. While everybody can now check their balance, expect better agent experience in the release. Cool thing is that balances loads from ipfs hash using IPLD selectors
- [Catching errors](https://github.com/cybercongress/dot-cyber/issues?q=is%3Aopen+is%3Aissue+label%3Aerror) in https://cyber.page based in the feedback
- A lot of minor improvements on faucets
- One more repetition of test~Foundation ceremony with @litvintech
- Improvement of workflow development. Now we work with pull request only
- Research of [Metamask](https://github.com/MetaMask/metamask-extension) and [in3](https://in3.readthedocs.io/en/develop/getting_started.html) codebase for better Cyb architecture
- Some collaboration with @savethealse on the Game of Links monitor

TODO:

- Next week Ceremony and [next dot-cyber release](https://github.com/cybercongress/dot-cyber/projects/3) are in focus

### @dimakorzhovnik

DONE

added features:

- Gift lookup [#124](https://github.com/cybercongress/dot-cyber/issues/124)
- Vesting page [#110](https://github.com/cybercongress/dot-cyber/issues/110)

bugs fixed:

- Remove check for metamask on brain [#131](https://github.com/cybercongress/dot-cyber/issues/131)
- Display error while linking 2 times [#132](https://github.com/cybercongress/dot-cyber/issues/132)

update page:

- Test of Thrones [#107](https://github.com/cybercongress/dot-cyber/issues/107)(16/20)
- Takeoff funding [#70](https://github.com/cybercongress/dot-cyber/issues/70)(7/11)
- Auction page [#117](https://github.com/cybercongress/dot-cyber/issues/117)(1/3)

TODO: 

- Test of Thrones [#107](https://github.com/cybercongress/dot-cyber/issues/107)(16/20)
- Takeoff funding [#70](https://github.com/cybercongress/dot-cyber/issues/70)(7/11)
- Auction page [#117](https://github.com/cybercongress/dot-cyber/issues/117)(1/3)
- Transaction page [#108](https://github.com/cybercongress/dot-cyber/issues/108)
- Account page [#109](https://github.com/cybercongress/dot-cyber/issues/109)
- No search path if search from main page [#130](https://github.com/cybercongress/dot-cyber/issues/130)
- Fix intro [#129](https://github.com/cybercongress/dot-cyber/issues/129)
- Bandwidth do not decrease [#128](https://github.com/cybercongress/dot-cyber/issues/128)

### @mrlp4

DONE:

- In collaboration with @xhipster and some other team members created a roadmap for deploying safe and redundant infrastructure for serving all cyber-related services.
- Deployed and configured monitoring/alerting system for cybercongress backend based on [Grafana](https://github.com/grafana/grafana) and [Prometheus](https://github.com/prometheus/prometheus).
- Created and tested docker setup of [Brain](https://github.com/cybercongress/brain)

### @litvintech

DONE:

- Upgraded contracts and enhanced frontend of [cyber~Vesting](github.com/cybercongress/aragon-auction-app) Aragon application
- Enhanced the frontend of [cyber~Auction](github.com/cybercongress/aragon-auction-app) Aragon application
- Implemented the initial version of the vesting companion which will send EUL/CYB (cyber) for vested GOL/THC (Ethereum) tokens with proofs. Will be published in [launch-kit](https://github.com/cybercongress/launch-kit/) this week
- Tweaked [Juno](https://github.com/fissionlabsio/juno/) to index cyber chain for GOL monitor
- One more repetition of test~Foundation ceremony with @xhipster. New record time!
- Discussed cybergraph project with @belya
- Meeting on GOL monitor with @savetheales
- Collaboration with @dimakorzhovnik on the implementation of Vesting app into cyber application

### @aha203

DONE: 

- Defined the scope of work for infrastructure and formalized the infrastructure improvement road map. Visualized and decomposed projects of Cyber ecosystem by their stack of technology. 

TODO: 

- Research of hosting provider services to improve infrastructure resistance and disaster recovery. 
