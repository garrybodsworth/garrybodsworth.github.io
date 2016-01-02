Title: New Github Repo - polipo on Microsoft Visual Studio
Date: 2012-03-02T21:15:00+00:00
Slug: new-github-repo-polipo-on-microsoft
Category: 
Tags: 
Authors: Garry Bodsworth

Today I've just uploaded a fork of <a href="http://www.pps.jussieu.fr/%7Ejch/software/polipo/">polipo</a> to my Github account.&nbsp; it is a caching proxy server which works really well with a tiny amount of resources. It is primarily driven by Unix development so it has a version that works on Cygwin and a version that is not considered complete or tested that can use the Mingw toolchain.

I wanted to get it working with Visual Studio and I stumbled across some work <a href="http://code.google.com/p/polipovc/">here at polipovc</a> where someone got it working with Visual Studio.&nbsp; It is a code dump rather than a series of patches, so I took the <a href="https://github.com/jech/polipo">polipo git repository on Github</a> and forked it.&nbsp; I then applied the changes as a series of patches making minimal changes in each one and tried to normalise it with the project coding style.&nbsp; I also created a solution for Visual Studio 2010.&nbsp; It compiles for 32-bit and 64-bit (but just ignore the swatches of warnings).

The on-disk cache seems to not be working properly right now so I might look a bit more closely into why that is the case.&nbsp; To be honest the directory checks need to be factored out.

You can see my <a href="https://github.com/garrybodsworth/polipo">polipo github repository here</a>.
