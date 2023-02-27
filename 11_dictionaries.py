#################
# Exercies 11-1 #
#################
# Write a function that reads the words in words.txt and stores them as keys in a dictionary.
fin = open('words.txt')

def word_dict(words):
    d = dict()
    for word in words:
        word = word.strip()
        d[word] = word
    return d

#print(word_dict(fin))
        
#################
# Exercies 11-2 #
#################
# Read the documentation of the dictionary method setdefault and use it to write a more
# concise version of invert_dict.
def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        inverse.setdefault(val, []).append(key)
    return inverse
hist = {'p': 1, 'a': 1, 'r': 2, 'o': 1, 't': 1}
print(invert_dict(hist))

#################
# Exercies 11-4 #
#################
# Use a dictionary to write a faster, simpler version of has_duplicates.
# Or....we'll just use set.
def has_duplicates(t):
    return len(set(t)) < len(t)

t = [1, 3, 2, 4]
t2 = [1, 2, 1, 5]
print(has_duplicates(t))
print(has_duplicates(t2))