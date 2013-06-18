---
title: Webkit Ported To EFL
author: Garry Bodsworth
layout: post
categories:
  - Uncategorized
tags:
  - development
  - enlightenment
  - webkit
---
EFL (Enlightenment Foundation Libraries) now has a [port for Webkit][1]. It is not in the Webkit trunk or anything but it is available in git form [here][2].

I&#8217;ve tried compiling it and using it on my Gnome VM and it works really well. The main missing parts are the NPAPI plug-ins rendering and the video tag support. Since this is an early stage all things will come in time (like video will probably use the Enlightenment Emotion engine). [Patches][3] are also coming along.

What I like about Enlightenment and its libraries is that they are all well-defined meaning it has lots of rendering back-ends like DirectFB, Cairo, X11, OpenGL, and tons more. The libraries are all lightweight enough for embedded devices making them even more interesting.

There has even been some work about wrapping the Webkit rendering in a user interface (apart from the example one available in the WebKit git) and it has a really good name [ewww][4].

All of these guys have done great work so far and it looks like the start of something good.

 [1]: http://codeposts.blogspot.com/2008/12/webkit-ported-to-enlightenment.html
 [2]: http://code.staikos.net/cgi-bin/gitweb.cgi?p=webkit;a=shortlog;h=kenneth/efl-port
 [3]: http://codeposts.blogspot.com/2008/12/webkit-efl-receives-its-first-patch.html
 [4]: http://blog.gustavobarbieri.com.br/2008/12/22/webkit-efl-interface-prototype/