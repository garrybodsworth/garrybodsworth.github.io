Title: Bug Databases - Bugzilla
Date: 2007-03-30T19:57:00+00:00
Slug: bug-databases-bugzilla
Category: 
Tags: 
Authors: Garry Bodsworth

One of the great things about working in computers is finding technologies that makes your life easier.  Finding a good fit for your development process is a bonus, but sometimes you do have to alter your process slightly to get the most out of those tools.  One of the best out there is Bugzilla.  When working on a product of any size a good bug/request/task tracker is completely essential.

Bugzilla is probably the best known bug tracker out there, but it simultaneously seems to have the Marmite effect on people.  It is a scalable, powerful, customisable system for managing a large amount of issues.  Certainly at some point in the development process you end up with more bugs than you know what to do with and it requires the ability to categorise and filter, this is where Bugzilla excels.

Recently <a href="http://www.bugzilla.org/">Bugzilla</a> 3.0 Release Candidate 1 was made available.  It adds spades of functionality, like custom fields, read-only fields, an XML-RPC interface, and more than that.

Bugzilla provides a massive breadth and depth of functionality.  The bug reports provide loads of information by default, an you can switch off or add to those fields.  The main power of the system is the search facility, it is fully comprehensive and daunting to the first-time user.  Most people who dislike Bugzilla have an aversion to the search feature, but it allows you to save searches and perform boolean searches, and now with version 3.0 you can assign searches to groups.

It has a powerful group feature where if you are a member of a group the group has its own permissions and settings.  It allows you to provide levels like sales, support, development, etc.

You can generate reports via searches, but also there is a set of comprehensive graphical charts.  It allows for you to track fixes by version, or by product, or component, and more.

Since it is open-source with all the source code it allows you to make it do whatever you want with enough hard graft.  In a previous job I implemented a custom Bugzilla database (based on a beta version 2.18).  Basically it involved tidying up the UI, providing per report storage areas via FTP, and a couple more tweaks like combo boxes for user names.  In the end it involved importing bugs from disparate sources like a well-structure bug database, Microsoft Access fiels, and even Excel spreadsheets.  Bugzilla provides an XML import feature which is invaluable when migrating to it.

With all the features and the proven stability and security (the Mozilla one must be over 300,000 bugs by now), it is a great tool for developers.