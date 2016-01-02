Title: Clutter 0.9.4 Released
Date: 2009-06-20T09:00:00+00:00
Category: 
Tags: 
Authors: Garry Bodsworth

A new developer snapshot version of [Clutter][1] has been released which is part of the journey towards Clutter 1.0. The project is an OpenGL renderer for user interfaces which uses the gobject base system.

The reason I post this though is that I have contributed (terribly minor) patches to this release. Plus also as part of the progress to 1.0 there are some very substantial changes under the hood. There is now a master clock for rendering which should improve rendering quality and smoothness. Also, beware, all units have been removed and it uses floating point values in the API now. There is some cool debugging features in the OpenGL wrapper part of Clutter so performance work can be done more easily.

You can see full release notes [here][2]. The snapshot is available from git [here][3].

Now I need to build a deb so I can test this out a little more&#8230;.

 [1]: http://www.clutter-project.org
 [2]: http://git.clutter-project.org/cgit.cgi?url=clutter/tree/NEWS
 [3]: http://git.clutter-project.org/?url=clutter/tag/&id=0.9.4