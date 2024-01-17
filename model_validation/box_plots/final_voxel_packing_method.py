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
import os
import glob
from natsort import natsorted
import pandas as pd
import konigcell as kc

# box dimensions

x_len = 0.12
y_len = 0.12

# calculate packing density half a particle radius from the periodic boundary
# avoids inaccurate packing density while particles passing through the periodic boundary wall

len_adjust = 0.005

# relative path to study

study = os.path.join("10_mm_diameter_particles")

glob_input_study = os.path.join(study, "*")
study = natsorted([k for k in glob.glob(glob_input_study)])

voxel_density_bank = []
columns = []
rows = []


for study_directory in study:

    # setting up seed values to run through

    glob_input_seeds = os.path.join(study_directory, "seed_*")
    seeds = natsorted([k for k in glob.glob(glob_input_seeds)])

    voxel_density_list = []
    
    # assigning column names

    column_name = os.path.basename(os.path.normpath(study_directory))
    columns.append(column_name)
    
    rows = []

    for seed in seeds:
        
        # assigning row names

        row_name = os.path.basename(os.path.normpath(seed))
        rows.append(row_name)

        # the final packing arrangement file

        glob_input = os.path.join(seed, "post", "particles_*")
        files = natsorted([f for f in glob.glob(glob_input) if "boundingBox" not in f])
        end_file = files[-1]

        print(end_file)
        data = pv.read(end_file)

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
        voxel_density_list.append(voxels_packing_density)
    voxel_density_bank.append(voxel_density_list)

voxel_density_bank = np.asarray(voxel_density_bank).T

# writing data to csv file

df = pd.DataFrame(voxel_density_bank, columns = columns, index = rows)
df.to_csv('final_voxels_packing_results.csv', index = True)