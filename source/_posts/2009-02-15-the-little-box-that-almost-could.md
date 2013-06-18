---
title: The Little Box That Almost Could
author: Garry Bodsworth
layout: post
categories:
  - Uncategorized
tags:
  - Embedded
  - Linux
---
A few weeks back I was looking at some small low-powered computer units. One was really interesting, a passively cooled ultra low voltage tiny computer you could VESA mount to the back of monitors.

It goes under a number of different names, [BVM&#8217;s EPC-500][1], [the eBox-4300 / 4310][2], and [the MicroClient Sr][3]. They all seem to be rebranded versions of the same platform, and I think the eBox is the original although I could be proved wrong.

**Features**  
* 500MHz VIA Eden ULV CPU with 512Mbyte/1Gbyte DDR2 RAM  
* Bootable from Compact Flash or USB  
* Internal HDD option  
* Linux port available on CF or USB Pendrive  
* Low power consumption  
* VESA mounting capability 

**Specifications**  
* CPU: VIA Eden ULV 500MHz.  
* BIOS: AMI BIOS.  
* System Chipset: VIA CX700M.  
* I/O Chip: Winbond W83697.  
* System Memory: Onboard 512MB/1GB DDR2.  
* I/O: 1 x EIDE, 1 x PS/2 K/B/Mouse; 1 x Type I/II CF slot  
* 2 x RS-232 Port (option); USB 3 x USB 2.0 Ports (two on front).  
* Display Chipset: Integrated VIA UniChrome 2D/3D Graphics with MPEG4/WMV9 decoding accelerator.  
* Display Memory: up to 128MBytes sharing system memory.  
* Resolution: up to 1920 x 1440.  
* Audio: AC97 2.2 (Codec); VIA Vinyl VT1708.  
* Audio Interface: Line out, Mic in.  
* Ethernet: Chipset Realtek 8100B 10/100 Base-T  
* Remote Boot ROM built-in boot ROM function, supports PXE boot and Wake-up on LAN.  
* Mechanical & Environment:  
* Power Requirement: +5V @ 3.0A.  
* Operating Temperature: 0 ~ 60°C.  
* Operating Humidity: 0% &#8211; 90% relative humidity, non-condensing.  
* Size (W x H x D): 115x 115 x 35mm.  
* Weight: 505g

Also the [motherboards are available on their own][4] with much more power processors (up to 1.5GHz passively cooled and 2.0GHz with a fan using VIA Eden ULV processors). The spec sheet is [available][5].

I was looking quite deeply into this platform to test its potential. I wanted to run Linux on this and it had an in-built video decoding co-processor as well as 3D support through the CX700M chipset. Anyway I eventually managed to get [Xubuntu][6] running with Compiz effects.

The problem I found with the system is that the drivers are thoroughly inadequate and that the open-source support is nowhere to be seen without VIA helping by supplying the documentation for the video decoding acceleration. The GPU is a [CX700M][7] and the binary drivers are [available][8] and the official drivers are [available from VIA][9] (Ubuntu 8.10 currently). With these the 3D support is okay apart from some font rendering issues when using Compiz.

Some of the older drivers supply the support for the video decoding co-processor. Unfortunately I could not get a version working with a current version of Ubuntu, which in turn even if it did work would not have supported the 3D graphics properly. Also in order to make use of it you have to jump through a number of extra hoops and also operate as root which is a good security risk(!)

There are two specialised version of the media players that VIA has customised to make use of the drivers that supply the MPEG-2/4/h.264 and WMV9 acceleration. These are [VeXP (Via Xine Player)][10] and [VeMP (the VIA enhanced mPlayer)][11]. I did put them into Git repositories starting from the base they branched from so I could work out what the patches did. They rely on closed-source library called libddmpeg.so that is part of some of the older drivers which provides the interface to the video acceleration hardware. This in turn relies n [linuxgate.so.1][12] which provides a direct interface into the kernel for interrupts and the suchlike. This probably explains why all these things if you can get them to work require root access. I did try grabbing the library from an older driver and using it on a newer driver, which would have been too good to be true if it worked (it didn&#8217;t but at least I didn&#8217;t kill the system).

The place to go for drivers and utilities is [VIA Arena][13] where they maintain all the older legacy downloads as only the bleeding edge are available on the official VIA website.

There is a special version of [Puppy Linux][14] that is optimised for the platform. The development website is [here][15]. Unfortunately the media player supplied is not the one that makes use of the co-processor functionality, well it didn&#8217;t for me anyway. Maybe this s worth revisiting again at some point.

There is a blog covering the Microclient Sr [here][16] and a Google Group discussin it [here][17]. There is also a good [comprehensive website (in French)][18]. Finally, a couple of reviews are [here][19] and [here][20].

This is a really cool bit of it with nothing else in its price range/features. Unfortunately the Linux support is such a headache, if it worked I would be extremely happy and it would be very interesting to see how it functions with video and 3D. The tiny little box can even do insanely high resolutions of 1920&#215;1440 which would be very useful.

 [1]: http://www.bvm-store.com/ProductDetail.asp?fdProductId=486
 [2]: http://www.compactpc.com.tw/ebox-4300.htm
 [3]: MicroClient Sr.
 [4]: http://www.liantec.com/product/emboard/EMB-3700.htm
 [5]: http://download.liantec.com/download/datasheet/EMB-3700.pdf
 [6]: http://www.xubuntu.org/
 [7]: http://www.via.com.tw/en/products/chipsets/c-series/cx700m/
 [8]: http://www.viaarena.com/default.aspx?PageID=420&OSID=25&CatID=2580&SubCatID=184
 [9]: http://linux.via.com.tw/support/downloadFiles.action
 [10]: http://sourceforge.net/projects/viaexp
 [11]: http://sourceforge.net/projects/vemp
 [12]: http://www.trilithium.com/johan/2005/08/linux-gate/
 [13]: http://www.viaarena.com/
 [14]: http://www.puppylinux.org/downloads/puplets/mcpup
 [15]: http://www.mcpup.org/
 [16]: http://microclient.wordpress.com/
 [17]: http://groups.google.com/group/microclient
 [18]: http://nettops.fr/index.php
 [19]: http://www.linuxdevices.com/news/NS9828354233.html
 [20]: http://www.linuxdevices.com/articles/AT4708024578.html