Title: Writing A Decent Library
Date: 2007-10-29T20:58:00+00:00
Slug: writing-decent-library
Category: 
Tags: 
Authors: Garry Bodsworth

When you are writing a shared library (DLL) you have to put a lot of thought into the public interface which your customer (another programmer) will be using.

What you have to work out is whether it is closed or open source, whether the binaries are supplied, and how you keep the user from having broken interfaces on different versions.  All of this is from the point of view from a C++ programmer.

I think it is best to start with how not to write a closed-source library:<br />* Do not use templates.<br />* Do not have implementation half in the binary and half in the headers.<br />* Do not expose the innards of your program.

When creating a closed-source library you have to firewall the innards (which are probably commercially sensitive) from the interface.  This would mean some use of the <a href="http://c2.com/cgi/wiki?PimplIdiom">Pimpl Idiom</a>.

You need to use solidly defined types like if you were binding to another language like Python.  This means that the implementation can live in the binary and the interface is defined in your headers.

One of the problems it is easy to encounter is when STL is exposed in the library.  The problem occurs when people use different implementations of the standard library which means you either need to maintain versions for that particular setup.

By making those two decisions you can massively simplify the maintenance and the headaches of people trying to implement it.  You have to think carefully about the simplest interface for the developers who have to work out how to integrate it.

By not exposing the innards of the library you can also protect yourself from problems when the library loads/unloads because you can't have conflicting CRTs/libraries.

I suppose what I am suggesting is to have the most simple public interface and make sure that all implementation is hidden away.  Almost only using a C interface for a library means you don't encounter the problems where you have to think about supplying a version for each version of the compiler your users have.
