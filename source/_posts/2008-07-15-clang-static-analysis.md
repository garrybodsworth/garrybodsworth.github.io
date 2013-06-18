---
title: Clang Static Analysis
author: Garry Bodsworth
layout: post
categories:
  - Uncategorized
tags:
  - c/c++
  - development
  - staticanalysis
---
The [Clang][1] Project (a C/C++/Objective-C front-end for the [LLVM][2]) has recently released the [LLVM/Clang Static Analyzer][3].

I&#8217;m a bit of a fan of static analysis, having posted quite a few times on my previous blog about Lint. Lint is much more comprehensive than the new one out of the Clang project but then again this is much younger and free.

At the moment the tool analyses C and Objective-C with rules to find problems with memory allocation patterns. It looks like the tool will be actively maintained as it will also be used inside of Apple. The HTML reports it generates are easy to use and read which is always a bonus.

There are a few posts about this analyser out there on the Internet. There are blog posts about using it [here][4] and [here][5]. There is also the original [Reddit discussion of the announcement][6].

Interestingly the [Adium X][7] (instant messaging client) have started to use the tool and have discovered a few problems. The results of the analysis are [here][8] (although there is some kind of server error at the moment so you can see it in the Google Cache [here][9]).

 [1]: http://clang.llvm.org/
 [2]: http://llvm.org/
 [3]: http://clang.llvm.org/StaticAnalysis.html
 [4]: http://www.noodlesoft.com/blog/2008/07/07/new-tool-on-the-block-the-llvmclang-static-analyzer/
 [5]: http://www.rogueamoeba.com/utm/2008/07/14/the-clang-static-analyzer/
 [6]: http://www.reddit.com/info/6qhdj/comments/
 [7]: http://www.adiumx.com/
 [8]: http://trac.adiumx.com/wiki/StaticAnalysis
 [9]: http://66.102.9.104/search?q=cache:5K2wbL2DVJEJ:trac.adiumx.com/wiki/StaticAnalysis+clang+static+analysis&hl=en&ct=clnk&cd=12&gl=uk&client=firefox-a