Title: Visual Studio 2005 - Lets Break Everything!
Date: 2006-10-04T20:05:00+00:00
Slug: visual-studio-2005-lets-break
Category: 
Tags: 
Authors: Garry Bodsworth

Since I've been using Visual Studio.NET 2005 I have discovered a myriad of undocumented (or documented in such a way as to seem inoccuous) breaks in the compilation of most code.

<span style="font-weight:bold;">Standard C - the CRT</span>

I should start with the simplest and probably most common breaks that would effect you if you use C or C++ with the Visual C++ 8.0 (VC8) compiler.  If you have used swprintf or any of its relations you will find your code no longer compiles, or it does and gives an odd warning.  This is extremely dangerous as to make it more conforming they have added an extra parameter for the buffer size.  All well and good, but you find most of the code you download of the Internet no longer compiles. Simply adding <span style="font-style:italic;">#define _CRT_NONSTDC_NO_DEPRECATE 1</span><br /> won't make a difference.  You need to add:<br />   <span style="font-style:italic;">#define _CRT_NON_CONFORMING_SWPRINTFS</span>

Make sure this all gets added as the first thing in the <span style="font-style:italic;">stdafx.h</span> or in the pre-processor definitions in the project settings.

The <span style="font-style:italic;">_CRT_NONSTDC_NO_DEPRECATE</span> will deal with the instances of other C runtime library code that has also changed.  This is because Microsoft have replaced all of the functions that you will get all the warnings about with "secure" functions.  This means that the function names are appended with <span style="font-style:italic;">_s</span>.

<span style="font-weight:bold;">Floating Point Operations</span>

There are three options now:<br /><ul><li><span style="font-weight:bold;">fp:fast</span> - The fastest implementation.</li><li><span style="font-weight:bold;">fp:precise</span> - slower but more "precise".</li><li><span style="font-weight:bold;">fp:strict</span> - the strictest implementation.</li></ul>You have to make a choice - faster or more precise.  I still haven't discovered how imprecise <span style="font-style:italic;">fp:fast</span> is yet.

<span style="font-weight:bold;">C++ Standard Template Library</span>

You'll probably find that any code you use will fall over in some obscure and not so obscure instances, as well as being much slower.  And that goes double for Debug builds.

So you need to add these to the top of your stdafx.h or your pre-processor definitions (or to your command line).  To get up and running use:<br />   <span style="font-style:italic;">#define _SECURE_SCL 0</span><br />   <span style="font-style:italic;">#define _SCL_SECURE_NO_DEPRECATE</span><br />   <span style="font-style:italic;">#define _HAS_ITERATOR_DEBUGGING 0</span>

<span style="font-weight:bold;">How to define these values.</span>

The options to add these things:<ol><li>Add to your stdafx.h as plain preprocessor definitions.  This option seems to be the most hit-and-miss.</li><li>Add to your pre-processor definitions in your project settings.  This is done with semi-colon separated values, eg, <span style="font-style:italic;">_SECURE_SCL=0</span></li><li>Add it to your commandline.  Do this in the project settings commandline tab.  Add /D_SECURE_SL=0 for instance, you simply add /D then the preprocessor symbol without a space with an optional assignment.</li></ol>In some instances one option may not work but one of the three will.
