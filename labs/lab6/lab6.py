"""
Name: <your name goes here – first and last>
<ProgramName>.py
Aidan Riordan lab 6
"""


def name_reverse():
    """
    Read a name in first-last order and display it in last-comma-first order.
    """
    name= input('enter the name of student')
    list=name.split()
    print(list[1] + ', ' + list[0])

def company_name():
    name= input('enter the three part domain name')
    list = name.split('.')
    print(list[1])

def main():
    name_reverse()
    # add other function calls here

def initials():
    num_names = int(input('how many names are there'))
    for i in range (num_names):
        first = input('enter the first name of student #' + str(i+1))
        last = input('enter ' + first + "'s last name")


        print(first + "'s initials are " + first[0] + last[0])
def names():
    names = input("enter a list of peoples names seperated by commas")
    names = names.split(', ')
    for name in names:
        new_names= name.split(' ')
        print(new_names[0][0] + new_names[1][0])

def thirds():
    num_sen= input('how many sentences will you input')
    for i in range (int(num_sen)):
        sentence= input('what is your sentence?')
        print(sentence[2::3])

def word_average():
    acc = 0
    sen = input('what is your sentence?')
    sentence = sen.split()
    for word in sentence:
        acc = acc + len(word)
    average = acc / len(sentence)
    print('the average word is ' + str(average))

def pig_lattin():
    sen = input('what is your sentence')
    sen = sen.split()
    for word in sen:
        new_word= word[1::] + word[0] + str('ay')
        print(new_word)



initials()
names()
# in for loop
# first = input("enter" + str(i+1))
# last = input()

# dice 2
# names = input
# names = names.split(",")
#for name in names (initials)

# [start:stop:step] non inclusive to stop

# every third
# n = num sentences
#for i in range(n):
# semse = input()
#print(sentence[0::3]
# do one at a time fo

# word average
# dont do a loop just do the first part
# sentence = input()
# sentence = sentence.split("")
# for word in sentence:
#acc = acc + len(word)

# pig lattin
#sentence = input()
#sentence = sentence.split()
#x = [1:]
#x = x + l[0] + 'ay'
pig_lattin()
word_average()
thirds()
names()
initials()
company_name()
