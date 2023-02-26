################
# Exercise 9-1 #
################
# Write a program that reads words.txt and prints only the words with more than 20
# characters (not counting whitespace).
fin = open('words.txt')

def words_twenty(words):
    for word in words:
        word = word.strip()
        if len(word) > 20:
            print(word)
words_twenty(fin)

################
# Exercise 9-2 #
################
# Write a function called has_no_e that returns True if the given word doesn’t have the
# letter “e” in it.
def has_no_e(word):
    if 'e' in word:
        print('False')
    else:
        print('True')
has_no_e('Gollum')

# Modify your program from the previous section to print only the words that have no “e”
# and compute the percentage of the words in the list that have no “e”.
fin = open('words.txt')
def no_e_list(words):
    count_e = 0
    count_no_e = 0
    for word in words:
        word = word.strip()
        if 'e' in word:
            count_e += 1
        if 'e' not in word:
            count_no_e += 1
    #print(count_e)
    #print(count_no_e)
    return str(round(count_no_e / (count_e + count_no_e) * 100, 2)) + '%'
print(no_e_list(fin))

################
# Exercise 9-3 #
################
# Write a function named avoids that takes a word and a string of forbidden letters, and that
# returns True if the word doesn’t use any of the forbidden letters.

#word = input('What is the word you would like to check?\n')
#forb = input('What is the forbidden string?\n')

def avoids(word, forb):
    if forb in word:
        print('False')
    else:
        print('True')
#avoids(word, forb)

# Modify your program to prompt the user to enter a string of forbidden letters and then
# print the number of words that don’t contain any of them.

fin = open('words.txt')
#forb = input('What is the forbidden string?\n')

def avoids(forb):
    for word in fin:
        if forb not in word:
           print(word)
#avoids(forb)

################
# Exercise 9-4 #
################
# Write a function named uses_only that takes a word and a string of letters, and that
# returns True if the word contains only letters in the list.
fin = open('words.txt')
forb = 'acefhlo'

def uses_only(forb):
    for line in fin:
        word = line.strip()
        if all(x in forb for x in word):
            print(word)
#uses_only(forb)

################
# Exercise 9-5 #
################
# Write a function named uses_all that takes a word and a string of required letters, and
# that returns True if the word uses all the required letters at least once.
fin = open('words.txt')

def uses_all(forb):
    count = 0
    for line in fin:
        word = line.strip()
        if all(x in word for x in forb): ### <-- Swap forb/word from previous statement.
            count += 1
    return count
print(uses_all('aeiou'))
print(uses_all('aeiouy'))

################
# Exercise 9-6 #
################
# Write a function called is_abecedarian that returns True if the letters in a word appear in
# alphabetical order (double letters are okay).
fin = open('words.txt')

def is_abecedarian(fin):
    count = 0
    for line in fin:
        word = line.strip()
        word_sorted = ''.join(sorted(word))
        if word == word_sorted:
            print(word)
is_abecedarian(fin)