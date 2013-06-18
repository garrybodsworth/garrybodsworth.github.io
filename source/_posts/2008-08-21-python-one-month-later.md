---
title: 'Python &#8211; One Month Later'
author: Garry Bodsworth
layout: post
categories:
  - Uncategorized
tags:
  - development
  - python
---
So I&#8217;ve been writing in Python as part of my job for a month now&#8230; I am still writing using a text editor and running stuff on the command line (after dabbling in Eclipse and other Python editors). I can see why people like Python so much, it has some cool stuff.

What I discovered this week was the [Queue][1] object in Python. It is a thread-safe FIFO queue and it is there and ready to use. In C++ I would probably have found the definitive implementation through some library (hopefully in [Boost][2]) or I would have to roll my own with all the headaches involved in making sure just the building blocks work correctly. I&#8217;m not using it in the way that most people would expect but that is the great part of supplying solidly tested building blocks.

As usual the code I am writing needed unit-testing to make sure it did what it says on the tin. This meant a multi-threaded unit-test &#8211; I know this is a [bad thing sometimes][3]. I had to thrash it with the mountain of threads but the tests seem to work consistently (although I imagine it could turn up to bite me in the future). I am sure three-quarters of the code I have been writing are unit tests.

Some other great parts of Python I found is the function is a first class object, and I&#8217;ve even played a little with lambdas. I&#8217;m looking forward to investigating where the best place is to put the boundaries between C++ and Python code.

At the moment I am really at the tip of the iceberg stage, there is the 75% that isn&#8217;t so obviously on display.

 [1]: http://docs.python.org/lib/module-Queue.html
 [2]: http://www.boost.org
 [3]: http://goodliffe.blogspot.com/2008/06/unit-testing-threads-is-hard-part-4.html