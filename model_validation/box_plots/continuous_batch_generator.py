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
#------------------------------------------------------------------------------------------
# Calling in Libraries
#------------------------------------------------------------------------------------------

import gmsh
if gmsh.isInitialized():
    gmsh.finalize()
gmsh.initialize()

from jinja2 import Template
import numpy as np
import os
import sympy
import glob
from natsort import natsorted

#------------------------------------------------------------------------------------------
# Container Geometry Specifications
#------------------------------------------------------------------------------------------

particle_diameter   = 10                #mm

# Square dimensions
z0_square           = 0                 #m
x0_square           = 0                 #m
y0_square           = 0                 #m
lc_square           = 1e-2              #-
square_size         = 0.122             #m

# inface dimensions
z0_inface           = 0.2872579001      #m
x0_inface           = 0                 #m
y0_inface           = 0                 #m
lc_inface           = 1e-2              #-
inface_size         = 0.12              #m

# Mesh Configuration
base_mesh_max       = 0.005             #-
base_mesh_min       = 0.0               #-

inface_mesh_max     = 1e22              #-
inface_mesh_min     = 0.0               #-

#------------------------------------------------------------------------------------------
# Simulation Specifications
#------------------------------------------------------------------------------------------

timestep            = 79e-7             #s
dumptime            = 0.079             #s
ontime              = 1                 #s
offtime             = 1                 #s
filltime            = 1                 #s
settletime          = 2                 #s
w                   = 200               #rad/s

N                   = 3000              #-
particle_rate       = 98                #s^-1
density             = 2500              #kg/m^3
youngs_modulus      = 1e7               #Pa
poisson_ratio       = 0.29              #-

sliding_pw          = 0.3               #-
rolling_pw          = 0.002             #-
restitution_pw      = 0.922             #-
cohesion_pw         = 0                 #-

sliding_pp          = 0.3               #-
rolling_pp          = 0.002             #-
restitution_pp      = 0.922             #-
cohesion_pp         = 0                 #-

number_of_seeds     = 20                 #-

#------------------------------------------------------------------------------------------
# Slurm Job Launch Specifications
#------------------------------------------------------------------------------------------

job_runtime         = "10:00:00"        # hr:min:sec
ntasks              = int(8)

#------------------------------------------------------------------------------------------
# Preliminary Calculations
#------------------------------------------------------------------------------------------


input_ontime        = np.round(np.ceil(ontime/timestep)*timestep,8)
input_offtime       = np.round(np.ceil(offtime/timestep)*timestep,8)
input_filltime      = np.round(np.ceil(filltime/timestep)*timestep,8)
input_settletime    = np.round(np.ceil(settletime/timestep)*timestep,8)
oscillation_period  = 2*np.pi/w

particle_radius     = np.round(particle_diameter/2000, 8)

seeds = [0]*number_of_seeds

for k in range(number_of_seeds):
    seeds[k] = sympy.prime(2000 + k)

#------------------------------------------------------------------------------------------
# Open Files
#------------------------------------------------------------------------------------------

with open(os.path.join("template_batch_continuous", "base_template.geo"), 'r') as f:
    base_template = f.read()

with open(os.path.join("template_batch_continuous", "inface_template.geo"), 'r') as f:
    inface_template = f.read()

with open(os.path.join("template_batch_continuous", "shake_template.sim"), 'r') as f:
    simulation_template = f.read()

with open(os.path.join("template_batch_continuous", "batch_launch_template.sh"), 'r') as f:
    batch_launch_template = f.read()

#------------------------------------------------------------------------------------------
# File Generation
#------------------------------------------------------------------------------------------


