command to get test error:

singularity run --nv ../../singularity_pytorch_geometric/singularity_pytorch_geometric.sif python3 ../../pet/estimate_error.py ../../datasets/methane/methane_test.extxyz results/10k_128/hypers_used.yaml results/10k_128/best_val_rmse_energies_model_state_dict results/10k_128/all_species.npy results/10k_128/self_contributions.npy 10


