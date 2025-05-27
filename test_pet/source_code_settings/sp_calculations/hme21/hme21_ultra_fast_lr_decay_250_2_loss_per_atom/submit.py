import os


def launch(dataset, calculation, checkpoint, calculation_aux, checkpoint_aux, destination, batch_size, sp_hypers, path_save, gpu_id):
   
    os.system(f"python3 run.py {dataset} {calculation} {checkpoint} {calculation_aux} {checkpoint_aux} {destination} {batch_size} {sp_hypers} {path_save} {gpu_id}")
    

for i in range(8):
    launch(f'hme21/hme21_test_chunk_{i}.xyz', 'hme21/results/hme21_ultra_fast_lr_decay_250_2_loss_per_atom', 'best_val_mae_both_model', 'None', 'None', f'hme21_chunk_{i}', 50, 'hme21_sp_hypers_selected.yaml', f'hme21_predictions_{i}', i)

    

