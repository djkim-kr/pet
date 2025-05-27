import os

def submit(yaml, name):
    os.system(f'srun -o {name}.out -e {name}.errr --time=72:00:00 --cpus-per-task=20 --ntasks=1 --mem=100G --gres=gpu:1 --partition=gpu singularity run --nv ../../singularity_pytorch_geometric/singularity_pytorch_geometric.sif python3 ../../pet_latest/train_model.py ../../datasets/water/water_train_1303.xyz ../../datasets/water/water_val.xyz {yaml} ../../pet_latest/default_hypers.yaml {name} & ')


submit('water_6_2_ultra_fast_lr_decay_after_best_val.yaml', 'water_6_2_ultra_fast_lr_decay_after_best_val')