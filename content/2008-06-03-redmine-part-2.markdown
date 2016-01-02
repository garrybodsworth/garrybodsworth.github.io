Title: Redmine - Part 2
Date: 2008-06-03T19:40:00+00:00
Slug: redmine-part-2
Category: 
Tags: 
Authors: Garry Bodsworth

I have been playing with the project management/issue tracker <a href="http://www.redmine.org/">Redmine</a> a bit more over the past couple of days.  I have been getting more and more impressed the more I use it because it is so swift to use, by swift I don't mean it runs fast, I mean it gets work done with the minimum of fuss.

The issue tracking system is pretty simplistic if you do a direct comparison to something like Bugzilla, but it provides the essentials.  The best bit though is the support for custom fields out of the box, so you can pretty much set up your bug report the way you want it.  You can do all the normal things as well like configuring your workflow.

Using the listview of issue gives you a great context menu that you can use to do common actions like setting the priority, status, and completion percentage.

The issue tracking also integrates time tracking so you can see the progress.  You have a percentage complete as well as estimated time and actual time.  The time estimations can be tagged with which sub-task took the time (like design, code and test).

I spent a bit of time messing around with the source control integration.  I decided to try it out with a Git installation I had laying about.  In the end it is pretty simple to actually do, and it provides a simple interface with coloured diffs.  This means it becomes trivial to cross reference issues, documents, code, revisions, and more in one place.  I noticed that the commit comments get added to the reports by adding the issue number.

The icing on the cake is that it is all wrapped in a clear and intuitive user interface.  It looks good and makes use of all the Javascript goodness that users come to expect and it actually helps to make it easy to use.
