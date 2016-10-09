# -*- coding: utf-8 -*-
"""
Created on Sun Oct  2 21:34:25 2016

@author: jpdjeredjian
"""
import math

def nCr(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)
    
a = 100 * ( (1/27)** 1 )    *   ( (1-1/27)**(100-1) )

b = 99 * (1/27)** 1 * (1-1/27)**(99-1)

proba = 0
probb = 0

n = 100
p = 1/27

for s in range(1,n+1):
    proba += nCr(n,s) * ( p**s)  *  ( (1-p)**(n-s) )
    
n = 99

for s in range(1,n+1):
    probb += nCr(n,s) * ( p**s)  *  ( (1-p)**(n-s) )