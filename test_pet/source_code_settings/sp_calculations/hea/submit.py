import os


def launch(dataset, calculation, checkpoint, calculation_aux, checkpoint_aux, destination, batch_size, sp_hypers, path_save, gpu_id):
   
    os.system(f"python3 run.py {dataset} {calculation} {checkpoint} {calculation_aux} {checkpoint_aux} {destination} {batch_size} {sp_hypers} {path_save} {gpu_id}")
    

launch('hea/hea_test.xyz', 'hea/results/hea_bond_energies_continuation_1', 'best_val_rmse_both_model', 'None', 'None', 'hea', 150, 'hea_sp_hypers_selected.yaml', 'hea_predictions', 1)

