Title: Interesting stuff - GPU general programming
Date: 2008-01-30T20:17:00+00:00
Slug: interesting-stuff-gpu-general
Category: 
Tags: 
Authors: Garry Bodsworth

An interesting library I stumbled across on the Internet the other day enables the user to accelerate general code by using your graphics hardware.  An open-source library <a href="http://libsh.org/">libsh</a> provides a high level metaprogramming language in C++ for programming GPUs.

Unfortunately, libsh is no longer actively developed because the developers behind it have created a commercial business around it (those lucky guys have found a way to make programming pay!)

It would be nice to utilise the processing power of the GPU, essentially treating the hardware like another (more specialised) processing core.  After all graphics cards have more transistors than the average CPU...  I think I mentioned something like this in my <a href="http://garrys-brain.blogspot.com/2006/12/multiple-core-madness.html">multithreading post</a> many a moon ago.  But I suppose also it ties into virtualisation of the procesing hardware available on the computer which I even <a href="http://garrys-brain.blogspot.com/2007/10/virtualisation-understanding.html">posted about before</a>.

A great website for this type of stuff is <a href="http://www.gpgpu.org/">General-Purpose Computation Using Graphics Hardware</a> which does exactly what it says on the tin.  There are active forums and tons of news and information.

Surprisingly there is not a huge amount of general purpose stuff out there freely available but as GPUs become more powerful and more programmable I am sure that will change.  Personally I think the future would be to use a core of these multi-core processors to do the graphics, even if it is slightly specialised for stream processing or something.  That would certainly negate the need for faster graphics buses as it would run on the processor (although other buses would still need to progress).  But yet again I have digressed....
