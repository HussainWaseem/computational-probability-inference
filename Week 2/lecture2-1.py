# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 01:06:59 2016

@author: jpdjeredjian
"""
import comp_prob_inference
prob_table = {('sunny', 'hot'): 3/10,('sunny', 'cold'): 1/5,('rainy', 'hot'): 1/30,('rainy', 'cold'): 2/15,('snowy', 'hot'): 0,('snowy', 'cold'): 1/3}


#Approach 1: Use dictionaries within a dictionary. This works as follows:

prob_W_T_dict = {}

for w in {'sunny', 'rainy', 'snowy'}:
    prob_W_T_dict[w] =  {}
    
prob_W_T_dict['sunny']['hot'] = 3/10
prob_W_T_dict['sunny']['cold'] = 1/5
prob_W_T_dict['rainy']['hot'] = 1/30
prob_W_T_dict['rainy']['cold'] = 2/15
prob_W_T_dict['snowy']['hot'] = 0
prob_W_T_dict['snowy']['cold'] = 1/3

comp_prob_inference.print_joint_prob_table_dict(prob_W_T_dict)
print()
print(prob_W_T_dict['rainy']['cold'])

#Approach 2: Use a 2D array. Another approach is to directly store the joint probability table 
#as a 2D array, separately keeping track of what the rows and columns are. 
#We use a NumPy array (but really you could use Python lists within a Python list, 
#much like how the previous approach used dictionaries within a dictionary;
#the indexing syntax changes only slightly):

import numpy as np

prob_W_T_rows = ['sunny', 'rainy', 'snowy']
prob_W_T_cols = ['hot', 'cold']

prob_W_T_array = np.array([[3/10, 1/5], [1/30, 2/15], [0, 1/3]])
comp_prob_inference.print_joint_prob_table_array(prob_W_T_array, prob_W_T_rows, prob_W_T_cols)

#Retrieving a specific table entry requires a little bit more code since we need to figure out what the row and column numbers are corresponding to a specific pair of row and column labels.
prob_W_T_array[prob_W_T_rows.index('rainy'), prob_W_T_cols.index('cold')]

#Using .index does a search through the whole list of row/column labels, which for large lists can be slow. Let's fix this!
#A cleaner and faster way is to create separate dictionaries mapping the row and column 
#labels to row and column indices in the 2D array. In other words, 
#instead of writing prob_W_T_rows.index('rainy') to find the row number for 'rainy', 
#we want to just be able to write something like prob_W_T_row_mapping['rainy'], 
#which returns the row number. We can define Python variable prob_W_T_row_mapping as follows:

prob_W_T_row_mapping = {}
for index, label in enumerate(prob_W_T_rows):
    prob_W_T_row_mapping[label] = index
    
print()
print(list(enumerate(prob_W_T_rows)))

#In fact, the three lines we used to define prob_W_T_row_mapping can be written 
#in one line with a Python dictionary comprehension:

prob_W_T_row_mapping = {label: index for index, label in enumerate(prob_W_T_rows)}

#We can do the same thing to define a mapping of column labels to column numbers:

prob_W_T_col_mapping = {label: index for index, label in enumerate(prob_W_T_cols)}



#-------------------------------------------
#In summary, we can represent the joint probability table as follows:
prob_W_T_rows = ['sunny', 'rainy', 'snowy']
prob_W_T_cols = ['hot', 'cold']
prob_W_T_row_mapping = {label: index for index, label in enumerate(prob_W_T_rows)}
prob_W_T_col_mapping = {label: index for index, label in enumerate(prob_W_T_cols)}
prob_W_T_array = np.array([[3/10, 1/5], [1/30, 2/15], [0, 1/3]])

print()
print(prob_W_T_row_mapping)
print(prob_W_T_col_mapping)
print()
print(prob_W_T_array)
print()