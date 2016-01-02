Title: Tools for TortoiseSVN
Date: 2006-10-06T11:32:00+00:00
Slug: tools-for-tortoisesvn
Category: 
Tags: 
Authors: Garry Bodsworth

In order to make my TortoiseSVN as useful as possible, I use some external tools to maximise productivity.  It took a while to find the right set up but I am happy with it now.

For merging with a three-way diff when there are conflicks I found <a href="http://kdiff3.sourceforge.net/">KDiff3</a>, which seems to not be considered as sexy or well-known as most other tools.  But it does the job admirably with plenty of powerful features.  Certainly it does not look fully Windows-native, but that should not put you off if you want to use this powerful tool, and after all it is very rare that Subversion wants me to do a three-way diff.

For standard diffs I use <a href="http://winmerge.org/">WinMerge</a>.  Simply it is the best Windows based diff and merge tool I have ever used.  It is powerful and intuitive, but is unfortunately limited to two-way diffs.  If it did do the three-way diffs I would not be using KDiff3.

For viewing patch files (unified diffs) I use <a href="http://www.flos-freeware.ch/notepad2.html">Notepad2</a> which has nice highlighting, but it very rare that I will have a need to look at these patch files.

After installing TortoiseSVN, install KDiff3 as it sets up your TortoiseSVN environment for you.  Then install WinMerge and choose <span style="font-style:italic;">"WinMergeU.exe"</span> as the diff viewer.  Then install Notepad2 and set it up as the unified diff viewer.  Doing it in this order means that you can let KDiff3's installation set up the bindings, and then configure the other ones by had as KDiff3's commandline isn't overly simple for TortoiseSVN.