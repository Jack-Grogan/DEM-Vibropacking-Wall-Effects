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
import matplotlib.pyplot as plt
from brokenaxes import brokenaxes
from matplotlib import ticker

# Setting pllot colours

colors = ['limegreen', 'b', '#FF0000', '#FFD300']

# Read in csv file

data = pd.read_csv(r"final_paper_packing_results.csv")
voxels_data = pd.read_csv(r"final_voxels_packing_results.csv")

data1 = data["continuous"]
data2 = data["periodic"]
data3 = data["batch_continuous"]
data4 = data["batch_periodic"]

voxels_data1 = voxels_data["continuous"]
voxels_data2 = voxels_data["periodic"]
voxels_data3 = voxels_data["batch_continuous"]
voxels_data4 = voxels_data["batch_periodic"]

# Generate figure

fig = plt.figure(figsize=(8, 7), layout = 'constrained')

# Set up broken axis
# Thanks to Ben Dichter, broken axis can be found via the link below
# https://github.com/bendichter/brokenaxes

bax = brokenaxes(
    ylims=((0.62, 0.627), (0.641, 0.655)),
    hspace=.05,
    despine= False,
)

box_1_data = [data1, data2]
box_1_labels = ["Continuous", "Periodic"]
box_1_positions = [1, 2]

bplot1 = bax.boxplot(box_1_data,
                    positions = box_1_positions,
                    vert=True,
                    widths = 0.4,
                    meanline =True,
                    showmeans = True,
                    showfliers = True
                    )

# formatting boxplot

for whisker in bplot1[0].get('whiskers'):
    whisker.set(color ='k',
                linewidth = 1.5,
                linestyle =":")

for cap in bplot1[0].get('caps'):
    cap.set(color ='k',
            linewidth = 1,
            linestyle = '--')

for median in bplot1[0].get('medians'):
    median.set(color = colors[0],
               linewidth = 2,
               linestyle = '-')
 
for flier in bplot1[0].get('fliers'):
    flier.set(marker ='D',
              color = 'k',
              alpha = 0.5)

for mean in bplot1[0].get('means'):
    mean.set(color = colors[1],
            linewidth = 2,
            linestyle = '--')

voxels_1_data = [voxels_data1, voxels_data2]
voxels_1_labels = ["Continuous", "Periodic"]
voxels_1_positions = [1.4, 2.4]

bplot1_voxels = bax.boxplot(voxels_1_data,
                    positions = voxels_1_positions,
                    vert=True,
                    labels=None,
                    widths = 0.4,
                    meanline =True,
                    showmeans = True,
                    showfliers = True
                    )

# formatting boxplot 1

for whisker in bplot1_voxels[1].get('whiskers'):
    whisker.set(color ='k',
                linewidth = 1.5,
                linestyle =":")

for cap in bplot1_voxels[1].get('caps'):
    cap.set(color ='k',
            linewidth = 1,
            linestyle = '--')

for median in bplot1_voxels[1].get('medians'):
    median.set(color = colors[2],
               linewidth = 2,
               linestyle = '-')
 
for flier in bplot1_voxels[1].get('fliers'):
    flier.set(marker ='D',
              color = 'k',
              alpha = 0.5)

for mean in bplot1_voxels[1].get('means'):
    mean.set(color = colors[3],
            linewidth = 2,
            linestyle = '--')

# Plotting literature values

exp_data_1 = [0.648, 0.645]
exp_data_x_1 = box_1_positions
expdata1 = bax.scatter(exp_data_x_1, exp_data_1, color = 'k', marker = 'x', s = 100)

# formatting figure 

legend_labels = ['An et al.\'s Results', 'Procedure 1 Medians', 'Procedure 1 Means', 'Procedure 2 Medians', 'Procedure 2 Means', 'Outliers']
legend_points = [ expdata1[0], bplot1[0].get('medians')[0], bplot1[0].get('means')[0], bplot1_voxels[1].get('medians')[0], bplot1_voxels[1].get('means')[0], bplot1[0].get('fliers')[0]]
vib_operation =  ("Continuous", "Periodic")
tick_positions_x = [(box_1_positions[0] + voxels_1_positions[0])/2 , (box_1_positions[1] + voxels_1_positions[1])/2]
bax.last_row[0].set_xticks(tick_positions_x)

