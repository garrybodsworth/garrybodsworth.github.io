---
title: Long-Lived Processes
author: Garry Bodsworth
layout: post
aktt_notify_twitter:
  - yes
aktt_tweeted:
  - 1
categories:
  - Uncategorized
tags:
  - development
---
One of the things about developing a [digital signage system][1] is that the software running the display has to run for a long period of time. From what I have heard some people set their digital signage players (from other companies) to reboot every night which is an odd state of affairs, whereas we just say plug it in and switch it on. That does not mean we are infallible and I am constantly hunting down strange behaviours in the long-lived process.

What I have really found from the reality of having real operating systems out there in the big wide world is that you will always encounter that which you cannot predict. There is however a way to mitigate the risk. You need to take a leaf out of the server world. Your main process should be as simple as possible doing the absolute minimum, then spawn processes to do the donkey work.

The advantage of this is that if anything does go wrong in the real hard work then when the process is closed or is aggressively killed the resources are returned back to the system. In Linux this is particularly good because it is really good at starting processes efficiently. I saw evidence of this when git was spawning lots of perl processes, which in Windows was a lot slower, meaning that git in Linux on a VM in Windows was much faster than on plain Windows.

Even Python has a built-in multiprocessing library (which was really put in place to get around the GIL issues) but it gives a great framework for managing processes and inter-process-communication. This is available from 2.6 up and I must get around to porting more stuff to it rather than rolling my own.

Another great feature of the Linux graphics stack is texture from pixmap so that you can have out-of-process rendering and composite it all together in OpenGL.

Really the lesson I learnt by forgetting to not put something into a separate process is that the unimaginable will happen, from bizarre corruptions, to parsers that should fail but are just too robust, which then means you have memory hanging around forever.

 [1]: http://www.camvine.com/