---
title: Good news for video acceleration on Linux
author: Garry Bodsworth
layout: post
aktt_tweeted:
  - 1
aktt_notify_twitter:
  - yes
categories:
  - Uncategorized
tags:
  - acceleration
  - development
  - gstreamer
  - video
---
Video acceleration has got a whole lot better on Linux. [Splitted Desktop][1] have released gstreamer plugins with [VA-API][2] support. gstreamer-vaapi was announced on the gstreamer-devel list [here][3].

There are VA-API backends (in the project [libva][4]) for Intel chips, VDPAU for nvidia (and allegedly S3) chips and XvBA for AMD chips (have they ever officially released it?) So this acceleration framework will work on tons of hardware out there. Except for the Intel open-source drivers you do need to use the binary closed source drivers (also for Intel Poulsbo).

The [gstreamer-vaapi][5] plugin supplies MPEG-2, MPEG-4, H.264, VC-1, WMV3 acceleration (providing your hardware supports it). Also output is on OpenGL rendering through VA/GLX or GLX texture-from-pixmap + FBO.

Being gstreamer it should be relatively swift for many applications to pick up the acceleration.

 [1]: http://www.splitted-desktop.com/en/
 [2]: http://en.wikipedia.org/wiki/Video_Acceleration_API
 [3]: http://sourceforge.net/mailarchive/forum.php?thread_name=alpine.DEB.1.10.1005101402160.21123%40thalys.splitted-desktop.com&forum_name=gstreamer-devel
 [4]: http://cgit.freedesktop.org/libva/
 [5]: http://www.splitted-desktop.com/~gbeauchesne/gstreamer-vaapi/