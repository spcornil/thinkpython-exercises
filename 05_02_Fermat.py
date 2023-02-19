# Fermat’s Last Theorem says that there are no positive integers a, b, and c such that
# for any values of n greater than 2.

# 1 #
# Write a function that checks to see if fermet's theorem holds.

import math

def check_fermat(a, b, n):
    c_2 = a**2 + b**2
    c = math.sqrt(c_2)
    test_ab = a**n + b**n
    test_c = c**n
    if a <= 0 or b <= 0 or n < 2:
        print('a and b should be positive')
    elif n == 2:
        print('Well of course it worked Pythagoras')
    elif test_ab == test_c and n > 2:
        print('Holy smokes, Fermat was wrong!')
    elif test_ab != test_c and n > 2:
        print('Looks like Fermat was correct.')

#check_fermat(2, 3, 4)

# 2 #
# Modify the function to take user input

a = int(input('What is the value of a?\n'))
b = int(input('What is the value of b?\n'))
n = int(input('What is the value of n?\n'))

def check_fermat_user(a, b, n):
    c_2 = a**2 + b**2
    c = math.sqrt(c_2)
    test_ab = a**n + b**n
    test_c = c**n
    if a <= 0 or b <= 0 or n < 2:
        print('a and b should be positive')
    elif n == 2:
        print('Well of course it worked Pythagoras')
    elif test_ab == test_c and n > 2:
        print('Holy smokes, Fermat was wrong!')
    elif test_ab != test_c and n > 2:
        print('Looks like Fermat was correct.')

check_fermat_user(a, b, n)