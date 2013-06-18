---
title: Cluttered Mind
author: Garry Bodsworth
layout: post
categories:
  - Uncategorized
---
Finally, I have contributed something back to an open-source project.

The memory leak in [Clutter][1] I mentioned in a previous post has been fixed. I submitted the [patches][2] last week, and they got pushed onto master in time for Clutter 1.0.

I&#8217;ve been playing around with Clutter a bit more now and it is well inside the GTK+ comfort zone. I am really pleased I can contribute something useful to a project of this size because I am so used to using libraries but not actually fixing them. It&#8217;s the glory of open-source.

I&#8217;ve been playing around a little with Clutter 1.0 and its master clock based animation and it looks really interesting. Just be careful that some parameters are floats instead of ints now and this caused me to segfault.

 [1]: http://www.clutter-project.org
 [2]: http://bugzilla.openedhand.com/show_bug.cgi?id=1640