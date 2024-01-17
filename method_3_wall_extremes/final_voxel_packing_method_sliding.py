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

# relative path to particle-wall sliding friction study

study = os.path.join("10_mm_diameter_particles", "sliding_pw")

# list extreme particle-particle interactions to investigate

glob_input_study = os.path.join(study, "sliding_*")
study = natsorted([k for k in glob.glob(glob_input_study)])

# setting up list of final packing density values

voxel_density_bank = []

# setting up list of column names

columns = []

for study_directory in study:

    # setting up seed values to run through

    glob_input_seeds = os.path.join(study_directory, "seed_*")
    seeds = natsorted([k for k in glob.glob(glob_input_seeds)])

    for seed in seeds:
            
        # assigning column names

        column_name_part_1 = os.path.basename(os.path.normpath(study_directory)) 
        column_name_part_2 = os.path.basename(os.path.normpath(seed))
        my_separator = '_'
        column_name = my_separator.join([column_name_part_1, column_name_part_2])

        columns.append(column_name)

        glob_input_directories = os.path.join(seed, "sliding_*")
        directories = natsorted([k for k in glob.glob(glob_input_directories)])

        # assigning row names

        rows = []
        voxel_density_list = []

        for directory in directories:

            row_data = os.path.basename(os.path.normpath(directory))
            _, row_value = row_data.split("_")
            rows.append(float(row_value))

            # the final packing arrangement file

            glob_input = os.path.join(directory, "post", "particles_*")
            files = natsorted([f for f in glob.glob(glob_input) if "boundingBox" not in f])
            end_file = files[-1]

            cylinder_glob_input = os.path.join(directory, "post", "mesh_*")
            cylinder_files = natsorted([f for f in glob.glob(cylinder_glob_input)])
            cylinder_end_file = cylinder_files[-1]

            print(end_file)
            data = pv.read(end_file)

            print(cylinder_end_file)
            cylinder_data = pv.read(cylinder_end_file)
            

            # setting domain limits of Konigcell
            
            z_low = min(data.points[:,2]) + 0.25*(max(data.points[:,2]) - min(data.points[:,2]))
            z_up = min(data.points[:,2]) + 0.75*(max(data.points[:,2]) - min(data.points[:,2]))
        
            x_low = cylinder_data.bounds[0]
            x_up = cylinder_data.bounds[1]

            y_low = cylinder_data.bounds[2]
            y_up = cylinder_data.bounds[3]

            z_lim = [z_low, z_up]
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
            
            voxel_region = (x_up - x_low)*(y_up - y_low)
            cylinder_region = np.pi*((x_up - x_low)**2)/4
            cylinder_fraction = cylinder_region/voxel_region

            print(f"cylinder region: {cylinder_region}\n")
            print(f"voxel region: {voxel_region}\n")
            print(f"cylinder fraction: {cylinder_fraction}\n")

        
            voxels.voxels[:] /= np.prod(voxels.voxel_size)

            pixels = kc.Pixels(
                np.mean(voxels.voxels, axis=1),
                xlim = voxels.xlim,
                ylim = voxels.zlim,
            )
                
            ypoints = np.mean(pixels.pixels, axis = 0)/cylinder_fraction
        
            # determining packing density between z_min and z_max
        
            voxels_packing_density = np.mean(ypoints)
            voxel_density_list.append(voxels_packing_density)
            
        voxel_density_bank.append(voxel_density_list)
voxel_density_bank = np.asarray(voxel_density_bank).T

# writing data to csv file

df = pd.DataFrame(voxel_density_bank, columns = columns, index = rows)
df.to_csv('final_voxel_packing_sliding_results_batch.csv', index = True)