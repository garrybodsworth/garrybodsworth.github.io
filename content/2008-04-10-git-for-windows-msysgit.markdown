Title: Git For Windows - msysgit
Date: 2008-04-10T18:04:00+00:00
Slug: git-for-windows-msysgit
Category: 
Tags: 
Authors: Garry Bodsworth

Today I finally got a chance to install <a href="http://code.google.com/p/msysgit/">msysgit</a> - the Git port for Windows using <a href="http://www.mingw.org">MinGW</a>.

I was extremely impressed with the painless install and the ease of integration (into the shell context menu and the commandline).  The installer size is a trim 8Mb so it is a quick download to try out.

The main thing I have tried out at the moment is the newly functioning (for Windows) Subversion bridge.  The git-svn import seems fairly speedy even on Windows and works seamlessly.  It is interesting how efficiently the data gets stored inteh repository as well, and the possibility of reconstructing information that has been lost due to file moves and other lossy operations in Subversion.

Git-GUI also works.  Obviously it does not look spiffy and shiny but presents the information you need, and access to the operations you need (on a basic level).

I would say Git For Windows is very close to being "ready" and providing you are not in need of the more difficult corner cases it is ready for production use.  The guys working on it have done a great job.

Now all we need is their version of TortoiseSVN to take off called <a href="http://repo.or.cz/w/git-cheetah.git/">git-cheetah</a> (which probably is getting easier thanks to some of the Tortoises sharing code now to do with displaying overlays).

<span style="font-weight:bold;">Git Is The New Unix</span>

There is a great article about what Git really means as a platform.  You can read it <a href="http://www.advogato.org/person/apenwarr/diary/371.html">here</a>.

This kind of opened my eyes to how Git differs from not only other source control systems, but other distributed source control systems.  I recommend giving it a quick read.
