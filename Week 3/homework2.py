# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 00:26:15 2016

@author: jpdjeredjian
"""

import numpy as np

prob_S_C = np.array([[0.4,  0.10],  
                     [0.25, 0.25]])

#We can get the marginal distributions pW and pI:

prob_S = prob_S_C.sum(axis=1)
prob_C = prob_S_C.sum(axis=0)

print(np.outer(prob_S,prob_C))
#No arroja una matriz igual a la inicial, por lo que NO son indpendientes



prob_S_C_givenTequals0 = np.array([[0.72, 0.08],  
                                   [0.18, 0.02]])
                                   
prob_S_givenTequals0 = prob_S_C_givenTequals0.sum(axis=1)
prob_C_givenTequals0 = prob_S_C_givenTequals0.sum(axis=0)

print("Outer de prob_S_C_givenTequals0")
outerprob_S_C_givenTequals0 = np.outer(prob_S_givenTequals0,prob_C_givenTequals0)
print(outerprob_S_C_givenTequals0)
print("Si es independiente porque da la misma matriz")

prob_S_C_givenTequals1 = np.array([[0.08, 0.12],  
                                   [0.32, 0.48]])

prob_S_givenTequals1 = prob_S_C_givenTequals1.sum(axis=1)
prob_C_givenTequals1 = prob_S_C_givenTequals1.sum(axis=0)

print("Outer de prob_S_C_givenTequals1")
outerprob_S_C_givenTequals1 = np.outer(prob_S_givenTequals1,prob_C_givenTequals1)
print(outerprob_S_C_givenTequals1)
print("Si es independiente porque da la misma matriz")

outerprob_S_C_givenTequals1_margS = outerprob_S_C_givenTequals1.sum(axis=1)
outerprob_S_C_givenTequals1_margS_C = outerprob_S_C_givenTequals1_margS.sum(axis=0)
