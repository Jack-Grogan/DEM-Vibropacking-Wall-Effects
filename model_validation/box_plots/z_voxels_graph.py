# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 11:07:11 2023

@author: JACK GROGAN

      ___  ________  ________  ___  __            ________     
     |\  \|\   __  \|\   ____\|\  \|\  \         |\   ____\    
     \ \  \ \  \|\  \ \  \___|\ \  \/  /|_       \ \  \___|    
   __ \ \  \ \   __  \ \  \    \ \   ___  \       \ \  \  ___  
  |\  \\_\  \ \  \ \  \ \  \____\ \  \\ \  \       \ \  \|\  \ 
  \ \________\ \__\ \__\ \_______\ \__\\ \__\       \ \_______\
   \|________|\|__|\|__|\|_______|\|__| \|__|        \|_______|
   
"""


import matplotlib.pyplot as plt
import string
import pandas as pd
import numpy as np

fig, axs = plt.subplots(2,2, figsize=(8, 12))
#fig.tight_layout()

[ax1, ax2],[ax3, ax4] = axs
axs = ax1, ax2, ax3, ax4

#%% Method 1 

# reading in z packing density data

continuous = pd.read_csv(r"z_voxels_continuous_packing_results.csv")
normalised_bed_height = np.linspace(0, 1, continuous.shape[0]+1)
normalised_bed_height = normalised_bed_height[1::]

continuous_study = continuous.columns[1::]

for col_name in continuous_study:
    ax1.plot(continuous[col_name], normalised_bed_height)
    ax1.plot([0.2,0.75], [0.25, 0.25], color='k')
    ax1.plot([0.2,0.75], [0.75, 0.75], color='k')

#%% Method 2

# reading in z packing density data

periodic = pd.read_csv(r"z_voxels_periodic_packing_results.csv")
normalised_bed_height = np.linspace(0, 1, periodic.shape[0]+1)
normalised_bed_height = normalised_bed_height[1::]

periodic_study = periodic.columns[1::]

for col_name in periodic_study:
    ax2.plot(periodic[col_name], normalised_bed_height)
    ax2.plot([0.2,0.75], [0.25, 0.25], color='k')
    ax2.plot([0.2,0.75], [0.75, 0.75], color='k')


#%% Method 3

# reading in z packing density data

batch_periodic = pd.read_csv(r"z_voxels_batch_periodic_packing_results.csv")
normalised_bed_height = np.linspace(0, 1, batch_periodic.shape[0]+1)
normalised_bed_height = normalised_bed_height[1::]

batch_periodic_study = batch_periodic.columns[1::]

for col_name in batch_periodic_study:
    ax3.plot(batch_periodic[col_name], normalised_bed_height)
    ax3.plot([0.2,0.75], [0.25, 0.25], color='k')
    ax3.plot([0.2,0.75], [0.75, 0.75], color='k')
    
#%% Method 4 

# reading in z packing density data

batch_continuous = pd.read_csv(r"z_voxels_batch_continuous_packing_results.csv")
normalised_bed_height = np.linspace(0, 1, batch_continuous.shape[0]+1)
normalised_bed_height = normalised_bed_height[1::]

batch_continuous_study = batch_continuous.columns[1::]

for col_name in batch_continuous_study:
    ax4.plot(batch_continuous[col_name], normalised_bed_height)
    ax4.plot([0.2,0.75], [0.25, 0.25], color='k')
    ax4.plot([0.2,0.75], [0.75, 0.75], color='k')
    
#%%
# adding a, b, c and d data to plots

for n, ax in enumerate(axs):
    ax.text(0, 1.02, f"{string.ascii_lowercase[n]}) Method {n+1}", transform=ax.transAxes, 
            size=18)
    ax.set_xlim(0.2,0.75)
    
ax1.set_xlabel('Packing Density (-)')
ax2.set_xlabel('Packing Density (-)')
ax3.set_xlabel('Packing Density (-)')
ax4.set_xlabel('Packing Density (-)')

ax1.set_ylabel('Normalised Bed Height (-)')
ax2.set_ylabel('Normalised Bed Height (-)')
ax3.set_ylabel('Normalised Bed Height (-)')
ax4.set_ylabel('Normalised Bed Height (-)')

ax1.grid(which='major', color='k', linestyle='-', alpha = 0.1)
ax1.grid(which='minor', color='black', linestyle='-', alpha = 0.1)
ax1.minorticks_on()

ax2.grid(which='major', color='k', linestyle='-', alpha = 0.1)
ax2.grid(which='minor', color='black', linestyle='-', alpha = 0.1)
ax2.minorticks_on()

ax3.grid(which='major', color='k', linestyle='-', alpha = 0.1)
ax3.grid(which='minor', color='black', linestyle='-', alpha = 0.1)
ax3.minorticks_on()

ax4.grid(which='major', color='k', linestyle='-', alpha = 0.1)
ax4.grid(which='minor', color='black', linestyle='-', alpha = 0.1)
ax4.minorticks_on()


plt.savefig('z_packing', bbox_inches="tight")