Title: Binary blobs&#8230;
Date: 2010-04-28T09:00:00+00:00
Category: 
Tags: 
Authors: Garry Bodsworth

I discovered a way to consistently crash xorg using the nvidia driver.  Open webkitgtk, close it, wait fiver seconds, open it again, rinse and repeat for 15 minutes.  Boom xorg explodes.  Go look at the logs and you have a stack trace telling you something went wrong. As far as I can tell it is running out of texture memory. Bizarrely it doesn&#8217;t do this for videos.

The nvidia driver itself is really quite good in the grand scheme of things providing things like tear-less, hardware accelerated video. It&#8217;s still more consistent and better quality than the open-source ones (obviously owning all the IP and information helps).

But this is the problem with binary blobs you can&#8217;t tell what is going on inside until the state is spat out in the event of failure. I generated the bug report using the nvidia supplied tool and looked at it myself, and there was no information in there that would give a clue as to why. If the internals were exposed you could look at where the memory was going like in the days of [GEM memory leaks on Intel][1].

I guess open-source has its own set of advantages and limitations, as well as the closed-source approach, but damn, I hate losing many hours trying to at first reproduce then diagnose it, let alone being able to make an attempt to fix it.

 [1]: http://blog.programmerslog.com/?p=367