//      ___  ________  ________  ___  __            ________     
//     |\  \|\   __  \|\   ____\|\  \|\  \         |\   ____\    
//     \ \  \ \  \|\  \ \  \___|\ \  \/  /|_       \ \  \___|    
//   __ \ \  \ \   __  \ \  \    \ \   ___  \       \ \  \  ___  
//  |\  \\_\  \ \  \ \  \ \  \____\ \  \\ \  \       \ \  \|\  \ 
//  \ \________\ \__\ \__\ \_______\ \__\\ \__\       \ \_______\
//   \|________| \|__|\|__|\|_______|\|__| \|__|       \|_______|
//                             

base_length = {{ square_size }};
x0          = {{ x0_square }};
y0          = {{ y0_square }};
z0          = {{ z0_square }};
lc          = {{ lc_square }};

Point(1) = {x0 - base_length/2, y0 - base_length/2 , z0, lc};
Point(2) = {x0 - base_length/2, y0 + base_length/2 , z0, lc};
Point(3) = {x0 + base_length/2, y0 + base_length/2 , z0, lc};
Point(4) = {x0 + base_length/2, y0 - base_length/2 , z0, lc};

Line(1) = {1, 2};
Line(2) = {2, 3};
Line(3) = {3, 4};
Line(4) = {4, 1};

Line loop(1) = {1, 2, 3, 4};
Plane Surface(1) = {1};

Mesh.MeshSizeFromPoints = 0;
Mesh.MeshSizeFromCurvature = 0;
Mesh.MeshSizeExtendFromBoundary = 0;
Mesh.MeshSizeMin = {{ mesh_min }};
Mesh.MeshSizeMax = {{ mesh_max }};
Mesh.Algorithm   = {{ Algor }};
Mesh.TransfiniteTri = 1;

Mesh 2;
Save "shake_base.stl";
