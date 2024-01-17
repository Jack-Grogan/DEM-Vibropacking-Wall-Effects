#!/bin/bash
#SBATCH --time=02:00:00
#SBATCH --nodes=1
#SBATCH --constraint=icelake
#SBATCH --ntasks=1


module purge; module load bluebear
module load bear-apps/2022a
module load SciPy-bundle/2022.05-foss-2022a
module load pyvista/0.36.1-foss-2022a
module load natsort/8.2.0-foss-2022a

export VENV_DIR="${HOME}/virtual-environments"
export VENV_PATH="${VENV_DIR}/my-virtual-env-${BB_CPU}"

# Create a master venv directory if necessary
mkdir -p ${VENV_DIR}

# Check if virtual environment exists and create it if not
if [[ ! -d ${VENV_PATH}  ]]; then
    python -m venv --system-site-packages ${VENV_PATH}
fi

# Activate the virtual environment
source ${VENV_PATH}/bin/activate

pip install konigcell

# Execute your Python scripts
mpiexec -n 1 python -u z_voxel_batch_continuous_packing_method.py
