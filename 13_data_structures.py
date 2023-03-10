#################
# Exercise 13-1 #
#################
# Write a program that reads a file, breaks each line into words, strips whitespace and
# punctuation from the words, and converts them to lowercase.
import string

fin = open('words.txt')

def clean_file(words):
    punc = string.punctuation
    for word in words:
        word.strip().lower()
        for ele in word:
            if ele in punc:
                wor = word.replacea(ele,'')
        #print(word)
    return word
#clean_file(fin)

#################
# Exercise 13-2 #
#################
# Go to Project Gutenberg (http://gutenberg.org) and download your favorite out-ofcopyright
# book in plain text format.
# Modify your program from the previous exercise to read the book you downloaded, skip
# over the header information at the beginning of the file, and process the rest of the words
# as before.

import re

rj = open('romeo_and_juliet.txt')

START = '*** START'
END = '*** END'
    
def process_book(book):
    parsing = False
    #b = []
    for line in book:
        if line.startswith(END):
            parsing = False
        if parsing:
            for word in line.split():
                word = word.strip().lower()
                word = re.sub('[^a-zA-Z]', '', word)    # Lots of weird characters so use regex instead of string punctuation
                print(word)
        if line.startswith(START):
            parsing = True
    #return b

#print(process_book(rj))

# Then modify the program to count the total number of words in the book, and the number
# of times each word is used.

def process_book(book):
    parsing = False
    b = []
    d = dict()
    for line in book:
        if line.startswith(END):
            parsing = False
        if parsing:
            for word in line.split():
                word = word.strip().lower()
                word = re.sub('[^a-zA-Z]', '', word)    # Lots of weird characters so use regex instead of string punctuation
                b.append(word)
                d[word] = 1+d.get(word, 0)
        if line.startswith(START):
            parsing = True
    #print(len(b))
    return d
    
#print(process_book(rj))

#################
# Exercise 13-3 #
#################
# Modify the program from the previous exercise to print the 20 most frequently used words
# in the book.

def most_frequent(book):
    hist = process_book(book)
    desc = []
    for x, freq in hist.items():
        desc.append((freq, x))
    desc.sort(reverse=True)
    return desc[:20]
#print(most_frequent(rj))

#################
# Exercise 13-4 #
#################
# Modify the previous program to read a word list (see ???Reading Word Lists???) and then
# print all the words in the book that are not in the word list.

import re

rj = open('romeo_and_juliet.txt')
fin = open('words.txt')


START = '*** START'
END = '*** END'
    
def process_book(book):
    parsing = False
    b = []
    #d = dict()
    for line in book:
        if line.startswith(END):
            parsing = False
        if parsing:
            for word in line.split():
                word = word.strip().lower()
                word = re.sub('[^a-zA-Z]', '', word)    # Lots of weird characters so use regex instead of string punctuation
                b.append(word)
        if line.startswith(START):
            parsing = True
    return list(set(b))
#print(process_book(rj))

def compare_lists(book, word_list):
    wl = []
    bl = process_book(book)
    book_not_word = []
    for word in word_list:
        word = word.strip().split()
        wl.append(word)
    for bword in bl:
        if bword not in wl:
            book_not_word.append(bword)
    return book_not_word
#print(compare_lists(rj, fin))

#################
# Exercise 13-5 #
#################
# Write a function named choose_from_hist that takes a histogram as defined in
# and returns a random value from the histogram

import random

s = 'parrot'

def histogram(s):
    d = dict()
    for i in s:
        d[i] = 1 + d.get(i, 0)
    return d
#print(histogram(s))

def choose_from_hist(s):
    hist = histogram(s)
    return random.choice(list(hist.values()))

#print(choose_from_hist(s))

#################
# Exercise 13-6 #
#################
# Write a program that uses set subtraction to find words in the book that are not in the word list.

# Note: already completed using sets in 13-4, so we'll just run the function with the new book and same word list
emma = open('emma.txt')
fin = open('words.txt')

#print(compare_lists(emma, fin))

#################
# Exercise 13-7 #
#################
# Write a program that uses this algorithm to choose a random word from the book.
import re
import random

#emma = open('emma.txt')
rj = open('romeo_and_juliet.txt')

START = '*** START'
END = '*** END'
    
def random_word(book):
    parsing = False
    b = []
    for line in book:
        if line.startswith(END):
            parsing = False
        if parsing:
            for word in line.split():
                word = word.strip().lower()
                word = re.sub('[^a-zA-Z]', '', word)    # Lots of weird characters so use regex instead of string punctuation
                b.append(word)
        if line.startswith(START):
            parsing = True
    #return b
    return random.choice(list(set(b)))

print(random_word(rj))