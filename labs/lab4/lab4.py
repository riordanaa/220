"""
Name: <Aidan Riordan>
<Lab4>.py
"""
from graphics import *
from math import *

def squares():
    """  <---  You can use tripled quotes to write a multi-line comment....

    Modify the following function to:

    Draw squares (20 X 20) instead of circles. Make sure that the center of the square
    is at the point where the user clicks. Make the window 400 by 400.

    Have each successive click draw an additional square on the screen (rather
    than just moving the existing one).

    Display a message on the window "Click again to quit" after the loop, and
    wait for a final click before closing the window.
    """
    # Creates a graphical window
    width = 400
    height = 400
    win = GraphWin("Lab 4", width, height)
    # number of times user can move circle
    num_clicks = 5
    # create a space to instruct user
    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click to make square")
    instructions.draw(win)
    # builds a square
    shape = Rectangle(Point(50, 50), Point(70, 70))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)
    # allows the user to click multiple times to move the circle
    for i in range(num_clicks):
        clicked = win.getMouse()
        s = Rectangle(Point(clicked.x - 10, clicked.y - 10), Point(clicked.x + 10, clicked.y + 10))
        s.setOutline("red")
        s.setFill("red")
        s.draw(win)
    point_message = Point(width / 2, height - 25)
    message = Text(point_message, "Click again to quit")
    message.draw(win)
    win.getMouse()
    win.close()

def rectangle():
    """
    This program displays information about a rectangle drawn by the user.
    Input: Two mouse clicks for the opposite corners of a rectangle.
    Output: Draw the rectangle.
         Print the perimeter and area of the rectangle.
    Formulas: area = (length)(width)   and    perimeter = 2(length+width)
    """
    win = GraphWin("Lab 4", 400, 400)
    Text(Point(250, 390), "Click the two opposite corners of the rectangle").draw(win)
    p1 = win.getMouse()
    x1 = p1.getX()
    y1 = p1.getY()
    p2 = win.getMouse()
    x2 = p2.getX()
    y2 = p2.getY()
    shape = Rectangle(Point(x1, y1), Point(x2, y2))
    shape.setFill("blue")
    shape.draw(win)
    Text(Point(150, 50), "The area is: " + str((abs(x2 - x1)) / (abs(y2-y1)))).draw(win)
    win.getMouse()
    win.close()

def circle():
    win = GraphWin("Lab 4", 400, 400)
    # instruction
    inst_pt = Point(200, 380)
    Text(inst_pt, "Click once to get center of circle and click again to get the outer point").draw(win)
    p1 = win.getMouse()
    x1 = p1.getX()
    y1 = p1.getY()
    p2 = win.getMouse()
    x2 = p2.getX()
    y2 = p2.getY()
    radius = sqrt((x2 - x1)**2 + (y2 - y1)**2)
    shape = Circle(p1, radius)
    shape.setFill("red")
    shape.draw(win)
    txt = Text(Point(150, 70), "The radius is " + str(radius))
    txt.draw(win)
    win.getMouse()
    win.close()

def pi2():
    n = eval(input("How many terms do you want to use in the approximation?"))
    acc = 0
    for i in range(n):
        numerator = 4
        denominator = 1 + (2*i)
        ratio = (numerator / denominator) * ((-1)**i)
        acc = acc + ratio
    print(acc)

def main():
    # squares()
    #rectangle()
    #circle()
    pi2()


main()