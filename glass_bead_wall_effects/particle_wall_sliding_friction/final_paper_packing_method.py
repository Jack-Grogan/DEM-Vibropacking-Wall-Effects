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
import toml

# relative path to particle-wall restitution study

study_directory ="10_mm_diameter_particles"

density_bank = []
columns = []

# setting up seed values to run through

glob_input_seeds = os.path.join(study_directory, "seed_*")
seeds = natsorted([k for k in glob.glob(glob_input_seeds)])

for seed in seeds:

    # assigning column names

    column_name = os.path.basename(os.path.normpath(seed))
    columns.append(column_name)

    glob_input_directories = os.path.join(seed, "sliding_*")
    directories = natsorted([k for k in glob.glob(glob_input_directories)])

    # assigning row names

    rows = []
    for directory in directories:
        row_data = os.path.basename(os.path.normpath(directory))
        _, row_value = row_data.split("_")
        rows.append(float(row_value))

    density_list = []

    for directory in directories:

        # the final packing arrangement file

        glob_input = os.path.join(directory, "post", "particles_*")
        files = natsorted([f for f in glob.glob(glob_input) if "boundingBox" not in f])
        end_file = files[-1]

        print(end_file)
        data = pv.read(end_file)

        # region between which packing density is calculated

        z_low = min(data.points[:,2]) + 0.25*(max(data.points[:,2]) - min(data.points[:,2]))
        z_upp = min(data.points[:,2]) + 0.75*(max(data.points[:,2]) - min(data.points[:,2]))
        z_lim = [z_low, z_upp]

        # reading the toml data

        toml_file = os.path.join(directory, "data.toml")

        with open(toml_file, 'r') as f:
            toml_data = toml.load(f)

        particle_volume = []

        # volume of spheres within the region between z_min and z_max

        for i in range(len(data.points)):
            if z_lim[0] <= data.points[i,2] <= z_lim[1]:
                vol = 4/3*np.pi*data["radius"][i]**3
                particle_volume.append(vol)

        particle_v = sum(particle_volume)

        # volume of region in which spheres lie

        cylinder_v = (z_lim[1] - z_lim[0])*np.pi*float(toml_data["cylinder_radii"])**2

        # determining packing density between z_min and z_max

        packing_density = particle_v/cylinder_v
        density_list.append(packing_density)

    density_bank.append(density_list)
density_bank = np.asarray(density_bank).T

# writing data to csv file

df = pd.DataFrame(density_bank, columns = columns, index = rows)
df.to_csv('final_paper_packing_sliding_results.csv', index = True)