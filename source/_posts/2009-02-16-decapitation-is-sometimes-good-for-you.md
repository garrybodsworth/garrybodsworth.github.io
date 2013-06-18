---
title: Decapitation Is Sometimes Good For You
author: Garry Bodsworth
layout: post
categories:
  - Uncategorized
tags:
  - clutter
  - development
  - mozilla
  - webkit
---
Lots of people out there are looking for headless web browsers to generate things like thumbnails. In the end most people either roll their own or cheat (use xvfb and grab the pixmap). You could use [Qt and grab the image][1], but it still requires xvfb, even if you write your own rendering backend (I assume for font stuff). There are a number of ways to solve the headless rendering problem, unfortunately not all of them are ideal.

For me I am looking at [EFL WebKit][2] as the best solution but it is not near maturity and because I quite like the way Enlightenment Foundation Libraries seem to work.

The latest possible solution(s) are born from the [Clutter Project][3] which is now under the guidance of Intel. There is [Clutter Webkit][4] which provides a Clutter Actor for rendering webpages essentially to a Cairo surface on the 3D surface. I got it to compile last night and ran a test program but it was pretty slow.

The other one is [mozilla-headless][5] which looks really interesting by providing a Mozilla library that renders to a Cairo surface. [Chris Lord][6] the main developer on this made presentation to FOSDEM available [here][7]. There is also a video of it in action [here][8] (requires OGG codecs). The source is all available [here][5] and the embedding into Clutter is available [here][9]. The source code for testing it is [here][10].

On a vaguely related note there is an interesting article about using gstreamer through Clutter&#8217;s python bindings &#8211; [awesome (gstreamer * clutter)][11].

 [1]: http://labs.trolltech.com/blogs/2009/01/15/capturing-web-pages/
 [2]: http://code.staikos.net/cgi-bin/gitweb.cgi?p=webkit;a=shortlog;h=kenneth/efl-port
 [3]: http://clutter-project.org/
 [4]: http://trac.webkit.org/wiki/clutter
 [5]: http://git.o-hand.com/cgit.cgi/mozilla-headless/
 [6]: http://chrislord.net/
 [7]: http://chrislord.net/files/fosdem-09-slides.odp
 [8]: http://chrislord.net/images/mozilla/mozilla-magic.png
 [9]: http://git.clutter-project.org/?r=clutter-mozembed
 [10]: http://git.clutter-project.org/cgit.cgi?url=clutter-mozembed/tree/tests
 [11]: http://luisbg.blogalia.com//historias/61951