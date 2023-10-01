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

# Setting out graph colours

colors = ['#410FDF', '#FF0000']

# Reading in data

df = pd.read_csv(r"final_paper_packing_sliding_results.csv")
df.rename({'Unnamed: 0': 'restitution_pw'}, axis=1, inplace=True)

# x axis labeling frequency

freq = 2

# Creating figure

fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(8, 7))

# Creating boxplot

df_columns = np.asarray(df['restitution_pw'])
df_seeds = df.drop(columns = ["restitution_pw"]).T

repeats = [0]*len(df_columns)

for i in range(len(df_columns)):
    repeats[i] = np.asarray(df_seeds[i])


scatter_cols = df.columns[1:]
data = [0]*len(repeats[0])
for i in range(len(repeats[0])):
    data[i] = np.asarray(df[scatter_cols[i]])

box_labels  = df_columns[::freq]

bplot1 = ax.boxplot( repeats,
                     vert=True,
                     widths = 0.4,
                     meanline =True,
                     showmeans = True,
                     showfliers = True
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

# Figure formatting

legend_points = [bplot1['means'][0], bplot1['medians'][0], bplot1['fliers'][0]]
legend_labels = ['Mean', 'Median', 'Fliers']
ax.legend(legend_points, legend_labels,  loc="upper left", bbox_to_anchor =(0, 1), ncol = 3, columnspacing=1, fontsize = 11.5)
ax.yaxis.grid(True)
ax.set_xlabel('Particle-Wall Sliding Friction Coefficient (-)', fontsize = 11.5)
ax.set_ylabel('Final Packing Density (-)', fontsize = 11.5)
ax.tick_params(axis = 'both', labelsize = 11.5)
ax.set_ylim(0.6175, 0.6550)
ax.set_xticks(np.arange(1, len(df_columns)+1, freq), labels = box_labels)


plt.savefig('wall_sliding_graph_box', bbox_inches="tight")