Title: The real important feature of C++
Date: 2012-04-09T21:13:00+00:00
Slug: real-important-feature-of-c
Category: 
Tags: 
Authors: Garry Bodsworth

<p>I've been having to write a lot of C code recently, and it makes me pine for some features of C++ because of the verbosity of some portions of code. It made me consider what really changes the way you code in C++ on comparison to C.</p><p>&nbsp;</p><p>There are features like inheritance, but that really just manages the function overriding that is implicit.  There is templates whilst discounting template meta programming is just a glorified way of avoiding code duplication.  There is obviously the more aggressive type checking which is handy but doesn't really change that much about your coding style.</p><p>&nbsp;</p><p>So what is this feature?  Destructors.  Immediately by adding that feature you change the way you can code and also by avoiding some C verbosity you avoid memory leaks.  This opens up the whole realm of RAII and the code scoping rules start to take on a different life because you can execute code when objects begin to fall out of scope and are freed.  This code then kind of discourages gotos (I really hate those) because you are relying more on the stack unwinding than remembering to malloc/free.</p><p>&nbsp;</p><p> I reckon if I had destructors for the C code I have written in the context of structs then I could have had a lot less code.</p><p>&nbsp;</p>
