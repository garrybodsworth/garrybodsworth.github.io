---
title: DisplayLink Open Source
author: Garry Bodsworth
layout: post
categories:
  - Uncategorized
tags:
  - development
  - DisplayLink
  - graphics
  - Linux
  - opensource
---
Yesterday [Displaylink][1] released Linux source code for its USB display adapters. The project is LGPL and available on [FreeDesktop][2]. The project itself is called libdlo and is available from [this link][3] with the Git repository [here][4]. You can see DisplayLink&#8217;s announcement [here][5].

At the moment it is a low-level library for speaking to the device and is not yet wrapped in a Xorg driver. The code itself supports ASIC devices and only the USB versions (if that means something to you then you have probably worked for DisplayLink at some point).

The code itself is impressively documented, and means people should be able to get something up and running pretty fast. I&#8217;m sure some interesting and exciting projects will come out of this.

Well done to DisplayLink on doing this &#8211; this is going to be a really good thing for getting content onto displays. USB is a really good solution &#8211; imagine daisy-chaining lots of displays controlled by a single computer.

 [1]: http://www.displaylink.com
 [2]: http://freedesktop.org
 [3]: http://freedesktop.org/wiki/Software/libdlo
 [4]: http://cgit.freedesktop.org/libdlo/
 [5]: http://www.displaylink.com/news/news150509.htm