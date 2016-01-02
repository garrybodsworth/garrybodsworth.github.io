Title: C++ Static Code Analysis
Date: 2008-01-21T21:49:00+00:00
Slug: c-static-code-analysis
Category: 
Tags: 
Authors: Garry Bodsworth

I've mentioned before about the usefulness of <a href="http://www.gimpel.com/">PC-Lint</a> when doing C++ development on Windows.  It closes off a whole class of bugs that can live in a codebase and raises teh minimum standard of development.

I came across a really decent article you can read <a href="http://powerof2games.com/node/27">here</a>.  They integrated it into their automated build process and bootstrapped Msbuild to use it.

Also, you can't forget that there are some good tools that can make it easier to use.  There is <a href="http://www.riverblade.co.uk/products/lintproject/">LintProject</a> to run Lint across an entire project, and also there is the <a href="http://www.riverblade.co.uk/products/visual_lint/index.html">Visual Lint</a> which is a nice integration into Visual Studio.

It would be nice however if somehow it was possible to integrate it completely with the cl.exe commandline.
