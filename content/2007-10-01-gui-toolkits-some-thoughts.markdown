Title: GUI Toolkits - Some thoughts
Date: 2007-10-01T18:57:00+00:00
Slug: gui-toolkits-some-thoughts
Category: 
Tags: 
Authors: Garry Bodsworth

I mentioned a couple of posts back that I was going to put some thought into GUI subjects and maybe trying out writing a simple toolkit.

I was thinking abut which way to jump with trying to write a toolkit.  First of all what should it be based on?  Should it just wrap Win32?  Cocoa?  Should it be entirely implemented on top of OpenGL from scratch?  Should it be cross-platform in design?  Just these questions could cause anyone to run away screaming.

Thinking about building it on top of OpenGL I encountered a couple of interesting GUI libraries <a href="http://glui.sourceforge.net/">GLUI</a> and <a href="http://glow.sourceforge.net/">GLOW</a>.  In these projects the windows are completely rendered by OpenGL which is an interesting approach.  I suppose <a href="http://www.rawmaterialsoftware.com/juce/">Juce</a> is built from similar roots as well where it implements its own toolkits.

I was thinking about writing a nice C++ wrapper for Win32 but then I started to think even Microsoft products don't use the standard widget rendering.  Then you start to think about built in custom drawn widget rendering, then you think why are you using standard widgets...

The whole idea about implementing a simple GUI toolkit is an education about the design decisions and pitfalls that you can get into.  You also need to decide which subset you decide to implement first.  The problem is most toolkits go for the same 10% and that is normally as far as they get.

The main idea I want to try out for an experimental GUI toolkit is some DSL (domain specific language).  What I mean is embedding a language in C++ in order to implement the user interface in a readable fashion.  It is certainly possible using modern C++ idioms as demonstrated in Boost.  I suppose the type of thing I want to do is (in some kid of C++ like pseudo code):
<pre>
dialog(...) +
widget<static>("Number", sizeX, sizeY) | widget<edit>(RESIZE_X) ||
widget<static>("Name", sizeX, sizeY)   | widget<edit>(RESIZE_X) ||
widget<list>("Blah", sizeX, sizeY, RESIZE_XY)
;
toolbar() +
button("image1", ...) |
button("image2", ...) |
separator() |
button("image3", ...) |
button("image4", ...)
;
</pre>
Complete and utter insanity?  Probably, but could be fun to try out.  It would certainly be something different and would create a parallel in your source in comparison to what you would see on screen.  I don't think anything quit like it has been tried before, so feel free to steal the idea - it would save me implementing it(!)

Enough rambling for today I think...
