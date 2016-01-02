Title: OpenGL - The OpenGL Window Framework
Date: 2006-12-06T20:48:00+00:00
Slug: opengl-opengl-window-framework
Category: 
Tags: 
Authors: Garry Bodsworth

During numerous hours of websurfing I stumbled across the <a href="http://oglwfw.sourceforge.net">OpenGL Window Framework</a>.  This is a thin layer on top of OpenGL to make extra nice for C++ developers.  Unfortunately it does not seem to be actively developed.

What it provides is a nice C++ interface for OpenGL with respect for making window contexts.  It gives you access to extensions via the <a href="http://elf-stone.com/glee.php">Glee</a> library.  It gives you an enumeration framework for modes and features, and also there are design considerations for multi-threaded programming which is important in this day and age.

It's a very tightly focussed library designed for making using OpenGL and creating the windows for it much easier, and it seems to do that pretty well.
