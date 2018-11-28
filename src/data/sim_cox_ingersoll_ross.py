#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 07:43:11 2018

@author: Martin
"""

import numpy as np

def sim_CIR(kappa,eta,xi,T,X0,n_paths,n_steps):
    """
    Generates paths from exact solution X of the Square-root process.
    
    Parameters
    -------
    **kappa** : scalar
        Mean-reversion rate.
    **eta** : scalar
        Mean-reversion level.
    **xi** : scalar
        Diffusion rate.
    **T** : scalar
        X over [0,T] with step-size dt = T/n_steps.
    **X0** : scalar or array of size n_paths
        Initial value of X.
    **n_paths** : scalar
        Number of paths.
    **n_steps** : scalar
        Number of steps of X.
        
    Returns
    -------
    **X** : array of size n_paths x n_steps 
        Output with paths of X.
    
    """
    
    
    
    