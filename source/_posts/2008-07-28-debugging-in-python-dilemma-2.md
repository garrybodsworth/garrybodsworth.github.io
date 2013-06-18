---
title: 'Debugging In Python &#8211; Dilemma #2'
author: Garry Bodsworth
layout: post
categories:
  - Uncategorized
tags:
  - debugging
  - development
  - python
---
The next stage in Python development is &#8220;how do I debug&#8221;.

I&#8217;m at the stage where I keep adding print statements into the code to spot code flows and inspect values (which is nice because you can print more or less anything). But this is an extremely archaic way of approaching it, especially in this day and age&#8230;

Apparently there is a [PDB module][1] (there is another nice article [here][2]) but it seems to require code changes (an import and where you want to break), not a great deal of fun, especially if you accidentally leave some of this code in. It&#8217;s quite odd that it is not immediately apparent how to have breakpoints or to inspect data values.

Also, because there is a lack of a sanity checker by default you have to run your code and exercise the code paths to test your code. The good thing is that there are a number of programs to help with that, [PyLint][3], [PyChecker][4] and [PyFlakes][5], so it is not much of a worry.

PyDev has an interactive [debugger][6] so this will require much more investigation because it also can integrate PyLint for some error checking.

 [1]: http://www.ferg.org/papers/debugging_in_python.html
 [2]: http://www.onlamp.com/lpt/a/6163
 [3]: http://www.logilab.org/857
 [4]: http://pychecker.sourceforge.net/
 [5]: http://divmod.org/trac/wiki/DivmodPyflakes
 [6]: http://pydev.sourceforge.net/debug.html