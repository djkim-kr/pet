import os

def submit(yaml, name):
    os.system(f'srun -o {name}.out -e {name}.errr --time=72:00:00 --cpus-per-task=20 --ntasks=1 --mem=100G --gres=gpu:1 --partition=gpu singularity run --nv ../../singularity_pytorch_geometric/singularity_pytorch_geometric.sif python3 ../../pet/train_model.py ../../datasets/water/water_train_1303.xyz ../../datasets/water/water_val.xyz {yaml} ../../pet/default_hypers.yaml {name} & ')

'''submit('water_1_1.yaml', 'water_1_1')
submit('water_1_2.yaml', 'water_1_2')
submit('water_1_3.yaml', 'water_1_3')
submit('water_2_1.yaml', 'water_2_1')
submit('water_2_2.yaml', 'water_2_2')
submit('water_2_3.yaml', 'water_2_3')
submit('water_3_1.yaml', 'water_3_1')
submit('water_3_2.yaml', 'water_3_2')'''

submit('water_4_1.yaml', 'water_4_1')
submit('water_4_2.yaml', 'water_4_2')
submit('water_5_1.yaml', 'water_5_1')
submit('water_5_2.yaml', 'water_5_2')
submit('water_6_1.yaml', 'water_6_1')
