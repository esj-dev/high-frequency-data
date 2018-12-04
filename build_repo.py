from .src.data.sim_cox_ingersoll_ross import sim_CIR
from .src.data.sim_ornstein_uhlenbeck import sim_OU
from .src.data.sim_3_over_2 import sim_32

# PATH SIMULATION

# Cox-Ingersoll-Ross

cir_param_k = 0.3
cir_param_e = 10
cir_param_x = 0.5

data_cir = target_cpa_from_roas_error()

# Ornstein-Uhlenbeck

ou_param_k = 0.3
ou_param_e = 10
ou_param_x = 0.5

data_ou = sim_ornstein_uhlenbeck(ou_param_k, ou_param_e, ou_param_x)
