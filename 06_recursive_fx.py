# Exercise 6-2 #
################
# Write a function named ack that evaluates the Ackermann function.
# Use your function to evaluate ack(3, 4), which should be 125.
# What happens for larger values of m and n?

def ack(m, n):
    if m == 0:
        return n +1
    if m > 0 and n == 0:
        return ack(m-1, 1)
    if m > 0 and n > 0:
        return ack(m-1, ack(m, n-1))

print(ack(3, 4))


# Exercise 6-3 #
################
#Write a function called is_palindrome that takes a string argument and returns True
# if it is a palindrome and False otherwise.

#w = 'radar'
w = 'radish'

def is_palindrome(w):
    return w == w[::-1]

is_palindrome(w)
if is_palindrome(w) == True:
    print(f'{w} is a palindrome')
if is_palindrome(w) == False:
    print(f'{w} is not a palindrome')

# Exercise 6-4 #
################
# A number, a, is a power of b if it is divisible by b and a/b is a power of b. Write a function
# called is_power that takes parameters a and b and returns True if a is a power of b.

def is_power(a, b):
    if a == 1:
        return True
    if b == 1:
        return False
    if a % b == 0:
        return is_power(a/b, b)
    else:
        return False

print(is_power(8,2))
print(is_power(10,2))

# Exercise 6-5 #
################
# Write a function called gcd that takes parameters a and b and returns their greatest
# common divisor.

def gcd(a, b):
    while b != 0:
        r = a % b
        return gcd(b, r)
    else:
        return a

print(gcd(2, 7))
    