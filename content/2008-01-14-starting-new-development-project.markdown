Title: Starting A New Development Project
Date: 2008-01-14T21:22:00+00:00
Slug: starting-new-development-project
Category: 
Tags: 
Authors: Garry Bodsworth

With all the tools out there to make developer's lives easier, what would I do when starting a new project.  When starting a new development project the initial decisions you make reflect throughout the life of the codebase because once the ship is in sail it is hard to change direction without real willingness.

There are really two areas that this would cover, first the tools you use, and then how you use those tools.

Lets say that you are developing on Windows.  You would use Visual Studio instinctively, unfortunately the build system sucks in the worst way when it comes to project dependencies and command-line operations. You could use something like CMake or bjam or any one of the other build systems available.  The problem then is that the features always lag behind what is available within the IDE.

But I am going off on a tangent.  I am deciding on a development environment for a new project (C++).  Right then what could we use that is more or less free...
* Source control : Subversion
    The main reason to use this is that there are so many tools available (most specifically TortoiseSVN).
* Bug tracking : Trac
    I would rather a more powerful bug tracking system (I am a big fan of Bugzilla) but the tight integration with Subversion is a major plus point.  Plus you get a wiki for free, and with the plug-ins you can have continuous integration and a myriad of other things integrated in one Intranet website.
* Compiler : Visual Studio
    This means you can support 32 and 64-bit (which MinGW sadly lacks at the moment) targets.
* Continuous Integration : Cruise Control.NET
    Regular builds make sure that you haven't gone too far down the wrong path.  It can also be used to do other processes like testing or analysis.  You can integrate it with Trac as well here http://syntactic.org/2007/7/23/cruisecontrol-net-trac-integration or here https://oss.werkbold.de/trac-cc/.
* Wiki : Trac
    Developer documentation should be quick and easy to edit and should be encourages.  It's good news it is also part of Trac.
* Unit testing : Boost
    Using Boost in a C++ project makes perfect sense, so using their unit testing framework would therefore be a good idea.  It can be difficult to drive but other C++ unit testing frameworks are as much a pain so rolling your own could also be an idea.
* Batch testing : Python
    Python scripting would be a good idea for doing actual system testing.  What would be even better is the ability to run the program due to Python being embedded in the program to drive it.  Get the output well formed and I think it can be integrated with Trac as well.

When you start:
* All commits must have a comment and preferably a bug number so you can always work out the reasoning behind all edits.  Being able to work out why is always useful to a developer.
* Compile with the warning levels on the maximum available level and have warnings as errors.
* Try to use some static analysis like Lint to improve the baseline coe quality.

By building in high standards in the beginning you don't have to go through laborious and error-prone tasks later in the day retrofitting some standard process.  Also, I like the idea of having Trac as a port of call or documentation, source code, and analysis means as a developer you can't complain any of the process is too difficult.

I've probably left out loads but its a start at least...
