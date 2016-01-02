Title: Bug Databases - Redmine
Date: 2008-05-29T22:13:00+00:00
Slug: bug-databases-redmine
Category: 
Tags: 
Authors: Garry Bodsworth

While on my Internet travels I found a bug database system I hadn't encounterd before called <a href="http://www.redmine.org/">Redmine</a>.  It's open-source and based on <a href="http://www.rubyonrails.org/">Ruby-On-Rails</a>, and provides much more than simply bugtracking.  It refers to itself as a project management tool as it provides enough tools to do that.

Features include:
* Per project wiki and forums
* Issue tracking
* Source control integration (Subversion, CVS, Darcs, Bazaar, Mercurial, Git)
* Gantt chart and calendar
* Time tracking functionality
* News, documents & files management

I did a quick test install on a Ubuntu virtual machine to see what it was like.  The user interface is really quite slick and very easy to use because it makes the most of Javascript.  Even when you have a list view you get a nice context menu to do the simple and most often done changes (priority and the suchlike).

One of the most interesting parts I found of the system is the paradigm it uses to partition data.  You create a project and it is possible to have per-project wikis, forums, and repositories.  You can even use different source control systems per project. What makes it interesting is that you can point a project at a sub-branch of a repository, so it would be possible to have a project per branch or group of branches.  This would make it much easier to track implementations on a per-branch basis.

With document and wiki management available it is then possible to integrate the peripheral information for a product with the items involved in actually implementing it.  With the integrated wiki you can also have your requirements and design documents easily at hand.

I know some of this is very similar to Trac, but it is good to see another tool approaching the same space.  Some of the features like the ease of source control integration is really nice.
