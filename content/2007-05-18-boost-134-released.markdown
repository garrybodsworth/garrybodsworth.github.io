Title: Boost 1.34 Released
Date: 2007-05-18T20:45:00+00:00
Slug: boost-134-released
Category: 
Tags: 
Authors: Garry Bodsworth

The latest version of the <a href="http://www.boost.org">Boost</a> Library has been released.  This is version 1.34 and you can read the changes on the <a href="http://www.boost.org/">Boost frontpage</a>.

Boost is a fantastic peer reviewed library collection for C++.  It adds power and robustness for C++ programmers, after all we shouldn't need to reinvent the wheel all of the time.

There are five new libraries:
     * Foreach Library:
         BOOST_FOREACH macro for easily iterating over the elements of a
         sequence, from Eric Niebler.
     * Statechart Library:
         Arbitrarily complex finite state machines can be implemented in
         easily readable and maintainable C++ code, from Andreas Huber.
     * TR1 Library:
         An implementation of the C++ Technical Report on Standard Library
         Extensions, from John Maddock.
         This library does not itself implement the TR1 components, rather
         it's a thin wrapper that will include your standard library's TR1
         implementation (if it has one), otherwise it will include the Boost
         Library equivalents, and import them into namespace std::tr1. Highlights
         include: Reference Wrappers, Smart Pointers, result_of,
         Function Object Binders, Polymorphic function wrappers, Type Traits,
         Random Number Generators and Distributions, Tuples, Fixed Size Array,
         Hash Function Objects, Regular Expressions and
         Complex Number Additional Algorithms.
     * Typeof Library:
         Typeof operator emulation, from Arkadiy Vertleyb and Peder Holt.
     * Xpressive Library:
         Regular expressions that can be written as strings or as expression
         templates, and that can refer to each other and themselves recursively
         with the power of context-free grammars, from Eric Niebler. 

Obviously lots of the other libraries have been updated like Boost::Python.
