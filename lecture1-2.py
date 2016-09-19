# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 22:09:14 2016

@author: jpdjeredjian
"""

model = {'heads':1/2, 'tails':1/2}
sample_space = set(model.keys())

x=6
y=6
z=1/36
model = {}
for i in range(1, x+1):
    for j in range(1, y+1):
        model[(i, j)] = z
        
print(model)

def prob_of_event(event, prob_space):
    total = 0
    for outcome in event:
        total += prob_space[outcome]
    return total
    
prob_space = {'sunny': 1/2, 'rainy': 1/6, 'snowy': 1/3}
rainy_or_snowy_event = {'rainy', 'snowy'}
print(" ")
print(prob_of_event(rainy_or_snowy_event, prob_space))

#Consider rolling two six-sided dice with faces numbered 1 through 6. "
#Again, we use the sample space from earlier Ω={(1,1),(1,2),…,(6,5),(6,6)}." 
#What is the event that the sum of the faces is 7? "
#Enter your answer as a Python set.""

prob_7 = {(1,6):1/36,(2,5):1/36,(3,4):1/36,(4,3):1/36,(5,2):1/36,(6,1):1/36}
event_7 = set(prob_7.keys())

