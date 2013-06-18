---
title: TortoiseSVN Visual Studio Integration
author: Garry Bodsworth
layout: post
categories:
  - Uncategorized
tags:
  - IDE
  - Integration
  - Subversion
  - TortoiseSVN
  - VisualStudio
---
I developed this Visual Studio integration whilst migrating a previous company (NC Graphics) from Visual SourceSafe to the brave new world of [Subversion][1].  Developing is a bit of a strong word since it is only a settings file for Visual Studio, but it does the job admirably in a non-intrusive way and has no performance effects at all on the IDE.

The settings file gives you a new toolbar, a new menu, and new items on the context menus in the solution view.  You get some nice [TortoiseSVN][2] standard icons to make it even easier.

This all works with Visual Studio 2005 and 2008 (and even the Express Editions), along with a standard installation of TortoiseSVN.  Unless you want to edit the commandline in the External Tools I recommend installing TortoiseSVN to the default location.

It&#8217;s quick to set up, just go to your &#8220;Tools&#8221; menu and choose &#8220;Import and Export Settings&#8221; and follow the instructions. Ensure the tick box for which settings to import are all ticked.  If the settings don&#8217;t work first time, try again, as Visual Studio can be a bit flaky when loading.  It will replace your External Tools because they have to be stored in the correct numbered slot due to the way they are implemented in Visual Studio.

Unfortunately renaming is well beyond the external tools implementation I have used.  TortoiseSVN 1.5 does have some additional functionality to rebuild the links for renamed files which is really useful.

[Download Here][3]

<div class="imageframe alignleft">
  <a title="Subversion Toolbar" rel="lightbox[pics4]" href="http://upload.programmerslog.com/toolbar.png"><img class="attachment wp-att-5" src="http://upload.programmerslog.com/toolbar.png" alt="Subversion Toolbar" /></a></p> <p>
    <strong>Supported TortoiseSVN operations</strong>
  </p>
  
  <p>
    The following Subversion/TortoiseSVN features are covered in the integration:
  </p>
  
  <ul>
    <li>
      <em>Commit</em> &#8211; Commit the files to the repository
    </li>
    <li>
      <em>Update</em> &#8211; Update the current working version
    </li>
    <li>
      <em>History</em> &#8211; Get the history for the selected file
    </li>
    <li>
      <em>Diff</em> &#8211; Get the diff compared to the base version
    </li>
    <li>
      <em>Blame</em> &#8211; Find out who committed the crimes in the file
    </li>
    <li>
      <em>Revert</em> &#8211; Undo local changes
    </li>
    <li>
      <em>Modifications</em> &#8211; Check to see if any files have been modified
    </li>
    <li>
      <em>Edit Conflicts</em> &#8211; Edit the conflicts that arise from merging/updating
    </li>
    <li>
      <em>Resolve</em> &#8211; Mark the file as resolved for conflicts
    </li>
    <li>
      <em>Repository</em> &#8211; View the repository on the server
    </li>
    <li>
      <em>Project History</em> &#8211; Get the history of the entire project
    </li>
    <li>
      <em>Add Solution</em> &#8211; Add the solution being edited to source control
    </li>
    <li>
      <em>Branch/Tag</em> &#8211; Perform a branch or tag on the current working copy
    </li>
    <li>
      <em>Settings</em> &#8211; Set up TortoiseSVN
    </li>
  </ul>
  
  <p>
    <strong>Files In The Distribution</strong>
  </p>
  
  <p>
    <strong>SubversionMenu.vssettings</strong>
  </p>
  
  <p>
    This is a settings file for Visual Studio 2008.  This adds a menu to the IDE for TortoiseSVN with the appropriate icons.
  </p>
  
  <p>
    <strong>SubversionMenuToolbar.vssettings</strong>
  </p>
  
  <p>
    This is a settings file for Visual Studio 2008.  This adds a menu for TortoiseSVN as well as a toolbar using the appropriate icons.
  </p>
  
  <p>
    <strong>SubversionMenuToolbarContexts.vssettings</strong>
  </p>
  
  <p>
    This is a settings file for Visual Studio 2008.  This adds not only the menu and toolbar, but also adds the items to the appropriate context menus for files and solutions.
  </p>
  
  <p>
    <strong>SubversionMenuToolbarContextsVS2005.vssettings</strong>
  </p>
  
  <p>
    This provides the menu, toolbar and context menus for TortoiseSVN in Visual Studio 2005.
  </p>
  
  <p>
    <strong>SubversionInstall.vbs</strong>
  </p>
  
  <p>
    Use this file if you want the external tools only.  These will be appended to the list, otherwise use the settings files.  Don&#8217;t use in addition to the settings file.
  </p>
  
  <p>
    This simply installs a set of External Tools into Visual Studio for common TortoiseSVN operations. It can be installed on versions above Visual Studio.NET (version 7.0). Currently it is configured for Visual Studio 2008 (version 9.0), to make it work on other versions change the variable &#8220;strVisualStudioVersionNumber&#8221; as outlined in the file&#8217;s comments.
  </p>
  
  <p>
    Also, if you have installed TortoiseSVN in a non-default location, make sure that you change the variable &#8220;strTortoiseSVNBin&#8221; to the correct binary path. Make sure that the backslashes are doubled up.
  </p>
  
  <p>
    <a href="http://upload.programmerslog.com/subversion.zip">Download Here</a>
  </p>
</div>

<a rel="license" href="http://creativecommons.org/licenses/by/3.0/"><img alt="Creative Commons License" style="border-width:0" src="http://i.creativecommons.org/l/by/3.0/88x31.png" /></a>  
This work is licenced under a <a rel="license" href="http://creativecommons.org/licenses/by/3.0/">Creative Commons Licence</a>.

 [1]: http://subversion.tigris.org/
 [2]: http://tortoisesvn.net/
 [3]: http://upload.programmerslog.com/subversion.zip