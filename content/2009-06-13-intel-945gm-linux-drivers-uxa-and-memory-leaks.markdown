Title: Intel 945GM Linux Drivers &#8211; UXA and Memory Leaks
Date: 2009-06-13T09:00:00+00:00
Category: 
Tags: 
Authors: Garry Bodsworth

One of the things I have been plugging away with at work is getting Intel 945GM graphics drivers working at their best. I was using 2.6 and 2.7 with the new UXA acceleration because it works really well with composite and xvideo.

The problem was there was a memory leak that you could drive a bus through. Because the Linux driver stack is so complex (Mesa, X Driver, X-server, kernel gubbins, the Direct Rendering Manager library) it was proving extremely difficult to find where the memory was going because it was still being used even when the process was closed.

With the code I was writing I found I could get the memory of the computer fully utilised in less than one hundred iterations. Luckily that meant I could write a [small test case][1]. The bug hit particularly hard in Moblin which relied on the Intel drivers and Clutter. At least five bugs in Freedesktop Bugzilla seem to report it, plenty in Launchpad, and several in Moblin.

As it turned out Shuang He of Intel diagnosed the root of the problem in the Mesa driver where pixmaps weren&#8217;t being released properly and has submitted [some patches][2] for that. The mesa patches have been applied if you use [xorg-edgers][3] on Ubuntu which makes life a lot easier considering I spent four hours building my own fixed Mesa&#8230;

Not only this but there was a memory leak in Clutter (which I submitted patches for) which are now in their git master repository.

Now with both of those things fixed compositing windows using Clutter works brilliantly and will work for an extended period of time rather than falling over after a short time. Also if these patches are used on Moblin v2, you should get a better experience.

 [1]: http://lists.freedesktop.org/archives/intel-gfx/2009-May/002559.html
 [2]: http://lists.freedesktop.org/archives/intel-gfx/2009-June/002791.html
 [3]: https://launchpad.net/~xorg-edgers/+archive/ppa