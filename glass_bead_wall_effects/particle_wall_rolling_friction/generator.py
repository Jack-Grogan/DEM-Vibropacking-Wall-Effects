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
import toml

#------------------------------------------------------------------------------------------
# Container Geometry Specifications
#------------------------------------------------------------------------------------------

particle_diameter   = 10                #mm

# cylinder dimensions
z0_cylinder         = 0                 #m
x0_cylinder         = 0                 #m
y0_cylinder         = 0                 #m
lc_cylinder         = 1e-2              #-
cylinder_height     = 0.32              #m

# inface dimensions
z0_inface           = 0.2872579001      #m
x0_inface           = 0                 #m
y0_inface           = 0                 #m
lc_inface           = 1e-2              #-

# Mesh Configuration
cylinder_mesh_max   = 0.005             #-
cylinder_mesh_min   = 0.0               #-

inface_mesh_max     = 1e22              #-
inface_mesh_min     = 0.0               #-

#------------------------------------------------------------------------------------------
# Simulation Specifications
#------------------------------------------------------------------------------------------

timestep            = 79e-7             #s
dumptime            = 0.079             #s
ontime              = 12.5              #s
filltime            = 2                 #s
settletime          = 1                 #s
w                   = 200               #rad/s

N                   = 3000              #-
density             = 2500              #kg/m^3
youngs_modulus      = 1e7               #Pa
poisson_ratio       = 0.29              #-

sliding_pw          = 0.3               #-
sliding_pp          = 0.3               #-

rolling_pw_min      = 0.001             #-
rolling_pw_max      = 0.03
num_studies         = 30

rolling_pp          = 0.002             #-
restitution_pw      = 0.922             #-
restitution_pp      = 0.992             #-
cohesion_pw         = 0                 #-
cohesion_pp         = 0                 #-

number_of_seeds     = 5                 #-

#------------------------------------------------------------------------------------------
# Slurm Job Launch Specifications
#------------------------------------------------------------------------------------------

job_runtime         = "02:00:00"        # hr:min:sec
ntasks              = int(8)

#------------------------------------------------------------------------------------------
# Preliminary Calculations
#------------------------------------------------------------------------------------------

input_ontime        = np.round(np.ceil(ontime/timestep)*timestep,8)
input_filltime      = np.round(np.ceil(filltime/timestep)*timestep,8)
input_settletime    = np.round(np.ceil(settletime/timestep)*timestep,8)
oscillation_period  = 2*np.pi/w

particle_radius     = np.round(particle_diameter/2000, 8)
cylinder_radii      = np.round(12*particle_radius, 8)
inface_radii        = np.round(cylinder_radii - 0.01,8)

rolling_pw          = np.round(np.linspace(rolling_pw_min, rolling_pw_max, num_studies),8)

seeds = [0]*number_of_seeds

for k in range(number_of_seeds):
    seeds[k] = sympy.prime(2000 + k)

#------------------------------------------------------------------------------------------
# Open Files
#------------------------------------------------------------------------------------------

with open(os.path.join("template", "cylinder_template.geo"), 'r') as f:
    cylinder_template = f.read()

with open(os.path.join("template", "inface_template.geo"), 'r') as f:
    inface_template = f.read()

with open(os.path.join("template","shake_template.sim"), 'r') as f:
    simulation_template = f.read()

with open(os.path.join("template","batch_launch_template.sh"), 'r') as f:
    batch_launch_template = f.read()

