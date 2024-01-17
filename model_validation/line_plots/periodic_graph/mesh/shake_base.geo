//      ___  ________  ________  ___  __            ________     
//     |\  \|\   __  \|\   ____\|\  \|\  \         |\   ____\    
//     \ \  \ \  \|\  \ \  \___|\ \  \/  /|_       \ \  \___|    
//   __ \ \  \ \   __  \ \  \    \ \   ___  \       \ \  \  ___  
//  |\  \\_\  \ \  \ \  \ \  \____\ \  \\ \  \       \ \  \|\  \ 
//  \ \________\ \__\ \__\ \_______\ \__\\ \__\       \ \_______\
//   \|________| \|__|\|__|\|_______|\|__| \|__|       \|_______|
//                             

base_length = 0.122;
x0          = 0;
y0          = 0;
z0          = 0;
lc          = 0.01;

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
Mesh.MeshSizeMin = 0.005;
Mesh.MeshSizeMax = 0.005;
Mesh.Algorithm   = 6;
Mesh.TransfiniteTri = 1;

Mesh 2;
Save "shake_base.stl";