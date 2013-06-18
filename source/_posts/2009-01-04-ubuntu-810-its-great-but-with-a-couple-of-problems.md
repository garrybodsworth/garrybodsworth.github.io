---
title: 'Ubuntu 8.10 &#8211; It&#8217;s Great But With A Couple Of Problems'
author: Garry Bodsworth
layout: post
categories:
  - Uncategorized
tags:
  - graphics
  - Linux
  - ubuntu
---
I am in the process of making my desktop computer into a work computer by removing Windows XP and going down the Ubuntu (8.10 Intrepid Ibex) route.

I thought I&#8217;d share some of the problems I had just in case some other people find my solutions useful since from my Googling I notice quite a few people have some issues. I think also I made the problem a bit worse because I am using 64-bit on my Core2Duo.

**Problem #1** : Can&#8217;t get my nVidia GeForce 6600GT to work with the nVidia binary blobs. I was using the latest out of the repositories and then tried the latest from nVidia and all I got was a blank screen and some not very helpful logs. I was getting seriously annoyed after hours of hacking at X configuration files and different nVidia drivers, almost to the point I was going to go out and buy an ATi in the hope open source or at least better drivers would be forthcoming.  
**Solution #1** : The way I ended up having to solve it was using the [Beta 1.80 drivers from nVidia][1]. Definitely not an ideal solution because I have now discovered problem #2.

**Problem #2** : Songbird 1.0.0 won&#8217;t work. There are two places to get 64-bit debs for [Songbird][2] which are both listed [here][3]. It won&#8217;t start though &#8211; bah! On closer investigation glibc is complaining about and invalid free() call. In the callstack you can see the [culprit is the nVidia driver][4]. So now I have to ask myself do I want Songbird or a proper nVidia driver, but Firefox does work with no problems for me. There is also a report of the problem at the [Songbird customer service site][5].

**Problem #3** : Sound didn&#8217;t work for my motherboard. I knew the chip and driver required which was a *snd-via82xx* (serves me right for using such a cheapskate sound solution). So a quick *sudo nano /etc/modules* and adding the driver name to the end of the file fixed that problem. It just needed a restart for the kernel to pick up the change.

But, enough about problems, I am very impressed now I have the basic system up and running. The desktop effects are extremely nice and non-intrusive. You need to install the &#8220;Advanced Desktop Effects Settings (ccsm)&#8221; and &#8220;Compiz Fusion Icon&#8221; to gain access to the UI for customisation. I did a few minor tweaks mainly to switch off wobbly windows and enable the Expose-a-like &#8220;Scale&#8221;. In general the user interface all looks great. If you don&#8217;t have the graphics card problems I have there is a good set of instructions [here][6] on getting the drivers and running Compiz.

I also installed Flash 10 (for x64) and it worked flawlessly. I even managed to watch the Dr Who announcement on the iPlayer Watch BBC One Now option. Flash does eat CPU but it seems to work fine apart from the fullscreen option on iPlayer. And obviously Firefox is as good as ever. I&#8217;ve installed [Screenlets][7] and used the widget layer available in Compiz for the OSX-like Dashboard. 

What I did next was to install [Virtualbox 2.1][8] using the [repository method][9] (to override the ones available from Ubuntu). Then I proceeded to install Windows XP that was on this machine in the VM. After finding the right disk installation was faster than when it was actually on the hardware as were reboots. I am really impressed with this. It even activated first time!

Now I have a properly working system I can say that the 12 hours I spent (mostly trying to fix the unfixable) doing this was more than worthwhile because it boots fast, lets me work fast, and is completely controllable. The only hope I have is that there are some mature open-source video drivers (with 3D) out there in the future because then I will know which cards to buy for minimal hair loss. Also I swear the Ubuntu installation takes about ten minutes maximum compared to the unwieldy Windows installation.

 [1]: ftp://download.nvidia.com/XFree86/Linux-x86_64/
 [2]: http://getsongbird.com
 [3]: https://help.ubuntu.com/community/Songbird
 [4]: http://www.nvnews.net/vbulletin/showthread.php?t=124972
 [5]: http://getsatisfaction.com/songbird/topics/glibc_2_8_detects_invalid_free_pointer
 [6]: http://reformedmusings.wordpress.com/2008/12/09/compiz-fusion-in-ubuntu-810-intrepid/
 [7]: http://www.screenlets.org/
 [8]: http://www.virtualbox.org/
 [9]: http://www.virtualbox.org/wiki/Linux_Downloads