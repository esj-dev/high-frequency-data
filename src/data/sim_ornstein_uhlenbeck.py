#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 16:48:11 2018

@author: Martin
"""

import numpy as np
import matplotlib.pyplot as plt

#%% Functions

def sim_OU(kappa,eta,xi,T,X0,n_paths,n_steps,dt=None,seed=None):
    """
    Generates paths from solution X of the Ornstein-Uhlenbeck process.
    
    Parameters
    -------
    kappa : scalar
        Mean-reversion rate.
    eta : scalar
        Mean-reversion level.
    xi : scalar
        Diffusion parameter.
    T : scalar
        X over [0,T] with step-size dt = T/n_steps.
    X0 : scalar or array of size n_paths
        Initial value of X.
    n_paths : int
        Number of paths.
    n_steps : int
        Number of steps of X (excluding initial X0)
    dt : scalar, optional
        If specified, input n_steps will be overruled, sometimes also T depending
        on if T/dt is integer or not.
        
    Returns
    -------
    X,t_vec : array of size n_paths x n_steps+1, array
        Output, paths of X and associated time points.
    
    """
    
    # initiate
    if dt is None:
        dt = T/n_steps
        t_vec = np.linspace(0,T,n_steps+1)
    else:
        t_vec = np.arange(start=0,stop=T+dt,step=dt)
        n_steps = t_vec.size-1
        T = t_vec[-1]
        
    X = np.zeros((n_paths,n_steps+1))
    X[:,0] = X0
    
    # generate paths
    for i in range(n_steps):
        X[:,i+1] = X[:,i]*np.exp(-kappa*dt) + eta*(1-np.exp(-kappa*dt)) + np.sqrt(xi**2*(1-np.exp(-2*kappa*dt))/(2*kappa))*np.random.normal(0,1,n_paths)
        
    # output
    return (X,t_vec)

#%% Example
    
if __name__ == "__main__":

    # params
    kappa = 10
    eta = 0.05
    xi = 2        
    X0 = [0,5]
    T = 5    
    
    # simulate
    X,t_vec = sim_OU(kappa,eta,xi,T,X0,n_paths=2,n_steps=1000)
        
    plt.plot(t_vec,X.transpose())
    plt.xlabel('time')
    plt.ylabel('OU process')





