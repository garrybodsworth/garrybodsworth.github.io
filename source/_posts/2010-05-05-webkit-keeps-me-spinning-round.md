---
title: WebKit keeps me spinning round
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
  - webkit
---
So after all the issues I was having with WebKitGTK having undebuggable crashes somewhere in the nvidia binary blob I decided to have a go at QtWebKit integration. It was fairly quick and easy to do (I cheated and used [PySide][1] for brevity). That was good &#8211; no crashes, some nice looking fonts, Flash working and generally all was good, so I started to think how to do a proper integration.

This is where it all goes wrong. I find with most things an initial test implementation is quick and gives you a feel for the problem, when you actually have to do the real thing you discover all kinds of creepy crawlies hiding under rocks. QtWebKit has now split out from Qt, but there is no packaging for this new branch that I could find under Ubuntu, not too much of an issue since I am used to packaging stuff up. I found HTML5 playback with the gstreamer Phonon backend simply did not work in any half decent fasion and they were concentrating on QtMultimedia which unfortunately is part of the development release.

The deal breaker was the speed of CSS animations, which I am lucky I actually got around to checking since I was juggling so many variables. It was unfeasibly slow. So I decided to use the new QtWebKit 2.0 as it contains compositing acceleration support for just this problem. Indeed, using raster or opengl graphics backends did speed up the animation to very smooth. What I then discovered was I could have smooth animations and no working Flash or rough animations and a kind of working Flash.

This was all most depressing, so I have gone back to WebkitGTK. It is only this crash issue I have to get to the bottom of but it only shows itself in one of my tests which is very specific, and I am thinking it is related to the way xlib is working in the nvidia driver. I do prefer GTK to Qt, so that is also good for me! I would have given EFL Webkit a go, but unfortunately they seem to have removed features in getting the functionality into the Webkit trunk.

 [1]: http://www.pyside.org/