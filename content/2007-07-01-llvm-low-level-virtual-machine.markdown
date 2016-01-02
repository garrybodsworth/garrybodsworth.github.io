Title: LLVM - Low-Level Virtual Machine
Date: 2007-07-01T14:15:00+00:00
Slug: llvm-low-level-virtual-machine
Category: 
Tags: 
Authors: Garry Bodsworth

Recently there has been a lot of development on the <a href="http://llvm.org/">Low-Level Virtual Machine (LLVM)</a>.  It provides a back-end for compilers to allow for optimisation for the entire lifetime of the program.

The GLSL in Mesa has been implemented using LLVM.  You can read a little about it <a href="http://zrusin.blogspot.com/2007/05/mesa-and-llvm.html">here</a>.  The OpenGL implementation in <a href="http://macslash.org/article.pl?sid=06/08/18/1248220">Mac OSX Leopard will be implemented using LLVM</a>.

There is an interesting article <a href="http://cliffhacks.blogspot.com/2007/03/experimenting-with-llvm.html">here</a> about the speed of LLVM.  It is surprising how close it gets in speed as things currently stand to GCC.

Recently there was a development meeting for LLVM in May and the presentations are available <a href="http://llvm.org/devmtg/2007-05/index.html">here</a>.  Of particular interest is the presentation by Apple about a new C front-end for LLVM called Clang with plans to support Objective C and C++.  You can read the slides <a href="http://llvm.org/devmtg/2007-05/09-Naroff-CFE.pdf">here</a> and see the presentation <a href="http://llvm.org/devmtg/2007-05/09-Naroff-CFE.mov">here</a>.  The new frontend is called Clang and probably won't be production ready for a while but it is interesting to see where compiler technologies are heading.

The most interesting area of LLVM is definitely the whole program optimisation potential of it.  Anyone who has seen the performance gains from using it knows this is good thing.
