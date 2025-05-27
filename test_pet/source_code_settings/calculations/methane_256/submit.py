import os

def submit(yaml, n_train, name):
    os.system(f'srun -o {name}.out -e {name}.errr --time=72:00:00 --cpus-per-task=20 --ntasks=1 --mem=100G --gres=gpu:1 --partition=gpu singularity run --nv ../../singularity_pytorch_geometric/singularity_pytorch_geometric.sif python3 ../../pet/train_model.py ../../datasets/methane/methane_train_{n_train}.extxyz ../../datasets/methane/methane_val_full.extxyz {yaml} ../../pet/default_hypers.yaml {name} & ')

submit('methane_256_5e-5.yaml', '100k', '100k_5e-5')
submit('methane_256.yaml', '300k', '300k')

