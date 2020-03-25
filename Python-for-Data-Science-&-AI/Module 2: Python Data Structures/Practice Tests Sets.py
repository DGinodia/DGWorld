# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 18:24:56 2020

@author: dginodia
"""

# Practice test for 
# Module 2: Data Structures --> Sets

#1. Consider the list A, what will be the result of the following operation: 
#   set(A)
# 1). the result will be a dictionary 
# 2). the result will be a set          (correct)
# 3). the result will be a list
A=[1,"@"]
set(A)

#2. Consider the Set: V={'A','B'}, what is the result of V.add('C')?
# 1). {'A','B','C'}     (Correct)
# 2). {'A','B'}
# 3). error
V={'A','B'}
V.add('C')
V

#3 What is the result of the following: '1' in {'1','2'}
# 1). False
# 2). True  (correct)
'1' in {'1','2'}
---------------------------------------------------------------------------
