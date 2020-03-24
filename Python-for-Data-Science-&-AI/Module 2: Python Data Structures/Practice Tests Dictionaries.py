# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 18:04:56 2020

@author: dginodia
"""

# Practice test for 
# Module 2: Data Structures --> Dictionaries

#1. Consider the following dictionary:
#   { "The Bodyguard":"1992", "Saturday Night Fever":"1977"}
#   select the values
# 1) "1977" (correct)
# 2) "1992" (correct)
# 3) "The Bodyguard"
# 4) "Saturday Night Fever"
Dic={"The Bodyguard":"1992", "Saturday Night Fever":"1977"}
print(Dic.values())


#2. The variable release_year_dict is a Python Dictionary, what is the result of applying the following method: release_year_dict.keys()
# 1)  retrieve the keys of the dictionary (correct)
# 2)  retrieves, the values of the dictionary
release_year_dict={"The Bodyguard":"1992", "Saturday Night Fever":"1977"}
print(release_year_dict.keys())


#3. What is wrong with the following dictionary: {'a':1, 'a':2}
#   it has duplicate entries for the keys   (correct)
#   it has different entries for the values
Dup_keys={'a':1, 'a':2}
print(Dup_keys)  #Duplicate key value gets overridden
print(Dup_keys.keys())
print(Dup_keys.values())
