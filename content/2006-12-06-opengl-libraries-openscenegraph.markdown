Title: OpenGL Libraries - OpenSceneGraph
Date: 2006-12-06T19:27:00+00:00
Slug: opengl-libraries-openscenegraph
Category: 
Tags: 
Authors: Garry Bodsworth

Since I spend a fair amount of time working with OpenGL I always take an interest in libraries that use it.  In fact a lot of game development libraries should really have applications outside of that domain, it is just that "professionals" see themselves as above using crude game development libraries.

One of the larger projects I have found really interesting is <a href="http://www.openscenegraph.org/">OpenSceneGraph</a>.  It is based on the idea of <a href="http://en.wikipedia.org/wiki/Scene_graph">scene graphs</a> which provides an object-oriented storage of the scene to aid rendering.

This library is quite a high level of abstraction away from the underlying rendering (although it will allow you access to it).  It provides cross platform support as well as 64 bit platforms.  It probably is seen not to have the shiny whizz-bang features that are more associated with the game dedicated libraries.  Nevertheless it scales really well and can produce some <a href="http://www.openscenegraph.org/osgwiki/pmwiki.php/Screenshots/Screenshots">stunning results</a>.  Most of the applications are more VR related but I am sure over time it will have more diverse applications.  I always winder how something like scene graphs would work in the land of CAD, although they are not really designed for that purpose.

Because it is OpenGL based it is really quite easy to create a view in your GUI toolkit using OpenSceneGraph, as normally they are constructed via the window handles.