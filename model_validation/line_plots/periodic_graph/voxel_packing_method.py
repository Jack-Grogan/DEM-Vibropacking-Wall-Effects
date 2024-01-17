"""
@author: Jack Richard Grogan

      ___  ________  ________  ___  __            ________
     |\  \|\   __  \|\   ____\|\  \|\  \         |\   ____\
     \ \  \ \  \|\  \ \  \___|\ \  \/  /|_       \ \  \___|
   __ \ \  \ \   __  \ \  \    \ \   ___  \       \ \  \  ___
  |\  \\_\  \ \  \ \  \ \  \____\ \  \\ \  \       \ \  \|\  \
  \ \________\ \__\ \__\ \_______\ \__\\ \__\       \ \_______\
   \|________|\|__|\|__|\|_______|\|__| \|__|        \|_______|

"""

import numpy as np
import pyvista as pv
import konigcell as kc
import os
from pathlib import Path
import glob
from natsort import natsorted
import pandas as pd

# relative path to particle-wall restitution study

directory ="post"
print(directory)

columns = []
time_bank = []
density_bank = []

# cube dimensions

x_len = 0.12
y_len = 0.12

# calculate packing density half a particle radius from the periodic boundary
# avoids inaccurate packing density while particles passing through the periodic boundary wall

len_adjust = 0.005

# time between simulation files

dump_time = 0.0079

# setting up files to run through

directory_name = os.path.basename(os.path.normpath(directory))

# assigning column names

columns.append(directory_name)

glob_input = os.path.join(directory, "particles_*.vtk")

files = natsorted([f for f in glob.glob(glob_input) if "boundingBox" not in f])
files = files[1::]

# running through files

for file in files:

    print(file)
    data = pv.read(file)

    # setting domain limits of Konigcell

    z_low = min(data.points[:,2]) + 0.25*(max(data.points[:,2]) - min(data.points[:,2]))
    z_upp = min(data.points[:,2]) + 0.75*(max(data.points[:,2]) - min(data.points[:,2]))

    x_low = -x_len/2 + len_adjust
    x_up = x_len/2 - len_adjust

    y_low = -y_len/2 + len_adjust
    y_up = y_len/2 - len_adjust

    z_lim = [z_low, z_upp]
    y_lim = [y_low, y_up]
    x_lim = [x_low, x_up]

    # Setting voxel resolution in x y and z

    res_x = 100
    res_y = 100
    res_z = 100

    # Voxelising data

    voxels = kc.static3d(data.points,
                        kc.INTERSECTION,
                        radii = data["radius"],
                        resolution = (res_x,  res_y, res_z),
                        xlim = x_lim,
                        ylim = y_lim,
                        zlim = z_lim,
                        max_workers = 1,
                        )

    voxels.voxels[:] /= np.prod(voxels.voxel_size)

    pixels = kc.Pixels(
        np.mean(voxels.voxels, axis=1),
        xlim = voxels.xlim,
        ylim = voxels.zlim,
    )

    ypoints = np.mean(pixels.pixels, axis = 0)
    xpoints = np.linspace(pixels.ylim[0], pixels.ylim[1], len(ypoints))

    # determining packing density between z_min and z_max

    voxels_packing_density = np.mean(ypoints)
    density_bank.append(voxels_packing_density)

density_bank = np.asarray(density_bank).T
print(density_bank)

# Generating time data

for j in range(len(density_bank)):
    time_bank.append((j+1)*dump_time)

time_bank =np.asarray(time_bank).T
print(time_bank)

# writing data to csv file

df1 = pd.DataFrame(density_bank, columns = columns)
df2 = pd.DataFrame(time_bank, columns =['Time'])
df = pd.concat([df2, df1], axis = 1, ignore_index = False, sort = False)
df.to_csv('voxel_packing_results_periodic.csv', index = True)