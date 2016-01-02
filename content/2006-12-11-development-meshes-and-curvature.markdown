Title: Development - Meshes And Curvature
Date: 2006-12-11T22:08:00+00:00
Slug: development-meshes-and-curvature
Category: 
Tags: 
Authors: Garry Bodsworth

I've been racking my brains recently about triangle meshes and curvature.  The problem with triangle meshes is that they don't really want to have decent normals defined for them, especially if your triangles have inflections between them from the generation.

Someone who is much better than me at geometry pointed me at a really good article about normals and curvature from arbitrary meshes.  The article is <a href="http://www.cs.princeton.edu/gfx/pubs/_2004_ECA/index.php">Estimating Curvatures and Their Derivatives on Triangle Meshes</a>.

There are implementations of the ideas in the article in <a href="http://www.cs.princeton.edu/gfx/proj/trimesh2/">trimesh2</a>.  It's worthwhile taking a look at the source code (it's in C/C++) and is fairly self-explanatory if not optimal.

Calculating the normal on an arbitrary mesh is fairly simple if you don't want to be accurate in the slightest.  Just take the average of the triangles that share the point.  This works fairly well if your triangles do not have inflections and they are divided into separate surfaces (or faces depending on your terminology).  The idea behind this paper is to look at regions of points and to get the average of these, but weight them for their distance from the point you are attempting to calculate.

If you store this data it is only a one time calculation hit, so it will not slow down your program.  This type of calculation is perfect for 3D rendering, although I need to see the overall quality in order to determine if it can be used for applications requiring more accurate results like CAD/CAM.
