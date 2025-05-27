import os


def launch(dataset, calculation, checkpoint, calculation_aux, checkpoint_aux, destination, batch_size, sp_hypers, path_save):
   
    os.system(f"srun -o {destination}.out -e {destination}.errr --time=72:00:00 --cpus-per-task=20 --ntasks=1 --mem=120G --gres=gpu:1 --partition=gpu python3 run.py {dataset} {calculation} {checkpoint} {calculation_aux} {checkpoint_aux} {destination} {batch_size} {sp_hypers} {path_save} &")
    

launch('MnO_scalar_spins/MnO_test.xyz', 'MnO_scalar_spins/results/spins_bond_energies_continuation_2', 'best_val_rmse_both_model', 'None', 'None', 'MnO_scalar_spins', 100, 'MnO_sp_hypers_selected.yaml', 'MnO_scalar_spins_predictions')

launch('MnO_scalar_spins/MnO_test.xyz', 'MnO_scalar_spins/results/no_spins_bond_energies', 'best_val_rmse_both_model', 'None', 'None', 'MnO_no_spins', 100, 'MnO_sp_hypers_selected.yaml', 'MnO_no_spins_predictions')

launch('MnO_scalar_spins/MnO_test_discretized.xyz', 'MnO_scalar_spins/results/spins_bond_energies_discretized_continuation_2', 'best_val_rmse_both_model', 'None', 'None', 'MnO_spins_discretized', 100, 'MnO_sp_hypers_selected.yaml', 'MnO_spins_discretized_predictions')

