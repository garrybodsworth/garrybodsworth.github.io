Title: Boost Python
Date: 2006-10-06T13:04:00+00:00
Slug: boost-python
Category: 
Tags: 
Authors: Garry Bodsworth

A few posts ago I wrote up how to compile the Boost Library and also Boost::Python with Visual C++ 2005 Express.

Boost::Python is a fantastic tool for binding your C++ functionality to the Python scripting language.  You just need to write some extra small templates to expose classes, functions and so on.

One of the things that bothered me about Boost Python is the need to use <span style="font-style:italic;">bjam</span> to build the resulting <span style="font-style:italic;">.pyd</span> file.  It complicates it all quite a lot, especially if you have not been using bjam.exe to compile your project anyway...

What I discovered with a little bit of experimentation is that the PYD file is just a DLL renamed(!)  And that seems to be it.  So if you compile your program into a DLL (with all the additional Boost::Python code) then you either change the extension or change the project settings for the output filename.
