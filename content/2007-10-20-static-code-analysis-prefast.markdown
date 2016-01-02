Title: Static Code Analysis - PREFast
Date: 2007-10-20T07:27:00+00:00
Slug: static-code-analysis-prefast
Category: 
Tags: 
Authors: Garry Bodsworth

At work we use <a href="http://www.gimpel.com/">Gimpel PC-Lint</a> to analyse our source code for defects that the compiler does not pick up.  We use it on quite a strict level even after bolting it on to a legacy code-base.  There are some tools to make your life a little easier when using it from <a href="http://www.riverblade.co.uk/">Riverblade Software</a>.  Gimpel Lint is not a perfect tool for an IDE as it is commandline based and these types of checks should honestly be part of a good quality compiler as additional warning levels.

What I have found out though is that in Visual Studio Team System there is a static code analysis tool that isn't even available in the Professional version.  It's internally called PREFast at Microsoft and apparently they use it to ensure code quality.  Apparently in the Windows Driver Development Kit (WDK) it is available so it is possible to use that to do some code analysis.  Check out <a href="http://buildingsecurecode.blogspot.com/2007/08/security-code-scanning-with-microsoft.html">this blog post for instructions</a>.  There are plenty of blog posts about it on the rest of Steve Dispensa's blog.

There is a small Microsoft Research Article available <a href="http://research.microsoft.com/displayArticle.aspx?id=634">here</a> about PREFast.

I've downloaded VS Team System to give it a go and to see how good it is.  Or maybe I will try out the PSDK hack...
