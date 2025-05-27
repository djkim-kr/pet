import os


def launch(dataset, calculation, checkpoint, calculation_aux, checkpoint_aux, destination, batch_size, sp_hypers):
   
    os.system(f"srun -o {destination}.out -e {destination}.errr --time=72:00:00 --cpus-per-task=20 --ntasks=1 --mem=120G --gres=gpu:1 --partition=gpu python3 run.py {dataset} {calculation} {checkpoint} {calculation_aux} {checkpoint_aux} {destination} {batch_size} {sp_hypers} &")
    

for n_train in [100, 200, 500, 1000, 2000, 5000, 10000, 15000, 19500]:
    launch('qm9_vectorial_dipole_moments/test_qm9_dipoles.xyz', f'qm9_vectorial_dipole_moments/results/dipoles_{n_train}', 'best_val_mae_dipoles_model', 'None', 'None', f'dipoles_{n_train}', 100, 'sp_hypers_selected.yaml')








