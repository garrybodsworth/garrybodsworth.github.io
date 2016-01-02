Title: New Github Project - pyxlib-ctypes
Date: 2011-08-23T20:33:00+00:00
Slug: new-github-project-pyxlib-ctypes
Category: 
Tags: 
Authors: Garry Bodsworth

I had written a pyrex based binding to some elements of Xlib, but I decided to make it pure python to avoid the compilation step.&nbsp; Luckily a kind person had created pyxlib-ctypes <a href="http://code.google.com/p/pyxlib-ctypes/">http://code.google.com/p/pyxlib-ctypes/</a> which is a pure Python binding to the underlying X functions.

I needed a few more features due to XComposite for writing crazy desktop compositors in pure Python and also some XFixes functionality so we can really hide the mouse cursor.

As such I am publishing my amendments to it on Github - you can check it out here: <a href="https://github.com/garrybodsworth/pyxlib-ctypes">https://github.com/garrybodsworth/pyxlib-ctypes</a> it literally has the bare minimum I needed and could probably be extended for greater coverage.&nbsp; It is used in production and seems to be working very happily.
