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

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read in csv file

data1 = pd.read_csv(r"voxel_packing_results_continuous.csv")

x_1 = data1['Time']
y_1 = data1['post']

# Generate figure

fig, ax = plt.subplots(figsize=(8, 7))

# Plot data

ax.plot(x_1, y_1, color = 'k', linewidth = 0.5)

# Formatting figure

ax.grid(which='major', color='black', linestyle='-', alpha = 0.5)
ax.grid(which='minor', color='black', linestyle='-', alpha = 0.2)
ax.minorticks_on()
ax.set_xlabel("Time (s)", fontsize = 16)
ax.set_ylabel("Packing Density (-)", fontsize = 16)
ax.annotate(text = f"Final\n packing density \n= {np.asarray(y_1.tail(1))[0]:.4f}", horizontalalignment = 'center', xy=(x_1.tail(1), y_1.tail(1)), xytext=(13.5, 0.5),arrowprops=dict(arrowstyle="->"), fontsize = 16)
ax.set_xlim(0, 16)
ax.set_ylim(0.2, 0.7)
ax.tick_params(axis = 'both', labelsize = 16)

# Generate zoomed in region

axins = ax.inset_axes([0.2, 0.15, 0.47, 0.47])

# Plot data

axins.plot(x_1, y_1, color = 'k', linewidth = 0.5)

# Region of ax to zoom in on

x1, x2, y1, y2 = 5, 8, 0.58, 0.65

# Formatting zoomed in plot

axins.set_xlim(x1, x2)
axins.set_ylim(y1, y2)
axins.grid(which='major', color='black', linestyle='-', alpha = 0.5)
axins.grid(which='minor', color='black', linestyle='-', alpha = 0.2)
axins.minorticks_on()
axins.tick_params(axis = 'both', labelsize = 16)
ax.indicate_inset_zoom(axins, edgecolor="black")

plt.savefig("voxel_continuous_vibration.png")