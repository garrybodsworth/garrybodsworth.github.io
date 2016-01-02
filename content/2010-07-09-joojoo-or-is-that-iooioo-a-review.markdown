Title: JooJoo or is that iooioo? A Review
Date: 2010-07-09T09:00:00+00:00
Category: 
Tags: 
Authors: Garry Bodsworth

So I finally managed to get myself a [Fusion Garage JooJoo][1] from eBay for a reasonable price. I had previously tried to order through their online shop with multiple failures, basically their payment system does not work (I tried with three different cards). This was not a great start to my experience, so I sat it out and waited for one of them to appear on eBay.

Why was I so keen to get hold of one? It is essentially an nVidia ION in a tablet. At [Camvine][2] the main hardware is based on this platform, so I thought it would be a great toy to play with and get our software working on it. I can say my gut feeling was right and I had it going quickly.

No pictures for this one as they are all over the Internet. But check out great internal photos [here][3].

And on to the review&#8230;.

**HARDWARE**  
I&#8217;ll start with the hardware. It&#8217;s not badly done, with a nice sturdy engineered body. The quality of finish does surpass what I thought it might be. What we have is nVidia ION netbook internals crammed into a slim tablet chassis.

**The Display**  
The screen size is just wrong, I know why they went for 16:9 (with a very respectable 1360&#215;768 720p resolution) but it just doesn&#8217;t work. When you are in portrait the top of the screen is way too far away from you. The screen is really configured for movies rather than web browsing with that shape and resolution. Ideally for a tablet you do want something closer to 4:3 and each edge being a minimum 1024 (I&#8217;ll come onto why in the software section). The viewing angle on the screen is good in one direction but then the other it is literally useless and you end up tilting it to see the content.

**Heat**  
The tablet does get very hot. It has a fan internally which you can hear quite clearly when you hold it up to your ear. That is good, but the thing that gets really hot on the ION is the video chipset (I&#8217;ve seen it going at 70ºC). The heat seems to be at its greatest somewhere around the battery pack area which is odd since it is the other side to the processor.

**Power Button**  
Either my fingers are too big or the power button is just not very good. It is quite good as it is orange when charging and white light when on, but it is recessed too far and seems terribly unresponsive.

**Ambient light sensor**  
Great to have one, but unfortunately it is positioned more or less where you place your left hand when you are operating in landscape.

**Weight**  
It is a bit more weighty than it needs to be but I put that down to the screen size. With a smaller, better screen it would have been much more of an impulse device to use.

**Logo**  
The logo on the case appears when the JooJoo is switched on which is a real nice touch. Also it illuminates the right one depending on the orientation you are currently in.

**Webcam**  
It has a webcam but I have not seen that it works &#8211; maybe it is for future software releases.

**Overall**  
I simultaneously dislike and like the hardware (from an external point of view). For the internals [some corners have been cut][4]. The niggles take away from the final finish, so with things like ambient sensor positioning, power button, and screen physical dimensions fixed it would be a lot better.

**SOFTWARE**  
For all of the hardware it is the software that will make or break the platform. The software is basically a web browser with a web based start page showing bookmarks, with compiz to switch between windows.

**Boot Time**  
It is fairly quick to boot, but now lots of things boot quickly. It mainly suspends when you &#8220;power off&#8221; and then restart. This is great for speed but unfortunately the software can get upset so you need to reset hard in order to get a working system.

**Main Menu**  
The main menu at the top I still haven&#8217;t quite worked out how you are supposed to bring it up. Sometimes it is a tap at the top and sometimes a one finger swipe near the top. Sometimes it is the top left only as well.

**Wifi**  
It seems it can only remember the last wifi network you were connected to so you have to type in the password again and again when you change locations. For a portable internet connected device that is pretty poor.

**Scrolling**  
The JooJoo is &#8220;multitouch&#8221; for differing values of multitouch. Essentially the only thing I have found multitouch is that webpages scroll by using two fingers (like the Apple touchpad). There is no other functionality I have found like rotate or pinch n zoom. The really annoying thing is that the main webpage that you start from uses one finger to scroll (due to the HTML implementation I am guessing) so once you are used to two-finger scrolling going back to the main page is really painful.

**Web Browser**  
According to some [hackery on the JooJoo forum][5] the browser is actually Google Chrome. It is surprising it has some performance deficiencies in scrolling and browsing. The browser supports Flash as well which may please some people (my intense aversion to it does not endear me to it).

**Multitasking**  
Because all webpages you have open are essentially live, you can end up with a Flash video playing int he background sapping CPU without even realising because it does not suspend the background processes.

**Compiz**  
You can switch the active web browser window using a compiz based switcher. It hasn&#8217;t been nicely user tested as you can end up scrolling off the left or right and struggling to get an active window. To throw away a page simply chuck it off the top which is a nice gesture.

**Rotation and Orientation**  
Rotation is obviously done using xrandr. This means no nice animation when changing orientation and you get the horrible destruction/creation of the framebuffer. Also the orientation seems to only have only two active edges because otherwise the illuminated logos would be upside down. This makes it inconvenient.

**GTK**  
It obviously has some GTK in the background (for Chrome), but I have seen GTK error dialog pop up momentarily whilst whizzing around the compiz 3D bit. It looked very odd. Also in the Chrome browser it is obvious there is no GTK theme because you have the default (and off-putting) grey standard widgets for combos and the suchlike.

**Webpages and Scaling and Zooming**  
As I mentioned earlier there is no pinch and zoom and no way to scale webpages. This is really important because of the resolution of the device. One direction it is 768 pixels, so most webpages are designed with a minimum 1024 width and this means that you have to scroll horizontally to see a whole webpage. There are two solutions &#8211; either scale a webpage (which is really easy in WebKit &#8211; even I have managed it for [CODA][6]), or supply a screen with a minimum 1024 in both directions (1280&#215;1024 is still a great resolution).

**Security**  
Okay, I log into all of these webpages and then switch off the device. Someone else switches it on and they can just go straight into those webpages because it simply remembers the credentials. This is a wide gaping security hole and brings me onto the next thing.

**Users**  
It is a single user device. I am pretty sure there is no particular &#8220;user&#8221; on this linux system, this means it is right pain for more than one person to check their gmail on this device.

**Overall**  
The software is OK for a toy, but not to be used beyond an internal engineering practice. I was pretty annoyed by it after five minutes, so it is time to nuke it.

**HACKY HACKETY HACK HACK**  
So the real reason I got it was to hack my own OS onto it and to play around writing apps for it.

For a stand I decided to order a plate display stand which should work a treat and you can get two for a fiver(!) Also I have ordered a 2Gb PC3-8500 204 pin DIMM for £25 to up the memory. This should make it even nicer to hack on.

The SSD storage is the biggest debacle though, it is a mini-PCIe mSATA with some flipped pins which makes it impossible to find a replacement. People have been trying for while now. However, what I have ordered is a SD card to mini-PCIe adapter so I should be able to shoe-horn in some storage.

The wifi is also horrific, it is a Realtek card and as anyone who has tried to get these working on Linux solidly can attest they are cheap and nasty. I can&#8217;t get it to work even when compiling the module under a 2.6.31 kernel. I might find another half height mini-PCIe wireless card to replace it with, Atheros has been quite good (and maybe find a wireless N).

The best bit is the screen and touchscreen is mounted upside down so all firmware images and media are stored upside down. Pointless attempt to avert hacking&#8230;.

**IS IT THE END YET?**  
So the JooJoo is good and bad, I couldn&#8217;t recommend it to &#8220;normal&#8221; users, but it is a real interesting hacking platform. If some of the tablet OSes come out this year they could give it a whole new lease of life. Hardware wise it is nearly there, but needs more work (and battery life). The software is a long way from being first useful, and then good which is unfortunate.

 [1]: http://thejoojoo.com/
 [2]: http://www.camvine.com
 [3]: http://thejoojooforum.com/viewtopic.php?f=4&t=316
 [4]: http://mjg59.livejournal.com/124426.html
 [5]: http://thejoojooforum.com/viewtopic.php?f=2&t=217
 [6]: http://camvine.com/products/coda