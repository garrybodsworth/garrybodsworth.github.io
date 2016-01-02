Title: Google Chrome &#8211; Technical Stuff
Date: 2008-09-06T09:00:00+00:00
Category: 
Tags: 
Authors: Garry Bodsworth

The coverage around Google Chrome hasn&#8217;t died down very much since its release, which is interesting in itself, but the coverage is starting to get more technical and taking it apart.

The post [&#8220;Code Reuse in Google Chrome Browser&#8221;][1] looks at al the external libraries used in Google Chrome. Apart from the obvious libraries WebKit and the new Javascript engine V8, there are some more interesting ones. Apparently it uses [WTL][2] for the GUI, which was a Microsoft originated GUI toolkit (with lots of excellent extensions) that ended up becoming open-source. It&#8217;s a very good toolkit for windows and developing for it is relatively painless but it is an interesting choice. Also there is Skia which is a vector graphics engine that is used for the rendering, apparently from an acquisition a few years back.

Alp Toker has blogged a little more in-depth about [&#8220;Skia graphics library in Chrome: First impressions&#8221;][3] with some interesting insights along with some code.

Wired Magazine also have an article [&#8220;Inside Chrome: The Secret Project to Crush IE and Remake the Web&#8221;][4] proving that the PR and technical launch have been very successful.

 [1]: http://www.catonmat.net/blog/code-reuse-in-google-chrome-browser/
 [2]: http://wtl.sourceforge.net/
 [3]: http://www.atoker.com/blog/2008/09/06/skia-graphics-library-in-chrome-first-impressions/
 [4]: http://www.wired.com/techbiz/it/magazine/16-10/mf_chrome?currentPage=all