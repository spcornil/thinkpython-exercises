#################
# Exercise 10-1 #
#################
# Write a function called nested_sum that takes a list of lists of integers and adds up the
# elements from all of the nested lists. For example:
def nested_sum(t):
    total = 0
    for x in t:
        total += sum(x)
    return total
#t = [1, 2, 3]
t = [[1, 2], [3], [4, 5, 6]]
print(nested_sum(t))

print('')
#################
# Exercise 10-2 #
#################
# Write a function called cumsum that takes a list of numbers and returns the cumulative sum
def cumsum(t):
    total = 0
    tc = []
    for i in t:
        total += i
        tc.append(total)
    return tc
t = [1, 2, 3]
print(cumsum(t))

print('')
#################
# Exercise 10-3 #
#################
# Write a function called middle that takes a list and returns a new list that contains all but
# the first and last elements.
def middle(t):
    return t[1:-1]

t = [1, 2, 3, 4]
print(middle(t))

print('')
#################
# Exercise 10-4 #
#################
# Write a function called chop that takes a list, modifies it by removing the first and last
# elements, and returns None.
def chop(t):
    del t[0]
    del t[-1]

t = [1, 2, 3, 4]
print(chop(t))

print('')
#################
# Exercise 10-5 #
#################
# Write a function called is_sorted that takes a list as a parameter and returns True if the
# list is sorted in ascending order and False otherwise.
def is_sorted(t):
    return t == sorted(t)

print(is_sorted([1, 2, 2]))
print(is_sorted(['b', 'a']))

print('')
#################
# Exercise 10-6 #
#################
# Write a function called is_anagram that takes two strings and returns True if they are anagrams.
def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)

print(is_anagram('shaw', 'wash'))
print(is_anagram('split', 'wood'))

print('')
#################
# Exercise 10-7 #
#################
# Write a function called has_duplicates that takes a list and returns True if there is any
# element that appears more than once.
def has_duplicates(t):
    ts = sorted(t)
    for i in range(len(ts)-1):
        if ts[i] == ts[i+1]:
            return True
        else:
            return False
t = [1, 3, 1, 4]
print(has_duplicates(t))
t = [1, 3, 5, 4]
print(has_duplicates(t))

print('')
#################
# Exercise 10-8 #
#################
# Write a function to estimate birthday paradox probability with 23 people in the room.
import math

def paradox(k):
    Vnr = math.factorial(365) / math.factorial(365-k)
    Vt = 365**23
    PA = Vnr / Vt
    PB = 1 - PA
    return 'There is a ' + str(round(PB*100, 2)) + f'% probability that two people in a room of {k} have the same birthday.'

print(paradox(23))

print('')
#################
# Exercise 10-9 #
#################
# Write a function that reads the file words.txt and builds a list with one element per word.
# Write two versions of this function, one using the append method and the other using the
# idiom t = t + [x].
fin = open('words.txt')

def one_per(words):
    one_list = []
    for word in words:
        word = word.strip()
        one_list.append(word)
    return one_list

#print(one_per(fin))

def one_per_dos(words):
    one_list = []
    for word in words:
        word = word.strip()
        one_list = one_list + [word]
    return one_list
#print(one_per(fin))


