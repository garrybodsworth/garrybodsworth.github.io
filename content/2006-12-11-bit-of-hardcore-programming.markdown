Title: A bit of hardcore programming
Date: 2006-12-11T18:51:00+00:00
Slug: bit-of-hardcore-programming
Category: 
Tags: 
Authors: Garry Bodsworth

Last week <a href="http://games.slashdot.org/article.pl?sid=06/12/01/184205">Slashdot</a> drew attention to an article about <a href="http://www.beyond3d.com/articles/fastinvsqrt/">the origin of the fast approximation of the inverse square root in Quake 3</a>.  For anyone who likes obscure bits of code it is really quite interesting and I think really understanding the code does make you a better programmer even if you never use it.<blockquote><br />float InvSqrt (float x) {<br />float xhalf = 0.5f*x;<br />int i = *(int*)&x;<br />i = 0x5f3759df - (i>>1);<br />x = *(float*)&i;<br />x = x*(1.5f - xhalf*x*x);<br />return x;<br />}</blockquote>It computes the result using integer maths instead of floating point operations because back in the day that was faster.  This function does the operation to an approximation which is fine when it is used in graphics where the human eye finds it impossible to differentiate small changes in colour.  It is one of those functions where the more you iterate the more accurate the result it.

It works by reinterpreting the float bit pattern as an integer then using bit shifting to get at the mantissa.  The "magic seed value" is an approximation of the result (it is easier to get a good approximation when the result is in a mostly predictable range).

Anyway a useful tome about this kind of trickery is <a href="http://en.wikipedia.org/wiki/HAKMEM">HACKMEM</a>, you can read it online <a href="http://home.pipeline.com/~hbaker1/hakmem/hakmem.html">here</a>.

It would also be a good idea to check out <a href="http://www.hackersdelight.org/">Hacker's Delight</a>.
