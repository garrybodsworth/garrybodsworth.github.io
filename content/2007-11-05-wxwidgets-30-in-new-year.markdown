Title: wxWidgets 3.0 In The New Year
Date: 2007-11-05T19:58:00+00:00
Slug: wxwidgets-30-in-new-year
Category: 
Tags: 
Authors: Garry Bodsworth

<div class='post'>
wxWidgets 3.0 will be released in 2008.  You can read some details <a href="http://wxwidgets.blogspot.com/2007/11/looking-forward-to-wxwidgets-3.html">here</a>.

Unfortunately (or fortunately depending on your viewpoint) this new major release will not be the radical rethink that has been mooted for the past couple of years.  The major feature will be the full integration of unicode which would be the only build type (as there was also an ANSI configuration).  This means that ANSI would get converted into unicode internally.  This new version will also require minimal changes to existing code to get it to compile.  I suppose people already working in unicode could potentially have no more upheaval than a point release.

This means all the plans which suggested the radical rethink for v3 have been moved under <a href="http://www.wxwidgets.org/wiki/index.php/Development:_wxTNG">wxTNG on the wiki</a>.  Certainly noone ever agreed on direction for this and this does mean there will be no compatibility issues.  Hopefully this means a gradual move to newer ideas rather than the complete redesign, which would be more likely to reap some results (eg, like improving the messaging framework would be one such thing).  Another avenue I reckon which would make more sense is to use current wx as a backend for a more experimental API.

Anyway it certainly is an extremely comprehensive framework with a liberal license unlike some other options, also the Python bindings in <a href="http://wxpython.org/">wxPython</a> are really very good
