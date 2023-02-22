################
# Exercise 7-1 #
################
import math

epsilon = 0.00000000001

def mysqrt(a):
    x = a/2
    true_a = math.sqrt(a)
    while True:
        print(round(x, 3),' ', true_a, round(abs(x-true_a), 3))
        y = (x + a/x) / 2
        if abs(y-x) < epsilon:
            return y
            break
        x = y

print(mysqrt(9))

################
# Exercise 7-2 #
################
# Write a function called eval_loop that iteratively prompts the user, takes the resulting
# input and evaluates it using eval, and prints the result.
# It should continue until the user enters 'done', and then return the value of the last
# expression it evaluated.

def eval_loop():
    while True:
        user_input = input('>')
        if user_input == 'done':
            break
        print(eval(user_input))
    return eval(user_input)

eval_loop()