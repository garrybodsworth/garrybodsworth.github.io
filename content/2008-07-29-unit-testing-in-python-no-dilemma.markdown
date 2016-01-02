Title: Unit Testing In Python &#8211; No Dilemma
Date: 2008-07-29T11:00:00+00:00
Category: 
Tags: 
Authors: Garry Bodsworth

Unit-testing in Python today&#8230;

Having unit testing built into the language (or at least the standard library) is a good move. With an interpreted language like Python it is invaluable to test the various code paths.

It also helped me find some obvious bugs in my code, which I probably shouldn&#8217;t say in public, entirely because it is embarrassing. That is the first obvious benefit of unit testing. The next benefit is more subtle, you discover how to structure your code in a better fashion because you are thinking about how to test the individual parts of the code.

Unit testing is another option instead of the code checkers PyLint, etc, because the code paths are exercised providing you have written the test. Not perfect, but better than not doing code checking.

The scary thing is you end up with much more testing code than actual executable code. I remember reading somewhere that if that is the case then you are doing something right(!)