Title: Intel 945GM Linux Drivers &#8211; The Good Bits
Date: 2009-06-13T09:00:00+00:00
Category: 
Tags: 
Authors: Garry Bodsworth

Using the latest Linux drivers for Intel 945GM are really, really good. The best drivers available for Linux displays in my humble opinion, especially since the deficiencies are more hardware related rather than the software.

Using the UXA acceleration you can even composite x-video windows in OpenGL. The 3D performance is impressive for such an old device and as of the end of last week xvmc was working as well with GEM. It uses the latest tech available in Linux display drivers like Kernel Mode Setting and DRI2 (which is a new interface for speaking to the kernel).

The latest drivers are also not only well capable of good compositing, but they are also capable of it without tearing, even with x-video surfaces. The actual rendering itself doesn&#8217;t tear any more thanks to people like [Jesse Barnes][1] who have put great effort into that work.

Since computers like netbooks/nettops are coming with the 945GM chipset, good support for it is essential. This is even better when it is open-source because you can help out with hackery and diagnosis (actually editing the code is very scary, but I tried a bit attempting to backport some changes to 2.7 because master was not stable enough at the time). It was a bit frustrating trying to balance performance, features and stability when deciding which driver version to finally run with, but I can see the driver is almost there with some minor stability work.

So I must say the guys have done really good work and 2.8 looks like it will be a really good release performance/feature-wise. I think I have wedged the hardware a few times, but I suppose the 2.7.99 releases are alpha, and also it is probably down to me hammering the graphics card.

 [1]: http://virtuousgeek.org/blog/index.php/jbarnes