Title: Google Open Source
Date: 2008-07-10T18:08:00+00:00
Category: 
Tags: 
Authors: Garry Bodsworth

Recently [Google][1] has been opening up more and more of its code, obviously hosting it on [Google Code][2]. I thought I&#8217;d highlight a few of them.

[Google C++ Testing Framework][3]  
*Google&#8217;s framework for writing C++ tests on a variety of platforms (Linux, Mac OS X, Windows, Windows CE, and Symbian). Based on the xUnit architecture. Supports automatic test discovery, a rich set of assertions, user-defined assertions, death tests, fatal and non-fatal failures, various options for running the tests, and XML test report generation.*

There are a number of C++ unit testing frameworks out there. A good article navigating the minefield can be read [here][4]. Advantages of the this framework is mainly it is backed by Google, it is mature, supplies a lot of functionality, and that it is portable.

[Protocol Buffers][5]  
*Protocol buffers are Google&#8217;s language-neutral, platform-neutral, extensible mechanism for serializing structured data – think XML, but smaller, faster, and simpler. You define how you want your data to be structured once, then you can use special generated source code to easily write and read your structured data to and from a variety of data streams and using a variety of languages – Java, C++, or Python.*

There are obviously loads of ways to serialise data, but it seems to support a number of languages and is space efficient (at least in comparison to XML). I&#8217;m not too sure how much it would offer over JSON although this does mean you don&#8217;t have to write or find some of the code yourself in the various languages.

[Ratproxy][6]  
*A semi-automated, largely passive web application security audit tool, optimized for an accurate and sensitive detection, and automatic annotation, of potential problems and security-relevant design patterns based on the observation of existing, user-initiated traffic in complex web 2.0 environments. Detects and prioritizes broad classes of security problems, such as dynamic cross-site trust model considerations, script inclusion issues, content serving problems, insufficient XSRF and XSS defenses, and much more. *

I mainly included this because I like the name&#8230; But it is also a useful tool for discovering weaknesses in your website&#8217;s security. I&#8217;ve read about commercial apps that do this but not too many open-source ones, so this release from Google can only be a good thing.

**Some other quick ones:**  
[Browser DOM Checker][7]  
*A simple utility to thoroughly validate DOM, XMLHttpRequest, and cookie security restriction handling in modern web browsers. Notable features include exhaustive hierarchy crawling, cross-domain IPC system for blind write verification, page transition checks, and more. *

[Bunny the Fuzzer][8]  
*A closed loop, high-performance, general purpose protocol-blind fuzzer for C programs. Uses compiler-level integration to seamlessly inject precise and reliable instrumentation hooks into the traced program. These hooks enable the fuzzer to receive real-time feedback on changes to the function call path, call parameters, and return values in response to variations in input data. This architecture makes it possible to significantly improve the coverage of the testing process without a noticeable performance impact usually associated with other attempts to peek into run-time internals. *

 [1]: http://www.google.com
 [2]: http://code.google.com/
 [3]: http://code.google.com/p/googletest/
 [4]: http://www.gamesfromwithin.com/articles/0412/000061.html
 [5]: http://code.google.com/apis/protocolbuffers/
 [6]: http://code.google.com/p/ratproxy/
 [7]: http://code.google.com/p/dom-checker/
 [8]: http://code.google.com/p/bunny-the-fuzzer/