Title: Merging On The Mac
Date: 2008-07-30T10:00:00+00:00
Category: 
Tags: 
Authors: Garry Bodsworth

Because I&#8217;m a cheapskate even when someone else is paying I was trying to find some three-way merge tools for the Mac, unfortunately my Googling didn&#8217;t turn up anything that doesn&#8217;t appear on other platforms. Obviously you have things like ediff3 in emacs and erm&#8230;.

One that I used extensively on Windows (also available for Linux) is [KDiff3][1]. It&#8217;s a great graphical merge tool, and it works on the Mac. I followed the instructions to integrate it into Git (check out the useful [post here][2]) but I haven&#8217;t had the mergetool successfully fire it up. When I load the files manually it seems to work fine. It&#8217;ll require some more perseverance. KDiff3 is a great tool though and is a pleasure to use.

I decided to also look at [Meld][3] through MacPorts. Unfortunately it has to pull in half the universe like a gravity well, so it was still compiling the dependencies when I decided to call it a day. It looks like a good tool though with all the features you would want, but will no doubt need to run on the X11 platform. Also it is regularly updated which is a good sign. So if I can get it to work expect a post about that&#8230;

FileMerge built into the Mac is only a two way tool, and I did consider the Perform Merge Tool which is available for free. So I think I will persevere with the top two.

 [1]: http://kdiff3.sourceforge.net/
 [2]: http://notch8.com/articles/2008/06/06/kdiff3-git-win
 [3]: http://meld.sourceforge.net/