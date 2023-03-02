#################
# Exercise 12-1 #
#################
# Write a function called most_frequent that takes a string and prints the letters in
# decreasing order of frequency.
s = 'brontosarrrus'
def histogram(s):
    d = dict()
    for i in s:
        d[i] = 1 + d.get(i, 0)
    return d
#print(hist(s))

def most_frequent(s):
    hist = histogram(s)
    desc = []
    for x, freq in hist.items():
        desc.append((freq, x))
    desc.sort(reverse=True)
    return desc
print(most_frequent(s))

#################
# Exercise 12-2 #
#################
# Write a program that reads a word list from a file and prints all the sets of words that are anagrams.

fin = open('words.txt')

def signature(s):
    t = list(s)
    t.sort()
    t = ''.join(t)
    return t

def all_anagrams(filename):
    d = {}
    for line in open(filename):
        word = line.strip().lower()
        t = signature(word)

        if t not in d:
            d[t] = [word]
        else:
            d[t].append(word)
    return d

print(all_anagrams('words.txt'))

    


    

        