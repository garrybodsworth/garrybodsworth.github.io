Title: Python 2.6 Released
Date: 2008-10-02T09:00:00+00:00
Category: 
Tags: 
Authors: Garry Bodsworth

Python 2.6 is [available now][1] from the Python website. You can see the what&#8217;s new [here][2]. This is going to make [MacPorts][3] much more complicated&#8230;

The most obvious addition is the support for the version 3.0 support. There is a -3 switch to check for future incompatibilities as well as all the new features and syntax. It seems to essentially provide the 3.0 features without breaking backwards compatibility.

The new look of the documentation is easy on the eyes and it all helps make it much easier to navigate. Documentation is normally an unloved part of most projects, but they have done a really good job [here][4].

The **with** statement has been added which means you can now write context managers. These things seem to simulate enforced scoping (like you would have in things like C++). Additionally there are some new packages including multiprocessing, fractions, JSON, and a propertylist parser. Obviously multiprocessing has been in the news recently thanks to the Google Chrome browser, and this will simplify other people trying to go the same route (I&#8217;d only recommend doing it on making sure your platform/OS allows for quick process creation if you are using lots of them). Obviously the JSON support will be handy for web developers and should simplify some web frameworks.

There is tons more in there &#8211; probably more than any sane person would ever learn, but it does help Python get stronger because we will all use different portions of the language.

 [1]: http://www.python.org/download/releases/2.6/
 [2]: http://docs.python.org/whatsnew/2.6.html
 [3]: http://www.macports.org/
 [4]: http://docs.python.org/