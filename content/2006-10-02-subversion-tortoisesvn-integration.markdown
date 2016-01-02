Title: Subversion : TortoiseSVN Integration into Visual Studio
Date: 2006-10-02T09:35:00+00:00
Category: 
Tags: 
Authors: Garry Bodsworth
Slug: subversion-tortoisesvn-integration

<span style="font-weight:bold;"><a href="/2007/07/tortoisesvn-and-visual-studio/">See the update here.</a></span>

This is the easy method of integrating <a href="http://www.tortoisesvn.net">TortoiseSVN</a> into Visual Studio.NET 2003 and 2005 (and probably Visual Studio 6.0).  I'll take it in stages first and show you how to add these useful things to your "External Tools" menu.

TortoiseSVN is kind enough to provide a decent command-line interface for bringing up the dialogs.  This gives us the ability to add External Tools that will operate on the currently open project in Visual Studio.

Here is a script (vbs) that will append the External Tools to the end of your list:
<table style="font-size:75%;border: 1px dashed #2f6fab; background-color: #f9f9f9;"><tr><td><pre>'
' Create the Subversion External Tools for Visual Studio
'

' Set the Visual Studio Version Number so we access the correct
' part of the registry for External Tools.
' Visual Studio.NET      = "7.0"
' Visual Studio.NET 2003 = "7.1"
' Visual Studio.NET 2005 = "8.0"
Dim strVisualStudioVersionNumber
strVisualStudioVersionNumber = "8.0"

Dim strTortoiseSVNBin
strTortoiseSVNBin = "c:\\program files\\TortoiseSVN\\bin\\"

' Create the scripting shell object
Dim WshShell
Set WshShell = WScript.CreateObject("WScript.Shell")

' Function to install an external tool
function WriteExternalTool( strVersionNumber, _
    iToolNumber, _
    strTitle, _
    strCommandLine, _
    strArgs, _
    strWorkingDir, _
    strSource, _
    strOptions)
 ' NOTES (from Google Groups):
 ' ToolTitle<your tool number>:
 '   stores the name of your tool
 ' ToolCmd<your tool number>:
 '   stores the path to your tool
 ' ToolArg<your tool number>: 
 '   stores the command line arguments for your tool.
 '   Set this to a blank string if your tool takes no arguments.
 ' ToolDir<your tool number>:
 '   stores the initial directory from which your tool
 '   should be run.  Set this to a blank string if you don't care where your tool
 '   is run from.
 ' ToolOpt<your tool number>:
 '   stores the settings for the checkboxes at the
 '   bottom of the external tools dialog.  The easiest way to determine what
 '   value you should set, is to create your tool once manually with the
 '   checkboxes set the way you like, and then exit visual studio.  Then look up
 '   the value that's written to this regkey.  The value that this registry
 '   entries got set to is the value your installer should set. 
 
 Dim strTitleKey, strCommandLineKey, strArgsKey, strWorkingDirKey, strSourceKey, strOptionsKey
 ' Construct the keys we will be adding to as strings.  These depend on the number of the tool.
 strTitleKey =  "HKEY_CURRENT_USER\Software\Microsoft\VisualStudio\" & _
     strVersionNumber & "\External Tools\ToolTitle" & iToolNumber
 strCommandLineKey = "HKEY_CURRENT_USER\Software\Microsoft\VisualStudio\" & _
     strVersionNumber & "\External Tools\ToolCmd" & iToolNumber
 strArgsKey =  "HKEY_CURRENT_USER\Software\Microsoft\VisualStudio\" & _
     strVersionNumber & "\External Tools\ToolArg" & iToolNumber
 strWorkingDirKey = "HKEY_CURRENT_USER\Software\Microsoft\VisualStudio\" & _
     strVersionNumber & "\External Tools\ToolDir" & iToolNumber
 strSourceKey =  "HKEY_CURRENT_USER\Software\Microsoft\VisualStudio\" & _
     strVersionNumber & "\External Tools\ToolSourceKey" & iToolNumber
 strOptionsKey =  "HKEY_CURRENT_USER\Software\Microsoft\VisualStudio\" & _
     strVersionNumber & "\External Tools\ToolOpt" & iToolNumber
 
 ' Write out the contents of an external tool 
 WshShell.RegWrite strTitleKey, strTitle
 WshShell.RegWrite strCommandLineKey, strCommandLine
 WshShell.RegWrite strArgsKey, strArgs
 WshShell.RegWrite strWorkingDirKey, strWorkingDir
 WshShell.RegWrite strSourceKey, strSource
 WshShell.RegWrite strOptionskey, strOptions, "REG_DWORD"

 ' Update the count of external tools for the benefit of Visual Studio
 WshShell.RegWrite "HKEY_CURRENT_USER\Software\Microsoft\VisualStudio\" & _
     strVersionNumber & _
     "\External Tools\ToolNumKeys", _
    iToolNumber + 1, _
    "REG_DWORD"
 
 WriteExternalTool = (iToolNumber + 1)
