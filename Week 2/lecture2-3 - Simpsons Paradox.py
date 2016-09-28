# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 15:38:13 2016

@author: jpdjeredjian
"""

#I followed from the example how to normalize over one variable (gender), but I still cant get how to normalize over two (gender and department, as we are asked the probability of being admitted, given that the gender is female and department is A)

#Any help would be appreciated. Thanks a lot!
from simpsons_paradox_data import *

print( joint_prob_table[gender_mapping['female'], department_mapping['C'], admission_mapping['admitted']] )

joint_prob_gender_admission = joint_prob_table.sum(axis=1)
print()


print("joint_prob_gender_admission:")
print(joint_prob_gender_admission)
print()

female_only = joint_prob_gender_admission[gender_mapping['female']]
print("female only - unnormalized:")
print(female_only)
print()

prob_admission_given_female = female_only / np.sum(female_only)
print("female only - normalized:")
print(prob_admission_given_female)
print()

#This is the right conditional probability table, represented as an array. 
#To get it into the dictionary format we've been dealing 
#with earlier in the course, we do:

prob_admission_given_female_dict = dict(zip(admission_labels, prob_admission_given_female))
print("female only - normalized & DICT:")
print(prob_admission_given_female_dict)
print()
#hago el mismo proceso, pero para hombres:
male_only = joint_prob_gender_admission[gender_mapping['male']]
print("male only - unnormalized:")
print(male_only)
print()

prob_admission_given_male = male_only / np.sum(male_only)
print("male only - normalized:")
print(prob_admission_given_male)
print()

prob_admission_given_male_dict = dict(zip(admission_labels, prob_admission_given_male))
print("male only - normalized & DICT:")
print(prob_admission_given_male_dict)

#Condition on being admitted
admitted_only = joint_prob_gender_admission[:, admission_mapping['admitted']]
#The conditional probability table of gender given admitted is:
print(),print("gender given admitted - normalized & DICT:")
prob_gender_given_admitted = admitted_only /np.sum(admitted_only)
prob_gender_given_admitted_dict = dict(zip(gender_labels, prob_gender_given_admitted))
print(prob_gender_given_admitted_dict)



#For the following part, we will condition on both G and D 
#taking on specific values together. For example, to only look at the entries 
#in the 3D joint probability table for when G=female and, at the same time, D=A, 
#then we can do the following:

#Department A
female_and_A_only = joint_prob_table[gender_mapping['female'], department_mapping['A']]
prob_admission_given_female_and_A_only = female_and_A_only /np.sum(female_and_A_only)
prob_admission_given_female_and_A_only_dict = dict(zip(admission_labels, prob_admission_given_female_and_A_only))
print(),print("Table of female_and_A_only, admitted vs rejected")
print(prob_admission_given_female_and_A_only_dict)

male_and_A_only = joint_prob_table[gender_mapping['male'], department_mapping['A']]
prob_admission_given_male_and_A_only = male_and_A_only /np.sum(male_and_A_only)
prob_admission_given_male_and_A_only_dict = dict(zip(admission_labels, prob_admission_given_male_and_A_only))
print(),print("Table of male_and_A_only, admitted vs rejected")
print(prob_admission_given_male_and_A_only_dict)
print()

#Department B
female_and_B_only = joint_prob_table[gender_mapping['female'], department_mapping['B']]
prob_admission_given_female_and_B_only = female_and_B_only /np.sum(female_and_B_only)
prob_admission_given_female_and_B_only_dict = dict(zip(admission_labels, prob_admission_given_female_and_B_only))
print(),print("Table of female_and_B_only, admitted vs rejected")
print(prob_admission_given_female_and_B_only_dict)

male_and_B_only = joint_prob_table[gender_mapping['male'], department_mapping['B']]
prob_admission_given_male_and_B_only = male_and_B_only /np.sum(male_and_B_only)
prob_admission_given_male_and_B_only_dict = dict(zip(admission_labels, prob_admission_given_male_and_B_only))
print(),print("Table of male_and_B_only, admitted vs rejected")
print(prob_admission_given_male_and_B_only_dict)
print()

#Department C
female_and_C_only = joint_prob_table[gender_mapping['female'], department_mapping['C']]
prob_admission_given_female_and_C_only = female_and_C_only /np.sum(female_and_C_only)
prob_admission_given_female_and_C_only_dict = dict(zip(admission_labels, prob_admission_given_female_and_C_only))
print(),print("Table of female_and_C_only, admitted vs rejected")
print(prob_admission_given_female_and_C_only_dict)

male_and_C_only = joint_prob_table[gender_mapping['male'], department_mapping['C']]
prob_admission_given_male_and_C_only = male_and_C_only /np.sum(male_and_C_only)
prob_admission_given_male_and_C_only_dict = dict(zip(admission_labels, prob_admission_given_male_and_C_only))
print(),print("Table of male_and_C_only, admitted vs rejected")
print(prob_admission_given_male_and_C_only_dict)
print()

#Department D
female_and_D_only = joint_prob_table[gender_mapping['female'], department_mapping['D']]
prob_admission_given_female_and_D_only = female_and_D_only /np.sum(female_and_D_only)
prob_admission_given_female_and_D_only_dict = dict(zip(admission_labels, prob_admission_given_female_and_D_only))
print(),print("Table of female_and_D_only, admitted vs rejected")
print(prob_admission_given_female_and_D_only_dict)

male_and_D_only = joint_prob_table[gender_mapping['male'], department_mapping['D']]
prob_admission_given_male_and_D_only = male_and_D_only /np.sum(male_and_D_only)
prob_admission_given_male_and_D_only_dict = dict(zip(admission_labels, prob_admission_given_male_and_D_only))
print(),print("Table of male_and_D_only, admitted vs rejected")
print(prob_admission_given_male_and_D_only_dict)
print()

#Department E
female_and_E_only = joint_prob_table[gender_mapping['female'], department_mapping['E']]
prob_admission_given_female_and_E_only = female_and_E_only /np.sum(female_and_E_only)
prob_admission_given_female_and_E_only_dict = dict(zip(admission_labels, prob_admission_given_female_and_E_only))
print(),print("Table of female_and_E_only, admitted vs rejected")
print(prob_admission_given_female_and_E_only_dict)

male_and_E_only = joint_prob_table[gender_mapping['male'], department_mapping['E']]
prob_admission_given_male_and_E_only = male_and_E_only /np.sum(male_and_E_only)
prob_admission_given_male_and_E_only_dict = dict(zip(admission_labels, prob_admission_given_male_and_E_only))
print(),print("Table of male_and_E_only, admitted vs rejected")
print(prob_admission_given_male_and_E_only_dict)
print()

#Department F
female_and_F_only = joint_prob_table[gender_mapping['female'], department_mapping['F']]
prob_admission_given_female_and_F_only = female_and_F_only /np.sum(female_and_F_only)
prob_admission_given_female_and_F_only_dict = dict(zip(admission_labels, prob_admission_given_female_and_F_only))
print(),print("Table of female_and_F_only, admitted vs rejected")
print(prob_admission_given_female_and_F_only_dict)

male_and_F_only = joint_prob_table[gender_mapping['male'], department_mapping['F']]
prob_admission_given_male_and_F_only = male_and_F_only /np.sum(male_and_F_only)
prob_admission_given_male_and_F_only_dict = dict(zip(admission_labels, prob_admission_given_male_and_F_only))
print(),print("Table of male_and_E_only, admitted vs rejected")
print(prob_admission_given_male_and_F_only_dict)
print()