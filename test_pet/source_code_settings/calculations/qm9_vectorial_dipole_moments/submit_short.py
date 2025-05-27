import os

def submit(n_train):
    name = f"dipoles_{n_train}"

    os.system(f'srun -o {name}.out -e {name}.errr --time=72:00:00 --cpus-per-task=20 --ntasks=1 --mem=100G --gres=gpu:1 --partition=gpu --comment="scitas_capping" singularity run --nv ../../singularity_pytorch_geometric/singularity_pytorch_geometric.sif python3 ../../pet_dipoles/train_model.py ../../datasets/qm9_vectorial_dipole_moments/train_qm9_dipoles_{n_train}.xyz ../../datasets/qm9_vectorial_dipole_moments/val_qm9_dipoles.xyz dipoles_short.yaml ../../pet_dipoles/default_hypers.yaml {name} &')
    
    
n_train_grid = [100, 200]
for n_train in n_train_grid:
    submit(n_train)