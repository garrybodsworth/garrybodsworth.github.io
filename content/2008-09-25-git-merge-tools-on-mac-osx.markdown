Title: Git Merge Tools On Mac OSX
Date: 2008-09-25T09:00:00+00:00
Category: 
Tags: 
Authors: Garry Bodsworth

I think I have mentioned before the merge hell you can hit in [Git][1] like other source control systems. What you really need in that instance is a good merge tool to make it easy. When I used [Subversion][2] on Windows I used [KDiff3][3] which did most merges automatically and made three-way merges pretty painless.

With Git on OSX the default mergetool is the built in file diff, which is pretty useless when it comes to merge hell.

I followed the KDiff3 integration article [here][4] but there is some kind of bug in KDiff3 that means that it does not save the files correctly even if you set up the merge manually.

However, there is good news with [this logical.rand article][5] which shows you how to integrate [Diffmerge][6] or [p4merge][7]. Both of these tools are very polished on the Mac and means merge hell manages to become much more manageable.

 [1]: http://git.or.cz/
 [2]: http://subversion.tigris.org/
 [3]: http://kdiff3.sourceforge.net/
 [4]: http://notch8.com/articles/2008/06/06/kdiff3-git-win
 [5]: http://blog.logicalrand.com/2008/9/9/use-p4merge-or-diffmerge-with-git-mergetool-on-os-x
 [6]: http://www.sourcegear.com/diffmerge/
 [7]: http://www.perforce.com/perforce/products/merge.html