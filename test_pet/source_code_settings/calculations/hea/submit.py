import os

def submit(yaml, name):
    os.system(f"srun -o {name}.out -e {name}.errr --time=72:00:00 --cpus-per-task=20 --ntasks=1 --mem=100G --gres=gpu:1 --partition=gpu singularity run --nv ../../singularity_pytorch_geometric/singularity_pytorch_geometric.sif python3 ../../pet/train_model.py ../../datasets/hea/hea_train_24630.xyz ../../datasets/hea/hea_val.xyz {yaml} ../../pet/default_hypers.yaml {name} & ")

submit('hea_bond_energies.yaml', 'hea_bond_energies')
