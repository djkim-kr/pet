import os


def launch(dataset, calculation, checkpoint, calculation_aux, checkpoint_aux, destination, batch_size, sp_hypers):
   
    os.system(f"srun -o {destination}.out -e {destination}.errr --time=72:00:00 --cpus-per-task=20 --ntasks=1 --mem=120G --gres=gpu:1 --partition=gpu python3 run.py {dataset} {calculation} {checkpoint} {calculation_aux} {checkpoint_aux} {destination} {batch_size} {sp_hypers} &")
    

launch('methane/methane_test.extxyz', 'methane/results/3k_128_3_layers_continuation_0', 'best_val_rmse_energies_model', 'None', 'None', 'methane_3k', 512, 'methane_sp_hypers.yaml')

'''launch('methane/methane_test.extxyz', 'methane/results/100k_128_3_layers_long_continuation_4', 'best_val_rmse_energies_model', 'None', 'None', 'methane_100k', 512, 'methane_sp_hypers.yaml')

launch('methane/methane_test.extxyz', 'methane/results/30k_128_3_layers_long_continuation_2', 'best_val_rmse_energies_model', 'None', 'None', 'methane_30k', 512, 'methane_sp_hypers.yaml')

launch('methane/methane_test.extxyz', 'methane/results/10k_128_3_layers_medium_continuation_2', 'best_val_rmse_energies_model', 'None', 'None', 'methane_10k', 512, 'methane_sp_hypers.yaml')

launch('methane/methane_test.extxyz', 'methane/results/1k_128_3_layers', 'best_val_rmse_energies_model', 'None', 'None', 'methane_1k', 512, 'methane_sp_hypers.yaml')

launch('methane/methane_test.extxyz', 'methane/results/300_methane_128_3_layers', 'best_val_rmse_energies_model', 'None', 'None', 'methane_300', 512, 'methane_sp_hypers.yaml')'''


