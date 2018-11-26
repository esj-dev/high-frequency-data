Numerical Results for Prediction-Based Estimation w/ High-Frequency Data
========================================================================

Project Organization
--------------------

    │
    ├── .gitignore
    │
    ├── build-repo.py      <- master file that 1) pulls, simulates and wrangles data, 2) evaluates estimators & 3) generates plots
    │
    ├── data
    │   ├── external	   <- 3rd party financial data
    │   └── simulated	   <- simulated time series
    │
    ├── figures            <- generated plots
    │
    ├── models             <- diffusion model summaries
    │
    ├── notebooks          <- exploratory studies (naming convention is number-short-description.ipynb)
    │
	├── README.md
    │
    ├── references         <- research literature
    │
    ├── requirements.txt   <- collaborative Python requirements
    │
    └── src                <- project source code
        ├── __init__.py    <- makes src a Python module
        │
        ├── data           <- scripts that pull or simulate data
        │   ├── sim-cox-ingersoll-ross.py
        │   └── sim-ornstein-uhlenbeck.py
        │
        └── estimators     <- scripts that implement prediction-based estimators for parameters and Monte Carlo estimators for AVAR
            ├── est-avar-empirical-monte-carlo.py
            ├── est-avar-approximate-monte-carlo.py
            ├── est-param-cox-ingersoll-ross.py
            └── est-param-ornstein-uhlenbeck.py
