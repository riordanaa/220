"""
Name: <your name goes here – first and last>
<ProgramName>.py
"""

from graphics import *


def target():
    win_width = 500
    win_height = 500
    win = GraphWin("Archery Target", win_width, win_height)

    # Add code here to get the dimensions and draw the target

    # Wait for another click to exit
    win.getMouse()
    win.close()


def triangle():
    win_width = 500
    win_height = 500
    win = GraphWin("Draw a Triangle", win_width, win_height)

    # Add code here to accept the mouse clicks, draw the triangle.
    p1 = win.getMouse()
    p2 = win.getMouse()
    p3 = win.getMouse()
    Line(p1, p2).draw(win)
    Line(p2, p3).draw(win)
    Line(p3, p1).draw(win)
    # and display its area in the graphics window.
    l1=((p1.getX()-p2.getX())**2+(p1.getX()-p2.getY())**2)**.5
    l2=((p2.getX()-p3.getX())**2+(p2.getX()-p3.getY())**2)**.5
    l3=((p3.getX()-p1.getX())**2+(p3.getX()-p1.getY())**2)**.5
    s = (l1+l2+l3)/2
    perimeter=l1+l2+l3
    area = (s*(s-l1)*(s-l2)*(s-l3))**.5
    print(area)

    inst = Text(Point(250,20),"your area is" + str(area))
    inst.draw(win)
    per = Text(Point(250, 100), "your perimeter is" + str(perimeter))
    per.draw(win)

    # Wait for another click to exit
    win.getMouse()
    win.close()


def color_shape():
    '''Create code to allow a user to color a shape by entering rgb amounts'''

    # create window
    win_width = 400
    win_height = 400
    win = GraphWin("Color Shape", win_width, win_height)
    win.setBackground("white")

    # create text instructions
    msg = "Enter color values between 0 - 255\nClick window to color shape"
    inst = Text(Point(win_width / 2, win_height - 20), msg)
    inst.draw(win)

    # create circle in window's center
    shape = Circle(Point(win_width / 2, win_height / 2 - 30), 50)
    shape.draw(win)

    # redTexPt is 50 pixels to the left and forty pixels down from center
    red_text_pt = Point(win_width / 2 - 50, win_height / 2 + 40)
    red_text = Text(red_text_pt, "Red: ")
    red_text.setTextColor("red")

    # green_text_pt is 30 pixels down from red
    green_text_pt = red_text_pt.clone()
    green_text_pt.move(0, 30)
    green_text = Text(green_text_pt, "Green: ")
    green_text.setTextColor("green")

    # blue_text_pt is 60 pixels down from red
    blue_text_pt = red_text_pt.clone()
    blue_text_pt.move(0, 60)
    blue_text = Text(blue_text_pt, "Blue: ")
    blue_text.setTextColor("blue")

    # display rgb text
    red_text.draw(win)
    green_text.draw(win)
    blue_text.draw(win)

# start here
    # get entry boxes
    blue_box=Entry(Point(200,50),3)
    green_box=Entry(Point(200,100),3)
    red_box=Entry(Point(200,150),3)
    blue_box.draw(win)
    red_box.draw(win)
    green_box.draw(win)

    win.getMouse()
    for i in range (5):
        red = int(red_box.getText())
        blue = int(blue_box.getText())
        green = int(green_box.getText())
        color = color_rgb(red,green,blue)
        shape.setFill(color)
        win.getMouse()


    # Wait for another click to exit
    win.getMouse()
    win.close()

def process_string():
    s=input("what is your string?")
    print(s[0])
    print(s[-1])
    print(s[2:6]) # what do you mean by positions
    print(s[0]+s[-1])
    for i in range (10):
        print(s[0:3])
    for c in s:
        print(c)
    print(len(s))

def process_list():
    pt = Point(5, 10)
    values = [5, 'hi', 2.5, 'there', pt, '7.2']

    x=values[1]+values[3]
    print(x)
    x=values[0]+values[2]
    print(x)
    x=values[1]*5
    print(x)
    x= [values[2],values[3],values[-2]]
    print(x)
    x= [values[2],values[3],values[0]]
    print(x)
    x=[values[2],values[0],values[-1]]
    print(x)
    x=values[0]+values[2]+float(values[-1])
    print(x)
    x=len(values)
    print(x)

def another_series():
    n = eval(input("how many terms?"))
    sum=0
    for i in range(n):
        z=2+(2*(i%3))
        print(z, end= " ")
        sum=sum+z
    print(sum)
    #s = 0
    # %3 to get 0 1 2 0 1 2 then make y = 2 + (2 * i%3)
    # print(y, end="")


def main():
    # target()
    # triangle()
    # color_shape()
    pass

another_series()
process_list()
process_string()
color_shape()
triangle()

# notes
#p1 = win.getmouse()
#p2 = and p3 =
#line(point,point) dothis from atob b to c c to a
# 3 distance formulas l1=distance a-b  l2 = distance b-c l3 = a-c (l1 is a b and c on the doc)
#text(point, "the perimiter is",+str (parameter)
#
# for circles
# instead of #display rgb text,
#win.getmouse
#for i in range(5)
# color_text = color_text.gettext()
# color_text = int(color_text)
#color = color_rgb(r,g,b)
#shape.setFill(color)
#win.getmouse

#indicies
# x = values[1] + values[3]
# x = [values[2], values[4], values[5]]
# float(values[-1]) because it is originally a string

# not another series
# n= eval(input())
# s = 0
# %3 to get 0 1 2 0 1 2 then make y = 2 + (2 * i%3)
# print(y, end="")

# for target
# edges of circle are edges of window

#for  color shape
#
main()
