Title: Windows Vista and MDI Applications
Date: 2006-11-20T21:38:00+00:00
Slug: windows-vista-and-mdi-applications
Category: 
Tags: 
Authors: Garry Bodsworth

If you have an MDI application and you are going to run it under Windows Vista you could be in trouble.  I mean the MDI applications that have multiple windows and are not tabbed.  The child windows you will notice are rendered with Windows Basic even in a fully composited theme.

Probably where I should start is the "Desktop Window Manager" or in your Task Manager dwm.exe.  This is what does the Window effects, so it is not a massive re-architecture but another application providing the extra rendering effects.  This applies the effects to the main window of your application via your graphics card.

Now this leads into the MDI problem.  An MDI application hosts multiple windows inside one main window.  The dwm.exe provides the rendering capabilities for your main Windows, not your child windows.  This is where the problem lies, your child windows will be rendered with Aero Basic and hence look out of place in a full Aero desktop.

Unfortunately this will make your application look a bit messy and inconsistent.  There is no solution as far as I can tell so far, although I am dedicated to finding an answer.  By far the simplest answer would be to make it a tabbed user interface, although this may not suit some applications.

Hopefully I can find some sort of answer soon.
