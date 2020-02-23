# IPFS Companion

Upgrade your browser with [IPFS](https://ipfs.io/) super powers

![demo of v2.8.0](https://user-images.githubusercontent.com/157609/55318231-938ce480-5472-11e9-8624-b0021a34c1a4.gif)

| <img src="https://unpkg.com/@browser-logos/firefox/firefox_16x16.png" width="16" height="16"> [Firefox](https://www.mozilla.org/firefox/new/) / [Firefox for Android](https://play.google.com/store/apps/details?id=org.mozilla.firefox) | <img src="https://unpkg.com/@browser-logos/chrome/chrome_16x16.png" width="16" height="16"> [Chrome](https://www.google.com/chrome/) / <img src="https://unpkg.com/@browser-logos/brave/brave_16x16.png" width="16" height="16"> [Brave](https://brave.com/) / <img src="https://unpkg.com/@browser-logos/opera/opera_16x16.png" width="16" height="16"> [Opera](https://www.opera.com/)  / <img src="https://unpkg.com/@browser-logos/edge/edge_16x16.png" width="16" height="16"> [Edge](https://www.microsoftedgeinsider.com/)
|------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [![Install From AMO](https://ipfs.io/ipfs/QmWNa64XjA78QvK3zG2593bSMizkDXXcubDHjnRDYUivqt)<br>![](https://img.shields.io/amo/users/ipfs-companion?label=AMO%20users&style=social)](https://addons.mozilla.org/firefox/addon/ipfs-companion/) | [![Install from Chrome Store](https://ipfs.io/ipfs/QmU4Qm5YEKy5yHmdAgU2fD7PjZLgrYTUUbxTydqG2QK3TT)<br>![](https://img.shields.io/chrome-web-store/users/nibjojkomfdiaoajekhjakgkdhaomnch?label=Chrome%20Web%20Store%20users&style=social)](https://chrome.google.com/webstore/detail/ipfs-companion/nibjojkomfdiaoajekhjakgkdhaomnch) |

## Features

### Automagical Detection of IPFS Resources

#### IPFS Path in URL

Requests for IPFS-like paths (`/ipfs/{cid}` or `/ipns/{peerid_or_host-with-dnslink}`) are detected on any website.  
If tested path is a [valid IPFS address](https://github.com/ipfs/is-ipfs) it gets redirected and loaded from a local gateway, e.g:  
> `https://ipfs.io/ipfs/QmbWqxBEKC3P8tqsKc98xmWNzrzDtRLMiMPL8wBuTGsMnR`  
> → `http://127.0.0.1:8080/ipfs/QmbWqxBEKC3P8tqsKc98xmWNzrzDtRLMiMPL8wBuTGsMnR`

#### DNSLink

Companion will detect presence of [DNSLink](https://docs.ipfs.io/guides/concepts/dnslink/) in DNS records of visited websites and redirect HTTP request to a local gateway.

> `http://docs.ipfs.io`  
> → `http://127.0.0.1:8080/ipns/docs.ipfs.io`

This means if you visit websites with a valid DNSLink (eg. https://docs.ipfs.io, https://ipld.io, http://tr.wikipedia-on-ipfs.org) browser will load them from IPFS.

More details: [DNSLink Support in IPFS Companion](https://github.com/ipfs-shipyard/ipfs-companion/blob/master/docs/dnslink.md)

#### X-Ipfs-Path

Companion will upgrade transport to IPFS if the header is found in any HTTP response headers. This is a fallback for edge cases when IPFS path is not present in URL.

More details: [`x-ipfs-path` Header Support in IPFS Companion](https://github.com/ipfs-shipyard/ipfs-companion/blob/master/docs/x-ipfs-path-header.md)

#### Redirect Opt-Out

It is possible to opt-out from Gateway redirect by:
- a) suspending redirect via global toggle (see [_Disable All Redirects_](#disable-all-redirects) below)
- b) suspending redirect for via per website opt-out (in [_Active Tab_ section of _Browser Action_](#disable-gateway-redirect-per-website) or _Preferences_)
- c) including `x-ipfs-companion-no-redirect` in the URL (as a [hash](https://ipfs.io/ipfs/QmbWqxBEKC3P8tqsKc98xmWNzrzDtRLMiMPL8wBuTGsMnR#x-ipfs-companion-no-redirect) or [query](https://ipfs.io/ipfs/QmbWqxBEKC3P8tqsKc98xmWNzrzDtRLMiMPL8wBuTGsMnR?x-ipfs-companion-no-redirect) parameter).

### IPFS API as `window.ipfs`

Your IPFS node is exposed as `window.ipfs` on every webpage.
Websites can detect if `window.ipfs` exists and opt-in to use it instead of creating their own `js-ipfs` node.
It saves system resources and battery (on mobile), avoids the overhead of peer discovery/connection, enables shared repository access and more!
Make sure to read our [notes on `window.ipfs`](https://github.com/ipfs-shipyard/ipfs-companion/blob/master/docs/window.ipfs.md), where we explain it in-depth and provide examples on how to use it your own dapp.

### Quick Toggles

The Browser Action pop-up provides handy toggles for often used operations.

#### Disable Gateway Redirect Per Website

> _Active Tab_ actions include option to opt-out current website from Gateway redirect of any IPFS subresources.    
> Disabling redirect for DNSLink website will restore original URL as well:
>
> ![per-site-opt-out](https://user-images.githubusercontent.com/157609/55317805-90452900-5471-11e9-9e0f-293afd261648.gif)

#### Disable All Redirects

> A handy toggle to disable all gateway redirects while keeping all other features enabled:
>
> ![redirect](https://user-images.githubusercontent.com/157609/55317804-90452900-5471-11e9-9fc1-42bee5b15a6a.gif)

#### Suspend IPFS Extension

> The "power" icon can be used to temporarily suspend all IPFS integrations
> (redirects, API status, content scripts, protocol handlers etc).
> Useful during testing. Extension can be re-enabled with a single click:
>
> ![screenshot of suspend toggle](https://user-images.githubusercontent.com/157609/55317803-8fac9280-5471-11e9-96e3-f068cc62148b.gif)

### IPFS Status and Context Actions

- IPFS API and Gateway status
- Add local (quick import) or remote files (context menu) to IPFS with option to preserve filename
- Easy access to [WebUI](https://github.com/ipfs/webui/) and add-on Preferences
- Toggle redirection to local gateway (automatic by default, manual mode can be enabled in Preferences)
- Additional actions for pages loaded from IPFS
    - Pin/Unpin of IPFS resources (via API)
    - Copy canonical IPFS address
    - Copy shareable URL to resource at preferred public gateway

## Install

### Release Channel

We recommend installing the stable release via your browser's add-on store.

| <img src="https://unpkg.com/@browser-logos/firefox/firefox_16x16.png" width="16" height="16"> [Firefox](https://www.mozilla.org/firefox/new/) / [Firefox for Android](https://play.google.com/store/apps/details?id=org.mozilla.firefox) | <img src="https://unpkg.com/@browser-logos/chrome/chrome_16x16.png" width="16" height="16"> [Chrome](https://www.google.com/chrome/) / <img src="https://unpkg.com/@browser-logos/brave/brave_16x16.png" width="16" height="16"> [Brave](https://brave.com/) / <img src="https://unpkg.com/@browser-logos/opera/opera_16x16.png" width="16" height="16"> [Opera](https://www.opera.com/)  / <img src="https://unpkg.com/@browser-logos/edge/edge_16x16.png" width="16" height="16"> [Edge](https://www.microsoftedgeinsider.com/)
|------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [![Install From AMO](https://ipfs.io/ipfs/QmWNa64XjA78QvK3zG2593bSMizkDXXcubDHjnRDYUivqt)<br>![](https://img.shields.io/amo/users/ipfs-companion?label=AMO%20users&style=social)](https://addons.mozilla.org/firefox/addon/ipfs-companion/) | [![Install from Chrome Store](https://ipfs.io/ipfs/QmU4Qm5YEKy5yHmdAgU2fD7PjZLgrYTUUbxTydqG2QK3TT)<br>![](https://img.shields.io/chrome-web-store/users/nibjojkomfdiaoajekhjakgkdhaomnch?label=Chrome%20Web%20Store%20users&style=social)](https://chrome.google.com/webstore/detail/ipfs-companion/nibjojkomfdiaoajekhjakgkdhaomnch) |

**Note:** `ipfs-companion` is designed to retrieve content from a locally running IPFS daemon.  
Make sure [IPFS is installed](https://docs.ipfs.io/introduction/usage/) on your computer.

***The content partially copied from https://github.com/ipfs-shipyard/ipfs-companion/blob/master/README.md***