#------------------------------------------------------------------------------------------
# File Generation
#------------------------------------------------------------------------------------------
for seed in seeds:

    j2_cylinder_template        = [0]*num_studies
    j2_inface_template          = [0]*num_studies
    j2_simulation_template      = [0]*num_studies
    j2_batch_launch_template    = [0]*num_studies

    newpath                     = [0]*num_studies


    for i in range(num_studies):

        # setting up jinja dictionaries for text replacement of tempalte files

        cylinder_mesh_data      = { "cylinder_height": cylinder_height,
                                    "cylinder_radius": cylinder_radii,
                                    "z_0": z0_cylinder,
                                    "y_0": y0_cylinder,
                                    "x_0": x0_cylinder,
                                    "lc": lc_cylinder,
                                    "mesh_max": cylinder_mesh_max,
                                    "mesh_min": cylinder_mesh_min,
                                    "Algor": 6
                                    }

        inface_mesh_data        = { "inface_radius": inface_radii,
                                    "z_0": z0_inface,
                                    "y_0": y0_inface,
                                    "x_0": x0_inface,
                                    "lc": lc_inface,
                                    "mesh_max": inface_mesh_max,
                                    "mesh_min": inface_mesh_min,
                                    "Algor": 6
                                    }

        simulation_data         = { "timestep": timestep,
                                    "dumptime": dumptime,
                                    "filltime": input_filltime,
                                    "ontime": input_ontime,
                                    "settletime": input_settletime,
                                    "number_particles": N,
                                    "particle_radius": particle_radius,
                                    "density": density,
                                    "youngs_modulus": youngs_modulus,
                                    "poisson_ratio": poisson_ratio,
                                    "sliding_pp": sliding_pp,
                                    "sliding_pw": sliding_pw,
                                    "rolling_pp": rolling_pp,
                                    "rolling_pw": rolling_pw[i],
                                    "restitution_pp": restitution_pp,
                                    "restitution_pw": restitution_pw,
                                    "cohesion_pp": cohesion_pp,
                                    "cohesion_pw": cohesion_pw,
                                    "seed": seed,
                                    "period": oscillation_period
                                    }

        batch_launch_data       = { "runtime": job_runtime,
                                    "ntasks": ntasks
                                    }

        post_processing_data    = { "cylinder_radii": cylinder_radii,
                                    "rolling_pw": rolling_pw[i]
                                    }

        j2_cylinder_template[i]         = Template(cylinder_template)
        j2_inface_template[i]           = Template(inface_template)
        j2_simulation_template[i]       = Template(simulation_template)
        j2_batch_launch_template[i]     = Template(batch_launch_template)

        # Creating file paths

        study_directory = os.path.join(f"{particle_diameter:.0f}_mm_diameter_particles", f"seed_{seed}")
        if not os.path.exists(study_directory):
            os.makedirs(study_directory)

        simulation_newpath = os.path.join(study_directory, f"rolling_{rolling_pw[i]:.3f}")
        if not os.path.exists(simulation_newpath):
            os.makedirs(simulation_newpath)

        batch_launch_newpath = os.path.join(study_directory, f"rolling_{rolling_pw[i]:.3f}")
        if not os.path.exists(batch_launch_newpath):
            os.makedirs(batch_launch_newpath)

        mesh_newpath = os.path.join(study_directory, f"rolling_{rolling_pw[i]:.3f}", "mesh")
        if not os.path.exists(mesh_newpath):
            os.makedirs(mesh_newpath)

        inface_newpath = os.path.join(study_directory, f"rolling_{rolling_pw[i]:.3f}", "mesh")
        if not os.path.exists(inface_newpath):
            os.makedirs(inface_newpath)

        toml_path = os.path.join(study_directory, f"rolling_{rolling_pw[i]:.3f}")
        if not os.path.exists(toml_path):
            os.makedirs(toml_path)

        # Creating new simulation files

        cylinder_geo_file_new = os.path.join(mesh_newpath, "shake_cylinder.geo")
        inface_geo_file_new = os.path.join(inface_newpath, "inface.geo")
        simulation_file_new = os.path.join(simulation_newpath, "shake.sim")
        batch_launch_file_new = os.path.join(batch_launch_newpath, "batch_launch.sh")
        toml_file = os.path.join(toml_path, "data.toml")

        # Writing parameters to new files

        with open(cylinder_geo_file_new, 'w') as f:
            f.write(j2_cylinder_template[i].render(cylinder_mesh_data))

        with open(inface_geo_file_new, 'w') as f:
            f.write(j2_inface_template[i].render(inface_mesh_data))

        with open(simulation_file_new, 'w') as f:
            f.write(j2_simulation_template[i].render(simulation_data))

        with open(batch_launch_file_new, 'w') as f:
            f.write(j2_batch_launch_template[i].render(batch_launch_data))

        with open(toml_file, 'w') as f:
            toml.dump(post_processing_data, f)

        # Creating stl files from the gmesh geo files

        gmsh.open(cylinder_geo_file_new)
        gmsh.open(inface_geo_file_new)

    #------------------------------------------------------------------------------------------
    # Launch Slurm Jobs
    #------------------------------------------------------------------------------------------

    glob_input = os.path.join(study_directory, "rolling_*")
    directories = natsorted([k for k in glob.glob(glob_input)])

    for directory in directories:
        launch_file = os.path.join(directory, "batch_launch.sh")
        cmd = f"sbatch --output={directory}/slurm-%j.out {launch_file} {directory}"
        print(cmd)
        os.system(cmd)