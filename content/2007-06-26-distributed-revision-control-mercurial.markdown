Title: Distributed Revision Control - Mercurial
Date: 2007-06-26T19:36:00+00:00
Slug: distributed-revision-control-mercurial
Category: 
Tags: 
Authors: Garry Bodsworth

<a href="http://www.selenic.com/mercurial/">Mercurial (hg)</a> is one of the distributed revision control systems I looked at in a previous post.  I've been looking more closely at these shttp://www.blogger.com/img/gl.link.gifystems and thinking about how they fit in to the different development methods (closed and open source don't normally need the same process).

Interestingly there is a talk at Google from last year by one of the main developers Bryan O'Sullivan on Google Video:

<embed style="width:400px; height:326px;" id="VideoPlayback" type="application/x-shockwave-flash" src="http://video.google.com/googleplayer.swf?docId=-7724296011317502612&#038;hl=en" flashvars=""></embed>

Version 0.9.4 of Mercurial was released today adding a fair amount of bugfixes and new functionality.  It is a very interesting system as it is implemented in Python, is very efficient and is one of the best for cross platform support out of the distributed revision control systems (with an extension adding the support for Windows file endings).

The commandline syntax is simple and easy to use.  It has a wide variety of additional tools and extensions.  Although these are not as mature or in-depth as other systems (like Subversion/CVS/and so on) they are providing a good basis.  Quite a few large projects are using Mercurial in production like Mozilla, OpenSolaris, Xine, and Xen.

There is a great book about using Mercurial <a href="http://hgbook.red-bean.com/">here</a>.  It covers many of the concepts and simply how to use it.  The wiki based website and the mailing lists are also great sources of information.

There seems to be lots of GUI tools but none providing full workflow support yet, but hopefully this will happen with time.
