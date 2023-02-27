# List: indices have to be integers
# Dictionary: indices can be almost any type
eng2sp = dict()
print(eng2sp)

# Key = 'one'
# Value = 'uno'
eng2sp['one'] = 'uno'
print(eng2sp)

eng2sp = {'one': 'uno', 'two': 'dos', 'three': 'tres'}
print(eng2sp)
print(eng2sp['two'])
print(len(eng2sp))

# Key returns true, value will return false.
print('one' in eng2sp)
print('uno' in eng2sp)

# Use below to pull values
vals = eng2sp.values()
print('uno' in vals)

#
def histogram(s):
    d = dict()
    for i in s:
        d[i] = 1 + d.get(i, 0)
    return d

print(histogram('brontosarus'))

# Looping & Dictionaries #
##########################
def print_hist(h):
    for c in h:
        print(c, h[c])
print_hist(histogram('parrot'))

# Reverse Lookup #
##################
h = histogram('parrot')

def reverse_lookup(d, val):
    for key in d:
        if d[key] == val:
            return key
    raise LookupError()

print(reverse_lookup(h, 2))

# Dictionaries & Lists #
########################
def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse

hist = histogram('parrot')
print(hist)
inverse = invert_dict(hist)
print(inverse)


