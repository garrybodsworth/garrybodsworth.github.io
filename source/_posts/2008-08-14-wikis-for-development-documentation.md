---
title: Wikis For Development Documentation
author: Garry Bodsworth
layout: post
categories:
  - Uncategorized
---
A couple of years back when migrating from Visual SourceSafe to Subversion for NC Graphics I decided to piggyback an install of [MediaWiki][1] onto the Apache install (I was using it to serve Subversion and it worked a treat). Initially it was just me playing around with it with some feedback from others. At some point we decided to use the wiki for internal documentation and Tristan Day took on the mantle of Benevolent Wiki Dictator. Without him the wiki wouldn&#8217;t have been as well organised or useful.

We put everything on there including Tristan&#8217;s horrific task of porting over old documents that were in various formats like Word or text. When they were online and it was the way they were supposed to be edited they became &#8220;living documents&#8221; that are continually updated. Some areas became repositories of information for what we were currently working on and what was done with some very nice tabe formatting.

It also meant the information was available anywhere with an Internet connection and since it was up to and was well presented if anyone had a question we could say &#8220;look at the wiki&#8221;. The wiki pages were even used for management presentations because it clearly showed our project progress and planning.

One of the things I do nowadays is whenever I do something and make a note of it, say a development process or carefully constructed command line, I put it in the wiki. I do that rather than having loads of notebooks because they are also useful for other developers, even the noddy stuff. The problem is you do need a housekeeper or Benevolent Wiki Dictator to keep it all well organised.

The thing is once you have reached critical mass with the documentation on a wiki then it takes on a life of its own and becomes a communal and extremely important resource. They get even more interesting when you have something like [Trac][2] or [Redmine][3] that integrate bug tracking and source control (and more via plug-ins).

The types of things you should have on a development wiki are:

*   Setting Up A New Computer &#8211; A well defined process for when you have a new starter that they can follow.
*   Setting Up A Development Environment &#8211; What you need to do to build and run a product.
*   Debugging Information &#8211; How to debug the system.
*   Coding Guidelines &#8211; Which have to be kept up to date making them perfect for a wiki.
*   Software Licences &#8211; An audit of licences (like GPL etc) used to achieve a product. It&#8217;s always important to know this information.

There is tons more but you get the idea of where to start.

 [1]: http://www.mediawiki.org/wiki/MediaWiki
 [2]: http://trac.edgewall.org/
 [3]: http://www.redmine.org/