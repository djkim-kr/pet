/datasets contains the datasets used in our work. 

******************************************************************************************************************

/singularity_pytorch_geometric contains a Singularity container we used for all our experiments.

******************************************************************************************************************

/code folder contains the source code of PET and our proof-of-principle implementation of the ECSE protocol.

/code/pet_latest is the main version of our code. Most of the fitting procedures were performed with the older version: /code/pet. Backward compatibility should be ensured, we include /code/pet just in case. /code/pet_dipoles contains implementation for covariant vectorial dipole moments that have not yet been integrated with the main codebase. /code/pet_loss_per_atom is a last-minute change of the loss in energies definition as we described for the HME21 dataset in appendices.

Benchmarks reported in our work were obtained using 3 scripts (inside any of the code subfolders): 1) train_model.py 2) estimate_error.py and 3) estimate_error_sp.py

train_model.py gets the following arguments: 
1) path to training .xyz structures
2) path to va .xyz structures
3) path to YAML file with hyperparameters
4) path to YAML file with default hyperparameters
5) string with the name of the calculation

It loads the hyperparameters from arguments 3) and 4) and overrides those in 4) that are provided in 3). There is a file with default hyperparameters: /code/pet_latest/default_hypers.yaml

Being invoked this script fits the PET and stores the result in the folder {folder_where_it_was_run}/results/{name_of_calculation}. If it observes that such a folder already exists it loads the last checkpoint for this folder and continues the calculation. See for example /calculations/coll/results/coll_3_3_seed_0_with_energies_0.03_long
/calculations/coll/results/coll_3_3_seed_0_with_energies_0.03_long_continuation_0
/calculations/coll/results/coll_3_3_seed_0_with_energies_0.03_long_continuation_1 and so on. Note that every time this script is invoked it starts counting epochs from scratch to towards the maximal one provided in the YAML file. Also, one can provide maximal duration time instead of the number of epochs. 

Each such folder contains  - a YAML file with hyperparameters used, for instance,/calculations/coll/results/coll_3_3_seed_0_with_energies_0.03_long/hypers_used.yaml. It saves logs, the last checkpoint, and several checkpoints with the best MAE or RMSE in energies or forces on the validation dataset. 

estimate_error.py is used to compute the error of not symmetrized model and gets the following arguments:
1) path to test structures
2) path to the folder with checkpoints such as discussed above
3) specific checkpoint, such as "best_val_rmse_forces" or "best_val_mae_energies".
4) number of test rotational augmentations
5) path to default hypers
6) batch size
7) path to save predictions or None, to not save them, and only print error metrics. 

estimate_error_sp.py is used to compute the error of symmetrized model (sp stands for symmetrization protocol, an old name of ECSE). 
parameters are:
1) path to test structures
2) path to the folder with checkpoints of the main model
3) specific checkpoint of the main model
4) path to the folder with checkpoints of the auxiliary model (or None)
5) specific checkpoint of the auxiliary model (or None)
6) path to YAML file with ECSE parameters
7) path to YAML file with default ECSE parameters (same semantics, as for train_model.py script)
8) batch size
9) path to save predictions or None
10) Bool indicating if it is verbose or not
11) Maximal number of coordinate systems in ECSE, so it stops if actuall number exceeds this threshold. 


******************************************************************************************************************


/calculations/ folder contains all the information about fitting the base PET model. As was already mentioned in the Code section full list of hypers can be accessed from YAML files stored in folders 
as: /calculations/coll/results/coll_3_3_seed_0_with_energies_0.03_long/hypers_used.yaml. 

Also files like /calculations/coll/coll_3_3_seed_0_with_energies_0.03_long.yaml corresponds to argument 3) of the train_model.py script mentioned above.

Files such as /calculations/coll/submit.py provide examples of how one can submit fitting procedure with train_model.py script using the slurm queue system. (it assumes that folders with code such as /code/pet are at the root level /pet, not in the /code subfolder)

Also, folders with calculations contain logs. See for example notebook/calculations/coll/plotting_energies.ipynb that loads them and plots train/val errors depending on the epoch num. (note that it plots exponential sliding average for better readability). 

******************************************************************************************************************

/sp_calculations/ folder contains YAML files with parameters of ECSE, outputs of the estimate_error_sp.py script, and sometimes saved predictions. 



******************************************************************************************************************


pet_hypers.txt file contains a short description of hyperparameters used by PET. 

