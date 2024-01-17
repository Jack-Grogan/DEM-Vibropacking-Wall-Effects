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
from matplotlib.legend_handler import HandlerTuple

# Setting out graph colours

colors = ['k','b',  'limegreen', 'r']

# Reading in data

df = pd.read_csv(r"final_voxel_packing_sliding_results.csv")
df.rename({'Unnamed: 0': 'sliding_pw'}, axis=1, inplace=True)
df_sliding_pw = np.asarray(df['sliding_pw'])

s0_r0_columns = [column for column in df.columns if column.startswith("sliding_0_rolling_0")]
s1_r0_columns = [column for column in df.columns if column.startswith("sliding_1_rolling_0")]
s0_r1_columns = [column for column in df.columns if column.startswith("sliding_0_rolling_1")]
s1_r1_columns = [column for column in df.columns if column.startswith("sliding_1_rolling_1")]

df_s0_r0= df[s0_r0_columns].T
df_s1_r0= df[s1_r0_columns].T
df_s0_r1= df[s0_r1_columns].T
df_s1_r1= df[s1_r1_columns].T

# Converting data into arrays

repeats_s0_r0 = [0]*len(df_sliding_pw)
repeats_s1_r0 = [0]*len(df_sliding_pw)
repeats_s0_r1 = [0]*len(df_sliding_pw)
repeats_s1_r1 = [0]*len(df_sliding_pw)

for i in range(len(df_sliding_pw)):
    repeats_s0_r0[i] = np.asarray(df_s0_r0[i])
    repeats_s1_r0[i] = np.asarray(df_s1_r0[i])
    repeats_s0_r1[i] = np.asarray(df_s0_r1[i])
    repeats_s1_r1[i] = np.asarray(df_s1_r1[i])  

data_s0_r0 = [0]*len(repeats_s0_r0[0])
data_s1_r0 = [0]*len(repeats_s1_r0[0])
data_s0_r1 = [0]*len(repeats_s0_r1[0])
data_s1_r1 = [0]*len(repeats_s1_r1[0])

for i in range(len(repeats_s0_r0[0])):
    data_s0_r0[i] = np.asarray(df[s0_r0_columns[i]])
    data_s1_r0[i] = np.asarray(df[s1_r0_columns[i]])
    data_s0_r1[i] = np.asarray(df[s0_r1_columns[i]])
    data_s1_r1[i] = np.asarray(df[s1_r1_columns[i]])

# Creating figure
  
fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(8, 7), layout = 'constrained')

# Creating scatterplot
      
scatter_s0_r0           = []
scatter_s0_r0_x_points  = []

scatter_s1_r0           = []
scatter_s1_r0_x_points  = []

scatter_s0_r1           = []
scatter_s0_r1_x_points  = []

scatter_s1_r1           = []
scatter_s1_r1_x_points  = []

for i in data_s0_r0:
    for j in i:
        scatter_s0_r0.append(j)
        
for i in range(len(data_s0_r0)):
    for j in df_sliding_pw:
        scatter_s0_r0_x_points.append(j)

for i in data_s1_r0:
    for j in i:
        scatter_s1_r0.append(j)
        
for i in range(len(data_s1_r0)):
    for j in df_sliding_pw:
        scatter_s1_r0_x_points.append(j)
        
for i in data_s0_r1:
    for j in i:
        scatter_s0_r1.append(j)  
        
for i in range(len(data_s0_r1)):
    for j in df_sliding_pw:
        scatter_s0_r1_x_points.append(j)
                
for i in data_s1_r1:
    for j in i:
        scatter_s1_r1.append(j)
        
for i in range(len(data_s1_r1)):
    for j in df_sliding_pw:
        scatter_s1_r1_x_points.append(j)
    
    
s1 = plt.scatter(scatter_s0_r0_x_points, scatter_s0_r0, color = colors[0], alpha = 0.4, marker = 'x')#, label = "Particle-Particle SLiding Friction = 0 \nParticle-Particle Rolling Friction = 0 ")
s2 = plt.scatter(scatter_s1_r0_x_points, scatter_s1_r0, color = colors[1], alpha = 0.4, marker = 'x')#, label = "Particle-Particle SLiding Friction = 1 \nParticle-Particle Rolling Friction = 0 ")
s3 = plt.scatter(scatter_s0_r1_x_points, scatter_s0_r1, color = colors[2], alpha = 0.4, marker = 'x')#, label = "Particle-Particle SLiding Friction = 0 \nParticle-Particle Rolling Friction = 1 ")
s4 = plt.scatter(scatter_s1_r1_x_points, scatter_s1_r1, color = colors[3], alpha = 0.4, marker = 'x')#, label = "Particle-Particle SLiding Friction = 1 \nParticle-Particle Rolling Friction = 1")

