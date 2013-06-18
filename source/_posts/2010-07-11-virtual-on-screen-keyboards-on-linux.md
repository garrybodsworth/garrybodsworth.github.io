---
title: Virtual On-Screen Keyboards On Linux
author: Garry Bodsworth
layout: post
aktt_notify_twitter:
  - yes
  - yes
aktt_tweeted:
  - 1
categories:
  - Uncategorized
tags:
  - development
  - keyboard
  - touch
---
With a [tablet][1] awaiting a better operating system I decided I had to evaluate the landscape on on-screen virtual keyboards on Linux. Obviously the ideal would be iPad/iPhone-esque, but that would be really frighteningly good, I had much lower expectations.

I was not sure if the tech was there to even show the keyboards automatically when an input field was selected. GTK are well ahead of the game on this with their IMContext base class to encapsulate input mainly for complex languages or disability accessibility, but a good side-effect is the ability to hook in an on-screen keyboard when a text input is focused. In that case the on-screen keyboard needs to know about GTK in order to know when to show.

I tested all these on a VM that has now run out of hard disk space thanks to having to compile lots of stuff. Most of the keyboards I completely failed to make automatically appear on the screen when a text input was selected, it was either me or them&#8230;.

So in no particular order&#8230;.

[Matchbox Keyboard][2]  
Some people are using this actively. It requires hacking to be able to toggle the display of it which makes it pretty much a no-go as it would always be on top of the screen. The GUI looks all right though. Some good info [here][3].

[xvkbd][4]  
The venerable old man of the line up. It&#8217;s been around the block and does exactly what it says on the tin. It has lots of good features and hacks (like making it appear for login windows). As far as I could see I couldn&#8217;t hook it up to the IMContext but I could be missing something.

[Gnome On-Screen Keyboard][5]  
The oldest GTK based one and seems to be showing its age thanks to the UI.

[onboard][6]  
This is the Ubuntu one. I couldn&#8217;t get it to automatically appear on focus. It looks OK, but seems to be lacking some features. At least it is easily hackable in Python. Some more interesting information [is here][7].

[Florence][8]  
This is the most recommended one and it is pretty good. The main pain was I had to compile it as their were no packages for it.

[fvkbd][9]  
This looks fairly promising as it is very skinnable on configurable. Unfortunately I could not work out how to hide or autohide the keyboard. Also this had no packages and requires compiling. This provides the basis for the OLPC virtual keyboard test and also the Meego/Maemo virtual keyboard.

[Caribou][10]  
This is the virtual keyboard testbed for Gnome 3.0. It is written in Python and needs packaging so I had to compile it. This was the one that got closest to what I want because it worked. It shows a small keyboard by the input with current focus. In my VM I had to disable the Clutter code for whizzy animations before getting it to work.

I&#8217;ve probably missed some but there are only so many not quite ready applications you can test before going completely and utterly bonkers.

Another thing I discovered was Google Chromium&#8217;s addressbar is accessibility implemented, but none of the content in webpages is. Firefox on the other hand and anything WebkitGTK based (like Epiphany) all work properly with their accessibility. Part of the Chrome problem is the multiprocess rendering and that they have not prioritised accessibility according the bug reports I have read.

 [1]: http://thejoojoo.com
 [2]: http://matchbox-project.org/?p=1
 [3]: http://japiblog.dddgames.com/?p=15
 [4]: http://homepage3.nifty.com/tsato/xvkbd/
 [5]: http://www.gok.ca/
 [6]: https://wiki.ubuntu.com/Accessibility/Projects/onBoard
 [7]: http://www.combibo.net/articles/using_an_onscreen_keyboard_in_ubuntu/
 [8]: http://florence.sourceforge.net/english.html
 [9]: http://gitorious.org/fvkbd
 [10]: http://live.gnome.org/Caribou