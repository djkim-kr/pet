import os


def launch(dataset, calculation, checkpoint, calculation_aux, checkpoint_aux, destination, batch_size, sp_hypers):
   
    os.system(f"srun -o {destination}.out -e {destination}.errr --time=72:00:00 --cpus-per-task=20 --ntasks=1 --mem=120G --gres=gpu:1 --partition=gpu python3 run.py {dataset} {calculation} {checkpoint} {calculation_aux} {checkpoint_aux} {destination} {batch_size} {sp_hypers} &")
    

'''launch('methane/methane_test.extxyz', 'methane_only_energies/results/300k_very_long_continuation_4', 'best_val_rmse_energies_model', 'None', 'None', 'methane_only_energies_300k', 512, 'methane_sp_hypers.yaml')


launch('methane/methane_test.extxyz', 'methane_only_energies/results/100k_long_continuation_0', 'best_val_rmse_energies_model', 'None', 'None', 'methane_only_energies_100k', 512, 'methane_sp_hypers.yaml')

launch('methane/methane_test.extxyz', 'methane_only_energies/results/30k_long_continuation_0', 'best_val_rmse_energies_model', 'None', 'None', 'methane_only_energies_30k', 512, 'methane_sp_hypers.yaml')


launch('methane/methane_test.extxyz', 'methane_only_energies/results/3k', 'best_val_rmse_energies_model', 'None', 'None', 'methane_only_energies_3k', 512, 'methane_sp_hypers.yaml')

launch('methane/methane_test.extxyz', 'methane_only_energies/results/1k', 'best_val_rmse_energies_model', 'None', 'None', 'methane_only_energies_1k', 512, 'methane_sp_hypers.yaml')

launch('methane/methane_test.extxyz', 'methane_only_energies/results/10k', 'best_val_rmse_energies_model', 'None', 'None', 'methane_only_energies_10k', 512, 'methane_sp_hypers.yaml')

launch('methane/methane_test.extxyz', 'methane_only_energies/results/methane_short_length_10k', 'best_val_rmse_energies_model', 'None', 'None', 'methane_only_energies_short_length_10k', 512, 'methane_sp_hypers.yaml')'''

launch('methane/methane_test.extxyz', 'methane_only_energies/results/30k', 'best_val_rmse_energies_model', 'None', 'None', 'methane_only_energies_30k', 512, 'methane_sp_hypers.yaml')








