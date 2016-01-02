Title: GUI Toolkits - wxWidgets
Date: 2006-10-10T14:45:00+00:00
Slug: gui-toolkits-wxwidgets
Category: 
Tags: 
Authors: Garry Bodsworth

<a href="http://www.wxwidgets.org">wxWidgets</a> is the 800lb gorilla in the open source GUI toolkit arena.  It goes well beyond being simply about the GUI and spreads into all areas of application development, from networking to database to threading to strings.

It isn't such a large leap from MFC to wxWidgets.  They are born from the design of macros and simple classes, and this is not as large a problem as sometimes it is made out to be, some people find it easier, some find it harder.

By far the easiest way to get up and running is to use <a href="http://wxpack.sourceforge.net/">wxPack</a> if you are using Visual Studio, or give <a href="http://www.codeblocks.org">Code::Blocks</a> a try.

The sheer breadth and depth of the project is amazing, and it keeps spreading further with more and more contributions.  What I have noticed over the past year is that it has really started to take off with millions of additions like wxAUI (docking toolkit), wxFlatNoteBook (a tab control window container like Visual Studio has), wxPDFDocument, wxSQLite3, and in the past few days wxSkin (a potential skinning package).  The website is also much better with a <a href="http://wiki.wxwidgets.org/">wiki</a>, a <a href="http://wxforum.shadonet.com/">forum</a>, and this week a <a href="http://wxwidgets.blogspot.com/">blog</a>.  Google Summer of Code seems to have been a success for wxWidgets as well.

I certainly have had some success with it writing a test program embedding an <a href="http://www.ogre3d.org">Ogre</a> rendering context into a docking user interface to try out wxAUI.  It looked impressive although didn't accomplish much...

Before making this post too long I will go into more depth in wxWidgets another time.