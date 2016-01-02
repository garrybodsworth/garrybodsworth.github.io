Title: More Vista and OpenGL
Date: 2006-11-24T21:53:00+00:00
Slug: more-vista-and-opengl
Category: 
Tags: 
Authors: Garry Bodsworth

I finally got to the bottom of my outstanding OpenGL problem on Vista.  It seems that the drivers were throwing floating point exceptions in random places, I tidied up the code as much as possible but it still happened.  The only way to get around this problem was to not unmask the floating point exceptions in the thread performing the OpenGL rendering (although most applications seem not to unmask floating point exceptions as I have discovered).

I imagine when the drivers are as mature as the XP drivers these will be but a distant memory, as in the olden days the way the OpenGL drivers handled exceptions was pretty random.

One thing I want to reiterate is that OpenGL works seamlessly on Vista with the dwm Aero experience.  People still think they have to migrate away from OpenGL to DirectX/Direct3D, I cannot emphasise enough this is not the case.  I know some companies still haven't managed to filter through that information, but it is the case and the computer I am using is evidence of that.

So spread the word OpenGL is fully compatible and runs natively with Windows Vista!
