---
title: In Programming Lies Madness
author: Garry Bodsworth
layout: post
categories:
  - Uncategorized
tags:
  - development
---
Sometimes programming makes you feel like you are losing your marbles. Over the past few days I have lost many hours of my spare time attempting to compile a branch of GTK+.

I went down the obvious route of installing the development libraries with apt-get and then attempting to compile the source code. That, needless to say did not work at all.

Next up I tried the suggested method of jhbuild, the package available in the Ubuntu repositories. I just ended up with multiple versions of glib all conflicting with one another.

Next up I tried building jhbuild from its source. Building jhbuild was pretty simple, and then I tried to bootstrap and compile GTK+. The pain then came that hidden deep within the logs it wasn&#8217;t installing the version of Cairo necessary for Pango, so I attempted to find my way around that which meant I ended up in library hell. It was so damn close though as it was only GTK+ left to build and there was a compilation error because something was missing from Glib to do with emblems &#8211; so close and yet so far. It seems to you need some libraries installed on your system as well as the ones that are constructed as part of jhbuild.

I persevered with lots of combinations, time and hard work, and still I didn&#8217;t manage to get it to compile. It&#8217;s a bit depressing to be defeated by a build system, but it seems to have grown so massive and baroque that it is a large barrier to entry. The thing was I really wanted to mess around with one of the git branches of GTK+.