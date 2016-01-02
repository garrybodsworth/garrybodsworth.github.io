Title: More STL - uSTL and stdcxx
Date: 2008-03-05T19:34:00+00:00
Slug: more-stl-ustl-and-stdcxx
Category: 
Tags: 
Authors: Garry Bodsworth

Thanks to a commenter on the <a href="http://garrys-brain.blogspot.com/2008/03/stl-related-rdestl.html">RDESTL post</a> I made yesterday, they pointed me at the <a href="http://ustl.sourceforge.net/">uSTL</a> (I assume pronounced micro-STL).

It is a partial implementation of the STL specification.  It reduces code size by making memory allocation a non-templated base class.  As far as I can tell this reduces executable size because of less template bloat.  Whether it is faster or smaller in memory for the containers is another matter.  I suppose by reducing the executable size  cache coherency could be improved leading to some interesting speed-ups.

It is for POSIX-based systems, and there is no maintained Windows port (a choice of the developer) although some peole have got it to work on Windows with differing levels of success.

And another STL implementation I stumbled across is the <a href="http://stdcxx.apache.org/">Apache stdcxx</a>.  The project was started from a code donation by Rogue Wave who decided to open-source their commercial offering.

At the end of 2007 stdcxx made it to an Apache Top-Level Project which means it should be well supported.  And apparently performance s quite good as well.
