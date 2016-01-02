Title: GUI Toolkits - Win32++
Date: 2007-02-10T14:35:00+00:00
Slug: gui-toolkits-win32
Category: 
Tags: 
Authors: Garry Bodsworth

<a href="http://users.bigpond.net.au/programming/">Win32++</a> is a GUI toolkit just for Windows.  It is a C++ toolkit providing abstraction from the base Win32 functionality, kind of like MFC, but written much better and more clearly.

It is a small toolkit that is a thin wrapper around the Win32 API.  It is not a drop-in replacement for anything else, but provides a simplified programming platform for beginners and intermediate programmers.

It provides facilities for MDI, rebars, toolbars, critical sections and more.  I suppose it must be relatively easy to expand the number of classes if you have greater requirements.  The advantage of this toolkit is that unlike MFC it works with the free compilers as MFC is only supplied with the professional versions of Visual Studio.  Customisation of existing classes is suggested via subclassing, which is the simplest conceptual way of adding functionality in C++.  With these classes you will not run into the problems with virtual destructors and the cobject derived class issues.

There are a variety of examples including a notepad program, some DirectX, some multithreading, and more.

The creator of this toolkit has written an article <a href="http://users.bigpond.net.au/programming/explanation.htm">Why Beginners Shouldn't use MFC</a>.