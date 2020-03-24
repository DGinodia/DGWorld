# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 17:40:44 2020

@author: dginodia
"""

# ---------------------------------------------------------------------
# Practice Test

#1. What is the syntax to obtain the first element of the tuple:
# A=('a','b','c')
A=('a','b','c')
print(A[1])
print(A[0]) # correct
print(A[:])


#2. Consider the tuple A=((11,12),[21,22]), that contains 
#   a tuple and list. What is the result of the following operation 
#   A[1]:
# 1) ((11,12),[21,22])
# 2) (11,12)
# 3) [21,22] (correct)

A=((11,12),[21,22])
print(A[1])


#3. Consider the tuple A=((1),[2,3],[4]), that contains 
#   a tuple and list. What is the result of the following 
#   operation A[2][0]:
# 1) 4  (correct)
# 2) [4]
# 3) 1
A=((1),[2,3],[4])
print(A[2][0])



#4. What is the result of the following operation: 
#   '1,2,3,4'.split(',')
# 1) '1','2','3','4'
# 2) ['1','2','3','4']      (correct)
# 3) '1234'
# 4) ('1','2','3','4')
print('1,2,3,4'.split(','))


#5. The method append does the following:
# 1) adds one element to a list
# 2) merges two lists or insert multiple elements 
#    to a list (correct)
A=[1,2,3,"4"]
B=["A", 12]
A.append(B)
print(A)


#6. lists are mutable
# 1) True   (correct)
# 2) False
A=[1,2,3,"4"]
A[0]="Lists can be changed"
print(A)


#7 consider the following list : A=["hard rock",10,1.2]
#   what will list A contain affter the following command is run: del(A[1])
# 1) [10,1.2]
# 2) ["hard rock",1.2] (correct)
# 3) ["hard rock",10]

A=["hard rock",10,1.2]
del(A[1])
print(A)


#8 what is the syntax to clone the list A and assign the result to list B
# 1) B=A
# 2) B=A[:] (Correct))
A=["hard rock",10,1.2]
B=A
A[0]=1
print(A) #A is changed
print(B) #B also changed hence not a clone

A=["hard rock",10,1.2]
B=A[:]
A[0]=1
print(A) #A is changed
print(B) #B did not change hence not a clone


#9 what is the result of the following: len(("disco",10))
# 1) 2 (correct))
# 2) 6
# 3) 5
print(len(("disco",10)))
