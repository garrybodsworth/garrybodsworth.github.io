Title: Microsoft STL Performance
Date: 2008-04-13T20:28:00+00:00
Slug: microsoft-stl-performance
Category: 
Tags: 
Authors: Garry Bodsworth

On the <a href="http://www.boost.org">Boost</a> discussion group there is a discussion started about <a href="http://www.nabble.com/High-Cost-of-MS-"Safe"-STL-for-Release-Builds-td16642449.html#a16642449">High Cost of MS "Safe" STL for Release Builds</a>.  It is an interesting look at the massive differences between "safe" and "non-safe" options in Microsoft STL.

I don't think there has been a clear look at the efficiencies and inefficiencies in the MS-STL implementation, especially with the different options (iterator debugging and safe options).  There have been some looks at comparing different STL implementations but it always difficult to do a good comparison, the main problem being comparing the correct "latest versions".

Going back a while I was justifying the use of <a href="http://stlport.sourceforge.net/">STLPort</a> instead of Microsoft STL supplied with Visual Studio.  Simply, it was a performance thing with both memory and efficiency.  Certainly with the new STLPort visualisers for the Microsoft debugger it is an even playing field for ease of use.

You can read those here:
* <a href="http://garrys-brain.blogspot.com/2006/10/visual-studio-2005-lets-break.html">Visual Studio 2005 - Lets Break Everything!</a> - a bit about how to switch off some of the more annoying "features".
* <a href="http://garrys-brain.blogspot.com/2007/01/development-stlport-versus-microsoft.html">Development - STLPort versus Microsoft STL performance</a> - A quick summary of my observations on the performance in a real-world complex application.
* <a href="http://garrys-brain.blogspot.com/2007/01/more-on-stlport-and-microsoft-stl.html">More on STLPort and Microsoft STL performance</a> - A little more background.
