"""
Name: <your name goes here – first and last>
<ProgramName>.py
"""
from random import randint
import algorithms

def find_and_remove_first(list,value):
    try:
        i = list.index(value)
        list[i] = "Aidan"
    except:
        pass
# in test file have numbers in ascending order

def read_data(filename):
    f = open(filename, "r")
    data = f.read()
    data = data.split()
    return data


def is_in_linear(search_val, values):
    i = 0
    while i < len(values):
        if values[i] == search_val:
            return True
        i = i + 1

    return False


def good_input():
    inp = eval(input("what is your number?"))
    while not(inp >=1 and inp <=10):
        inp = eval(input("Please enter a new number that is in the range 1 - 10"))

def num_digits():



    num = eval(input("please enter a positive integer"))
    while num>0:
        digits = 0
        while num//10 >0:
            num = num // 10
            digits = digits + 1
        print("This number has " + digits + " digits")
        num = eval(input("enter a new positive integer to continue"))

def hi_lo_game():
    secret = randint(1,100)
    guesses = 1
    num = eval(input("what number do you guess?"))
    while num != secret and guesses < 7:
        guesses += 1
        if secret>num:
            print("to high")
        else:
            print("to low")
    if secret == num:
        print("You won! the correct number was " + str(secret) + " it took you" + str(guesses) + " guesses.")
    else :
        print("You ran out of guesses the number was" + str(secret))

def main():

    # add other function calls here

    pass





#def good_input():
#x = eval(input())
#while oposite of x>=1 and x<=10:
#x=eval(input()

#return x


#55//10 = 5
#5//10 = 0





if __name__ == '__main__':
    main()
