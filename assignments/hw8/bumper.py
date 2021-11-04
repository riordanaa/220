
"""
Name: <Aidan Riordan>
program name: <vigenere>
I Aidan Riordan certify that this is my own work
"""

from random import randint
import math
from graphics import *


def get_random_color():
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    color1 = color_rgb(red, green, blue)
    return color1


def get_random(move_amount):
    rand_move_amount = randint(-1*move_amount, move_amount)
    return int(rand_move_amount)


def hit_vertical(ball, win):
    # get r and center for both balls
    center = ball.getCenter()
    r = ball.getRadius()
    # left and right bounds as vars from win
    right_chord = win.getWidth()

    distance_of_ball_horiz1 = math.sqrt((center.getX() - right_chord) ** 2)
    distance_of_ball_horiz2 = math.sqrt((center.getX()) ** 2)

    if float(distance_of_ball_horiz1) <= r or float(distance_of_ball_horiz2) <= r:
        return True

    return False


def hit_horizontal(ball, win):
    center = ball.getCenter()
    r = ball.getRadius()
    lower_bound_chord = win.getHeight()

    distance_of_ball_horiz1 = math.sqrt((center.getY() - lower_bound_chord) ** 2)
    distance_of_ball_horiz2 = math.sqrt((center.getY()) ** 2)

    if float(distance_of_ball_horiz1) <= r or float(distance_of_ball_horiz2) <= r:
        return True

    return False


def did_collide(ball, ball2):
    # get r and center for both balls
    center = ball.getCenter()
    r = ball.getRadius()
    center2 = ball2.getCenter()
    r2 = ball.getRadius()

    dist_balls = math.sqrt((center.getX() - center2.getX())**2+(center.getY()-center2.getY())**2)
    rad_len = r + r2

    if float(dist_balls) <= rad_len:
        return True
    else:
        return False


def main():
    # screen setup
    win = GraphWin("bouncing balls", 600, 400)
    # make circle
    ball = Circle(Point(40, 50), 10)
    color1 = get_random_color()
    ball.setFill(color1)
    ball.draw(win)
    # make ball 2
    ball2 = Circle(Point(60, 30), 10)
    color1 = get_random_color()
    ball2.setFill(color1)
    ball2.draw(win)
    # make circle move
    # initialize movement increments
    move_x = get_random(4)
    move_y = get_random(4)
    move_x2 = get_random(4)
    move_y2 = get_random(4)
    # loop movement check hits
    while True:
        # add a random move amount
        ball.move(move_x, move_y)

        if hit_vertical(ball, win) is True:
            move_x = move_x * -1
        if hit_horizontal(ball, win) is True:
            move_y = move_y * -1

        # repeat for ball 2
        ball2.move(move_x2, move_y2)

        if hit_vertical(ball2, win) is True:
            move_x2 = move_x2 * -1

        if hit_horizontal(ball2, win) is True:
            move_y2 = move_y2 * -1

        if did_collide(ball, ball2) is True:
            move_x2 = move_x2 * -1
            move_y2 = move_y2 * -1
            move_x = move_x * -1
            move_y = move_y * -1
        time.sleep(.01)

# close
    win.getMouse()
    win.close()


if __name__ == '__main__':
    main()
