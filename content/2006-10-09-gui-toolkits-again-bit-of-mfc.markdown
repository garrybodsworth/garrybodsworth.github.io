Title: GUI Toolkits Again - a bit of MFC
Date: 2006-10-09T19:58:00+00:00
Slug: gui-toolkits-again-bit-of-mfc
Category: 
Tags: 
Authors: Garry Bodsworth

At work, I only use MFC and the antiquated design features in Visual Studio for working on resources.  These interfaces still feel like they haven't moved on for a lifetime (and are in fact pretty much unchanged from Visual Studio 6.0).

The most annoying part about working with the resources is I have to resort to handcoding most of the time.  It is especially necessary in order to follow the <a href="http://msdn.microsoft.com/library/default.asp?url=/library/en-us/dnwue/html/ch14e.asp">Official Guidelines for User Interface Developers and Designers</a> (self-inflicted myself, but you need some level of consistency).  Also the IDE design features have an uncanny knack for orphaned <span style="font-style:italic;">#defines</span> and controls.

MFC doesn't really feel like an API as most of the stuff I want to do I end up having to subclass and write lots of specific code.  There are subclasses for just about every type of control, and in that a lot of it is direct access to the Win32 API.

I must admit that I don't have an intense hatred for MFC like a lot of developers.  It seems to serve its purpose well, and there are so many extensions and large applications built on it.  I don't think Microsoft envisioned being unable to kill it off because it is used by too many applications.  It will still be developed and have some new "managed" features which strikes me as odd...  MFC is a thin wrapper around the Win32 API, but .NET is a wrapper around the Win32 API, so there would be a double level of indirection for these new features.

A lot of people would love to migrate away from MFC, but they are too integrally tied into their applications.  The cause of that is normally the initial codebase grew from a small code-generated wizard application.  I know I would love to do move away from MFC, but it is first necessary to find a new GUI toolkit that is capable of doing every feature you have probably handcoded in extensions to MFC, or if you have to write the extensions yourself it is no more difficult to do than the first time you wrote it.

That is part of the reason to really look in depth at GUI toolkits.  It is really necessary to find one that will allow the most active development by the virtue of being easy to pick up.  Also, the grass is not always greener on the other side.