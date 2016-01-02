Title: Start Me Up
Date: 2010-04-25T09:00:00+00:00
Category: 
Tags: 
Authors: Garry Bodsworth

This may turn out to be one of those hollow promises again, but I am going to get this blog up and running again even if it kills me. The baby is sleeping (and snoring) upstairs so I have time, unless I am forced to do cleaning.

So what is new? [Camvine][1] did fill those vacancies with some good guys. I was surprised to hear some people even heard about it form this humble page.

What I need to do now though is try and get some Python changes merged upstream. I have been beating the networking code in urllib2 and httplib (two completely separate yet hopelessly intertwined) modules actually working. This means fixing HTTPS, digest proxy authentication, in fact proxy authentication, and tons more subtle interactions (like passing on CONNECT requests).

Strangely prescient was the article [Why Aren&#8217;t You Contributing To Python][2] since I have worked out all these fixes. I think the order will need to be 1) write lots of tests 2) get a number of small patches 3) cross reference it all with the python bug tracker. And this is all only in 2.6.4 currently.

And this year I will be going to [Europython][3] and aiming to not get serious food poisoning again&#8230;

 [1]: http://www.camvine.com
 [2]: http://jessenoller.com/2010/04/22/why-arent-you-contributing-to-python/
 [3]: http://www.europython.eu/