Title: How to install the latest Intel drivers on Ubuntu
Date: 2009-06-20T09:00:00+00:00
Category: 
Tags: 
Authors: Garry Bodsworth

This is a fairly painless process to get the latest and greatest drivers for Intel integrated graphics (like the 945GM). Since it is on the more or less bleeding edge of development there can be some issues, but personally I tend to see more issues with outdated drivers than running the latest.

There reason that this process is so simple on Ubuntu is that some nice and clever people have packaged it all up on [xorg-edgers][1]. The instructions here are for Ubuntu Jaunty 9.04.

There are some commandline incantations to make and some text files to edit.

Create a file **/etc/apt/sources.list.d/xorg-edgers.list** that contains the following text:<pre lang=”Bash”> deb http://ppa.launchpad.net/xorg-edgers/ppa/ubuntu jaunty main deb-src http://ppa.launchpad.net/xorg-edgers/ppa/ubuntu jaunty main </pre> 

Now execute the following commands:<pre lang=”Bash” line=”1″ file=”update.sh” colla=”+”> sudo apt-key adv --recv-keys --keyserver keyserver.ubuntu.com 0x165d673674a995b3e64bf0cf4f191a5a8844c542 sudo apt-get update sudo apt-get upgrade </pre> 

Now you should have pulled in the latest Intel drivers and related dependencies. You might have also updated other packages on your system if you are not fully up to date with your software &#8211; don&#8217;t worry this should be fine. If you reboot now your system should use these latest drivers with some spiffing UXA acceleration&#8230;. but that is not all.

There are some stability issues if you are using a 945 based card, so you need some minor configuration changes. Run the following commandline:<pre lang=”Bash”> dpkg-reconfigure xserver-xorg </pre> 

Now you need to edit your **/etc/X11/xorg.conf** and edit the device section so it looks a bit like this:<pre lang=”Bash” file="part-xorg.conf"> Section "Device" Identifier "Configured Video Device" Driver "intel" Option "Tiling" "false" Option "FramebufferCompression" "False" EndSection </pre> 

The most important part is to get those two lines containing &#8220;Option&#8221; which fixes the problems.

If you are using stock Jaunty then you will not have Kernel Mode Setting which provides better mode detection and switching for Linux. This requires a new kernel, but I will blog about that tomorrow.

 [1]: https://launchpad.net/~xorg-edgers