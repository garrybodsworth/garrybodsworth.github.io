---
title: 'Video Codecs That Don&#8217;t Make You Go Grey'
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
  - video
---
Great news today, [Google are open-sourcing and more importantly free patent licensing][1] the VP8 codec. As part of this they are creating the [WebM][2] project with a new container format that uses the open-source [Vorbis][3] audio codec.

As someone who has to deal with video codecs every day and the horrors they induce (not just from a technical standpoint but legal) this is a very good thing. Unfortunately it does have some way to go to depose the incumbent codecs, and to reach parity with respect to hardware acceleration, but I am sure it will happen swifter than we can imagine. The main reasons for this is that Youtube will be using it which is a large portion of the web&#8217;s video, and th enames that are all on board to support it in both software and hardware.

I can tell you as soon as gstreamer gets support [CODA][4] will be getting WebM.

There is also now a technical analysis from an x264 developer which can be read [here][5].

 [1]: http://googleblog.blogspot.com/2010/05/google-io-2010-day-1-more-powerful-web.html
 [2]: http://www.webmproject.org/
 [3]: http://www.vorbis.com/
 [4]: http://www.camvine.com
 [5]: http://x264dev.multimedia.cx/?p=377