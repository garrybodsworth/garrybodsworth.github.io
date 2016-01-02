Title: Intel Open-Sources Threading Bulding Blocks
Date: 2007-07-25T20:44:00+00:00
Slug: intel-open-sources-threading-bulding
Category: 
Tags: 
Authors: Garry Bodsworth

Intel has just <a href="http://threadingbuildingblocks.org/">open-sourced their Threading Building Blocks library</a>.  Intel describe it as a "rich and complete approach to expressing parallelism in a C++ program".

With multi-threading in general being so immature when looking at other libraries, another solution can never hurt.  So add it to Boost.Threads, OpenMP, wxThread and the myriad of others.  Admittedly the way that all of the alternatives work is very low-level and means very careful design is required.

I'm interested to see the approach of the library to multi-threading as it looks quite complicated to wrap your head around.  The best bit though is there is apparently a cache aligned memory allocator as part of it that can be used independently.

There is a Slashdot article about it <a href="http://developers.slashdot.org/developers/07/07/25/1324221.shtml">here</a>.  Also a bog post <a href="http://softwareblogs.intel.com/2006/12/18/threading-building-blocks-solution-looking-for-a-problem/">here</a> looks interesting covering the subject.

All I can say is let battle commence and lets see what multi-threading packages are left standing ;)
