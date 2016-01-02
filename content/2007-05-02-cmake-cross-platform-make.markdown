Title: CMake - Cross-Platform Make
Date: 2007-05-02T19:55:00+00:00
Slug: cmake-cross-platform-make
Category: 
Tags: 
Authors: Garry Bodsworth

<a href="http://www.cmake.org">CMake</a> is a cross-platform make system that seems to be gaining a large following.  It is simple to write the make definitions and the program can create platform specific builds including Visual Studio.NET project and solution files.  There is a nice Wikipedia article <a href="http://en.wikipedia.org/wiki/CMake">here</a>.

Recently KDE successfully <a href="http://lwn.net/Articles/188693/">transitioned to the new build system</a> relatively painlessly, when the previous system was essentially unmaintainable.

It provides support even for <a href="http://www.swig.org/">SWIG</a> - the Simple Wrapper Interface Generator.  Which is interesting from a library standpoint.

There are hooks for testing regimes available from the main website.

Admittedly from the Visual Studio viewpoint it would probably be a hard sell to others.  The main problem I have with Visual Studio is that it screws with the vcproj files massively on seemingly innocuous edits.  At least then you have complete control of your build environment without worrying everything getting altered due to GUI edits.
