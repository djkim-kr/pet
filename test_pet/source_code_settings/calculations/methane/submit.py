import os

def submit(yaml, n_train, name):
    os.system(f'srun -o {name}.out -e {name}.errr --time=72:00:00 --cpus-per-task=20 --ntasks=1 --mem=100G --gres=gpu:1 --partition=gpu singularity run --nv ../../singularity_pytorch_geometric/singularity_pytorch_geometric.sif python3 ../../pet/train_model.py ../../datasets/methane/methane_train_{n_train}.extxyz ../../datasets/methane/methane_val.extxyz {yaml} ../../pet/default_hypers.yaml {name} & ')
    
    
def submit_pet_latest(yaml, n_train, name):
    os.system(f'srun -o {name}.out -e {name}.errr --time=72:00:00 --cpus-per-task=20 --ntasks=1 --mem=100G --gres=gpu:1 --partition=gpu singularity run --nv ../../singularity_pytorch_geometric/singularity_pytorch_geometric.sif python3 ../../pet_latest/train_model.py ../../datasets/methane/methane_train_{n_train}.extxyz ../../datasets/methane/methane_val.extxyz {yaml} ../../pet_latest/default_hypers.yaml {name} & ')
    
submit('methane_128_3_layers.yaml', '3k', '3k_128_3_layers')

