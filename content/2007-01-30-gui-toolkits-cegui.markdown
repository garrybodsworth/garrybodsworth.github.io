Title: GUI Toolkits - CEGUI
Date: 2007-01-30T22:43:00+00:00
Slug: gui-toolkits-cegui
Category: 
Tags: 
Authors: Garry Bodsworth

<a href="http://www.cegui.org.uk">CEGUI or Crazy Eddie's GUI System</a> is not a typical GUI toolkit.  It is designed primarily for gamers to embed a GUI interface into graphics windows (normally in order to use this they would be fullscreen or you would use the platform toolkit).<br /><br />The GUI toolkit itself has backends for DirectX 8.1 & 9, <a href="http://www.opengl.org">OpenGL</a>, <a href="http://www.ogre3d.org/">OGRE</a> and <a href="http://irrlicht.sourceforge.net/">Irrlicht</a>.  This allows you to then overlay GUI elements into your program window.  The advantage of being self-rendering is that it is then cross platform.  Currently it supports Linux and Windows and Mac OSX support is on its way.  The nature of the renderer backend means it would be trivial to use it in something like <a href="http://www.openscenegraph.org">OpenSceneGraph</a>.<br /><br />With the theming ability of the engine it is possible to use this toolkit as your start screen menus for games or even more.<br /><br />The toolkit itself is written in object-oriented C++ and looks really quite clean from the examples.  For its niche it really doesn't have masses of competition, but it does not preclude it from being and impressive solution.