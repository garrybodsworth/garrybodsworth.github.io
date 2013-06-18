---
title: The Many Faces Of WebKit
author: Garry Bodsworth
layout: post
aktt_tweeted:
  - 1
aktt_notify_twitter:
  - yes
categories:
  - Uncategorized
tags:
  - development
  - webkit
---
I&#8217;ve been back into the belly of the beast investigating different implementations of WebKit again. So I thought I&#8217;d share some of the things I picked up about them.

Obviously the Apple implementation is the cream of the crop for speed an features. In fact the Mac OSX version isn&#8217;t top of the tree, it&#8217;s the [iPhone/iPad version][1] that has been furthest ahead. It got the accelerated compositing of web elements first and could do all kinds of funky 3D transforms using OpenGL. The OS X version got those features only in the [middle of last year][2].

Other ports vary in stability, features and usefulness.

[WebkitGTK][3]  
This is the port of WebKit to the GTK+ widget set. It has been through a lot of changes like where the network backend moved to a new library which meant that proxies could not work for a fair while. The rendering itself uses Cairo (good stuff), but it is just a shame you can&#8217;t easily switch backend (like swapping from xlib to opengl). It uses Pango for font rendering which I know is very good, but it has a serious limitation, it can&#8217;t load temporary fonts directly from a file, this means that the new font-face features in HTML will be a long way off.

[QtWebKit][4]  
The rendering quality does look seriously good, but as usual with Qt I am finding very bad performance metrics. I&#8217;ve tried changing rendering backends where &#8220;native&#8221; seems to perform best and &#8220;opengl&#8221; fails then segfaults (which is even more surprising when you consider I am using the nvidia binary drivers on Linux which are pretty full featured).

HTML5support seems a bit flaky at best with one of my sample set completely freezing the process. On the plus side there is integration work already done for compositing, and fonts look seriously good. I got Flash working and it seems OK, but not quite as fast as WebkitGTK.

The biggest advantage though is [PySide][5] which are comprehensive generated Python bindings for Qt. It allowed me to a do a very quick integration with the gobject mainloop in Python as well.

They have also broken away from the protracted Qt release process which allow them to release WebKit features much faster. This makes life a lot easier and they are allowing targetting of more than one version (although not officially supported).

[EFL Webkit][6]  
I have a soft spot for EFL and [Enlightenment][7], it gets a lot of the basics very right (small reusable components and fast and low footprint). EFL Webkit shares a majority of infrastructure with GTK including the Cairo rendering and network backend. The project has also recently picked up sponsorship from Samsung.

There is a really cool demo of the web browser being drawn on a 3D surface using the EFL libraries. You can see it [here][8]. It&#8217;s got gstreamer integration for HTML5 video and plugin support for Flash (oh well).

Now that just covers those main ones available on Linux. There is still the [Palm WebOS][9] version, Blackberry, [OWB][10], and tons more. OWB looks the simplest for enabling porting to new platforms and I have built the SDL version in the past. Then there is the Windows version of WebKit and the standalone Mac build&#8230;

 [1]: http://www.satine.org/archives/2008/11/06/coverflow-for-safari-on-iphone/
 [2]: http://www.satine.org/archives/2009/07/11/snow-stack-is-here/
 [3]: http://www.webkitgtk.org/
 [4]: http://trac.webkit.org/wiki/QtWebKit
 [5]: http://www.pyside.org/
 [6]: http://trac.webkit.org/wiki/EFLWebKit
 [7]: http://www.enlightenment.org/
 [8]: http://blog.gustavobarbieri.com.br/2009/11/04/evas-uv-mapping-and-webkit-efl/
 [9]: http://opensource.palm.com/1.4.1.1/index.html
 [10]: http://www.sand-labs.org/owb