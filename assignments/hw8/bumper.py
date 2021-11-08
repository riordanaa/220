
from graphics import *
import math
from random import randint





def get_random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return color_rgb(r, g, b)


def get_random(move_amount):
    return randint(-1*move_amount, move_amount)


def hit_vertical(ball, win):
    right_chord = win.getWidth()
    c = ball.getCenter()
    rad = ball.getRadius()
    distance_of_ball_horiz1 = math.sqrt((c.getX() - right_chord) ** 2)
    distance_of_ball_horiz2 = math.sqrt((c.getX()) ** 2)
    if distance_of_ball_horiz1 <= rad:
        return True
    if distance_of_ball_horiz2 <= rad:
        return True
    else:
        return False


def hit_horizontal(ball, win):
    lower_bound_chord = win.getHeight()
    center = ball.getCenter()
    rad = ball.getRadius()
    distance_of_ball_horiz1 = math.sqrt((center.getY() - lower_bound_chord) ** 2)
    distance_of_ball_horiz2 = math.sqrt((center.getY()) ** 2)
    if float(distance_of_ball_horiz1) <= rad:
        return True
    if float(distance_of_ball_horiz2) <= rad:
        return True
    else:
        return False


def did_collide(ball, ball2):
    # get r and center for both balls
    rad = ball.getRadius()
    center = ball.getCenter()
    rad_2 = ball.getRadius()
    center2 = ball2.getCenter()
    dist_balls = math.sqrt((center.getX() - center2.getX())**2+(center.getY()-center2.getY())**2)
    rad_len = rad + rad_2

    if float(dist_balls) <= rad_len:
        return True

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