end function

' Get the number of current external tools as this will tell us where to start the numbering
Dim iNumTools
iNumTools = WshShell.RegRead( "HKEY_CURRENT_USER\Software\Microsoft\VisualStudio\" & _
    strVisualStudioVersionNumber & _
    "\External Tools\ToolNumKeys")

' Install Subversion Tools

' The order is:
'   SVN Commit
'   SVN Update
'   SVN History
'   SVN Diff
'   SVN Blame
'   SVN Revert
'   SVN Modifications
'   SVN Repository
'   SVN Project History
'   SVN Settings

iNumTools = WriteExternalTool( strVisualStudioVersionNumber, _
    iNumTools, _
    "SVN Commit", _
    strTortoiseSVNBin & "tortoiseproc.exe", _
    "/command:commit /path:""$(SolutionDir)"" /notempfile", _
    "$(SolutionDir)", _
    "", _
    17)

iNumTools = WriteExternalTool( strVisualStudioVersionNumber, _
    iNumTools, _
    "SVN Update", _
    strTortoiseSVNBin & "tortoiseproc.exe", _
    "/command:update /path:""$(SolutionDir)"" /notempfile", _
    "$(SolutionDir)", _
    "", _
    17)
    
iNumTools = WriteExternalTool( strVisualStudioVersionNumber, _
    iNumTools, _
    "SVN History", _
    strTortoiseSVNBin & "tortoiseproc.exe", _
    "/command:log /path:""$(ItemPath)"" /notempfile", _
    "$(ItemDir)", _
    "", _
    17)
    
iNumTools = WriteExternalTool( strVisualStudioVersionNumber, _
    iNumTools, _
    "SVN Diff", _
    strTortoiseSVNBin & "tortoiseproc.exe", _
    "/command:diff /path:""$(ItemPath)"" /notempfile", _
    "$(ItemDir)", _
    "", _
    17)

iNumTools = WriteExternalTool( strVisualStudioVersionNumber, _
    iNumTools, _
    "SVN Blame", _
    strTortoiseSVNBin & "tortoiseproc.exe", _
    "/command:blame /path:""$(ItemPath)"" /notempfile", _
    "$(ItemDir)", _
    "", _
    17)

iNumTools = WriteExternalTool( strVisualStudioVersionNumber, _
    iNumTools, _
    "SVN Revert", _
    strTortoiseSVNBin & "tortoiseproc.exe", _
    "/command:revert /path:""$(SolutionDir)"" /notempfile", _
    "$(SolutionDir)", _
    "", _
    17)

iNumTools = WriteExternalTool( strVisualStudioVersionNumber, _
    iNumTools, _
    "SVN Modifications", _
    strTortoiseSVNBin & "tortoiseproc.exe", _
    "/command:repostatus /path:""$(SolutionDir)"" /notempfile", _
    "$(SolutionDir)", _
    "", _
    17)

iNumTools = WriteExternalTool( strVisualStudioVersionNumber, _
    iNumTools, _
    "SVN Repository", _
    strTortoiseSVNBin & "tortoiseproc.exe", _
    "/command:repobrowser /path:""$(SolutionDir)"" /notempfile", _
    "$(SolutionDir)", _
    "", _
    17)

iNumTools = WriteExternalTool( strVisualStudioVersionNumber, _
    iNumTools, _
    "SVN Project History", _
    strTortoiseSVNBin & "tortoiseproc.exe", _
    "/command:log /path:""$(SolutionDir)"" /notempfile", _
    "$(SolutionDir)", _
    "", _
    17)

iNumTools = WriteExternalTool( strVisualStudioVersionNumber, _
    iNumTools, _
    "SVN Settings", _
    strTortoiseSVNBin & "tortoiseproc.exe", _
    "/command:settings /path:""$(SolutionDir)"" /notempfile", _
    "$(SolutionDir)", _
    "", _
    17)

' Reset the scripting shell object
set WshShell = nothing</pre></td></tr></table>
<a href="http://garry.bodsworth.googlepages.com/SubversionInstall.zip">Download the script from this link</a>

You can set your Visual Studio version by setting the <span style="font-style: italic;">strVisualStudioVersionNumber</span> variable according to the comment.

If your TortoiseSVN is not in the default installation location change the <span style="font-style: italic;">strTortoiseSVNBin </span>variable (making sure you use \\ as separators).

I am not a vbs expert but I tried to make this script as reusable as possible, especially with respect to writing the external tools to the registry.  This should work with any external tools you may want to add via this script.  There are probably some TortoiseSVN features that should be added as well, but I have got by on what is in that script so far.

For the next part I will describe how to make a toolbar to access the new External Tools.