import os

def submit(yaml, name):
    os.system(f'srun -o {name}.out -e {name}.errr --time=72:00:00 --cpus-per-task=20 --ntasks=1 --mem=100G --gres=gpu:1 --partition=gpu singularity run --nv ../../singularity_pytorch_geometric/singularity_pytorch_geometric.sif python3 ../../pet/train_model.py ../../datasets/water/water_train_1303.xyz ../../datasets/water/water_val.xyz {yaml} ../../pet/default_hypers.yaml {name} & ')

#submit('water_3_3.yaml', 'water_3_3')
#submit('water_1_12.yaml', 'water_1_12')
#submit('water_2_6.yaml', 'water_2_6')
#submit('water_3_4.yaml', 'water_3_4')
#submit('water_4_3.yaml', 'water_4_3')
#submit('water_6_2.yaml', 'water_6_2')
#submit('water_12_1.yaml', 'water_12_1')

#submit('water_6_2_4.0.yaml', 'water_6_2_4.0')
#submit('water_6_2_4.25.yaml', 'water_6_2_4.25')

submit('water_6_2_4.5.yaml', 'water_6_2_4.5')
#submit('water_6_2_3.5.yaml', 'water_6_2_3.5')
#submit('water_6_2_3.25.yaml', 'water_6_2_3.25')
#submit('water_6_2_3.0.yaml', 'water_6_2_3.0')