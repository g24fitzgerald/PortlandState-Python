#py Chal 4.4

import random

word_list = ['heyalz', 'boyztoyz', 'cexcells', 'offata', 'bermsie']

word= random.choice(word_list)

guess= 0

while guess <=5:
    letter = input("Guess a letter")
    if letter in word:
        print(letter, "is in word")
        guess +=1
    else:
        print("nope")
        guess += 1

final = input("what's the word?")
if final == word:
    print('yay')

else:
    print('sorry the answer is ', word)

