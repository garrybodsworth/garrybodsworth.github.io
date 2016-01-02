Title: Vista and system RAM
Date: 2007-03-01T19:26:00+00:00
Slug: vista-and-system-ram
Category: 
Tags: 
Authors: Garry Bodsworth

There is an article <a href="http://www.codinghorror.com/blog/archives/000688.html">here</a> about how Vista handles system memory.  It is called "Why does Vista use all my memory" by Jeff Atwood.

Essentially all system memory is now considered a cache (using a system called SuperFetch).  This means that the amount of memory used would be as much RAM as is available to cache from the hard-drive.

I don't know if I am completely sure it is a good idea because if a program requires a lot of memory then it has the initial lag to clear the cache in order to service memory requests.  Maybe as time goes on the technology will get better, so it may be more usable in the future.
