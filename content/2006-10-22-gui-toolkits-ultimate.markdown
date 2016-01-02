Title: GUI Toolkits - Ultimate++
Date: 2006-10-22T15:25:00+00:00
Slug: gui-toolkits-ultimate
Category: 
Tags: 
Authors: Garry Bodsworth

This is a fairly new toolkit on the scene, but that doesn't make it particularly lacking.  I have been scouring the Internet for unbiased reviews of most toolkits before downloading them and it is seriously hard to find them.

<a href="http://upp.sourceforge.net/">Ultimate++</a> is more than just a GUI toolkit (in fact I could probably say that about every single one I have looked at), it has an IDE, a build system, a visual designer, code-completion, code documentation, and its own standard library.  As a compiler back-end it can use <a href="http://www.mingw.org">Mingw</a>, Visual Studio Toolkit 2003, and <a href="http://msdn.microsoft.com/vstudio/express/">Visual C++ 2005 Express</a>.

It seems that you are unable to use your IDE of choice as Ultimate++ is more of a platform than simply a library.  TheIDE does allow you to simplify starting up development in Ultimate++ since you don't have to worry too much about environmental setup and they don't have to support multiple IDEs.  TheIDE is OK as a development environment, it lacks a plug-in framework that I could find but it does have a macro language.  This means integration of external development tools seems difficult which I find useful.

The basis of Ultimate++ is the NTL which is a replacement for STL due to their perceived deficiencies for the project.  I honestly can't say if it is a giant leap forward or reinventing the wheel, I've heard these arguments in the past that turn out to be null and void.

But on to the most interesting part - the actual GUI Toolkit.  It has a fairly modest collection of widgets, not as deep as more mature toolkits.  I have noticed it is possible to get a fair amount of flicker from the projects when resizing and a simple solution didn't immediately present itself.

The user interface is not actually built on the common controls of the operating system, but is custom drawn, and as such in previous versions did not match the widgets of the underlying system in all cases.  This has improved massively recently (gone away completely I believe) thanks to a new Chameleon theming engine that uses the operating system UI theming engine (uxtheme on Windows).

What I feel about Ultimate++ is that it is a decent new stab at something a little different to the other UI libraries by making it more of a platform.  I don't think it is ready if you are evaluating it for use in a big application.

For me when I read <span style="font-style:italic;">"Rapid development is achieved by the smart and aggressive use of C++ rather than through fancy code generators"</span> I thought it was interesting, but I always take this kind of stuff with a pinch of salt.  The code although shorter in a manner of speaking I don't think is any more readable, and doesn't really show any reduction in programmer thought or time (if you are comparing to more modern toolkits).

The activity of the community seems fairly large, so they may be able to add functionality faster than other toolkits.  You can check out a fairly in-depth <a href="http://www.codeproject.com/useritems/IntroUpp.asp">getting started tutorial on the CodeProject</a>.