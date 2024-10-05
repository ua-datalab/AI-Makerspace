#!/bin/bash

#SBATCH --job-name=resnet
#SBATCH --output=%x_%A_%a.out
#SBATCH --account=windfall
#SBATCH --partition=gpu_windfall
#SBATCH --nodes=2
#SBATCH --gres=gpu:1
#SBATCH --ntasks=2
#SBATCH --cpus-per-task=8
#SBATCH --time=01:00:00

module load anaconda
source ~/.bashrc
conda activate makespace
export MASTER_ADDR=$(scontrol show hostname ${SLURM_NODELIST} | head -n 1)
echo $MASTER_ADDR
echo $SLURM_NODELIST
#torchrun --nnodes=2 --nproc_per_node=1 --rdzv_id=100 --rdzv_backend=c10d --rdzv_endpoint=$MASTER_ADDR:29401 toytorch.py
srun torchrun --nnodes=2 --nproc_per_node=1 --rdzv_id=100 --rdzv_backend=c10d --rdzv_endpoint=$MASTER_ADDR:29401 resnet50.py --batch_size 128 1 1
