Title: GUI Toolkits - Mythos
Date: 2008-03-04T19:28:00+00:00
Slug: gui-toolkits-mythos
Category: 
Tags: 
Authors: Garry Bodsworth

A while back I <a href="http://garrys-brain.blogspot.com/2007/10/gui-toolkits-some-thoughts.html">blogged about some ideas</a> for GUI toolkits, not that I ever managed to get off my backside and do something about it.

Well someone has done a great job with a DSEL (domain specific embedded language) with a toolkit called <a href="http://code.google.com/p/mythos/">Mythos</a>.  To quote the website <span style="font-style:italic;">"Mythos is a GUI library written in C++ using modern C++ techniques."</span>  It does state on the website that it is more of a proof of concept than a fully-blown attempt.

Still, it looks really interesting and has a few different components that make it up.  There is <span style="font-weight:bold;">khaos</span> which does the low level windowing bits and pieces.  <span style="font-weight:bold;">nyx</span> is the window layout library with a DSEL that lets you define the ayout in the C++ files.  <span style="font-weight:bold;">iris</span> does the event handling with another DSEL for associating events and actions.  <span style="font-weight:bold;">gaia</span> is the widget abstraction.

Overall it looks like a very interesting use of modern C++ applied to GUI toolkits.  It is a different approach to something like <a href="http://stlab.adobe.com/">Adobe's ASL</a> (adam and eve) but I think if the use of the code generation available through templates should be used to take the legwork out of defining user interfaces.  Mythos, which is the work of one person as far as I can tell (Benaka Moorthi) is a pretty neat accomplishment.
