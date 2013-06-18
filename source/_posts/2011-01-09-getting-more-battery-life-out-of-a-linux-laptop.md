---
title: Getting More Battery Life Out Of A Linux Laptop
author: Garry Bodsworth
layout: post
aktt_tweeted:
  - 1
aktt_notify_twitter:
  - yes
categories:
  - Uncategorized
tags:
  - laptop
  - Linux
  - powersaving
---
On my ASUS UL20A out of the box power management is pretty good but it still does not reach the heady climbs of Windows.  In running [powertop][1] it gave a lot of useful suggestions like SATA, soundcard and USB, but when you apply these you only get it for that session.  You need some way of making these power saving settings permanent.

Here are a few power management scripts that have increased my battery life by about 20-40% as a rough estimate.  The best way to increase battery life dramatically is to reduce the brightness of your monitor which obviously diminishes the usefulness of your display at a certain point.

Here are the files you need to create (all derived from [this forum post][2]).

**vm\_dirty\_writeback**  
`<br />
[sourcecode language="bash"]<br />
#!/bin/sh</p>
<p>path_dwc="/proc/sys/vm/dirty_writeback_centisecs"<br />
val=500</p>
<p>case "$1" in<br />
	true)<br />
		echo "**VM dirty writeback 15 seconds"<br />
		val=1500<br />
		;;<br />
	false)<br />
		echo "**VM dirty writeback 5 seconds"<br />
		val=500<br />
		;;<br />
esac</p>
<p># 5 seconds on AC, 15 seconds on battery</p>
<p>if [ -w "$path_dwc" ] ; then<br />
	echo $val > $path_dwc<br />
fi</p>
<p>exit 0<br />
[/sourcecode]<br />
`

**link\_pm\_policy**  
`<br />
[sourcecode language="bash"]<br />
#!/bin/sh</p>
<p>path_host0="/sys/class/scsi_host/host0/link_power_management_policy"<br />
path_host1="/sys/class/scsi_host/host1/link_power_management_policy"<br />
path_host2="/sys/class/scsi_host/host2/link_power_management_policy"<br />
path_host3="/sys/class/scsi_host/host3/link_power_management_policy"<br />
val=max_performance</p>
<p>case "$1" in<br />
	true)<br />
		echo "**lpm policy powersave ON"<br />
		val=min_power<br />
		;;<br />
	false)<br />
		echo "**lpm policy powersave OFF"<br />
		val=max_performance<br />
		;;<br />
esac</p>
<p># max_performance on AC min_power on battery</p>
<p>if [ -w "$path_host0" ] ; then<br />
	echo $val > $path_host0<br />
fi</p>
<p>if [ -w "$path_host1" ] ; then<br />
	echo $val > $path_host1<br />
fi</p>
<p>if [ -w "$path_host2" ] ; then<br />
	echo $val > $path_host2<br />
fi</p>
<p>if [ -w "$path_host3" ] ; then<br />
	echo $val > $path_host3<br />
fi</p>
<p>exit 0<br />
[/sourcecode]<br />
`

**snd_suspend**  
`<br />
[sourcecode language="bash"]<br />
#!/bin/sh</p>
<p>path_dwc="/sys/module/snd_hda_intel/parameters/power_save"<br />
val=1</p>
<p>case "$1" in<br />
	true)<br />
		echo "**Intel HD sound suspend"<br />
		val=1<br />
		;;<br />
	false)<br />
		echo "**Intel HD sound on power"<br />
		val=0<br />
		;;<br />
esac</p>
<p># 5 seconds on AC, 15 seconds on battery</p>
<p>if [ -w "$path_dwc" ] ; then<br />
	echo $val > $path_dwc<br />
fi</p>
<p>exit 0<br />
[/sourcecode]<br />
`

**network_powersave**  
`<br />
[sourcecode language="bash"]<br />
#!/bin/sh</p>
<p>if [ "$1" = "true" ]; then<br />
            iwconfig wlan0 power on<br />
fi</p>
<p>if [ "$1" = "false" ]; then<br />
            iwconfig wlan0 power off<br />
fi</p>
<p>exit 0<br />
[/sourcecode]<br />
`

**usb_autosuspend**  
`<br />
[sourcecode language="bash"]<br />
#!/bin/bash<br />
if [ "$1" = "true" ]; then</p>
<p>  for i in /sys/bus/usb/devices/*/power/level; do<br />
	[ "$(cat $i)" = "auto" ] && continue<br />
	echo "auto" > $i<br />
  done</p>
<p>  for i in /sys/bus/usb/devices/*/power/autosuspend; do<br />
	[ "$(cat $i)" -ge 0 2>/dev/null ] && continue<br />
	echo "2" > $i<br />
  done</p>
<p>fi<br />
[/sourcecode]<br />
`

Then do:

*   Put all the files above in a directory and cd into it.
*   chmod 755 *
*   sudo install * /usr/lib/pm-utils/power.d/
*   Do a reboot here.

You can check how it is running by looking at the log in /var/log/pm-powersave.log

 [1]: http://www.lesswatts.org/projects/powertop/
 [2]: http://ubuntuforums.org/showthread.php?t=1326333