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
from matplotlib.patches import ConnectionPatch

# Setting out graph colours

colors = ['#410FDF', '#FF0000']

# Reading in data

df = pd.read_csv(r"final_paper_packing_rolling_results_wide.csv")
df.rename({'Unnamed: 0': 'restitution_pw'}, axis=1, inplace=True)

# x axis labeling frequency

freq = 2

# Creating figure

fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, sharey=True, figsize=(8, 14))
plt.subplots_adjust(wspace=0, hspace=0.1)
fig.supylabel('FInal Packing Density (-)', fontsize = 11.5)

df_columns = np.round(np.asarray(df['restitution_pw']), 8)
box_labels  = df_columns[::freq]

df_seeds = df.drop(columns = ["restitution_pw"]).T

repeats = [0]*len(df_columns)

for i in range(len(df_columns)):
    repeats[i] = np.asarray(df_seeds[i])


scatter_cols = df.columns[1:]
data = [0]*len(repeats[0])

for i in range(len(repeats[0])):
    data[i] = np.asarray(df[scatter_cols[i]])

#########################################################################################################################################################
# BOX PLOT 1
#########################################################################################################################################################

bplot1 = ax1.boxplot(repeats,
                     vert=True,
                     positions = range(0, len(repeats)),
                     widths = 0.4,
                     meanline =True,
                     showmeans = True,
                     showfliers = True,
                     )

for whisker in bplot1['whiskers']:
    whisker.set(color ='k',
                linewidth = 1.5,
                linestyle =":")

for cap in bplot1['caps']:
    cap.set(color ='k',
            linewidth = 1,
            linestyle = '--')

for median in bplot1['medians']:
    median.set(color = colors[0],
               linewidth = 2,
               linestyle = '-')
 
for flier in bplot1['fliers']:
    flier.set(marker ='D',
              color = 'k',
              alpha = 0.6)

for mean in bplot1['means']:
    mean.set(color = colors[1],
            linewidth = 2,
            linestyle = '-')

# setting up axis parameters

legend_points = [bplot1['means'][0], bplot1['medians'][0], bplot1['fliers'][0]]
legend_labels = ['Mean', 'Median', 'Fliers']
ax1.legend(legend_points, legend_labels,  loc="upper right", bbox_to_anchor =(1, 1), ncol = 3, columnspacing=1, fontsize = 11.5)
ax1.yaxis.grid(True)
ax1.set_ylim(0.6175, 0.6550)
ax1.tick_params(axis = 'both', labelsize = 11.5)
ax1.set_xticks(np.arange(0, len(df_columns)+1, freq), labels = box_labels)


#########################################################################################################################################################
# BOX PLOT 2
#########################################################################################################################################################

# Reading in data

df2 = pd.read_csv(r"final_paper_packing_rolling_results.csv")
df2.rename({'Unnamed: 0': 'restitution_pw'}, axis=1, inplace=True)

# x axis labeling frequency

freq2 = 4

df2_columns = np.round(np.asarray(df2['restitution_pw']), 8)
box_labels2  = df2_columns[::freq2]

df2_seeds = df2.drop(columns = ["restitution_pw"]).T

repeats2 = [0]*len(df2_columns)

for i in range(len(df2_columns)):
    repeats2[i] = np.asarray(df2_seeds[i])


scatter_cols2 = df2.columns[1:]
data2 = [0]*len(repeats2[0])

for i in range(len(repeats[0])):
    data2[i] = np.asarray(df2[scatter_cols2[i]])


bplot2 = ax2.boxplot( repeats2,
                     vert=True,
                     positions = range(0, len(repeats2)),
                     widths = 0.4,
                     meanline =True,
                     showmeans = True,
                     showfliers = True,
                     ) 

for whisker in bplot2['whiskers']:
    whisker.set(color ='k',
                linewidth = 1.5,
                linestyle =":")

for cap in bplot2['caps']:
    cap.set(color ='k',
            linewidth = 1,
            linestyle = '--')

for median in bplot2['medians']:
    median.set(color = colors[0],
               linewidth = 2,
               linestyle = '-')
 
for flier in bplot2['fliers']:
    flier.set(marker ='D',
              color = 'k',
              alpha = 0.6)

for mean in bplot2['means']:
    mean.set(color = colors[1],
            linewidth = 2,
            linestyle = '-')

# setting up axis parameters

legend_points2 = [bplot2['means'][0], bplot2['medians'][0], bplot2['fliers'][0]]
legend_labels2 = ['Mean', 'Median', 'Fliers']
ax2.legend(legend_points2, legend_labels2,  loc="upper right", bbox_to_anchor =(1, 1), ncol = 3, columnspacing=1, fontsize = 11.5)
ax2.yaxis.grid(True)
ax2.set_xlabel('Particle-Wall Rolling Friction Coefficient (-)', fontsize = 11.5)
ax2.set_ylim(0.6175, 0.6550)
ax2.tick_params(axis = 'both', labelsize = 11.5)
ax2.set_xticks(np.arange(0, len(df2_columns), freq2), labels = box_labels2)

#########################################################################################################################################################
# BORDER PARAMETERS
#########################################################################################################################################################

autoAxis1 = ax1.axis()
autoAxis2 = ax2.axis()

xy1a = (0,0.6175)
xy2a = (autoAxis2[0],0.655)

xy1b = (0.6,0.6175)
xy2b = (autoAxis2[1],0.655)

xy1c = (0,0.6175)
xy2c = (0,0.655)

xy1d = (0.6,0.6175)
xy2d = (0.6,0.655)


con1 = ConnectionPatch(xyA=xy1a, xyB=xy2a, coordsA="data", coordsB="data", axesA=ax1, axesB=ax2, color="k", lw = 1.5, linestyle = '--')
con2 = ConnectionPatch(xyA=xy1b, xyB=xy2b, coordsA="data", coordsB="data", axesA=ax1, axesB=ax2, color="k", lw = 1.5, linestyle = '--')

con3 = ConnectionPatch(xyA=xy1c, xyB=xy2c, coordsA="data", coordsB="data", axesA=ax1, axesB=ax1, color="k", lw = 1.5, linestyle = '--')
con4 = ConnectionPatch(xyA=xy1d, xyB=xy2d, coordsA="data", coordsB="data", axesA=ax1, axesB=ax1, color="k", lw = 1.5, linestyle = '--')

ax1.add_artist(con1)
ax1.add_artist(con2)
ax1.add_artist(con3)
ax1.add_artist(con4)

for axis in ['top', 'bottom', 'left', 'right']:
    ax2.spines[axis].set_linewidth(1.5)             # change width
    ax2.spines[axis].set_color('k')                 # change color
    ax2.spines[axis].set_linestyle('--')            # change width

ax2.spines.top.set_visible(False)
ax1.spines.bottom.set_visible(False)
ax1.tick_params(top=True, labeltop=True, bottom=False, labelbottom=False)

plt.savefig('wall_rolling_graph_box', bbox_inches="tight")