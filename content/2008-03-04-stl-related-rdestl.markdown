Title: STL-related : rdestl
Date: 2008-03-04T20:16:00+00:00
Slug: stl-related-rdestl
Category: 
Tags: 
Authors: Garry Bodsworth

A while back I <a href="http://garrys-brain.blogspot.com/2007/09/eastl-and-allocators.html">blogged</a> about the <a href="http://www.open-std.org/jtc1/sc22/wg21/docs/papers/2007/n2271.html">EASTL</a> - Electronic Arts Standard Template Library.

It is an interesting look at how EA have internally implemented their own STL with their own improvements/changes specific to their problem domain.

<a href="http://msinilo.pl/blog/">Maciej Sinilo</a> has spent some time putting together a small subset of the STL changed for some game development requirements called the <a href="http://code.google.com/p/rdestl/">RDESTL</a>.  The related blog posts can be read <a href="http://msinilo.pl/blog/?p=25">here</a>, <a href="http://msinilo.pl/blog/?p=28">here</a> and <a href="http://msinilo.pl/blog/?p=33">here</a>.  It provides some basic containers (vector, etc), a string class, and some additional container types like intrusive containers.  It also provides the EASTL outlook on allocators (which I don't agree with but that is another story).

It is definitely interesting to see the code as it is quite readable.  I do wonder whether it achieved part of the EASTL goal which was allowing the compiler to optimise more aggressively because the code is simpler with less indirection.

Also, here is a <a href="http://www.spreetree.net/blog/?p=7">link</a> to someone else who is replacing the STL.  Link via the excellent <a href="http://warpedvisions.org/">warpedvisions</a> (with an excellent biting comment).
