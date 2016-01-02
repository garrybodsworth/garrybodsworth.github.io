Title: How To Ruin A Long Weekend
Date: 2009-04-13T09:00:00+00:00
Category: 
Tags: 
Authors: Garry Bodsworth

One of the things I was looking forward to this long weekend was watching DVDs. So I come back home on Thursday plonk my Tales Of The Black Freighter into my Windows Media Center 2005 box and I get jerky video and crackly sound. So I then spend a day trying to diagnose the problem&#8230;. Starting with making sure my Windows install is up to date with patches, new nVidia drivers (which managed to successfully break everything so I tried multiple versions), and new versions of the codecs I use. The best part was in Media Player I got no sound and fine video, but on Media Center I got jerky video and crackly sound. All from the same codec.

So, I decided it was time try MythTV properly, so I nuked the drive with a Xubuntu install which crashed halfway through showing me the true nature of my problem when there was no turning back &#8211; the DVD drive was dying. So I decided to proceed with my Linux install because I was on my way and liked the philosophy behind MythTV&#8217;s design.

Now three days later I have a mostly working system, but I have had a number of casualties. First my DVD drive, then I blew up my monitor which I had to drive all the way to the office to collect, and now my graphics card is living on borrowed time (I will post about that in a bit). None of it is MythTV&#8217;s or Ubuntu&#8217;s fault, but I should of known when the weekend starts badly it can only get worse. I even got so desperate I considered installing Vista, but I am now really close to getting the whole system up and running.

As for MythTV itself &#8211; the features it provides were exactly what I wanted, DVD, TV, CD music, random downloaded videos. But it has proved to be such a pain, some of it Xubuntu&#8217;s fault, some of it is MythTV&#8217;s, and my greatest share of pain has come from nVidia.

The backend design of MythTV is a real good idea but it is painful to get up and running &#8211; even with the nicely supplied packages. Especially if you decide to change your IP address or XMLTV stops working briefly. The setup user interface is designed to be used from a big screen, but is extremely unintuitive and counter to any GUI guidelines you have ever seen. It took about three attempts to get the hook up between XMLTV and my DVB-T card correct and in the database.

The frontend is okay, but is at least five years behind anything you have seen for media centers (they have a new version they are working on but there is no planned release yet). You have to fiddle around so you can successfully eject DVDs, get your remote set up (involving text configuration files) which works okay but not intuitively (the stop button doesn&#8217;t do what I expect on a Windows MCE remote), watch DVDs (enable the correct repositories), and getting your Samba mounts working (why on earth aren&#8217;t Samba shares an optional directory rather than having to mess around with fstab?)

I did try X-Box Media Center as a front-end for the MythTV backend. It is much nicer to look at, provides some real good features (with a great iPlayer plug-in), worked with the MCE remote flawlessly and sensibly, and is only lacking the ability to schedule recordings. If that was possible I would use that as a frontend, because it seems much more stable than the MythTV UI. I did also try Boxee, the commercial version of XBMC, but although it looked quite nice I found it was not as good as XBMC it is derived from and its MythTV frontend refused to work as it is broken.

My thoughts this weekend have gone from MCE2005 to MythTV to XBMC to Boxee to XBMC to MythTV&#8230;. That also discounts the amount of time I sat down considering how I would write my own.

My main work now is to get hibernate and suspend working, but that requires a post all of its own. At least at that point I will be functionally equivalent to my Windows MCE2005 install that I nuked.