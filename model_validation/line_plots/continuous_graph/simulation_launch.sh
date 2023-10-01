#!/bin/bash
#SBATCH --time=04:00:00
#SBATCH --ntasks=8
#SBATCH --nodes=1
#SBATCH --constraint=icelake

set -e

module purge; module load bluebear
module load bear-apps/2022a
module load PICI-LIGGGHTS/3.8.1-foss-2022a-VTK-9.2.2

mpiexec -n 8 liggghts -in shake.sim
