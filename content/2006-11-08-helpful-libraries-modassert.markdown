Title: Helpful Libraries - ModAssert
Date: 2006-11-08T20:50:00+00:00
Slug: helpful-libraries-modassert
Category: 
Tags: 
Authors: Garry Bodsworth

Anyone who has programmed in MFC and ATL will have encountered the ASSERT macro.  Due to it being rather simplistic and essentially a one-size-fits-all.

I was pleased to see someone has developed a very comprehensive assertion library which makes it into a really useful debugging tool.  I first encountered the project with <a href="http://www.codeproject.com/library/ModAssert.asp">this article on CodeProject</a>.  It allows compile time disabling/compiling out, and also run time diabling.  It also provides levels to give a granularity to your debug output.  Also you can use it to output log information which can be invaluable for debugging (with lots of useful information like threads and so on).

The library is fairly large and comprehensive, but since you should compile it out for your final release build it isn't really a problem at all.  It certainly should be useful for C++ developers.

The Sourceforge Project is <a href="http://sourceforge.net/projects/modassert/">here</a>.
