---
title: JooJoo Technical Details
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
  - hardware
  - joojoo
  - Linux
---
For those of you as nerdy as me I thought I would try a virtual teardown of the JooJoo to gather information on its internals.

First up the nvidia ION platform it is using is the MCP79 (revision b1). They are all much the same when it comes to ION motherboards with the revisions.

lspci output:  
`<br />
00:00.0 Host bridge: nVidia Corporation MCP79 Host Bridge (rev b1)<br />
00:00.1 RAM memory: nVidia Corporation MCP79 Memory Controller (rev b1)<br />
00:03.0 ISA bridge: nVidia Corporation MCP79 LPC Bridge (rev b3)<br />
00:03.1 RAM memory: nVidia Corporation MCP79 Memory Controller (rev b1)<br />
00:03.2 SMBus: nVidia Corporation MCP79 SMBus (rev b1)<br />
00:03.3 RAM memory: nVidia Corporation MCP79 Memory Controller (rev b1)<br />
00:03.5 Co-processor: nVidia Corporation MCP79 Co-processor (rev b1)<br />
00:04.0 USB Controller: nVidia Corporation MCP79 OHCI USB 1.1 Controller (rev b1)<br />
00:04.1 USB Controller: nVidia Corporation MCP79 EHCI USB 2.0 Controller (rev b1)<br />
00:06.0 USB Controller: nVidia Corporation MCP79 OHCI USB 1.1 Controller (rev b1)<br />
00:06.1 USB Controller: nVidia Corporation MCP79 EHCI USB 2.0 Controller (rev b1)<br />
00:08.0 Audio device: nVidia Corporation MCP79 High Definition Audio (rev b1)<br />
00:09.0 PCI bridge: nVidia Corporation MCP79 PCI Bridge (rev b1)<br />
00:0b.0 IDE interface: nVidia Corporation MCP79 SATA Controller (rev b1)<br />
00:10.0 PCI bridge: nVidia Corporation MCP79 PCI Express Bridge (rev b1)<br />
00:15.0 PCI bridge: nVidia Corporation MCP79 PCI Express Bridge (rev b1)<br />
00:16.0 PCI bridge: nVidia Corporation MCP79 PCI Express Bridge (rev b1)<br />
02:00.0 VGA compatible controller: nVidia Corporation Device 0876 (rev b1)<br />
03:00.0 Network controller: Realtek Semiconductor Co., Ltd. Device 8172 (rev 10)<br />
`

The mini PCIe networking card is a Realtek 8172. Ubuntu details are [here][1] and driver install instructions are [here][2] for older kernels. I found the drivers very problematic, and according to the discussions out there on the Internet many other people struggle to get it working well on Linux.

You&#8217;ll also notice there are no ethernet controllers listed.

And now stuff from dmesg&#8230;.

A normal looking Atom chip.  
`<br />
CPU0: Intel(R) Atom(TM) CPU N270   @ 1.60GHz stepping 02<br />
`  
And I assume hyperthreading is enabled:  
`<br />
CPU1: Intel(R) Atom(TM) CPU N270   @ 1.60GHz stepping 02<br />
`  
Bluetooth is pretty standard:  
`<br />
Bluetooth: Generic Bluetooth USB driver ver 0.5<br />
`  
About 128Mb is allocated for graphics from the 1Gb total:  
`<br />
Memory: 888772k<br />
`  
There is a USB hub with 6 ports somewhere:  
`<br />
hub 4-0:1.0: 6 ports detected<br />
`  
The touch controller:  
`<br />
input: eGalax Inc. USB TouchController as /devices/pci0000:00/0000:00:06.0/usb4/4-1/4-1:1.0/input/input3<br />
`  
The driver for the touchscreen is [here][3].

There is a keyboard somewhere maybe it is used for something internally:  
`<br />
input: Chicony USB Keyboard as /devices/pci0000:00/0000:00:04.1/usb1/1-1/1-1.2/1-1.2:1.0/input/input4<br />
`

I&#8217;m still trying to work out the ambient light sensor and rotation sensor (which allegedly us ACPI through a hacked kernel that has not been GPL released yet).

 [1]: https://help.ubuntu.com/community/WifiDocs/Device/Realtek%208172
 [2]: http://www.linwik.com/wiki/using+the+realtek+8172+and+8192se+wireless+controller+with+ubuntu+9.10
 [3]: http://home.eeti.com.tw/web20/eGalaxTouchDriver/linuxDriver.htm