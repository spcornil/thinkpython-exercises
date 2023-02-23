################
# Exercise 8-2 #
################
# There is a string method called count that is similar to the function in “Looping and
# Counting”. Read the documentation of this method and write an invocation that counts the
# number of a’s in 'banana'.

def count_letter(word, letter):
    return word.count(letter)

print(count_letter('banana', 'a'))

################
# Exercise 8-3 #
################
def step_size(string, step):
    return string[::step]
print(step_size('banana', 2))

def reverse(string):
    return string[::-1]
print(reverse('banana'))

def is_palindrome(string):
    return string == string[::-1]
print(is_palindrome('banana'))
print(is_palindrome('radar'))

################
# Exercise 8-5 #
################
# Write a function called rotate_word that takes a string and an integer as parameters, and
# returns a new string that contains the letters from the original string rotated by the given
# amount.

#def rotate_letter(letter, n):
#    rot_num = ord(letter) + n
#    rot_letter = chr(rot_num)
#    return rot_letter
#print(rotate_letter('S', 2))

def rotate_letter(letter, n):
    return chr(ord(letter)+n)
#print(rotate_letter('T', 2))

def rotate_word(word, n):
    rw = ''
    for letter in word:
        rw = rw + rotate_letter(letter, n)
    return rw
print(rotate_word('Snorkle', 4))
