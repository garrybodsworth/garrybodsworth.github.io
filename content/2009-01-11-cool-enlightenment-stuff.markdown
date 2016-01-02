Title: Cool Enlightenment Stuff
Date: 2009-01-11T09:00:00+00:00
Category: 
Tags: 
Authors: Garry Bodsworth

I&#8217;ve been playing around with the EFL (Enlightenment Foundation Libraries) [port of WebKit][1] and I have been very impressed by the quality of the page rendering. In fact I have been playing around with Enlightenment E17 libraries, although I haven&#8217;t gone the whole hog and installed the desktop environment.

The quality of the building blocks that have been put together are extremely impressive with multiple rendering backends for the Evas canvas including X11, OpenGL, Windows and Quartz. It&#8217;s a highly optimised canvas to build UIs with. I&#8217;ve spent some time reading the source to work out how it all fits together. I liked the &#8220;buffer&#8221; backend for Evas that allows you to render to that engine and capture the output as a buffer of bytes, but in order to use it there was no massive difference in code.

But I digress, on my travels through the internet I found a few interesting projects related to Enlightenment e17.

First up there is a comprehensive skin for the Enlightenment areas that require it. It is called [Detour (DTR)][2] and looks clean and consistent.

Next up I found [iTask][3] (and its relations iTask-NG and WinList-NG) which are new taskbars for Enlightenment. These look good and provide integration with compositing with the NG versions.

Finally, the best thing I found was someone had put e17 together with the compositing of Compiz called [ecomorph][4]. This is an alpha project but is showing some impressive results. There is a three part video : [one][5], [two][6], [three][7]. Also you can see a super dark demo [here][8].

Enlightenment has not been at the forefront unfortunately because of a lack of official e17 release, but hopefully that will be rectified in the near future, mainly because a lot of the framework provided could be really useful (and it is a British thing to root for the underdog).

 [1]: http://code.staikos.net/cgi-bin/gitweb.cgi?p=webkit;a=shortlog;h=kenneth/efl-port
 [2]: http://code.google.com/p/detour/
 [3]: http://code.google.com/p/itask-module/
 [4]: http://code.google.com/p/itask-module/wiki/Stuff
 [5]: http://www.youtube.com/watch?v=RHbQ0ASlzCQ
 [6]: http://www.youtube.com/watch?v=5G9hr-izzn4
 [7]: http://www.youtube.com/watch?v=21VURWljN4A
 [8]: http://www.youtube.com/watch?v=w5gDEiJpBwI