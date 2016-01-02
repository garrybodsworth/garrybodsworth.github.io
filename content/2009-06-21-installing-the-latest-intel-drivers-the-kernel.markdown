Title: Installing The Latest Intel Drivers &#8211; The Kernel
Date: 2009-06-21T09:00:00+00:00
Category: 
Tags: 
Authors: Garry Bodsworth

So installing the drivers, latest X-server, mesa and so on is only part of the puzzle to use the latest Intel graphics drivers. You also need to update your kernel for more features like better kernel memory management, kernel mode switching, and other basic things. The driver can work (for differing levels of working) for older kernels, but the bugfixes tend to be on the latest version. I have tried this on an Intel 945GM.

So this is how you update your kernel for Jaunty (and other Ubuntus would probably work). A really handy repository of kernels is maintained by Ubuntu called [Mainline PPA][1] where you can download pretty much any version of the kernel.

So for kernel 2.6.30 you need to download the following file : [linux-image-2.6.30-020630-generic\_2.6.30-020630\_i386.deb][2]  
You need to install this by calling:<pre colla="+" lang=”Bash”> sudo dpkg -i linux-image-2.6.30-020630-generic\_2.6.30-020630\_i386.deb </pre> 

As part of the install it should have run update-grub. If not run **sudo update-grub**

To get kernel modesetting working as well as fixing a couple of minor issues you need to edit the file **/boot/grub/menu.lst** for some extra parameters. You need to edit the line that looks like:

<pre colla="+" lang="Bash">kernel      /vmlinuz-2.6.30-020630-generic root=/dev/sda7 ro 
</pre>

And add the following between &#8220;generic&#8221; and &#8220;root&#8221;:

<pre colla="+" lang="Bash">nopat enable_mtrr_cleanup i915.modeset=1
</pre>

The first two sort out some hardware bugs on the Intel 945 depending on the hardware platform which can vary. Acer Aspire Ones don&#8217;t necessarily have the same mtrr bugs as MSI Winds and so on. The modeset parameter switches on kernel modesetting which you will hopefully not notice many changes with.

I did find kernel modesetting played a lot better running X without any monitor connected and dealt with a lot of odd mode issues.

 [1]: http://kernel.ubuntu.com/~kernel-ppa/mainline/
 [2]: http://kernel.ubuntu.com/~kernel-ppa/mainline/v2.6.30/linux-image-2.6.30-020630-generic_2.6.30-020630_i386.deb