Title: Source Control - Subversion and TortoiseSVN 1.5
Date: 2008-03-19T20:43:00+00:00
Slug: source-control-subversion-and
Category: 
Tags: 
Authors: Garry Bodsworth

There is no official release date for Subversion 1.5 although Alpha 2 is currently available.  I thought I'd post about the upcoming features that will be making their way into the release.  there is also a little bit at the end about TortoiseSVN 1.5 features.

<span style="font-weight:bold;">Merge Tracking</span>

The most important feature in the upcoming 1.5.  The initial concept is based on svnmerge.py but has gone far beyond that and is fully integrated into the repository format.  This means it will be possible to see which revisions have yet to be merged or have already been done.  For people with complex branching or regular merging it should be an indispensable feature.

Interesting links about it are <a href="http://blogs.open.collab.net/svn/2007/05/the_subversion__1.html">here</a>, <a href="http://blogs.open.collab.net/svn/2007/11/what-about-bran.html">here</a>, and <a href="http://blogs.open.collab.net/svn/2007/11/branching-strat.html">here</a>.  The functional spec is available <a href="http://subversion.tigris.org/merge-tracking/func-spec.html">here</a>.

<span style="font-weight:bold;">Sparse Checkouts</span>

This allows for checking out portions of a larger repository.  This means it is possible to specify the depth that the operations take into the directory structure.
 
<span style="font-weight:bold;">Conflict Resolution</span>

There are improvements to the conflict resolution for merges.  It is now possible to use the command-line to perform the resolution and a better interface for graphical clients.

<span style="font-weight:bold;">Changelists</span>

It is possible to work on several sets of files on a single working copy.  You can associate those files together with a name in order to work on more than one problem in a single working copy.  I really needed this feature at work today trying to do more than one thing in a single working copy.

<span style="font-weight:bold;">Externals Improvements</span>

The improvements allow svn:externals to be pegged at a revision.  Also they can use relative paths from the current directory (that will be really good in some instances with external deliverables) and if you use externals it makes managing a code tree much easier because it treats it like it is part of the current code tree.

<span style="font-weight:bold;">Copy/Rename Improvements</span>

There is an improvement in the behaviour on copy/renaming of files (not currently directories until version 1.6) by the client trying to be smarter.  If a file has been renamed/copied then rather than the server sending the whole new file it does the copy operation so you should not lose the changes that had been made to the old file.

<span style="font-weight:bold;">TortoiseSVN 1.5</span>

This should be released not long after the main Subversion 1.5 release.  The major changes will be the user interface work for merge tracking, changesets, and sparse checkouts.  There are some other features that will be part of the 1.5 release:
* Client side hook scripts – You can run some scripts before or after committing - this should help people create better processes.
* If a program has done some file operations like renaming and deleting without using the Subversion interface (drag-right-click) then it is possible to fix the file relationships in the UI.  This would be quite useful to inte3grate as an external tool in Visual Studio.
* Repository browser now has a two pane look like Windows Explorer with a tree-view and list of files.  Apparently it is much faster.
* A new merge wizard rather than the dialog which improves the workflow for merging.
