---
title: Open-Source CAD/CAM
author: Garry Bodsworth
layout: post
categories:
  - Uncategorized
tags:
  - CAD
  - CAM
  - opensource
  - Programming
---
I spent over seven years working in the CAD/CAM industry. It&#8217;s a very archaic industry with virtually no open-source building blocks available, and those that are tend be be extremely old or not even useful.

There are a few green shoots of open-source out there. First up there is [wildcat-cad][1] which is an attempt to create an open-source 3D solid modelling kernel and associated tools.

There is also [heekscad][2] which is a modelling program using the [OpenCascade][3] solid modelling kernel (GPL licensed I believe). There is also a CAM add-on for heekscad called [heekscnc][4] with a lot of associated libraries providing some good functionality.

An additional program is [voxelcut][5] which allows for a solid machining simulation to see what damage you&#8217;ll do to your hardened steel.

One of the libraries is [libarea][6] which is for area-clearance algorithms in CAM. This is normally one of the most closely guarded secrets in commercial CAD/CAM so it is interesting to see an open implementation.

[libactp][7] is an adaptive clearance toolpath which originated from [Freesteel][8]. They&#8217;ve got it integrated into heekscnc so you can try it out for yourself.

You can keep track of a lot of this stuff through [Dan Heek&#8217;s blog][9].

Another unrelated program is <monocam> which uses C-sharp as a development language and has soem interesting algorithms like the drop cutter which provides the basis for most 3D machining algorithms.

 [1]: http://code.google.com/p/wildcat-cad/
 [2]: http://code.google.com/p/heekscad/
 [3]: http://www.opencascade.org/
 [4]: http://code.google.com/p/heekscnc/
 [5]: http://code.google.com/p/voxelcut/
 [6]: http://code.google.com/p/libarea/
 [7]: http://code.google.com/p/libactp/
 [8]: http://www.freesteel.co.uk
 [9]: http://heekscnc.blogspot.com/