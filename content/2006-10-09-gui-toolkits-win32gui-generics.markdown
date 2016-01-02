Title: GUI Toolkits - Win32GUI Generics
Date: 2006-10-09T21:37:00+00:00
Slug: gui-toolkits-win32gui-generics
Category: 
Tags: 
Authors: Garry Bodsworth

<a href="http://www.torjo.com/win32gui/">Win32GUI Generics Homepage</a>

When I found this project I thought I had found the holy grail.  An advanced use of C++ for user interface purposes.  I looked past the screenshots on the website which seemed odd, but downloaded it anyway.  The last release of the project and any active development was nearly a year ago.

It certainly pressed all the right buttons for me.  It was a wrapper for the Win32 API with aspirations to be cross-platform.  I encountered my first set of problems when I tried to get it to compile, you shouldn't use the solution files for Visual Studio.  There is a "build library" utility that works with Visual C++ 8.0.  I got a few examples up and running with minor project file tweaks like include directories, and found that custom draw buttons were not XP themed so I hacked in a small theming API.

All seems okay so far.  The biggest problem I found was the resizing, it caused massive amounts of flicker.  Having solved a lot of similar problems in MFC I tried to get it to flicker less with no success.  Then attempting lots of other examples I found they simply crashed or would not compile.  Most disappointing was I could not have a look at the new "Surfaces" version of the library.

The compiled size of the library is massive with large amounts of global static data.  I found building a bit pot-luck.  I had to configure the Boost Jam files to not use iterator debugging or safe iterators.

The thing is I really like this library and it seems really powerful, but simultaneously lacks a little robustness.  There is a lot of work to be done on this library to make it ready for the primetime which is really unfortunate.  John Torjo definitely deserves a pint of beer for fantastic and thought provoking work.

There is a great little article about it <a href="http://blog.davber.com/2006/07/10/win32-for-real-c-developers/">here</a>.
