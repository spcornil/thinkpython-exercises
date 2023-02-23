fruit = 'apple'
index = 0

while index < len(fruit):
    letter=fruit[index]
    print(letter)
    index = index + 1

print('')

for letter in fruit:
    print(fruit)

print('')
    
prefixes = 'JKLMNOPQ'
suffix = 'ack'

for letter in prefixes:
    if letter in ('O', 'Q'):
        print(letter + 'u' + suffix)
    else:
        print(letter + suffix)

print('')

print(fruit[:])

print('')

greeting = 'Hello Zoooooooooorld!'
print(greeting.find('Z'))
new_greeting = greeting[:6] + 'W' + greeting[7:]
print(greeting)
print(new_greeting)

def find(word, letter, index):
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1

print(find(greeting, 'o', 6))

count = 0
def count(l, word):
    count = 0
    for letter in word:
        if letter == l:
            count = count + 1
    print(count)

count('o', greeting)

print('')

print(greeting.count('Z'))

print('')

new_fruit = fruit.upper()
print(new_fruit)

print(new_fruit.lower())

print(fruit.find('l', 0, 5))
print(fruit.find('l', 0, -1))

print('a' in 'banana')
print('e' in 'banana')

print('')
def in_both(word1, word2):
    for letter in word1:
        if letter in word2:
            print(letter)
in_both('apple', 'orange')
