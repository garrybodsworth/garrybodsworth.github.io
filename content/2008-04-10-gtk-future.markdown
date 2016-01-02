Title: GTK+  The Future
Date: 2008-04-10T18:03:00+00:00
Slug: gtk-future
Category: 
Tags: 
Authors: Garry Bodsworth

Lots of information has been revealed recently about possible future directions for GTK+.  There is a comprehensive article on <a href="http://arstechnica.com/articles/culture/reinventing-gtk.ars">ArsTechnica here</a>.

Imendio, one of the active developers of GTK+ made a recent presentation you can see <a href="http://developer.imendio.com/sites/developer.imendio.com/files/gtk-hackfest-berlin2008.pdf">here</a>.  This outlines what they see as the future direction and release plans for GTK+ in the future, with more detail available in the <a href="http://developer.imendio.com/sites/developer.imendio.com/files/imendio-gtk-vision.pdf">position document</a>.  Essentially it involves taking it forward by having a clear roadmap to break the ABI which has been stable for a long time, but has limited leaps forward in development.

<a href="http://ometer.com/">Havoc Pennington</a> had a proposal also, this is available <a href="http://docs.google.com/Present?docid=dgn6j4pg_50dw7wh6vt#0">here</a>.  His proposal did not necessarily overlap the Imendio one but involved using a scenegraph API for defining the UI.  He also suggests looking at the OpenGL based <a href="http://www.clutter-project.org/">Clutter</a> which uses a GObject API for its rich user interface experience.

Some additional experimentation has been made with <a href="http://arstechnica.com/news.ars/post/20071028-making-linux-application-user-interfaces-richer-with-opengl.html">integrating OpenGL with GTK+</a>.  A lot of work has been done to try and keep GTK+ up to date with theming and transparency but it can look off the pace especially when attempting to mimic the look of a native platform.  Hopefully all these changes will improve the situation on push the GUI even further since Windows development tools seem to be pushing the "every application looks different" paradigm, Apple making iTunes look the same on all platforms and applications like Songbird using the same theme on all platforms (and still looking good).
