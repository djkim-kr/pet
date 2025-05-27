import os
import sys
import numpy as np
import time

dataset = sys.argv[1]
calculation = sys.argv[2]
checkpoint = sys.argv[3]
calculation_aux = sys.argv[4]
checkpoint_aux = sys.argv[5]
destination = sys.argv[6]
batch_size = sys.argv[7]
sp_hypers = sys.argv[8]
path_save = sys.argv[9]
gpu_id = sys.argv[10]

def launch(dataset, calculation, checkpoint, calculation_aux, checkpoint_aux, sp_hypers, destination, batch_size, path_save, gpu_id):
    
    with open(destination, 'a') as f:
        f.write(f'\n {sp_hypers} \n')
        
    os.system(f"CUDA_VISIBLE_DEVICES={gpu_id} MKL_THREADING_LAYER=GNU nohup python3 ../../pet_latest/estimate_error_sp.py ../../datasets/{dataset} ../../calculations/{calculation} {checkpoint} {calculation_aux} {checkpoint_aux} {sp_hypers} ../../pet_latest/default_hypers.yaml {batch_size} {path_save} True None >>{destination} &")
    
    with open(destination, 'a') as f:
        f.write('\n*******************************\n')
    
launch(dataset, calculation, checkpoint, calculation_aux, checkpoint_aux, sp_hypers, destination, batch_size, path_save, gpu_id)
   