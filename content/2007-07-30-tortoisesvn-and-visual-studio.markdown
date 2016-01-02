Title: TortoiseSVN and Visual Studio Integration - Visual Studio 2008
Date: 2007-07-30T20:12:00+00:00
Slug: tortoisesvn-and-visual-studio
Category: 
Tags: 
Authors: Garry Bodsworth

Finally, I am getting around to an update to the TortoiseSVN Visual Studio Integration.  The catalyst for this is the release of Visual Studio 2008 (formally codename Orcas) Beta 2, and making sure I can still play with Subversion through the IDE.

I have made a new distribution ZIP file with a few more configurations inside.

<span style="font-weight: bold;"><a href="http://garry.bodsworth.googlepages.com/Subversion.zip">Download it here.</a></span>

It has a few more features than before including some for dealing with conflicts.  The distribution itself has a few more files so you can decide whether you want to just have the menus, toolbars or context menus.

<a onblur="try {parent.deselectBloggerImageGracefully();} catch(e) {}" href="http://4.bp.blogspot.com/_1xvreyfQ6ns/Rq5I_talWbI/AAAAAAAAAAM/55l1sNrJM7o/s1600-h/Toolbar.png"><img style="cursor:pointer; cursor:hand;" src="http://4.bp.blogspot.com/_1xvreyfQ6ns/Rq5I_talWbI/AAAAAAAAAAM/55l1sNrJM7o/s320/Toolbar.png" border="0" alt=""id="BLOGGER_PHOTO_ID_5093088487962663346" /></a>

<span style="font-weight: bold;">Supported operations</span>

The following Subversion/TortoiseSVN features are covered in the integration:<br /><ul><li><span style="font-weight: bold;">Commit</span> - Commit the files to the repository</li><li><span style="font-weight: bold;">Update</span> - Update the current working version</li><li><span style="font-weight: bold;">History</span> - Get the history for the selected file</li><li><span style="font-weight: bold;">Diff</span> - Get the diff compared to the base version</li><li><span style="font-weight: bold;">Blame</span> - Find out who committed the crimes in the file</li><li><span style="font-weight: bold;">Revert</span> - Undo changes</li><li><span style="font-weight: bold;">Modifications</span> - Check to see if any files have been modified</li><li><span style="font-weight: bold;">Edit Conflicts</span> - Edit the conflicts that arise from merging/updating</li><li><span style="font-weight: bold;">Resolve</span> - Mark the file as resolved for conflicts</li><li><span style="font-weight: bold;">Repository</span> - View the repository on the server</li><li><span style="font-weight: bold;">Project History</span> - Get the history of the entire project</li><li><span style="font-weight: bold;">Add Solution</span> - Add the solution being edited to source control</li><li><span style="font-weight: bold;">Branch/Tag</span> - Perform a branch or tag operation on the current working copy</li><li><span style="font-weight: bold;">Settings</span> - Set up TortoiseSVN</li></ul><span style="font-weight: bold;">SubversionInstall.vbs</span>

This simply installs a set of External Tools into Visual Studio for common TortoiseSVN operations.  It can be installed on versions above Visual Studio.NET (version 7.0).  Currently it is configured for Visual Studio 2008 (version 9.0), to make it work on other versions change the variable "strVisualStudioVersionNumber" as outlined in the file's comments.

Also, if you have installed TortoiseSVN in a non-default location, make sure that you change the variable "strTortoiseSVNBin" to the correct binary path.  Make sure that the backslashes are doubled up.

<span style="font-weight: bold;">SubversionMenu.vssettings</span>

This is a settings file for Visual Studio 2008.

This adds a menu to the IDE for TortoiseSVN with the appropriate icons.

<span style="font-weight: bold;">SubversionMenuToolbar.vssettings</span>

This is a settings file for Visual Studio 2008.

This adds a menu for TortoiseSVN as well as a toolbar using the appropriate icons.

<span style="font-weight: bold;">SubversionMenuToolbarContexts.vssettings</span>

This is a settings file for Visual Studio 2008.

This adds not only the menu and toolbar, but also adds the items to the appropriate context menus for files and solutions.

<span style="font-weight: bold;">SubversionMenuToolbarContextsVS2005.vssettings</span>

This provides the menu, toolbar and context menus for TortoiseSVN in Visual Studio 2005.

Unfortunately there is no good solution for file renaming (I always do it through Windows Explorer) since this integration uses the External tools and allows for it to work in Visual Studio Express.
