Title: How a C++ developer writes Python
Date: 2008-08-20T09:00:00+00:00
Category: 
Tags: 
Authors: Garry Bodsworth

I&#8217;ve been writing Python professionally for about a month and I am still in the process of shaking out my C++isms. This is not a diatribe about how C++ is rubbish, because I think C++ is great. I am making some &#8220;mistakes&#8221; as I am in the learning process.

So today I was writing a function to parse a URL into the useful parts that make it up. I&#8217;d laid it out all nicely, written some unit-tests and it did its job exactly how I wanted. Then I was asked did the Python [urlparse][1] module not do what I wanted. Damn &#8211; as a C++ developer I&#8217;m used to rolling a lot of stuff that make up the building blocks of the software, so what I did was pretty natural. What I need to learn is to check the Python libraries first before doing obvious things.

The other thing I am rapidly unlearning is writing verbose loops. In C++ I am used to writing loops int he way I am expecting them to be executed. In Python you need to express them differently using list comprehension, which I am liking a lot. I even rewrote some loops today I wrote in my first week where I replaced seven lines with one that expressed the intent of the statement perfectly.

Another thing that weirded me out was creating threads. You create the variables for them, start them off and they know when to clean themselves up&#8230; I think it is because I am still thinking about the C++ scoping rules rather than garbage collecting.

I am sure these Python-ing mistakes won&#8217;t be my last, but it is interesting to wrap your head around some new things. I do miss manually managing my memory and knowing when stuff gets destroyed, I think it probably is because I&#8217;m paranoid and need to relax and go with the flow.

 [1]: http://docs.python.org/lib/module-urlparse.html