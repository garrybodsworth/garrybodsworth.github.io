Title: Windows Vista and its API
Date: 2006-10-04T14:47:00+00:00
Slug: windows-vista-and-its-api
Category: 
Tags: 
Authors: Garry Bodsworth
Summary: 

After lots of uncertainty with Windows Vista as a developer (it's sad, I worry about such things), I breathed a huge sigh of relief today.  Windows Vista has generated such things as WPF and Aero and other things that mean very little to me as a developer.  Simply, I want to know how to access all the good stuff.

This had me worried as they seem to want to make non-managed code a ghetto, but this is mainly from reading allt he public information and marketing.  It seems that the Win32 is still the basis of everything, although the name Win32 is ultimately misleading.  To cut to the chase, .NET sits on top of Win32, even in Vista, and you still have access to it.

There is a great little article on the <a href="http://www.codeproject.com/winfx/VGGlassIntro.asp">CodeProject</a> that shows that you can write in what are now called the "Native APIs".  Hit the link and have a quick read.

I find this exciting as a developer as this means that I can write my own wrappers for stuff and extend those wrappers I have written previously.

Now I'm in the middle of downloading the <a href="http://www.microsoft.com/downloads/details.aspx?FamilyId=117ECFD3-98AD-4D67-87D2-E95A8407FA86&displaylang=en">new Windows SDK for Vista</a> and I am going to have a closer look at the native APIs in order to work out what it can do.
