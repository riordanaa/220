"""
Name: Aidan Riordan
chaos.py

Problem: lab 2
I certify that this assignment is entirely my own work.

"""

# for x in range(0,16,3) Range is (start, end, steps
#print x

# writing a n accumulator
#def sum1to10():
# acc=0
# for x in range (1,11,1)
#   acc=acc+x
# print(acc)

# range(0,a+1,3)
import math




def sum_of_threes():
    acc = 0
    upper_bound=eval(input("What is your upper bound?"))
    for x in range (0,upper_bound+1,3): #why upperbound a+1
        acc=acc+x
    print(acc)


def multiplication_table():
    for h in range (1,11,1):
        for l in range (1,11,1):
            print (h*l, end=" ")
        print()

def triangle_area():
        a=eval(input("what is a"))
        b = eval(input("what is b"))
        c = eval(input("what is c"))
        s= (a+b+c)/2
        area = math.sqrt(s*(s-a)*(s-b)*(s-c))
        print("the area of this triangle is", area)

def sumsquares():
    start = eval(input("what is the starting value for the range of the values of sums of squares"))
    end = eval(input("What is the end value of the range"))
    sum = 0
    for x in range (start, end+1, 1):
        sum=sum+x*x
    print(sum)


def finding_power():
    base = eval(input("what is the base number?"))
    exp = eval(input("what is the exponent?"))
    acc = 1
    for x in range (0,exp,1):
        acc = acc * base
    print (base, "^", exp, "=", acc)



multiplication_table()
finding_power()
sumsquares()
triangle_area()
sum_of_threes()


# ask about range starting / ending
# do : for multiplication table
#multiplication table
# for h in range (1,11)
#   for L in range (1,11)
#       print(h*l, end=" ") end=" " will put a space
#    print()
# pring(1,"ln") will create a new line
