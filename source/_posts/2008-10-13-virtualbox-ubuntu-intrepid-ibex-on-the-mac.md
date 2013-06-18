---
title: VirtualBox Ubuntu Intrepid Ibex On The Mac
author: Garry Bodsworth
layout: post
categories:
  - Uncategorized
tags:
  - Linux
---
I&#8217;ve been playing around Intrepid Ibex on my Macbook Pro. I discovered Parallels frankly is pretty poor in Ubuntu support so I decided to try out [VirtualBox][1].

I downloaded the latest Intrepid Ibex Beta and it installed quickly and cleanly on the virtual machine. Then I installed the the Guest Additions that improve the performance of working in the virtual machine (the equivalent would not play ball with me on Parallels even with Hardy 8.04). There is a bit of manual tweaking to get it all working because the resolution is stuck at 800&#215;600. What you need to do is edit your *xorg.conf* by typing the following in terminal `sudo gedit /etc/X11/xorg.conf`

You need to replace the contents of the file with (just choose your resolution by replacing 1024&#215;768):

<pre>Section "Device"
   Identifier   "Configured Video Device"
   Driver    "vboxvideo"
EndSection
Section "Monitor"
	Identifier	"Configured Monitor"
EndSection
Section "Screen"
   Identifier    "Default Screen"
   Device    "VirtualBox graphics card"
   Monitor    "Generic Monitor"
   DefaultDepth    24
   SubSection "Display"
     Depth    24
     Modes      "1024x768"
   EndSubSection
EndSection
</pre>

Restart your system and you are good to go!

 [1]: http://www.virtualbox.org/