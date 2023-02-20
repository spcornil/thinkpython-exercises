################
# Exercise 5-3 #
################
# If any of the three lengths is greater than the sum of the other two, then you cannot form
# a triangle. Otherwise, you can.
# Write a function that identifies if you can you form a triange given 3 integers.

import math

#a = int(input('What is the value of side a?\n'))
#b = int(input('What is the value of side b?\n'))
#c = int(input('What is the value of side c?\n'))

def is_triangle(a, b, c):
    v = [a, b, c]
    v.sort()
    if sum(v[:-1]) < v[-1]:
        print("No")
    if sum(v[:-1]) >= v[-1]:
        print("Yes")
    
#is_triangle(10, 2, 7)

################
# Exercise 5-4 #
################
# Modify the above function to prompt user input for side lengths

a = int(input('What is the value of side a?\n'))
b = int(input('What is the value of side b?\n'))
c = int(input('What is the value of side c?\n'))

def is_triangle(a, b, c):
    v = [a, b, c]
    v.sort()
    if sum(v[:-1]) < v[-1]:
        print("No")
    if sum(v[:-1]) >= v[-1]:
        print("Yes")
    
is_triangle(a, b, c)