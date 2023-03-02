# Tuples are Immutable #
########################
# Tuple is sequence of values, can be any type.
# Indexed with values, so a lot like lists.
# Difference is tuples are immutable.

t = ('a', 'b', 'c', 'd', 'e')
print(t)

# To create tuple with single element, need to include final comma.
# Otherwise type will just be a string.
t1 = 'a',
print(type(t1))

# Can also use built in tuple function to build a tuple.
t = tuple()
print(t)

# Most list operators also work with tuples
t = tuple('pacific')
print(t)
print(t[0])
print(t[1:3])
print(t[::-1])

# Difference lies in tuples being immutable.
# Have to create new tuple to incorporate any changes.
t = ('P',) + t[1:] + ('o',)
print(t)

# Tuple Assignment #
####################
addr = 'monty@python.org'
uname, domain = addr.split('@')
print(uname, domain)

# Tuples as Return Values #
###########################
# divmod takes two arguments and returns a tuple of two values: the quotient and remainder.
t = divmod(7, 3)
print(t)

quot, rem = divmod(7, 3)
print(quot)
print(rem)

def min_max(t):
    return min(t), max(t)
print(min_max(t))

# Variable-Length Arg Types #
#############################
# Gathers all args into a tuple
def returnall(*args):
    return(args)
print(returnall(1, 2.0, 3))

# Opposite is to Scatter args
t = (7, 3)
# divmod(t) # <-- Will return error (expects 2 args)
print(divmod(*t)) # <-- Now we can pull in all args

# Many built-in fx take multiple args
print(max(1, 2, 5))

# 'Sum' do not. Ha. Ha.
#print(sum(1, 2, 5))

# As an exercise, write a function called sumall that takes any number of arguments and
# returns their sum.
def sumargs(*args):
    total = 0
    for i in args:
        total +=i
    return total
print(sumargs(1, 2, 5))

# Lists & Tuples #
##################
# Zip is built-in fx that takes 2+ sequences and returns list of tuples.
s = 'abc'
t = [0, 1, 2]

def print_zipped(s, t):
    for pair in zip(s, t):
        print(pair)

print_zipped(s, t)

# Zip is an iterator, but can't use an index to select from an iterator.
# Need to turn into a list, etc.
zl = list(zip(s, t))
print(zl)

# If sequences are not the same length, result has length of the shorter seq.
ae = list(zip('Anne', 'Elk'))
print(ae)

def loop_zl(zl):
    for letter, number in zl:
        print(number, letter)
loop_zl(zl)

# Enumerate: traverses elements of sequence & indices.
x = enumerate('abc')
print(list(x))

for index, element in enumerate('abc'):
    print(index, element)

# Dictionaries & Tuples #
#########################
# items: returns sequence of tuples as key-value pairs.
d = {'a':0, 'b':1, 'c':2}
t = d.items()
print(t)

for key, value in d.items():
    print(key, value)

# Combining dict w/ zip is a useful way to create a dictionary:
d = dict(zip('abc', range(3)))
print(d)

