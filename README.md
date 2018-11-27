Numerical Results for Prediction-Based Estimation w/ High-Frequency Data
========================================================================

Project Organization
--------------------

    │
    ├── .gitignore
    │
    ├── build_repo.py      <- master file that 1) pulls, simulates and wrangles data, 2) evaluates estimators & 3) generates plots
    │
    ├── data
    │   ├── external	   <- 3rd party financial data
    │   └── simulated	   <- simulated time series
    │
    ├── figures            <- generated plots
    │
    ├── models             <- diffusion model summaries
    │
    ├── notebooks          <- exploratory studies (naming convention is date_short_description.ipynb)
    │
	├── README.md
    │
    ├── references         <- research literature
    │
    ├── requirements.txt   <- collaborative Python requirements
    │
    └── src                <- project source code
        ├── __init__.py    <- makes src an importable Python module
        │
        ├── data           <- functions that pull or simulate data
        │   ├── __init__.py
        │   ├── sim_cox_ingersoll_ross.py
        │   └── sim_ornstein-uhlenbeck.py
        │
        └── estimators     <- functions that implement prediction-based estimators for parameters and Monte Carlo estimators for AVAR
            ├── __init__.py
            ├── est_avar_empirical_monte_carlo.py
            ├── est_avar_approximate_monte_carlo.py
            ├── est_param_cox-ingersoll_ross.py
            └── est_param_ornstein_uhlenbeck.py
