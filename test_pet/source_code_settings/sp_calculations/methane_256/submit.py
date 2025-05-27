import os


def launch(dataset, calculation, checkpoint, calculation_aux, checkpoint_aux, destination, batch_size, sp_hypers, path_save, gpu_id):
   
    os.system(f"python3 run.py {dataset} {calculation} {checkpoint} {calculation_aux} {checkpoint_aux} {destination} {batch_size} {sp_hypers} {path_save} {gpu_id}")        

launch('methane/methane_test.extxyz', 'methane_256/results/300k_continuation_8', 'best_val_rmse_energies_model', 'None', 'None', 'methane_300k_256', 512, 'methane_sp_hypers.yaml', '300k_256_predictions', 0)


