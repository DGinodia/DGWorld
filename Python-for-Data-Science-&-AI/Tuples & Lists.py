# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 15:29:34 2020

@author: dginodia
"""

# Week 2 Python Data Structures
# -------------------------------------------------------------
# Tuples

Tuple1 = ("disco", 10, 1.2) # Tuples "()" are compound data types
print(type(Tuple1)) #This results in response: <class 'tuple'>

# 1. Indexing
print(Tuple1[0]) #Indexing 1st element of the Tuple

# 1.1 Find a string in the tuple
Tuple1.index("disco")

# 2. Slicing
print(Tuple1[1:3]) #slicing last 2 elements of the Tuple

print(Tuple1[1:len(Tuple1)+1]) #Same using a len command

# 3. Function sorted
Tuple2 = (10.7,8,5,3,1,2)
Tuple2 = sorted(Tuple2)
print(Tuple2)

# 4. Nesting
Tuple3=("Devesh", ("is", "learning"), 'Python', (1,8))
print(Tuple3[0])
print(Tuple3[1][0:2]) #Example of indexing a nested Tuple
print(Tuple3[2])

# 5. Concatenate
Tuple_Concat = Tuple3 + ("Today", " 3/22/2020")
print(Tuple_Concat)

# 6. Tuple is Immutable
#Tuple3[3]=(9,0) #returns TypeError

Tuple4=Tuple3 #Assign value of Tuple3 to Tuple 4
print("Tuple4:", Tuple4)
Tuple3=("Devesh", ("is", "learning"), 'Tuples') #Replace the value of Tuple3
print("Tuple3 reassigned:", Tuple3)
print("Tuple4 remains unchanged:", Tuple4) 
# Tuple4 remains unaffected due to change in Tuple3

# -------------------------------------------------------------
# Lists

# just playing with a list
List = [9,1,2,3.9,1,2.0, 5.0, 3.1, 0]
Sum1=0.0
i=0
while i < len(List):
    Sum1 = Sum1 + List[i]
    i = i+1
print(Sum1)

List1 = ["disco", 10, 1.2] # Lists "[]" are compound data types sames as Tuples
print(type(List1)) #This results in response: <class 'list'>

# 1. Indexing
print(List1[0]) #Indexing 1st element of the List

# 2. Slicing
print(List1[1:3]) #slicing last 2 elements of the List

print(List1[1:len(List1)+1]) #Same using a len command

# 3. Function sorted
List2 = (10.7,8,5,3,1,2)
List2 = sorted(List2)
print(List2)

# 4. Nesting
List3=["Devesh", ("is", "learning"), 'Python', (1,8)]
print(List3[0])
print(List3[1][0:2]) #Example of indexing a nested Tuple
print(List3[2])

# 5. Concatenate
List_Concat = List3 + ["Today", " 3/22/2020"]
print(List_Concat)

# 6. Aliasing Lists are Mutable i.e. can be changed unlike Tuples
List3[3]=[9,0] #Doesn't return any error
List3[0]=['DG']
print(List3) #result: ['DG', ('is', 'learning'), 'Python', (9, 0)]
List4=List3 #List4 is an alias of variable List3
print("List4:", List4)
List3[2]=["Lists"] #Change the value of an element in List3 
print("List3 changed:", List3)
print("List4 changed too:", List4) 
    # Notice List4 changes without any reassignment due to change in List3

# 6.1 Clone
List3=["Devesh", ("is", "learning"), 'Python', (1,8)]
List4=List3[:] #Clone value of List3 to List4
print("List4:", List4)
List3[2]=["Lists"] #Replace the value of an element in List3 
List3[0]=["DG"] #Replace the value of an element in List3 
print("List3 reassigned:", List3)
print("List4 remains unchanged:", List4) 
    # Notice List4 remains unchanged even with a change in List3



# 7. Methods: Extend, Append, Delete, Split
# 7.1 Extend
List3=["Devesh", ("is", "learning"), 'Python', (1,8)]
List3.extend(["Today", " 3/22/2020"])
print(List3) 
    # Notice the difference with #5.Concatenate. The final value is changed 
    # in List3 without using another variable List_Concat

# 7.2 Append
List3.append(["Its nice", "to", "learn", "coding", "again!"])
print(List3)
print(List3[len(List3)-1]) #Indexing the last element of List3

#7.3 Delete
del(List3[6][4]) #Removes the last element "again!" in the nested List
print(List3[6])

#7.4 Split
List3[6][0].split()
    #This splits element List3[6][0] but doesn't replace the element in List3
print(List3[6][0])
List3[6][0] = List3[6][0].split() 
    #To split the element in List3, reassign the value
print(List3[6]) 
    # Notice Split string in element List3[6][0]=['Its', 'Nice'] 

# ---------------------------------------------------------------------
# Using Help Command

help(List1)
help(Tuple1)