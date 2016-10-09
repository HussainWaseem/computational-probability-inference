# -*- coding: utf-8 -*-
"""
Created on Sun Oct  2 22:56:08 2016

@author: jpdjeredjian
"""

import numpy as np

prob_W_I = np.array([[1/2,0],  [0,1/6],  [0,1/3]])

#We can get the marginal distributions pW and pI:

prob_W = prob_W_I.sum(axis=1)
prob_I = prob_W_I.sum(axis=0)

print(np.outer(prob_W, prob_I))
#No arroja una matriz igual a la inicial, por lo que no son Independientes



#Repito lo mismo para la table X, Y

prob_X_Y = np.array([[1/4,1/4],  [1/12,1/12],  [1/6,1/6]])

prob_X = prob_W_I.sum(axis=1)
prob_Y = prob_W_I.sum(axis=0)

print(np.outer(prob_X, prob_Y))
#SI arroja una matriz igual a la inicial, por lo que SI son Independientes