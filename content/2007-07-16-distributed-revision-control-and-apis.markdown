Title: Distributed Revision Control And APIs
Date: 2007-07-16T21:33:00+00:00
Slug: distributed-revision-control-and-apis
Category: 
Tags: 
Authors: Garry Bodsworth

One of the reasons blogging has been quiet the past week or so is I've been fiddling about with some coding.

I've been trying out <a href="http://www.wxpython.org">wxPython</a> and using it as an interface to a distributed source control system.  It's purely experimental, but it did show me some deficiencies and strengths in some of the ones available.

Here is what I learnt though...  wxPython is a great way of hacking together a coherent UI fast, I am still relatively inexperienced in Python and wxPython but the resources out there on the Internet are very useful.

As for the source control systems...  First I tried out <a href="http://www.selenic.com/mercurial/">Mercurial</a>, but I am really struggling with the API and trying to write extensions.  This is mainly due to the lack of documentation, and a lot of current tools like <a href="http://qct.sourceforge.net/">Qct</a> simply parse the commandline.  I did work out some of the parts of the API to wrap, but I found it hard going with limited Python knowledge and a lack of comments.

The other system I tried was <a href="http://bazaar-vcs.org/">Bazaar</a> which I found a very different experience.  The API is excellently documented and the plug-in API is excellent.  Admittedly the criticism levelled at this source contrl system is the speed, but it gets so much right.  It is built on a solid foundation of correctness and the barrier for entry is lowered thanks to the excellent documentation.  I managed o get a working status dialog up and running in a very short period of time (although admittedly I got sidetracked afterwards fiddling around with wxPython).

One of the reasons I was using wxPython is that it looks native on my Macbook Pro as a lot of the available UIs are GTK based meaning they look pretty bad on OS X.  Also I wanted to try it out on Windows which meant it looked pretty good on that platform as well.

Hopefully I can find the time to tidy some of this code up into a reusable form and actually see something like at least the status and commit dialogs through to completion.