#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 21:42:34 2018

@author: Martin
"""

import numpy as np
import matplotlib.pyplot as plt
from .src.data.sim_cox_ingersoll_ross import sim_CIR

#%%

def sim_32(kappa,eta,xi,T,X0,n_paths,n_steps,dt=None,seed=None):
    """
    Generates paths from exact solution X of the 3-over-2 process.
    
    Parameters
    -------
    kappa : scalar
        Mean-reversion rate.
    eta : scalar
        Mean-reversion level.
    xi : scalar
        Diffusion rate.
    T : scalar
        X over [0,T] with step-size dt = T/n_steps.
    X0 : scalar or array of size n_paths
        Initial value of X.
    n_paths : int
        Number of paths.
    n_steps : int
        Number of steps of X (excluding initial X0)
    dt : scalar, optional
        If specified, input n_steps will be overruled, sometimes also T, depending
        on if T/dt is integer or not.
        
        
    Returns
    -------
    X,t_vec : array of size n_paths x n_steps+1, array
        Output, paths of X and associated time points.
    
    """
    
    # simulate reciprocal CIR process
    Y,t_vec = sim_CIR(kappa=kappa*eta,eta=(kappa+xi**2)/(kappa*eta),xi=xi,T=T,X0=1/X0,n_paths=n_paths,n_steps=n_steps,dt=dt,seed=seed)
        
    # output
    return (1/Y,t_vec)

#%%

if __name__ == "__main__":

    # params
    kappa = 2.5
    eta = 30
    xi = 100        
    X0 = 0.2
    T = 5    
    
    # simulate
    X,t_vec = sim_32(kappa,eta,xi,T,X0,n_paths=2,n_steps=10000)
    X,t_vec = sim_32(kappa,eta,xi,T,X0,n_paths=1,n_steps=10000,dt=0.49)
    
    t_vec[-1]           # actual T
    t_vec.size-1        # actual n_steps
    T/(t_vec.size-1)    # not equal dt if T redefined
    t_vec[1]            # actual dt
    
    plt.plot(t_vec,X.transpose())
    plt.xlabel('time')
    plt.ylabel('3-over-2 process')
    
    