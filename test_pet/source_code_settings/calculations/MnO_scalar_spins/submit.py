import os

def submit(yaml, name):
    os.system(f'srun -o {name}.out -e {name}.errr --time=72:00:00 --cpus-per-task=20 --ntasks=1 --mem=100G --gres=gpu:1 --partition=gpu singularity run --nv ../../singularity_pytorch_geometric/singularity_pytorch_geometric.sif python3 ../../pet/train_model.py ../../datasets/MnO_scalar_spins/MnO_train.xyz ../../datasets/MnO_scalar_spins/MnO_val.xyz {yaml} ../../pet/default_hypers.yaml {name} & ')

    
def submit_discretized(yaml, name):
    os.system(f'srun -o {name}.out -e {name}.errr --time=72:00:00 --cpus-per-task=20 --ntasks=1 --mem=100G --gres=gpu:1 --partition=gpu singularity run --nv ../../singularity_pytorch_geometric/singularity_pytorch_geometric.sif python3 ../../pet/train_model.py ../../datasets/MnO_scalar_spins/MnO_train_discretized.xyz ../../datasets/MnO_scalar_spins/MnO_val_discretized.xyz {yaml} ../../pet/default_hypers.yaml {name} & ')
    
    
#submit('spins_bond_energies.yaml', 'spins_bond_energies')

#submit('no_spins_bond_energies.yaml', 'no_spins_bond_energies')
submit_discretized('spins_bond_energies.yaml', 'spins_bond_energies_discretized')