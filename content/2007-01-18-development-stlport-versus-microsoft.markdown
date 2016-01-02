Title: Development - STLPort versus Microsoft STL performance
Date: 2007-01-18T18:59:00+00:00
Slug: development-stlport-versus-microsoft
Category: 
Tags: 
Authors: Garry Bodsworth

The product I work on uses STL in quite an aggressive way and also it permeates all of the source code, so any change to the performance of it can have very severe knock-on effects.

We upgraded to Visual Studio .NET 2005 from Visual Studio .NET 2003 with <a href="http://stlport.sourceforge.net/">STLPort</a> 4.6.  We decided to make the switch to Microsoft STL which in coding terms was very simple.  This slowed the entire system down massively, especially in debug mode.  I covered in <a href="http://garrys-brain.blogspot.com/2006/10/visual-studio-2005-lets-break.html">a previous post</a> how to gain back some of the performance.  This speeds up the STL by a massive amount as the safe iterator and iterator checking have large overheads.

In comparison to STLport the performance in debug is so much slower that it is completely unusable for anything beyond the most simple operations.

In release mode the performance is not quite as bad.  For one of our large tests it takes approximately 30000 seconds with our old build system.  With the Microsoft STL with all the possible performance improvements possible the tests took over 36000 seconds to run.  The performance degradation was unacceptable.  It was not only the time but memory as well, with the large data sets we use this causes massive amounts of paging to hard drive.  The Microsoft STL uses about 50% more memory than STLport.

Unfortunately STLport is not as easy to debug as the Microsoft implementation is coupled with the debugger.  But the performance degradation is simply too much to ignore.

The current version of <a href="http://stlport.sourceforge.net/">STLport is 5.1</a> and works with loads of compilers and platforms.
