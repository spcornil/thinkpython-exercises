################
# Exercise 3-1 #
################
# Write a function named right_justify that takes a string named s as a parameter and
# prints the string with enough leading spaces so that the last letter of the string is in column
# 70 of the display:
   
def right_justify(monty):
    print(' ' * (70 - len(monty)) + monty)

right_justify('dudeguy')

################
# Exercise 3-2 #
################
# Functions within functions #
# 1 #
# Type this example into a script and test it.
def do_twice(f):
    f()
    f()

# 2 #
# Modify do_twice so that it takes two arguments, a function object and a value, and
# calls the function twice, passing the value as an argument.
def do_twice(f, a):
    f(a)
    f(a)

# 3 #
# Copy the definition of print_twice from earlier in this chapter to your script.
def print_twice(a):
    print(a)
    print(a)

# 4 #
# Use the modified version of do_twice to call print_twice twice, passing 'spam' as
# an argument.
do_twice(print, 'spam')

# 5 #
# Define a new function called do_four that takes a function object and a value and
# calls the function four times, passing the value as a parameter. There should be only
# two statements in the body of this function, not four.
def do_four(f, a):
    do_twice(f, a)
    do_twice(f, a)

print('')
do_four(print, 'spam')

################
# Exercise 3-3 #
################
# Write a function that draws a grid like the following:
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +

def draw_grid(c, r):
    r_bord = '+----' * c + '+'
    r_mid = '|    ' * c + '|'
    for i in range(r):
        print(r_bord)
        print(r_mid)
        print(r_mid)
        print(r_mid)
    print(r_bord)


draw_grid(2, 2)

# Write a function that draws a similar grid of with four rows & four columns
draw_grid(4, 4)
