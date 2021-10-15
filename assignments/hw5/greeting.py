"""
Name: <Aidan Riordan>
program name: <greeting.py>
problem: greeting card
I Aidan Riordan certify that this is my own work
"""
from graphics import *


def main():
    # setup
    win = GraphWin("greeting card", 500, 500)
    win.setCoords(0, 0, 100, 100)
    # circles
    circle = Circle(Point(40, 50), 10)
    circle.draw(win)
    circle_2 = circle.clone()
    circle_2.draw(win)
    circle_2.move(10, 0)
    circle.setFill("red")
    circle_2.setFill("red")
    circle.setOutline("red")
    circle_2.setOutline("red")
    # triangle
    triangle = Polygon(Point(45, 25), Point(30, 50), Point(60, 50))
    triangle.setOutline("red")
    triangle.setFill("red")
    triangle.draw(win)
    # arrow
    arrow = Line(Point(0, 0), Point(40, 40))
    arrow.setWidth(10)
    arrow.setFill("gold")
    arrow.setArrow("last")
    arrow.draw(win)
    # make arrow move
    greeting = Text(Point(50, 90), "Happy Valentine's Day!")
    greeting.draw(win)
    time.sleep(3)
    greeting.setText("")
    for _ in range(15):
        arrow.move(5, 5)
        time.sleep(.1)
    # write click anywhere to close
    message = Text(Point(40, 10), "Click anywhere to close")
    message.draw(win)
    win.getMouse()
    win.close()


if __name__ == '__main__':
    main()
