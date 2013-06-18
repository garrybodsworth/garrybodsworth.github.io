---
title: Tablet PCs And The Multi-Touch Future
author: Garry Bodsworth
layout: post
categories:
  - Uncategorized
tags:
  - GUI
  - Interaction
  - Multitouch
---
Over the past six months I have actually got to use some tablet PCs, and I wonder why any company pursues that market unless it is seriously high margins. For a start the power of these computers are some way off the cutting edge both by processor and graphically. Also the build quality is not good with cheap flimsy plastic made to feel even more unstable thanks to a swivelling monitor so it can be a normal laptop as well.

What really gets me about tablet PCs is the software. I have tried both Windows XP Tablet PC Edition and Windows Vista which has integrated the functionality into the core system (I guess for certain levels of Vista). Additional functionality is provided by the driver software in order to make it easier to use. This is my main gripe, the entire GUI system is predicated around [WIMP][1] and specifically the way that has been set in stone by Windows. The problem is that the pen then becomes basically a pressure sensitive mouse which makes it more difficult and more work to do basic things like resize windows or the horrific right-click if there is a button on the pen. In addition there is normally a trackpad or mouse pointer mechanism built into the computer because it has not fully embraced the tablet way of doing things.

The drivers that the hardware suppliers give try to get around problems like multiple selection (in this instance there is a tick box next to every item in Explorer), and try to make it a bit easier. Unfortunately, because this is not integrated with the core system it is not perfect and needs to deal with unexpected system changes, say for instance plugging in an external display.

The tablet PCs do thrive in environments with a very focussed use where a custom UI is constructed that provides the correct interaction mechanisms.

I read this article [The Mouse Is For The Scrapheap][2] this morning and thought they are a bit hopeful. They are really talking about other interaction mechanisms for specific tasks, not for general computing. This is entirely down to the GUI provided in the operating system, it is not designed for any other way of interacting. Microsoft want [multi-touch at the centre of Windows 7][3], but unless the user interface changes substantially it will be a half-hearted solution. The demonstrations centred around demonstration applications that could use it rather than the framework for the entire GUI.

How would the problem be solved? You would start with the multi-touch implementation and a blank screen. Then create a window that allows for the interactions user&#8217;s expect such as resizing, moving, minimising, etc. This would have to work for the hand driven multitouch in a quick and painless fashion because current window implementations would be too fiddly, but you may find some common ground that can be used in the prototype.

Luckily Apple had a chance for a clean break with the iPhone/iTouch and designed the user interface in a pared down fashion that works for even my fat fingers. This was done by working on a Cocoa Touch API where it is the basis of the interactions the user has, and the main system applications provide a roadmap for the GUI design.

 [1]: http://en.wikipedia.org/wiki/WIMP_(computing)
 [2]: http://uk.gizmodo.com/2008/07/18/the_mouse_is_for_the_scrapheap.html
 [3]: http://windowsvistablog.com/blogs/windowsvista/archive/2008/05/27/microsoft-demonstrates-multi-touch.aspx