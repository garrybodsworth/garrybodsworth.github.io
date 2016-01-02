Title: Visual Studio 2005 and TortoiseSVN Subversion Integration - Update
Date: 2006-11-08T21:12:00+00:00
Slug: visual-studio-2005-and-tortoisesvn
Category: 
Tags: 
Authors: Garry Bodsworth

<span style="font-weight:bold;"><a href="http://garrys-brain.blogspot.com/2007/07/tortoisesvn-and-visual-studio.html">See the update here.</a></span>

Hi there everyone,

Here is an update to the TortoiseSVN integration into Visual Studio 2005.  This update is a fairly major change since this will only have the changes to external tools, menus and toolbars.  This means when you import these settings you get a new menu at the top of the screen (with icons), a new toolbar with proper TortoiseSVN icons, and context menus for solutions and files.

You can download the <a href="http://garry.bodsworth.googlepages.com/SubversionToolbarsAndMenus.zip">new settings file here</a> (it is 9k in size compressed).  All you need to do is go to your Tools menu and choose "Import and Export Settings" and follow the instructions.  Ensure the tick box for which settings to import are all ticked.

Here are the original posts from the Subversion integration (and old files are still available).<br /><ul><li><a href="http://garrys-brain.blogspot.com/2006/10/subversion-and-tortoisesvn-programmers.html">Subversion and TortoiseSVN - A programmers best friend</a></li><li><a href="http://garrys-brain.blogspot.com/2006/10/subversion-tortoisesvn-integration.html">Subversion : TortoiseSVN Integration into Visual Studio</a> - A vbs script that will add Subversion to your external tools in Visual Studio 2003 and 2005.</li><li><a href="http://garrys-brain.blogspot.com/2006/10/subversion-tortoisesvn-integration_03.html">Subversion : TortoiseSVN Integration into Visual Studio.NET 2005 Again</a></li><li><a href="http://garrys-brain.blogspot.com/2006/10/tortoisesvn-vsnet-2005-good-stuff.html">TortoiseSVN + VS.NET 2005 = Good Stuff</a> - The original vssettings based integration with additional screenshots that still apply.</li><li><a href="http://garrys-brain.blogspot.com/2006/10/tools-for-tortoisesvn.html">Tools for TortoiseSVN</a> - Some recommended tools for TortoiseSVN.</li><li><a href="http://garrys-brain.blogspot.com/2006/10/updated-visual-studio-2005-express-and.html">Updated Visual Studio 2005 Express and TortoiseSVN Integration</a> - The first update to the vssettings implementation.</li></ul><br /><a href="http://garry.bodsworth.googlepages.com/SubversionToolbarsAndMenus.zip">DOWNLOAD SETTINGS FILE</a>

<span style="font-weight:bold;">Edit: </span> Now there is a yet another update - this is now 7k.  This makes a minimum of changes to your IDE as humanly (or inhumanly) possible.  There is still a deficiency in the .vssettings that messes up the build toolbar comboboxes, but this seems unfixable in the current format.

Oh, and don't forget to leave some comments as to whether this new stuff is all working for you (along with the new "Add Solution To Repository" functionality.