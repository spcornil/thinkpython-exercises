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
