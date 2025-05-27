import os

def submit(yaml, name):
    os.system(f'srun -o {name}.out -e {name}.errr --time=70:00:00 --cpus-per-task=10 --ntasks=1 --mem=60G --gres=gpu:1 --partition=gpu singularity run --nv ../../singularity_pytorch_geometric/singularity_pytorch_geometric.sif python3 ../../pet/train_model.py ../../datasets/qm9/qm9_train.xyz ../../datasets/qm9/qm9_val.xyz {yaml} ../../pet/default_hypers.yaml {name} & ')

submit('qm9_length_long.yaml','qm9_length_long')



