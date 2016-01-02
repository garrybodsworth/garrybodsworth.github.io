Title: Python, You Little Star (Args)
Date: 2008-09-02T09:00:00+00:00
Category: 
Tags: 
Authors: Garry Bodsworth

I like features that make code more concise, manageable and expressive.

I was writing some code in Python that was essentially a function dispatcher where all the functions have the same arguments. When writing them in a more static language you have to specify all the arguments wherever they are forwarded when what you really want to say is take all the arguments and bung them into the next function. Not really a problem with cut and paste, but when you start changing the function protoype you have to make sure you change it in all the related places.

In Python you have the option of using \*args which consumes the rest of the arguments of a function and puts them into a list. This meant that I could define lots of the functions which were just forwarding using \*args and then pass them into the function being forwarded to using *args.

You can write:  
`
<pre>
foo1('yes', True, 100, 3.14, 'hello world')
def foo1(param1, param2, param3, param4, param5):
    foo2(param1, param2, param3, param4, param5)
def foo2(*args):
    foo3(*args)
def foo3(param1, *args):
    print param1
def foo4(param2, param3, param4, param5):
    print '%s %s %s %s' % (param2, param3, param4, param5)
</pre>
<p>`  
foo1() is the long winded way to write it. foo2() just forwards all of the arguments. foo3() takes the first parameter (and prints it) and forwards the four remaining parameters. foo4() finally just prints out the four remaining parameters.

Anyway, the reason I liked it was it removed the horrific evolution overhead of rapidly developing some code. When I wanted to add/remove/consolidate parameters in the code for a lot of related functions using *args made it much simpler to do. You don&#8217;t have to settle for a little less perfect solution because making a minor adjustment is a large amount of work.