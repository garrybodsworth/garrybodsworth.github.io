---
title: 'When your Mac boots slow&#8230;'
author: Garry Bodsworth
layout: post
aktt_notify_twitter:
  - yes
aktt_tweeted:
  - 1
categories:
  - Uncategorized
tags:
  - apple
  - boot
  - mac
---
I am sure I have been emitting an EM field for the past week. My router, my iPhone and my MacBook have all been playing up.

My MacBook has been booting really slow (I&#8217;m talking 20 to 40 minutes) and the graphics and general operation have been going downhill. I thought I would take a Windows inspired fix after trying everything else I could think of (blaming the processor, hard drive, graphics chip), and reinstall the operating system.

This failed numerous times. Something as simple as an install? Great. Eventually getting the install log shows this type of message:

> Unable to set as boot disk: the bless tool was unable to set the current boot disk

This is on a completely clean install of Snow Leopard. The installer was also unable to unmount which inturn means repair the disk.

Somehow I stumbled on [this fix on the Apple Support Site][1]. Apparently you have to reset your parameter random access memory (PRAM) and nonvolatile RAM (NVRAM). This involves the incantation Command-Option-P-R keys and restarting. Now the install took first time, this has been a public service announcement.

 [1]: http://support.apple.com/kb/HT1379