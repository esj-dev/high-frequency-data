#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 07:43:11 2018

@author: Martin
"""

import numpy as np
import matplotlib.pyplot as plt

#%% Functions

def sim_CIR(kappa,eta,xi,T,X0,n_paths,n_steps,dt=None,seed=None):
    """
    Generates paths from exact solution X of the Square-root process.
    
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
        
    X = np.zeros((n_paths,n_steps+1))
    X[:,0] = X0
    
    # auxilary variables
    d = 4*eta*kappa/xi**2
    nn = 4*kappa/xi**2*np.exp(-kappa*dt)/(1-np.exp(-kappa*dt))
    
    # set seed?
    if seed is not None:
        np.random.seed(seed)
    
    # generate paths
    for i in range(n_steps):
        N = np.random.poisson(0.5*X[:,i]*nn,n_paths)
        df = d + 2*N
        Xi = np.random.chisquare(df,n_paths)
        X[:,i+1] = Xi*np.exp(-kappa*dt)/nn
        
    # output
    return (X,t_vec)
    

#%% Example
    
if __name__ == "__main__":

    # params
    kappa = 10
    eta = 0.05
    xi = 2        
    X0 = 0.2
    T = 5
    
    
    # simulate
    X,t_vec = sim_CIR(kappa,eta,xi,T,X0,n_paths=1,n_steps=10000)
    X,t_vec = sim_CIR(kappa,eta,xi,T,X0,n_paths=1,n_steps=10000,dt=0.49)
    
    t_vec[-1]           # actual T
    t_vec.size-1        # actual n_steps
    T/(t_vec.size-1)    # not equal dt if T redefined
    t_vec[1]            # actual dt
    
    plt.plot(t_vec,X.transpose())
    plt.xlabel('time')
    plt.ylabel('CIR process')
    

