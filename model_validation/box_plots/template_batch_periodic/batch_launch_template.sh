#!/bin/bash
#SBATCH --time={{ runtime }}
#SBATCH --ntasks={{ ntasks }}
#SBATCH --nodes=1
#SBATCH --constraint=icelake

set -e

module purge; module load bluebear
module load bear-apps/2022a
module load PICI-LIGGGHTS/3.8.1-foss-2022a-VTK-9.2.2

cd $1
mpiexec -n {{ ntasks }} liggghts -in shake.sim
