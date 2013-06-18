---
title: What should be built into an operating system?
author: Garry Bodsworth
layout: post
categories:
  - Uncategorized
tags:
  - multimon
  - Windows
---
This post is otherwise known as &#8220;Why multiple monitor support in Windows sucks&#8221;&#8230;

Noah Coad, one of the Program Managers on the Visual Studio team blogged about [Multi Monitor Support in VS10][1] and it is confirmed on the [Microsoft Connect site][2]. When I worked at [DisplayLink][3] we obviously used multiple monitors on Windows in development so any help in that regard is welcomed. When you use multiple monitors every day you do discover the deficiencies in the operation of such set-ups (even on the latest Windows Vista). Things like disappearing windows, incorrect sizing, incorrect windows flags (saying its maximised when it isn&#8217;t leading to all kinds of bizarre effects), losing display configurations, and the most important &#8211; that virtually all Windows applications are designed to be operated when the parent frame is full-screen.

These features that are being suggested should be in the operating system, not just support in certain applications that never even make it into the higher level APIs (how many implementations should there be of ribbon? one provided by the API). These features are also not just the realm of developers, I am sure artists, sound engineers and many other disciplines would like to see better multiple monitor support. Also, when it is in the operating system it is consistent across all applications rather than having similar or completely different behaviour between applications. The main problem with Windows in this regard is if there is a good feature that is applicable to more situations it never propagates up to the API level within the organisation.

By operating system I mean graphical user interface <img src='http://localhost:8888/wordpress/wp-includes/images/smilies/icon_wink.gif' alt=';)' class='wp-smiley' />

 [1]: http://blogs.msdn.com/noahc/archive/2007/10/10/multi-monitor-support-in-vs10.aspx
 [2]: https://connect.microsoft.com/VisualStudio/feedback/ViewFeedback.aspx?FeedbackID=351965
 [3]: http://displaylink.com