# Creating line plot of means

mean_s0_r0 = []
std_s0_r0 = []

mean_s1_r0 = []
std_s1_r0 = []

mean_s0_r1 = []
std_s0_r1 = []

mean_s1_r1 = []
std_s1_r1 = []


for i in repeats_s0_r0:
    mean_s0_r0.append(np.mean(i))
    std_s0_r0.append(np.std(i))

for i in repeats_s1_r0:
    mean_s1_r0.append(np.mean(i))
    std_s1_r0.append(np.std(i))
    
for i in repeats_s0_r1:
    mean_s0_r1.append(np.mean(i))
    std_s0_r1.append(np.std(i))

for i in repeats_s1_r1:
    mean_s1_r1.append(np.mean(i))
    std_s1_r1.append(np.std(i))
    
# Creating shade of +- 1 standard deviation either side of the mean

top_line_s0_r0 = np.asarray(mean_s0_r0) + np.asarray(std_s0_r0)
bottom_line_s0_r0 = np.asarray(mean_s0_r0) - np.asarray(std_s0_r0)

top_line_s1_r0 = np.asarray(mean_s1_r0) + np.asarray(std_s1_r0)
bottom_line_s1_r0 = np.asarray(mean_s1_r0) - np.asarray(std_s1_r0)

top_line_s0_r1 = np.asarray(mean_s0_r1) + np.asarray(std_s0_r1)
bottom_line_s0_r1 = np.asarray(mean_s0_r1) - np.asarray(std_s0_r1)

top_line_s1_r1 = np.asarray(mean_s1_r1) + np.asarray(std_s1_r1)
bottom_line_s1_r1 = np.asarray(mean_s1_r1) - np.asarray(std_s1_r1)

p1, = plt.plot(df_sliding_pw, mean_s0_r0, color = colors[0], linewidth = 0.7)
f1 = plt.fill_between(df_sliding_pw, top_line_s0_r0, bottom_line_s0_r0, color=colors[0], alpha=.2)#, label = '1 Standard Deviation')
    
p2, = plt.plot(df_sliding_pw, mean_s1_r0, color = colors[1], linewidth = 0.7)
f2 = plt.fill_between(df_sliding_pw, top_line_s1_r0, bottom_line_s1_r0, color=colors[1], alpha=.2)#, label = '1 Standard Deviation')

p3, = plt.plot(df_sliding_pw, mean_s0_r1, color = colors[2], linewidth = 0.7)
f3 = plt.fill_between(df_sliding_pw, top_line_s0_r1, bottom_line_s0_r1, color=colors[2], alpha=.2)#, label = '1 Standard Deviation')

p4, = plt.plot(df_sliding_pw, mean_s1_r1, color = colors[3], linewidth = 0.7)
f4 = plt.fill_between(df_sliding_pw, top_line_s1_r1, bottom_line_s1_r1, color=colors[3], alpha=.2)#, label = '1 Standard Deviation')

# Figure formatting

plt.grid(which='major', color='k', linestyle='-', alpha = 0.5)
plt.grid(which='minor', color='black', linestyle='-', alpha = 0.2)
plt.minorticks_on()   
plt.xlim([0,1])
plt.ylim([0.53,0.64])
plt.tick_params(axis = 'both', labelsize = 11.5)
plt.xlabel("Particle-Wall Sliding Friction Coefficient (-)", fontsize = 11.5)
plt.ylabel("Final Packing Density (-)", fontsize = 11.5)

handles, labels = ax.get_legend_handles_labels()

legend_points = [(p1, s1), f1, (p2, s2), f2, (p3, s3), f3, (p4, s4), f4]
legend_labels = ["Particle-Particle: \nSliding Friction = 0 \nRolling Friction = 0",
                    "1 Standard \nDeviation",
                    "Particle-Particle \nSliding Friction = 1 \nRolling Friction = 0",
                    "1 Standard \nDeviation",
                    "Particle-Particle: \nSliding Friction = 0 \nRolling Friction = 1",                     
                    "1 Standard \nDeviation",
                    "Particle-Particle: \nSliding Friction = 1 \nRolling Friction = 1 ",
                    "1 Standard \nDeviation"]

plt.legend(legend_points, legend_labels,  loc="upper left", bbox_to_anchor =(1, 1), ncol = 1, numpoints=8, handler_map={tuple: HandlerTuple(ndivide=None)}, frameon = False, labelspacing=1.9, fontsize = 11.5)

plt.savefig('method_1_procedure_2_sliding_graph', bbox_inches="tight")