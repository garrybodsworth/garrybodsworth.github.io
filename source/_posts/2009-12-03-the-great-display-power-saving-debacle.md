---
title: The Great Display Power Saving Debacle
author: Garry Bodsworth
layout: post
categories:
  - Uncategorized
---
We are supposed to be concerned with our power consumption. After all [California has enshrined in law][1] restrictions on the power usage of televisions.

Working for a [digital signage company][2] I have to deal with a lot of displays. The initial hardware platform only had VGA output, great, power saving worked using DPMS. The [VESA Display Power Management Signaling][3] standard version 1.0 was released in 1993, even since moving from CRTs to the flat screen world we live in nowadays (making some of hsync and vsync options surplus to requirements on new flat screens, but it simply maps to &#8220;off&#8221;). The monitors people used behaved themselves. The next platform we used briefly had DVI and VGA output and monitors that supported those inputs all adhered to the teenage standard.

But this is where problems now creep in. DVI can be plugged into an HDMI port very easily. The current hardware platform has native HDMI so it is fairly obvious to suggest that customers use this rather than the VGA output that is also available.

This is where I stepped through the looking glass. Apparently because HDMI and DVI are electrically equivalent then there is nothing to stop the manufacturer having DPMS support. I was developing thinking that HDMI would be great for users since they would also get audio transport built into the single cable. I kind of assumed DPMS was still working.

I have yet to find a single display that does respect DPMS. Of course most people want to use cheap consumer televisions so they don&#8217;t stand a chance of this support.

The most worrying thing I have found about those cheap consumer displays is that they do supply VGA ports that don&#8217;t even support DPMS. A lot of these displays also have a &#8220;feature&#8221; to power off after a ten minute (or so) period of inactivity and the only way to power it on is to physically press the power button or the remote, it doesn&#8217;t even notice when a signal starts again(!)

There are two possible solutions. One is [HDMI-CEC][4], which is Consumer Electronic Control. One or two of the pins (depending on the HDMI version) is essentially a serial port, and this provides the standard for communication on this. This would be good but you need extra chips built into your HDMI output which only one computer has (a Toshiba laptop &#8211; and it only works on Windows&#8230;). Also the even larger problem is that every manufacturer seems to have their own standard, RegzaLink, SIMPLink, VIERAlink, BRAVIAsync, and a myriad of others. If you buy all your equipment from the same manufacturer you will end up with some benefit.

The other solution at least in the digital signage use is to use the RS232 service port for controlling the display. Each monitor tends to have its own way of doing it and can even vary between model numbers. Also it has been heard from the manufacturers that they will be phasing this out and most new TVs don&#8217;t even have it.

In summary? Display power saving used to work for most people, now it doesn&#8217;t. So, it is all well and good reducing the power consumption of the devices but there is a way of removing a lot of power from the equation by switching off the panel when it isn&#8217;t being used. This was a solved problem that has been unsolved by engineering madness. Because some TVs are unable to wake from their power saving state over any connection I ended up having to add a &#8220;power saving&#8221; option that doesn&#8217;t actually save any power&#8230;.

 [1]: http://www.latimes.com/business/la-fi-big-screen-tvs19-2009nov19,0,4027697.story
 [2]: http://www.camvine.com
 [3]: http://en.wikipedia.org/wiki/VESA_Display_Power_Management_Signaling
 [4]: http://en.wikipedia.org/wiki/HDMI#CEC