Title: nVidia + Linux + ACPI = Borked
Date: 2009-04-13T09:00:00+00:00
Category: 
Tags: 
Authors: Garry Bodsworth

It&#8217;s a simple equation and has cost me a day of trying to get ACPI suspend/hibernate working on Linux. It took me long enough to realise it was the nVidia driver causing the issue.

Whenever I tried suspend or hibernate I would get a black screen with a flashing cursor in the top left. After working out it was the nVidia driver I tried all the remedies I could find on the Internet by other people with the same bug. What I discovered was this problem has been around for going on at least three years and no solution is being worked on.

The obvious articles are [here][1], [here][2], [here][3], [here][4], and [here][5].

All solutions provide slightly different but the same solution, you need to set NvAGP in your xorg.conf to either 0 or 1 and optionally use agp=off for your kernel. I tried various concoctions and none of them worked.

I think I worked out what the problem is though. If your motherboard chipset is not nVidia (I think they call them nForce) then NvAGP will never work because mine always drops back to agpgart. This must be why most of the success is seen on laptops where the IGP must be using nVidia chipsets. My motherboard has a VIA chipset (old and crusty I know) with a GeForce 8500GT hence my complete and utter lack of success.

Like I said this problem has been around for quite a while and the chipset problem could be why the only responses I have read from nVidia is that they are unable to reproduce it. So for me it will be a new sensible graphics card with hopefully fairly open drivers.

 [1]: http://www.amitsrivastava.net/2008-03-23-hibernate-suspend-resolved-ubuntu-gutsy-nvidia-dell-vostro/
 [2]: https://help.ubuntu.com/community/NvidiaLaptopBinaryDriverSuspend
 [3]: http://us.download.nvidia.com/XFree86/Linux-x86/1.0-9755/README/appendix-f.html
 [4]: http://en.opensuse.org/Talk:NVidia_Suspend_HOWTO
 [5]: http://susewiki.org/index.php?title=Suspending_with_the_NVidia_drivers