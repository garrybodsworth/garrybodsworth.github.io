Title: EASTL And Allocators
Date: 2007-09-10T20:51:00+00:00
Slug: eastl-and-allocators
Category: 
Tags: 
Authors: Garry Bodsworth

A few months back a document appeared on the Internet about <a href="http://www.open-std.org/jtc1/sc22/wg21/docs/papers/2007/n2271.html">EASTL</a>.  It details alterations to the STL that Electronic Arts implemented (as well as their own version of the STL) to meet its requirements for standard containers and algorithms.  It has been published on the <a href="http://www.open-std.org/jtc1/sc22/wg21/docs/papers/2007/n2363.html">C++ standardisation website</a> as a reference paper.

Some of the ideas in it are very interesting and some are a little naive and lack generality, but the document itself is thoroughly worth it.  The main thrust of the document is efficiency in terms of memory and speed.  This amounts to better allocators, better control of low-level memory (alignment and so on) and intrusive type containers.

It covers the deficiencies of std::allocator for EA's requirements like the copy semantics and the lack of alignment controls.  It has got me thinking there is a lack of a generic allocator framework that makes it easier for writing pluggable allocators that could be thread local, or global, or thread-safe, or instance-based.  But I'll come back to that later.

vector bool is not a bit-based array but there is an implementation of a bitvector that gives the same behaviour.  That makes sense to me!

The ability to resize a containers capacity to a smaller size and for the storage to respect that as most STL implementations do not do this.  Means memory can be returned back to the system.

Apparently the implementation is easy to debug through a simple debugger with no overhead.  I don't know whether that is the case in reality but it certainly has its appeal, but I'm sure it would make plenty of sense in open-source implementations meaning there would be more people able to contribute.

Apparently some compilers struggle with inlining so the implementation reduces code complexity to allow less able compilers to inline more.

A lot of the motivation behind this is cross-platform in nature and part of that is that the platforms can be limited in memory and processing power.  Some of the ideas brought up are possible in the current STL framework with some minor jumping through hoops, fortunately EA expended the manpower on implementing exactly what they want.

Now back to the allocators...  The ideas make <a href="http://www.ogre3d.org/phpBB2/viewtopic.php?t=27220&postdays=0&postorder=asc&highlight=eastl&start=25"></a>a lot of sense in this document and I wonder how many are available to coders from the current STL framework.  One thing that requires clarity is what the alignment needs in order to align, by this I mean is it easily determined from the type you are using or is it a combination of that and the machine type.  If so some of the work could be done via type traits like those available through Boost.

A lot of the allocator type suggestions do not even have an easy to use reference implementation in the open-source world.  Allocators are so important but there is a lack of availability of those apart from simple HOWTOs for writing allocators.

This has got me thinking about actually writing some.  Coming up with a good framework has lead me to reading big stacks of articles online about allocators, and I think there is a good way forward but 'll leave that to another post.

And there is some additional discussion on the Ogre forums <a href="http://www.ogre3d.org/phpBB2/viewtopic.php?t=35473&view=previous&sid=ce193664e1d3d7c4af509e6f4e2718c6">here</a> and <a href="http://www.ogre3d.org/phpBB2/viewtopic.php?p=225568&sid=ce193664e1d3d7c4af509e6f4e2718c6">here</a>.
