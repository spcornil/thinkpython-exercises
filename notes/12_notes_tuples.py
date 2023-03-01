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