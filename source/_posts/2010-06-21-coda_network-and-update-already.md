---
title: 'coda_network &#8211; and update already(!)'
author: Garry Bodsworth
layout: post
aktt_notify_twitter:
  - yes
  - yes
aktt_tweeted:
  - 1
categories:
  - Uncategorized
tags:
  - coda_network
  - development
  - network
  - proxy
  - python
---
After releasing the first version of [coda_network][1] over the weekend I have found a few bugfixes (corner cases).

Mainly these involved using an NTLM proxy and attempting to tunnel a socket through it. This makes sense of the proxy case where you are trying to daisy-chain sockets together. This was really an issue with keep-alive proxies where the Request object was not resetting some cached state that would only ever work once.

The main feature now though is I have added mini_proxy.py. A multiprocess proxy server using all my code changes. Only GET, POST and CONNECT are implemented, but that should be sufficient for most tests. This mini proxy can then speak to upstream proxies of no authentication types, as well as basic. digest, and NTLM.

The readme on the [github page][1] has been updated with example commandlines for the proxy and I have tested it against all kinds of proxies. Because of all the other work put into httplib and urllib2 the proxy itself is actually only 200 lines. I&#8217;ve got no idea how efficient it is, but it should work fine.

 [1]: http://github.com/garrybodsworth/coda_network