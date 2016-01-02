Title: More STL - MCSTL and STXXL
Date: 2008-04-11T19:22:00+00:00
Slug: more-stl-mcstl-and-stxxl
Category: 
Tags: 
Authors: Garry Bodsworth

In a few previous posts I have mentioned some alternative STL implementations.  You can read about <a href="http://garrys-brain.blogspot.com/2008/03/stl-related-rdestl.html">rdestl here</a> as well as <a href="http://garrys-brain.blogspot.com/2008/03/more-stl-ustl-and-stdcxx.html">uSTL and stdcxx here</a>.

I've stumbled across a couple of other STL implementations for more specific purposes that I thought some people might find useful.

First up is <a href="http://algo2.iti.uni-karlsruhe.de/singler/mcstl/">MCSTL - The Multi-Core Standard Template Library</a> which is a multi-core implementation of certain STL algorithms.  This has actually been integrated into the GCC STL implementation with version 4.3.  It uses OpenMP internally for the multi-threading so would be limited to compilers with valid implementations of that functionality.

Next up there is <a href="http://stxxl.sourceforge.net/">STXXL: Standard Template Library for Extra Large Data Sets</a>.  I think the blurb sums it up:
<blockquote>The core of STXXL is an implementation of the C++ standard template library STL for external memory (out-of-core) computations, i.e., STXXL implements containers and algorithms that can process huge volumes of data that only fit on disks. While the compatibility to the STL supports ease of use and compatibility with existing applications, another design priority is high performance.</blockquote>After seeing some extra long and large computations on huge data sets this can be used to get around limitations of the platform with less addressable space.
