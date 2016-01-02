Title: Some interesting C++ articles
Date: 2007-04-22T19:33:00+00:00
Slug: some-interesting-c-articles
Category: 
Tags: 
Authors: Garry Bodsworth

On <a href="http://www.osnews.com/comment.php?news_id=17741">osnews there is a story linking to some articles about C++</a>.  These articles cover C++ polymorphism and leveraging vector processing capabilities of modern processors with C++.

The polymorphism articles cover the use of templates to define interfaces and avoid inheritance.  It all looks very COM like...  There should be performance gains with this approach due to the lack of real vtables and the ability for the compiler to optimise much better due to the code being static at compile time.  Although, who knows how much gain there will be without proper testing.

The other article is about using vector processing units to speed up computation.  The article says that this is not a cross-platform solution but I think there must be some vector processing interfaces out there for C++ (I just can't remember any off the top of my head).
