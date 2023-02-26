cheeses = ['Cheddar', 'Edam', 'Gouda']
numbers = [42, 123]

# Lists are Mutable #
#####################
numbers[1] = 5

print(numbers)

# Traversing a List #
#####################
for cheese in cheeses:
    print(cheese)

for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2
print(numbers)

# List Operations #
###################
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)

print([0]*4)
print(a*3)

# List Slices #
###############
t = ['a', 'b', 'c', 'd', 'e', 'f']
print(t[1:3])
print(t[:4])
print(t[3:])
print(t[:])
print(t[::-1])

t[1:3] = ['x', 'y']
print(t)

print('')
# List Methods #
################
# Append: adds a new element to end of list
t = ['a', 'b', 'c']
t.append('d')
print(t)

# Extend: takes another list as an arg and appends all elements
t1 = ['a', 'b', 'c']
t2 = ['d', 'e']
t1.extend(t2)
print(t1)

# Sort: arranges elements of list from low to high
t = ['d', 'c', 'e', 'b', 'a']
t.sort()
print(t)
print('')
# Map, Filter, & Reduce #
#########################

# REDUCE function: reduces list into single varaiable
# Let's add all items in a list
def add_all(t):
    total = 0
    for x in t:
        total += x
    return total

t = [1, 2, 3]
print(add_all(t))

# Or we could just use sum fx
print(sum(t))

# MAP function: 'maps' a fx (capitalize) onto each element
# Capitalize all strings s in list
def capitalize_all(t):
    res = []
    for s in t:
        res.append(s.capitalize())
    return res

t = ['cheddar', 'Edam', 'gouda']
print(t)
print(capitalize_all(t))

# FILTER function: filter items in a list based on condition
# Return only strings s that are entirely uppercase
t = ['Cheddar','EDAM', 'gouda']
def only_upper(t):
    res = []
    for s in t:
        if s.isupper():
            res.append(s)
    return res
print(only_upper(t))
print('')
###########################################################################################
# Most common list operations can be expressed as a combination of map, filter and reduce #
###########################################################################################

# Deleting Elements #
#####################

# Pop: 'pops' an item out of the list based on index:
# If no index specified it pops the last element in the list
t = ['a', 'b', 'c']
x = t.pop(1)
print(t)
print(x)

# Del: if we don't need the removed/popped value, use delete operator:
t = ['a', 'b', 'c']
del t[1]
print(t)

t = ['a', 'b', 'c', 'd', 'e', 'f']
del t[1:5]
print(t)

# If you know the element you want to remove (but not index), use remove:
t = ['a', 'b', 'c']
t.remove('b')
print(t)

print('')

# Lists and Strings #
#####################
s = 'spam'
t = list(s)
print(t)

# Split a string into a list
s = 'pining for the fjords'
t = s.split()
print(t)

s = 'brap-brap-brap'
delimiter = '-'
t = s.split(delimiter)
print(t)

# Join a list into a string (opposite of split)
s = ['pining', 'for', 'the', 'fjords']
#delimiter = ' '
t = ' '.join(s)
print(t)

# Objects & Values #
####################

a = 'banana'
b = 'banana'
# Calling 'a is b' will return True.

c = [1, 2, 3]
d = [1, 2, 3]
# Calling 'c is d' will return False.

# This is b/c the two lists are equivalent, and have the same elements,
# but not identical b/c they are not the same object.
# Identical objects are also equivalent, but equivalent objects are not necessarily identical.

# Aliasing #
############

a = [1, 2, 3]
b = a
# 'b is a' will return True.
# b is referencing and a and is not necessarily its own object

b[0] = 42
print(a)
# This changes the value of a[0] as well.
# Which can be confusing & error-prone - so best to avoid aliasing list objects.
print('')

# List Arguments #
##################
# Important to distinguish b/w functions that modify lists vs leave untouched
def delete_head(t):
    del t[0]

letters = ['a', 'b', 'c']
delete_head(letters)
print(letters)

def trail(t):
    return t[1:]
letters = ['a', 'b', 'c']
rest = trail(letters)
print(letters)
print(rest)