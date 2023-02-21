import math

# Incremental Development: Hypotenuse #
#######################################
def hypotenuse(a, b):
    a2 = a**2
    b2 = b**2
    a2b2 = a2 + b2
    c = math.sqrt(a2b2)
    #print(c)
    return(c)

# Streamlined code
def hypotenuse(a, b):
    return math.sqrt(a**2 + b**2)

#hypotenuse(3, 4)

# Incremental development: Cirle radius & area #
################################################
def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    dsquared = dx**2 + dy**2
    result = math.sqrt(dsquared)
    return result

def area(radius):
    a = math.pi * radius**2
    return a

def circle_area(xc, yc, xp, yp):
    radius = distance(xc, yc, xp, yp)
    result = area(radius)
    return result

# Final streamlined product
def circle_area(xc, yc, xp, yp):
    return area(distance(xc, yc, xp, yp))

# Booleans #
############
def is_divisible(x, y):
    if x % y == 0:
        return True
    else:
        return False

#is_divisible(6,4)

def is_divisible(x, y):
    return x % y == 0

if is_divisible(4, 2) == True:
    print('x is divisible by y')

# Booleans Exercise #
#####################
#As an exercise, write a function is_between(x, y, z) that returns True if
# x <= y <= z or False otherwise.

def is_between(x, y, z):
    return x <= y <= z

if is_between(2, 8, 6) == True:
    print('True')
else:
    print('False')

# Recursion #
#############

def factorial(n):
    if n == 0:
        return 1
    else:
        recurse = factorial(n-1)
        result = n * recurse
        return result

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

factorial(6)