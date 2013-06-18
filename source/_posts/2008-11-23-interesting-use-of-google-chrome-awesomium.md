---
title: 'Interesting Use Of Google Chrome &#8211; Awesomium'
author: Garry Bodsworth
layout: post
categories:
  - Uncategorized
tags:
  - development
---
Well, actually more an interesting use of Webkit rather than Chromium I suppose&#8230;

[Awesomium][1] enables offscreen rendering of webpages by using the [Chromium][2] libraries which in turn are based on [Webkit][3]. Rendering to an offscreen buffer means you can embed the web content on things like OpenGL surfaces.

Currently the code only works on Windows (mainly because the Chromium source is not yet fully ported). The reason for using Crome over vanilla Webkit is that it uses its own rendering framework to deliver pixels from multiple processes to the main program window. This means you can use that rendering pipeline more easily because it is not so reliant on platform specifics and uses Skia to put the content together. From what I have tried to work out writing a backend for Webkit is a non-trivial process and tends to require lots of extra plumbing.

The latest version of Awesomium even lets you use the Flash plugin for extra rendering goodness.

Check out the developers blog [here][4].

 [1]: http://code.google.com/p/awesomium/
 [2]: http://code.google.com/chromium/
 [3]: http://webkit.org/
 [4]: http://ajeanius.wordpress.com/