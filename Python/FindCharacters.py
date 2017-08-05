# Write a program that takes a list of strings and a string containing a single
# character, and prints a new list of all the strings containing that character.

word_list = ['hello','world','my','name','is','Anna']

char = set('o')
n = []

for word in word_list:
    if char & set(word):
        n.append(word)

print n
