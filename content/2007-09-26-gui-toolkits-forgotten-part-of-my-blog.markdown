Title: GUI Toolkits - The Forgotten Part Of My Blog
Date: 2007-09-26T19:59:00+00:00
Slug: gui-toolkits-forgotten-part-of-my-blog
Category: 
Tags: 
Authors: Garry Bodsworth

I have been doing this blog nearly a year now and certainly in 2007 I have neglected GUI coverage.  The main problem is that there hasn't been a huge amount of impressive work on the open-source front and those libraries that showed the most promise are languishing in Sourceforge hell.

Maybe Winforms has caught on big-style?  Maybe, but as far as I can tell when you get down to the OS level it still amounts to Win32 function calls, it is just the framework is built on top of that.  Also, many more applications can now be run as web-based applications, with its own plethora of GUI toolkits.

Qt is obviously the leader but is only open-source for open-source applications unfortunately (and quite rightly as they do deserve to make money off it).  wxWidgets is not making as massive strides as many would have hoped in order to have really good looking native Windows applications.  The most recent substantial addition was wxAUI that added lots of good stuff like docking.  None of the ideas floating around Boost got off the ground unfortunately, and Win32GUI Generics and Notus and many others are mothballed.  Maybe there needs to be a "State Of The GUI Union" post...

I am thinking of doing a small GUI toolkit just to test out the theories and get a better appreciation of the difficulties involved in design and implementation.  It would also mean I could play around with some of my memory allocation and multithreading ideas as part of it.  I've been trying to pull together as much information about Win32 as posible and I'll definitely put them all together in one article.
