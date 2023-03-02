import re

rj = open('romeo_and_juliet.txt')

START = '*** START'
END = '*** END'
    
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

def most_frequent(book):
    hist = process_book(book)
    desc = []
    for x, freq in hist.items():
        desc.append((freq, x))
    desc.sort(reverse=True)
    return desc[:20]
print(most_frequent(rj))
