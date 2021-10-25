"""
Name: <your name goes here – first and last>
<ProgramName>.py

Aidan Riordan
Lab 8
"""

from encode import encode

def count_voids(in_name, out_name):
    infile = open(in_name, "r")
    outfile = open(out_name, "w+")
    i = 1
    for line in infile:
        words = line.split()
        for word in words:
            outfile.write(str(i) + " " + word + " ")
            i = i + 1




#def count_voids()

def hourly_wages(ifn, ofn):
    infile = open(ifn,"r")
    outfile = open(ofn,"w+")
    for line in infile:
        pats = line.split()
        wage = pats[2]
        wage = float(float(wage) + 1.65)
        wage = wage * int(pats[3])
        outfile.write(pats[0] + " " + pats[1] + " " + str(wage) + "\n")

def calc_check_sum(isbn):
    acc = 0
    for i in range(10):
        pos = 10-i
        acc = acc + int(isbn[i]) * pos
    print(acc)
    return acc

def send_message(file, friend):
    friend = friend + ".txt"
    infile = open(file, "r")
    outfile = open(friend, "w+")
    for line in infile:
        outfile.write(line)

def send_safe_message(file, friend, key):
    friend = friend + ".txt"
    infile = open(file, "r")
    outfile = open(friend, "w+")
    encoded = encode(infile.read(),key)
    outfile.write(encoded)



def encode_better(message, pad):
    m = ""
    shifter = str(pad)
    acc = ""
    for i in range(len(m)):
        c =ord(m[i])
        key = ord(shifter[i])
        z = c + key - 97
        acc = acc + chr(z)

    m = m + acc
    return m
def send_uncrackable_message(file, friend, pad):
    padfile = open(pad, "r")
    key = padfile.read()
    friend = friend + ".txt"
    infile = open(file, "r")
    outfile = open(friend, "w+")
    encoded = encode_better(infile.read(),key)
    outfile.write(encoded)

def main():
    # add other function calls here
    send_uncrackable_message("message.txt", "jamal", "pad.txt")

    send_safe_message("message.txt", "bobs", 5)
    send_message("message.txt", "Hunter")
    calc_check_sum("0072946520")
    hourly_wages("hourly_wages.txt", "new_wages.txt")
    count_voids("Walrus.txt", "wout.txt")
    pass


main()



# next three are very similar with one change
# def sm(fn, friend):
#infile = open(fn, "r")
#outfile = open(friend + "txt", "wt")
#copy infile into outfile
# for line in inflile:
# outfile.write(line)
# files should look the same

# next
# from encripton import

# def ssm(fm, friend, key):
#
#call it by
#ssm("secret.txt, "bob", s)
#write encode(line, trex)

#def ssu(fn,friend,pad)
#dont use a onetime pad. he gives one abc on a file
# padfile = open(pad, "r")
#key = padfile.read()
#ssm("secret.txt", "bob", s)
#ssu("secret.txt", "jim", "pad.txt")
#one thing you change is

