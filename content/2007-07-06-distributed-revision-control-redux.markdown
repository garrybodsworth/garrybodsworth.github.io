Title: Distributed Revision Control Redux
Date: 2007-07-06T22:01:00+00:00
Slug: distributed-revision-control-redux
Category: 
Tags: 
Authors: Garry Bodsworth

Leading on from my previous posts <a href="http://garrys-brain.blogspot.com/2007/06/tortoises-are-coming.html">here</a> and <a href="http://garrys-brain.blogspot.com/2007/06/distributed-revision-control-mercurial.html">here</a>  I have been doing a lot of research into the distributed revision control arena.

Admittedly I have got fixated on three, <a href="http://git.or.cz/">Git</a>, <a href="http://www.selenic.com/mercurial/wiki/">Mercurial</a> and <a href="http://bazaar-vcs.org/">Bazaar</a>.  All three projects are about the same age, but each have their own strengths and weaknesses.

Briefly to sum them up Git is fast, it has a large developer community behind it and seems to be developing at breakneck speed.  The disadvantages are mainly due to the reliance on the POSIX systems which means cross-platform (well, Windows) support is weak.  I know there are some initiatives to get it working on Windows but I can see it losing steam as there is not enough interest in it due to the POSIX platform supports being so strong.  Also, Git is a bit more obscure than the others due to being a bit more low-level with plug-ins adding the ease of use.

Mercurial is written is Python and is easily cross-platform  It is much simpler than the aforementioned Git to use and is close to it in speed and storage.  The disadvantages which I must admit are not many are that the community is not as fast moving as Git, but new versions are very regular.  I do see this as a better prospect than Git as it is better designed whereas as better design is being retroactively added to Git.

Bazaar (Bazaar NG to give it its full name) is sponsored by <a href="http://www.canonical.com/">Canonical</a>, the company running Ubuntu.  Mark Shuttleworth has blogged about Bazaar recently which I mentioned in a previous post.  Bazaar is also written in Python and is cross-platform with a nice Windows installer for those people scared of installing Python.  It is very well designed with comprehensive renaming and merge support.  The main disadvantage is that it is not as fast as Mercurial or Git.  To be honest I am taking a liking to this system and have been investigating it quite deeply (but that is for another post).

These three young projects are really progressing fast though and they are already good enough to use providing you are not too tied to your current extras from more mature systems (like TortoiseSVN).
