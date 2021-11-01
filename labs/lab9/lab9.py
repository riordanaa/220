"""
Name: <your name goes here – first and last>
<ProgramName>.py
"""

def addTen(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] + 10

def squareEach(nums):
    for i in range(len(nums)):
        nums[i] = nums[i]**2

def sumList(nums):
    acc = 0
    for i in nums:
        acc = acc + i
    return acc

def returnNumbers(StrNums):
    for i in range(len(StrNums)):
        StrNums[i] = float(StrNums[i])

def writeSumOfSquares():
    infile = input("")
    outfile = input("")
    readfile = open(infile, "r")
    writefile = open(outfile, "w")
    for line in readfile:
        nums = line.split()
        returnNumbers(nums)
        squareEach(nums)
        sq_each = sumList(nums)
        writefile.write("sum of squares =" + str(sq_each))


def starter():
    weight = float(input("what is the weight?"))
    numWins = int(input("what is the number of wins the player has?"))
    if weight >= 150 and weight < 160 and numWins > 4:
        print("This player is a starter")
    elif weight >199 or numWins > 20:
        print("This player is a starter")
    else:
        print("this player is not a starter")

def leapYear(year):
    if year % 4 == 0 and (not year % 100 == 0 or year % 400 == 0):
        return True
    else:
        return False


from graphics import *
import math
def circleoverlap():
    win = GraphWin("Circle", 400, 400)
    p1 = win.getMouse()
    p2 = win.getMouse()
    r = math.sqrt((p1.getX() - p2.getX()) **2 + (p1.getY() - p2.getY())**2)
    c1 = Circle(p1, r)
    c1.draw(win)

    p3 = win.getMouse()
    p4 = win.getMouse()
    r2 = math.sqrt((p3.getX() - p4.getX()) ** 2 + (p3.getY() - p4.getY()) ** 2)
    c2 = Circle(p3, r)
    c2.draw(win)

    if math.sqrt((p1.getX() - p3.getX()) **2 + (p1.getY() - p3.getY())**2) < r + r2:
        print("the circles overlap")


    else:
        print("The circles do not overlap")

    win.getMouse()
    win.close()

    # if the distance betweeen p1 and p3 <= r1 + r2 it overlaps
#circle



#starterif
#elif
#else "is not a starter
#150 <= weight < 160 and wins >=5
#weight >199 or wins > 20

#leapyear
#year%4 == 0
# year% 100 != 0
#or year % 400 == 0





def main():
    # add other function calls here
    circleoverlap()
    #addTen()
    pass


main()
