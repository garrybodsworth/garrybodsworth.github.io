---
title: '&#8220;Boot Error&#8221; when booting from USB'
author: Garry Bodsworth
layout: post
categories:
  - Uncategorized
---
Some BIOS have problems booting from USB pen drives. This lead to to what I consider an insane discovery, USB flash drives have heads, cylinders, and sectors/tracks, but they are entirely virtual.

What your normally end up with is a prompt saying &#8220;Boot Error&#8221; and nothing else of use. This is because some BIOS are limited to 1024 cylinders so you need to change the geometry of the flash drive.

You can do this in Linux with the following commandline (where sdX is the device which is the usb flash storage):

<pre lang="Bash" colla="+">mkdiskimage -4 /dev/sdX 0 63 62
</pre>

The numbers depend on the size of the USB key as they need to be chosen to get a total number of cylinders less than 1024.

A 1GB stick would be:

<pre lang="Bash" colla="+">mkdiskimage -4 /dev/sdX 0 64 32
</pre>

A 1GB-2GB stick would be:

<pre lang="Bash" colla="+">mkdiskimage -4 /dev/sdX 0 128 32
</pre>

A 2GB-8GB stick would be:

<pre lang="Bash" colla="+">mkdiskimage -4 /dev/sdX 0 255 63
</pre>

Once your geometry is set up you can go ahead and partition your device and use it.