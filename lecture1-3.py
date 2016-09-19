# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 00:34:52 2016

@author: jpdjeredjian
"""
import comp_prob_inference
prob_space = {'sunny': 1/2, 'rainy': 1/6, 'snowy': 1/3}

random_outcome = comp_prob_inference.sample_from_finite_probability_space(prob_space)
W = random_outcome
if random_outcome == 'sunny':
    I = 1
else:
    I = 0
    

#Crear set con probabilidad de que salga 
#cada numero (de 2 a 12) al tirar dos dados

dice_dict = dict()
for i in range(1,7):
    for j in range(1,7):
        try: 
            dice_dict[i+j] += 1/36
        except:     
            dice_dict[i+j] = 1/36
        