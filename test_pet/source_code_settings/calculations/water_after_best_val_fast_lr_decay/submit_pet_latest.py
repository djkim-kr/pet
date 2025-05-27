import os

def submit(yaml, name):
    os.system(f'srun -o {name}.out -e {name}.errr --time=72:00:00 --cpus-per-task=20 --ntasks=1 --mem=100G --gres=gpu:1 --partition=gpu singularity run --nv ../../singularity_pytorch_geometric/singularity_pytorch_geometric.sif python3 ../../pet_latest/train_model.py ../../datasets/water/water_train_1303.xyz ../../datasets/water/water_val.xyz {yaml} ../../pet_latest/default_hypers.yaml {name} & ')

'''submit('12_1_after_best_val.yaml', '12_1_after_best_val')
submit('6_2_after_best_val.yaml', '6_2_after_best_val')
submit('4_3_after_best_val.yaml', '4_3_after_best_val')
submit('3_4_after_best_val.yaml', '3_4_after_best_val')
submit('2_6_after_best_val.yaml', '2_6_after_best_val')
submit('1_12_after_best_val.yaml', '1_12_after_best_val')'''


#submit('6_2_after_best_val_4.0.yaml', '6_2_after_best_val_4.0')

#submit('6_2_after_best_val_3.0.yaml', '6_2_after_best_val_3.0')
#submit('6_2_after_best_val_3.25.yaml', '6_2_after_best_val_3.25')
#submit('6_2_after_best_val_3.5.yaml', '6_2_after_best_val_3.5')
submit('6_2_after_best_val_4.25.yaml', '6_2_after_best_val_4.25')
submit('6_2_after_best_val_4.5.yaml', '6_2_after_best_val_4.5')
