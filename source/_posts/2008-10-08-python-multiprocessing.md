---
title: Python Multiprocessing
author: Garry Bodsworth
layout: post
categories:
  - Uncategorized
tags:
  - development
  - multithreading
  - python
---
One of the most interesting parts of the new Python 2.6 is the [multiprocessing][1] module now available. This will massively simplify the problem of writing an application that has multiple processes.

The problem with multiprocessing before is that you spend ages writing a framework and boilerplate to do things like messaging, monitoring, and starting/stopping processes. This is a right pain and has its own share of bugs. You need to think how to pass state between the processes normally resorting to using the stdout/stdin mechanism.

The multiprocessing module provides an interface indistinguishable from the [threading][2] interface. It means you end up writing multiple processes in the same way you would write threads &#8211; which is pretty darn easy. The only guilt you will feel when you use it is when you are chucking away bucketfulls of redundant code.

I think this also will make it really easy to share logging between processes which if you do manually you will be finding problems until the end of time. This is especially interesting with a rotating log because you won&#8217;t have to worry about multiple processes making different decisions. I don&#8217;t know what the communication overhead will be for using it though&#8230;

Also with this library you are given ways to synchronise between processes and you can even share data. These are obviously going to have a lot of applications and be extremely useful.

 [1]: http://docs.python.org/library/multiprocessing.html#module-multiprocessing
 [2]: http://docs.python.org/library/threading.html