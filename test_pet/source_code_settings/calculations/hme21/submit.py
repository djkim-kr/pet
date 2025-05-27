import os

def submit(yaml, name):
    os.system(f"srun -o {name}.out -e {name}.errr --time=72:00:00 --cpus-per-task=20 --ntasks=1 --mem=100G --gres=gpu:1 --partition=gpu singularity run --nv ../../singularity_pytorch_geometric/singularity_pytorch_geometric.sif python3 ../../pet/train_model.py ../../datasets/hme21/hme21_train.xyz ../../datasets/hme21/hme21_val.xyz {yaml} ../../pet/default_hypers.yaml {name} & ")

submit('hme21_ultra_fast_lr_decay_250_1.yaml', 'hme21_ultra_fast_lr_decay_250_1')
submit('hme21_ultra_fast_lr_decay_250_2.yaml', 'hme21_ultra_fast_lr_decay_250_2')
submit('hme21_ultra_fast_lr_decay_250_3.yaml', 'hme21_ultra_fast_lr_decay_250_3')
submit('hme21_ultra_fast_lr_decay_250_4.yaml', 'hme21_ultra_fast_lr_decay_250_4')

