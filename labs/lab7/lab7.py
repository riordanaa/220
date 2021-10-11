"""
Aidan Riordan
Name: <your name goes here – first and last>
Partner: <your partner's name goes here – first and last>
<lab7>.py
"""



def cash_conversion():
    inte = eval(input("what is your integer?"))
    print('${:.2f}'.format(inte))


def encode():
    message = input("what is your message")
    key = eval(input("what is your key value"))
    for c in message:
        i = ord(c)
        z= i+key
        print(chr(z), end="")
def main():
    n = eval(input("what is your n"))
    print("the sum of n natural numbers in sequence is", sum_n(n))
    print("the sum of the cubes of n natural numbers in sequence is", sum_n_cubes(n))

    radius = eval(input("what is the radius?"))
    print("the surface area is", sphere_area(radius))
    print("the volume is", sphere_volume(radius))
def sphere_area(radius):
    area = 4*3.14*(radius)**2
    return area
def sphere_volume(radius):
    volume = (4/3)*3.14*(radius)**3
    return volume

def sum_n(n):
    total = 0
    for i in range(n+1):
        total = total + i

    return total
def sum_n_cubes(n):
    total = 0
    for i in range(n + 1):
        total = total + i**3

    return total

def encode_better():
    m = input("what is your message")
    shifter = input("what is your shifter")
    acc = ""
    for i in range(len(m)):
        c =ord(m[i])
        key = ord(shifter[i])
        z = c + key - 97
        acc = acc + chr(z)
    print(acc)
encode_better()
main()
encode()
cash_conversion()

# format strings
#{} this means something will go here
#{:.x.y} x = left of deciman  y is right of decimal
#print(f"{are} {two}"}
#i = eval(input
#print( format string for)
#  "${}".format(i)

#cipher rotates letters 3 characters right abc = def
# a = 97 b = 98 c = 99
# x = input
# k = eval(input())
#acc = ""
# for c in x:
    #i = ord(c)  gives number value for character
    #z= i+k
    # new(new = chr())

#defsphere_area(radius):
    #return area
#def sphere_volume:
    #return volume
# def main:
    # print(sphere_area(2))
    # print(sphere_volume(5)
    # print(sphere(10)
    #print(sum_n(10)
#def sum_n(n):
    #return total
#def sum cubes(n):
    #return total

#open
# for line in file will be every line in the file one at a time

# ord(r) + c - 97

#m = input()
#n = input()
#acc = ""
#for i in range(len(m))
#   c =ord(m[i])
#   key = ord(k[i])
#   add c + key - 97
#   acc = acc + chr