for ax in bax.axs:
    ax.set_xticks(tick_positions_x, ["Continuous", "Periodic"])
    ax.yaxis.grid(True)
    ax.tick_params(axis='both', labelsize=14)
    ax.set_xlim([0.7, 2.7])

bax.set_xlabel('Vibration Operation', loc='center', labelpad= 27, fontsize = 16)
bax.set_ylabel('Packing Density', loc='center', labelpad= 55, fontsize = 16)
bax.legend(legend_points, legend_labels, ncol = 2, loc='center', bbox_to_anchor =(0.45,-0.25), fontsize = 16, frameon = True, labelspacing=0.8)

plt.savefig('model_validation_dump_fill', bbox_inches="tight")

#%%

# Generating figure

fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(8, 7))

# Plotting data

box_2_data = [data3, data4]
box_2_labels = ["Continuous", "Periodic"]
exp_data_2 = [0.729,0.739]
exp_data_x_2 = [1, 2]
box_2_positions = [1, 2]

bplot2 = ax.boxplot(box_2_data,
                    positions = box_2_positions,
                    vert=True,
                    widths = 0.4,
                    meanline =True,
                    showmeans = True,
                    showfliers = True
                    )

# formatting boxplot 1

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
            linestyle = '--')

voxels_2_data = [voxels_data3, voxels_data4]
voxels_2_positions = [1.4, 2.4]

bplot2_voxels = ax.boxplot(voxels_2_data,
                           positions = voxels_2_positions,
                           vert=True,
                           widths = 0.4,
                           meanline =True,
                           showmeans = True,
                           showfliers = True
                           )

# formatting boxplot 1

for whisker in bplot2_voxels['whiskers']:
    whisker.set(color ='k',
                linewidth = 1.5,
                linestyle =":")

for cap in bplot2_voxels['caps']:
    cap.set(color ='k',
            linewidth = 1,
            linestyle = '--')

for median in bplot2_voxels['medians']:
    median.set(color = colors[2],
               linewidth = 2,
               linestyle = '-')
 
for flier in bplot2_voxels['fliers']:
    flier.set(marker ='D',
              color = 'k',
              alpha = 0.6)

for mean in bplot2_voxels['means']:
    mean.set(color = colors[3],
            linewidth = 2,
            linestyle = '--')

# Plotting literature values

expdata2 = ax.scatter(exp_data_x_2, exp_data_2, color = 'k', marker = 'x', s = 100)

# formatting figure 

legend_labels = ['Yu et al.\'s Results', 'Procedure 1 Medians', 'Procedure 1 Means', 'Procedure 2 Medians', 'Procedure 2 Means', 'Outliers']
legend_points = [ expdata2, bplot2['medians'][0], bplot2['means'][0], bplot2_voxels['medians'][0], bplot2_voxels['means'][0], bplot2['fliers'][0]]
ax.legend(legend_points, legend_labels, ncol = 2, loc='center', bbox_to_anchor =(0.45,-0.25), fontsize = 16, frameon = True, labelspacing=0.8)
fill_operation =  ("Continuous", "Periodic")
formatter = ticker.FormatStrFormatter('%1.3f')
ax.yaxis.set_major_formatter(formatter)
ax.tick_params(axis='both', labelsize=14)
tick_positions_x_2 = [(box_2_positions[0] + voxels_2_positions[0])/2 , (box_2_positions[1] + voxels_2_positions[1])/2]
ax.set_xlim([0.7, 2.7])
ax.set_xticks(tick_positions_x_2, fill_operation)
ax.yaxis.grid(True)
ax.set_xlabel('Fill Operation', fontsize = 16)
ax.set_ylabel('Packing Density', loc='center', labelpad= 10, fontsize = 16)

plt.savefig('model_validation_batch_fill', bbox_inches="tight")
