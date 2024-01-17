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

# relative path to particle-wall restitution study

directory ="post"
print(directory)

columns = []
time_bank = []
density_bank = []

# cube dimensions

x_len = 0.12
y_len = 0.12

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
    density_bank.append(packing_density)

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
df.to_csv('paper_packing_results_periodic.csv', index = True)