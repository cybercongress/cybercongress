---
date: 2018-09-25
url: zh-cn/45-ipfs-weekly-11
translationKey: 45-ipfs-weekly-11
tags: weekly
title: IPFS 周报-11
author: Jenn Turner
---

## 欢迎回到IPFS周报！👋

[InterPlanetary File System (IPFS, 星际文件系统)](https://ipfs.io/) 是一种新型的，基于内容和身份的，超媒体分发协议。IPFS使得开发完全分布式的应用程序成为可能。它旨在使网络更快、更安全、更开放。因为这是一个相当大范围的任务，在这篇周报中，我们跟踪、汇总了（IPFS）整个生态系统的发展。

想参与进来吗？点击下面的一些链接，看看我们在GitHub上做了什么，或者在IRC上加入我们（Freenode网络上的#ipfs）。
希望收到邮件更新吗？订阅我们的每周通讯！

以下是自上一期IPFS周报以来的一些新亮点：

最新进展：
- IPFS现已有22种语言支持，更多的语言还在加入中。得益于最近的“IPFS本地化”努力，IPFS正在向全世界进发！
- [CloudFlare 加入了我们的星际任务](https://blog.cloudflare.com/distributed-web-gateway/)。尝试下CloudFlare的IPFS网关，该网关是在其第一次的Crypto Week 活动中宣布的。
- 观看9月18号发布的最新的“[动态数据及能力工作小组”会议视频](https://www.youtube.com/watch?v=EiJE59uYNAk)，迅速了解关于身份管理的演示和讨论。
- 第一次柏林IPFS会议将于10月11日举行！[在此处注册参加Meetup](https://www.meetup.com/IPFS-Berlin/events/254816369/)。
- IPFS的JavaScript实现版本刚刚有了新的主页：[js.ipfs.io](https://js.ipfs.io)。

野生态IPFS：
你有在推特上[关注IPFS](https://twitter.com/IPFSbot)吗？对于最新的新闻中提到的ipfs，请查看我们的twitter feed或阅读：[关于最棒的ipfs的最新文章](https://awesome.ipfs.io/categories/articles/)。



-   [Dweb: Creating Decentralized Organizations with Aragon](https://hacks.mozilla.org/2018/09/aragon-ethereum-dweb/), （DWeb：使用Aragon来创建去中心化组织）作者：Mozilla Hacks, 2018年9月19日
-   [End-to-End Integrity with IPFS](https://blog.cloudflare.com/e2e-integrity/), （IPFS的点到点完整性）作者：Cloudflare, 2018年9月17日
-   [CloudFlare’s IPFS Gateway Makes it Easy to Create Distributed Web Sites](https://www.bleepingcomputer.com/news/technology/cloudflares-ipfs-gateway-makes-it-easy-to-create-distributed-web-sites/), （CloudFlare的网关大大简化了分布式网站的构建）2018年9月17日
-   [An Interview with Textile](https://medium.com/textileio/an-interview-with-textile-6d52632f611b), （对Textile的采访）（**译者注：该采访由星鉴网完成**）2018年9月13日
-   [The Centralized Secret](https://medium.com/@kyletut/the-centralized-secret-c7de795ddd9f), （中心化的秘密）2018年9月12日
-   [Decentralisation: the next big step for the world wide web](https://www.theguardian.com/technology/2018/sep/08/decentralisation-next-big-step-for-the-world-wide-web-dweb-data-internet-censorship-brewster-kahle), （去中心化：万维网的下一个里程碑）作者：The Guardian （卫报），2018年9月8日
-   [Swapping bits and distributing hashes on the decentralized web](https://medium.com/textileio/swapping-bits-and-distributing-hashes-on-the-decentralized-web-5da98a3507), （在去中心化网络上交换比特，分发哈希），2018年9月4日
-   [Introducing Origin Messaging: Decentralized, Secure, and Auditable](https://medium.com/originprotocol/introducing-origin-messaging-decentralized-secure-and-auditable-13c16fe0f13e), （起源信息简介：去中心化，安全和审查）作者：Origin，2018年8月29日
-   [Dweb: Building Cooperation and Trust into the Web with IPFS](https://hacks.mozilla.org/2018/08/dweb-building-cooperation-and-trust-into-the-web-with-ipfs/), （DWeb：使用IPFS技术，将合作与信任融入到网络中）作者：Mozilla Hacks，2018年8月29日




软件更新和新版本发布：

以下是IPFS工具和IPFS生态项目的发布情况：




-   [ipfs-cluster 0.5.0](https://github.com/ipfs/ipfs-cluster/releases/tag/v0.5.0) – IPFS Cluster 是一个独立的程序和命令行客户端；可以在IPFS daemon的集群上分配、复制以及追踪pins
-   [go-ipfs 0.4.17](https://github.com/ipfs/go-ipfs/releases/tag/v0.4.17) – IPFS 在 Go 语言上的实现
-   [ipfs-companion v2.5.0.11550 (Beta)](https://github.com/ipfs-shipyard/ipfs-companion/releases/tag/v2.5.0.11550) – 一个大大简化了IPFS资源获取过程的浏览器插件，开发人员和爱好者可以选择使用我们的浏览器插件的手工选择的开发版本
-   [js-ipfs v0.32.0](https://github.com/ipfs/js-ipfs/releases/tag/v0.32.0) – IPFS 在 JavaScript语言上的实现
-   [npm-on-ipfs v0.6.4](https://github.com/ipfs-shipyard/npm-on-ipfs/releases/tag/v0.6.4) – 📦 通过IPFS安装npm模块！
-   [Replicated Object Notation 2.1](https://github.com/gritzko/ron/blob/master/docs/Objectives%20for%20RON%2021.md) – 一个分布式的实时数据格式
-   DNSLink Detection in IPFS Companion: 我们的浏览器插件现在可以在默认模式下检测DNSLink，访问[docs.ipfs.io](http://docs.ipfs.io/) 或者[tr.wikipedia-on-ipfs.org](https://tr.wikipedia-on-ipfs.org/)，你就可以从IPFS，而不是HTTP上加载它，通过以下链接获取更加详细信息:[DNSLink Support in IPFS Companion](https://github.com/ipfs-shipyard/ipfs-companion/blob/master/docs/dnslink.md)
-   [Qri 0.5.2](https://github.com/qri-io/qri/releases/tag/v0.5.2), 即 Prune Norwegian Buhund, 在此！
-   [The Graph Development Update](https://medium.com/graphprotocol/the-graph-development-update-d90321e22748), 2018年9月13日
-   [Polkadot PoC-2 在此](https://medium.com/polkadot-network/polkadot-poc-2-is-here-parachains-runtime-upgrades-and-libp2p-networking-7035bb141c25): Parachains, 运行更新，libp2p更新




我们喜爱的工具和项目：

[Awesome IPFS （完美IPFS）](https://awesome.ipfs.io/)是由社区维护和更新的，包括了一系列的工具、项目，以及基本上与IPFS相关的很棒的一切。查看更多，或将你的项目添加到其中，请访问以下Github地址：[Awesome IPFS on GitHub](https://github.com/ipfs/awesome-ipfs)

-   [Neocities hit 200K sites this month!](https://twitter.com/neocities/status/1039204355763666945) （Neocites这个月达到了20万个网站！）
-   [are we distributed yet?](https://arewedistributedyet.com/) （我们已经实现分布式了吗？）
-   [Pinata](https://www.pinata.cloud/), 轻松自如的在IPFS上部署.




社区活动：

你知道ipfs有一个社区论坛discuss.ipfs.io吗？报名参加关于编码的讨论，教程，请参阅通知并了解即将到来的社区活动。

-   [35th Chaos Communication Congress](https://events.ccc.de/2018/09/11/35c3-call-for-participation-and-submission-guidelines/) （第35届混沌通讯议会）CFP 现已开放
-   新的见面会提醒:[peer to peer ÖRESUND](http://p2p-oresund.org/), 地点：瑞典马尔默 时间：10月27日
-   [在此注册，接收IPFS里斯本会议的通知](https://docs.google.com/forms/d/e/1FAIpQLSfJVVPwvp6RY3MUg1zAVl1g_5y2nGb7WJIMI1Hs6glzm7FLHQ/viewform)




感谢阅读☺️

以上就是本周关于IPFS一切的新闻。如果我们错过了什么，请回复这个邮件，让我们知道！这样我们就可以在下次周报中介绍您了。
