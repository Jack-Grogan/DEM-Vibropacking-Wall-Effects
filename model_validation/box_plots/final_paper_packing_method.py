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
import os
import pyvista as pv
import glob
from natsort import natsorted
import pandas as pd

# box dimensions

x_len = 0.12
y_len = 0.12

# relative path to study

study = os.path.join("10_mm_diameter_particles")

glob_input_study = os.path.join(study, "*")
study = natsorted([k for k in glob.glob(glob_input_study)])

density_bank = []
columns = []
rows = []


for study_directory in study:

    # setting up seed values to run through

    glob_input_seeds = os.path.join(study_directory, "seed_*")
    seeds = natsorted([k for k in glob.glob(glob_input_seeds)])

    density_list = []

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

        # region between which packing density is calculated

        z_low = min(data.points[:,2]) + 0.25*(max(data.points[:,2]) - min(data.points[:,2]))
        z_upp = min(data.points[:,2]) + 0.75*(max(data.points[:,2]) - min(data.points[:,2]))
        z_lim = [z_low, z_upp]

        # volume of spheres within the region between z_min and z_max

        particle_volume = []

        for i in range(len(data.points)):
            if z_lim[0] <= data.points[i,2] <= z_lim[1]:
                vol = 4/3*np.pi*data["radius"][i]**3
                particle_volume.append(vol)

        particle_v = sum(particle_volume)

        # volume of region in which spheres lie

        box_v = (z_lim[1] - z_lim[0])*x_len*y_len

        # determining packing density between z_min and z_max

        packing_density = particle_v/box_v
        density_list.append(packing_density)

    density_bank.append(density_list)
density_bank = np.asarray(density_bank).T

# writing data to csv file

df = pd.DataFrame(density_bank, columns = columns, index = rows)
df.to_csv('final_paper_packing_results.csv', index = True)