for seed in seeds:

    # setting up jinja dictionaries for text replacement of tempalte files 

    base_mesh_data          = { "square_size": square_size,
                                "z0_square": z0_square,
                                "y0_square": y0_square,
                                "x0_square": x0_square,
                                "lc_square": lc_square,
                                "mesh_max": base_mesh_max,
                                "mesh_min": base_mesh_max,
                                "Algor": 6
                                }

    inface_mesh_data        = { "inface_size": inface_size,
                                "z0_inface": z0_inface,
                                "y0_inface": y0_inface,
                                "x0_inface": x0_inface,
                                "lc_inface": lc_inface,
                                "mesh_max": inface_mesh_max,
                                "mesh_min": inface_mesh_min,
                                "Algor": 6
                                }

    simulation_data         = { "timestep": timestep,
                                "dumptime": dumptime,
                                "ontime": input_ontime,
                                "offtime": input_offtime,
                                "filltime": input_filltime,
                                "settletime": input_settletime,
                                "number_particles": N,
                                "particle_rate": particle_rate,
                                "particle_radius": particle_radius,
                                "period": oscillation_period,
                                "density": density,
                                "youngs_modulus": youngs_modulus,
                                "poisson_ratio": poisson_ratio,
                                "sliding_pp": sliding_pp,
                                "sliding_pw": sliding_pw,
                                "rolling_pp": rolling_pp,
                                "rolling_pw": rolling_pw,
                                "restitution_pp": restitution_pp,
                                "restitution_pw": restitution_pw,
                                "cohesion_pp": cohesion_pp,
                                "cohesion_pw": cohesion_pw,
                                "seed": seed
                                }

    batch_launch_data       = { "runtime": job_runtime,
                                "ntasks": ntasks
                                }

    j2_base_template                = Template(base_template)
    j2_inface_template              = Template(inface_template)
    j2_simulation_template          = Template(simulation_template)
    j2_batch_launch_template        = Template(batch_launch_template)

    # Creating file paths

    study_directory = os.path.join(f"{particle_diameter:.0f}_mm_diameter_particles", "batch_continuous", f"seed_{seed}")
    if not os.path.exists(study_directory):
        os.makedirs(study_directory)

    simulation_newpath = os.path.join(study_directory)
    if not os.path.exists(simulation_newpath):
        os.makedirs(simulation_newpath)

    batch_launch_newpath = os.path.join(study_directory)
    if not os.path.exists(batch_launch_newpath):
        os.makedirs(batch_launch_newpath)

    mesh_newpath = os.path.join(study_directory, "mesh")
    if not os.path.exists(mesh_newpath):
        os.makedirs(mesh_newpath)

    inface_newpath = os.path.join(study_directory, "mesh")
    if not os.path.exists(inface_newpath):
        os.makedirs(inface_newpath)

    # Creating new simulation files

    base_geo_file_new = os.path.join(mesh_newpath, "shake_base.geo")
    inface_geo_file_new = os.path.join(inface_newpath, "inface.geo")
    simulation_file_new = os.path.join(simulation_newpath, "shake.sim")
    batch_launch_file_new = os.path.join(batch_launch_newpath, "batch_launch.sh")

    # Writing parameters to new files

    with open(base_geo_file_new, 'w') as f:
        f.write(j2_base_template.render(base_mesh_data))

    with open(inface_geo_file_new, 'w') as f:
        f.write(j2_inface_template.render(inface_mesh_data))

    with open(simulation_file_new, 'w') as f:
        f.write(j2_simulation_template.render(simulation_data))

    with open(batch_launch_file_new, 'w') as f:
        f.write(j2_batch_launch_template.render(batch_launch_data))

    # Creating stl files from the gmesh geo files

    gmsh.open(base_geo_file_new)
    gmsh.open(inface_geo_file_new)

#------------------------------------------------------------------------------------------
# Launch Slurm Jobs
#------------------------------------------------------------------------------------------

glob_input = os.path.join(f"{particle_diameter:.0f}_mm_diameter_particles", "batch_continuous", "seed_*")
directories = natsorted([k for k in glob.glob(glob_input)])

for directory in directories:
    launch_file = os.path.join(directory, "batch_launch.sh")
    cmd = f"sbatch --output={directory}/slurm-%j.out {launch_file} {directory}"
    print(cmd)
    os.system(cmd)