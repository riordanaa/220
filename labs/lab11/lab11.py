"""
Name: <Aidan Riordan>
<hangman>.py
"""
import random
from random import randint

def words(ifn):
    infile = open(ifn, "r")
    contents = infile.read()
    return contents.split("\n")

def random_word(words):
    return words[randint(0, len(words)-1)]

def fill(word, letters):
    leng = len(word)
    secret = ["_"] * leng
    #secret = ["_"].len(word)
    for letter in letters:
        for i in range(len(word)):
            if letter == word[i]:
                secret[i] = letter
    return "".join(secret)

def won(secret, letters):
    #fill(word, letters)
    i = 0
    if len(secret) == len(letters):
        for _ in secret:
            if secret[i] != letters[i]:
                return False
            elif len(secret)-1 == i:
                return True
            i = i + 1
    else:
        return False

def play():
    w = words("words.txt")
    secret = random_word(w)
    incorrect = 0
    guesses = []

    while incorrect < 7 and won(secret, guesses) == False:
        display = fill(secret, guesses)
        print(display)
        print(guesses)
        letter = input("what letter do you guess?")
        while letter in guesses:
            letter = input("Already Guessed. what letter do you guess?")
        guesses.append(letter)
        if not(letter in secret):
            incorrect = incorrect + 1


def main():

    play()
    # add other function calls here
    pass



#





#def play():
# w = words("wordst.txt")
#secret = randomword(w)
# incorrect = 0
# guesses = []
#current= "".len(secret)
#while _and__
#keep running if =7 and
#for l in guesses
#   print (L, end = "")
#letter = input()
#while _ in _ :
#letter = input
#guesses.append(letter)
#display = fill(secret, guesses)
#if :
# incorect = incorect + 1
# else: current = display

# we want to see if the letter we checked has no been geussed
# befor. when letter is letter allready geussed ask for
# another letter.





main()
