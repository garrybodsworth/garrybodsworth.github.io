---
title: 'Asus UL20A &#8211; Hints And Tips For Running Linux'
author: Garry Bodsworth
layout: post
aktt_notify_twitter:
  - yes
aktt_tweeted:
  - 1
categories:
  - Uncategorized
tags:
  - install
  - laptop
  - Linux
  - mint
  - setup
---
My MacBook Pro developed the [nVidia graphics failure problem][1] and I got the motherboard replaced, it has never been the same since and when I asked I basically had no warranty for it. So after three-and-a-half years I decided to buy myself a new laptop. Lacking the riches required for another Apple I decided to go where I am really most comfortable &#8211; Linux. So after a lot of research and fingers crossing I picked up an [Asus UL20A][2] off of eBay for 318 quid including postage.

The specs are as follows:

*   Core2Duo SU7300 (dual core 1.3GHz)
*   12 inch display at 1366&#215;768
*   Quoting something like 8 hours battery life.
*   4GB RAM (upgraded by me for 25 quid)
*   60GB solid state drive (upgraded by me for 95 quid) &#8211; an OCZ Vertex 2E with the respected Sandisk controller.

The point of this post, however, is not to review a piece of hardware, but to get Linux working flawlessly on it.

**Linux Mint 10**

I decided to use[ Linux Mint 10][3] (Ubuntu base), this is instead of stock Ubuntu which I find very cluttered on initial install and also requires me to do loads of fiddling to get a normal looking and clean desktop environment.  Linux Mint 10 is based on the latest Ubuntu but presents the user a very nicely set up session after the first install.  The desktop is uncluttered, there is only one panel at the bottom, and theme is head and shoulders above the Ubuntu default.

Linux Mint does have a Debian based edition which I will switch to later but the packages are a lot further behind the latest Ubuntu and since I was going to use some more modern features for the SSD I would have to have done a lot more hacking.

**Installing**

I partitioned the SSD the following way:

*   256MB ext2 /boot partition
*   4.1GB /swap partition
*   15GB btrfs / partition
*   40GB btrfs /home partition

I decided to use btrfs because it is the latest and greatest available file system for Linux.  This means it has things like TRIM support for SSDs and can do cool stuff like snapshots, but this also requires a newer kernel for better support hence not using the Linux Mint Debian Edition.

The ext2 boot partition is required as you can&#8217;t boot directly from btrfs according to the information I found out there.  The swap partition is memory + 100MB for supporting hibernate.  The main partition is separate from the home partition &#8211; **this is very important when you use Ubuntu**.  Because Ubuntu does releases every six months you can attempt upgrades, but I have seen and experienced this failing with catastrophic consequences.  Luckily having a separate home partition means you can tell Ubuntu to reinstall to the main partition but just mount and use you home directory without formatting it.

Installation took me about 10-15 minutes before I was there in my freshly installed desktop.  Now, almost everything works straight out of the box, it is case of tweaking to get some of the more hidden features working.

**Two Finger Scrolling**

Two finger scrolling on the Synaptics touchpad requires a little bit of tweaking.   Create a file called /usr/share/X11/xorg.conf.d/50-twofingerscroll.conf with the folling contents:  
`<br />
Section "InputClass"<br />
Identifier "touchpad catchall"<br />
MatchProduct "SynPS/2 Synaptics TouchPad"<br />
Option "VertTwoFingerScroll" "on"<br />
Option "HorizTwoFingerScroll" "on"<br />
Option "EmulateTwoFingerMinW" "5"<br />
Option "EmulateTwoFingerMinZ" "48"<br />
EndSection`

Then start up* gconf-editor* and change* /desktop/gnome/peripherals/touchpad/scroll_method* to the value *2*.

Now you have two finger scrolling working and also two finger right click!

**The LCD Brightness Keys**

This requires a small change to your boot settings so that you can use the function keys to set the screen brightness.

Edit */etc/default/grub* so that the line with *GRUB\_CMDLINE\_LINUX = &#8220;&#8221;* says:  
`<br />
GRUB_CMDLINE_LINUX="acpi_backlight=vendor"`

Then run *sudo update-grub *and reboot.

**Power Settings**

To help improve battery life install powertop by using *sudo apt-get install powertop* then run *sudo powertop* and follow its instructions.  You should be able to help squeeze precious minutes out of your battery.

**Mistakes**

I did attempt installing the latest kernel along with the latest graphics drivers.  This was mainly for graphical hacking and trying out newer btrfs options.  This is a big mistake.  For a start the battery monitoring stops working although I managed to solve that, then shutdown stopped working consistently.  So for all the benefits don&#8217;t bother if you prefer your system to be properly functioning.

**What I Did Next&#8230;.**

I always use [Ubuntu Tweak][4] and it works on Linux Mint 10.  This allows you to get some more interesting packages and also update to cutting edge versions.

There is something I don&#8217;t like about Google Chrome despite its super-speed, so I always go back to Firefox.  Unfortunately distros currently use 3.6 but I have been using 4.0 for about six months, it is much quicker, better looking and more robust.  Through Ubuntu Tweak enable the Minefield repositories and get it.  Also install the Nightly Tools Addon to help get your Addons all working.

I install ttf-droid fonts normally and switch all my desktop to use that as it gives more space, but for people who don&#8217;t like small fonts you probably should avoid it.

I have also installed and am running the theme from the [elementary project][5] which gives a less Minty user interface for Linux Mint.  It&#8217;s purely aesthetical, although the elementary Nautilus file browser is much better than the default.

**All In All**

At the end of it I have a fully working Linux laptop that boots in less than 20 seconds and shuts down in about a second.  It is easy to use and responsive which makes me really happy.  From what I have been trying to work out the ASUS laptops seem to have fairly decent Linux support.

Next up I am going to have to get hacking on [libimobiledevice][6] because I have an iPhone and I would like to avoid running updates via a virtual machine or something.

 [1]: http://support.apple.com/kb/TS2377
 [2]: http://www.amazon.com/UL20A-A1-Light-12-1-Inch-Silver-Laptop/dp/B002PAQXAE
 [3]: http://www.linuxmint.com/
 [4]: http://ubuntu-tweak.com/
 [5]: http://www.elementary-project.com/
 [6]: http://www.libimobiledevice.org/