//      ___  ________  ________  ___  __            ________     
//     |\  \|\   __  \|\   ____\|\  \|\  \         |\   ____\    
//     \ \  \ \  \|\  \ \  \___|\ \  \/  /|_       \ \  \___|    
//   __ \ \  \ \   __  \ \  \    \ \   ___  \       \ \  \  ___  
//  |\  \\_\  \ \  \ \  \ \  \____\ \  \\ \  \       \ \  \|\  \ 
//  \ \________\ \__\ \__\ \_______\ \__\\ \__\       \ \_______\
//   \|________| \|__|\|__|\|_______|\|__| \|__|       \|_______|
//                             

h   = {{ cylinder_height }};
r   = {{ cylinder_radius }};
z0  = {{ z_0 }};
x0  = {{ x_0 }};
y0  = {{ y_0 }};
lc  = {{ lc }};

// -----------------------------------------------------------------
// Defining points 
// -----------------------------------------------------------------

Point(1) = {x0, y0, z0, lc};  // Base plate centre

// Points on circle

Point(2) = {x0 + r, y0, z0, lc};
Point(3) = {x0, y0 + r, z0, lc};
Point(4) = {x0 - r, y0, z0, lc};
Point(5) = {x0, y0 - r, z0, lc};

// -----------------------------------------------------------------
// Defining lines 
// -----------------------------------------------------------------

Circle(1) = {2, 1, 3};
Circle(2) = {3, 1, 4};
Circle(3) = {4, 1, 5};
Circle(4) = {5, 1, 2};

Line loop(1) = {1, 2, 3, 4};
Plane Surface(1) = {1};

Extrude {0,0,h} {Surface{1};}
// Specify some meshing size constraints

Mesh.MeshSizeFromPoints = 0;
Mesh.MeshSizeFromCurvature = 0;
Mesh.MeshSizeExtendFromBoundary = 0;
Mesh.MeshSizeMin = {{ mesh_min }};
Mesh.MeshSizeMax = {{ mesh_max }};
Mesh.Algorithm   = {{ Algor }};
Mesh.TransfiniteTri = 1;

Mesh 2;
Save "shake_cylinder.stl";