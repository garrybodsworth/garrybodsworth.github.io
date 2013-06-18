---
title: How I Solved My Graphics Card Problem
author: Garry Bodsworth
layout: post
categories:
  - Uncategorized
---
A little while ago I [posted][1] about having problems getting my nVidia GeForce 6600GT AGP working on Ubuntu. I tried everything that a sane person would and then some. I tried Nouveau, Ubuntu&#8217;s various versions in their repository, and the ones direct from nVidia. The closest I had to working was the beta 1.80 which kept crashing&#8230; When 1.80 was officially released I tried that and that did not work at all with a completely black screen (like the other official version I tried).

Anyway, my solution was to order from Play an [ATi HD2600 Pro][2] for £30. It&#8217;s even got 512Meg on board which is a huge amount of memory. The main reason for this was an eye on the future for proper open-source support, that although is not currently comprehensive will improve in the future.

So I plugged the card in after cleaning out all remnants of all nVidia drivers, rebooted and it worked straight away. I enabled the closed-source ATi drivers and got all eye candy working as well. Ultimately I will use the RadeonHD driver that is open source in XOrg repositories, but it isn&#8217;t quite complete. You can also keep track of available features in a handy table [here][3].

Now I am happily able to use Ubuntu at 1920&#215;1200 with useful 3D features like Expose and desktop expose.

 [1]: http://blog.programmerslog.com/?p=274
 [2]: http://www.play.com/PC/PCs/4-/7871884/Play-Value-ATI-Radeon-HD-2600-Pro-512MB-PCI-E-Graphics-Card/Product.html?cm_mmc=Froogle-_-PC-_-Components-_-Play%2BValue%2BATI%2BRadeon%2BHD%2B2600%2BPro%2B%2F%2B512MB%2B%2F%2BPCI-E%2B%2F%2BGraphics%2BCard&source=5066&engine=froogle_pc&keyword=Play+Value+ATI+Radeon+HD+2600+Pro+%2F+512MB+%2F+PCI-E+%2F+Graphics+Card
 [3]: http://www.x.org/wiki/RadeonFeature