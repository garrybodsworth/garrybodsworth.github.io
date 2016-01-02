Title: More Vista - Menus
Date: 2006-11-28T12:18:00+00:00
Slug: more-vista-menus
Category: 
Tags: 
Authors: Garry Bodsworth

One thing I have been continually sidetracked from sorting out recently is menus for Windows Vista.

Currently we use DrawItem() and MeasureItem() to custom draw the menu items so that they have icons next to the items.  Unfortunately on Vista the custom drawing of the base implementation of DrawItem() simply does not look right under Vista.  It utilises the solid dark blue bar when you hover the mouse and the spacings look odd, and this is the default implementation.  Also, the background colour is a little darker and the disabled text does not look very good.  Without the custom draw functions it integrates much better in Vista, but I need to finish implementing some code for the associated icons.

So, I was using Windows Explorer under Vista and realised the context menus have EXACTLY the same problem.  This is just completely insane, they obviously implemented the functionality in exactly the same way, but the underlying Windows API could not have been updated for this.
