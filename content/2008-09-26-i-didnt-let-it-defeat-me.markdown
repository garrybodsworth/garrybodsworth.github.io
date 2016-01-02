Title: I Didn&#8217;t Let It Defeat Me
Date: 2008-09-26T09:00:00+00:00
Category: 
Tags: 
Authors: Garry Bodsworth

So I was having a bit of an unhappy time attempting to get GTK+ to compile successfully. My determination has finally paid off and I got it to work.

As it turns out I built Glib and GTK+ from their respective trunks so I could guarantee they were in sync. But what I was trying to achieve was to use a Git master tracking branch and I finally discovered my own ineptitude:

`git pull . master`

It is your friend and pulls the changes from the master and applies them to your branch. I then tried to compile it and it worked! So I now have a compiled version of [GTK+ that can run on a headless server][1] with absolutely no X server dependencies. Now I just need to experiment with the library.

I wrote down all the notes on how to compile your own GTK+ so I will post those online in the hope I will save someone else losing their hair.

 [1]: http://nanosleep.org/wiki/GTK%2B_Indirect_Renderer