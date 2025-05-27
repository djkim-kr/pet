import os


def launch(dataset, calculation, checkpoint, calculation_aux, checkpoint_aux, destination, batch_size, sp_hypers):
   
    os.system(f"srun -o {destination}.out -e {destination}.errr --time=72:00:00 --cpus-per-task=20 --ntasks=1 --mem=120G --gres=gpu:1 --partition=gpu python3 run.py {dataset} {calculation} {checkpoint} {calculation_aux} {checkpoint_aux} {destination} {batch_size} {sp_hypers} &")

#launch('coll/coll_v1.2_AE_test.xyz', 'coll/results/coll_3_3_seed_0_with_energies_0.03_long_continuation_5', 'best_val_mae_both_model', '../../calculations/coll_auxiliary/results/coll_auxiliary_continuation_1', 'best_val_mae_both_model',  'coll', 150, 'coll_sp_hypers.yaml')




