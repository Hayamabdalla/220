"""
name: Hayam Abdalla
bumper.py

problem: Write a program that creates two bumper circles .
certification of authenticity:
I certify that this assignment is entirely my own work.
"""

from random import randint
from math import sqrt
from time import sleep
from graphics import GraphWin, Circle, color_rgb, Point


def main():
    win = GraphWin("Bumber", 500, 500)

    ball_1 = Circle(Point(50, 50), 35)
    ball_2 = Circle(Point(100, 100), 35)

    ball_1.setFill(get_random_color())
    ball_2.setFill(get_random_color())

    ball_1.draw(win)
    ball_2.draw(win)

    # initial random points
    ball_1_x = get_random(10)
    ball_2_x = get_random(10)
    ball_1_y = get_random(10)
    ball_2_y = get_random(10)

    while not win.checkMouse():
        ball_1.move(ball_1_x, ball_1_y)
        ball_2.move(ball_2_x, ball_2_y)

        if did_collide(ball_1, ball_2):
            ball_1_x = ball_1_x * -1
            ball_2_x = ball_2_x * -1
            ball_1_y = ball_1_y * -1
            ball_2_y = ball_2_y * -1
        if hit_horizontal(ball_1, win):
            ball_1_y = ball_1_y * -1
        if hit_vertical(ball_1, win):
            ball_1_x = ball_1_x * -1
        if hit_horizontal(ball_2, win):
            ball_2_y = ball_2_y * -1
        if hit_vertical(ball_2, win):
            ball_2_x = ball_2_x * -1

        sleep(0.1)

    win.close()


def get_random(move_amount):
    rand = randint(-1 * move_amount, move_amount)
    return rand


def did_collide(ball, ball2):
    cent_1 = ball.getCenter()
    cent_2 = ball2.getCenter()
    dist = sqrt((cent_1.getX() - cent_2.getX())**2 + (cent_1.getY() - cent_2.getY())**2)
    sum_r = ball.getRadius() + ball2.getRadius()

    return dist <= sum_r


def hit_vertical(ball, win):
    center = ball.getCenter()
    rad = ball.getRadius()
    width = win.getWidth()

    if center.getX() <= rad:
        return True
    if center.getX() >= width - rad:
        return True
    return False


def hit_horizontal(ball, win):
    center = ball.getCenter()
    rad = ball.getRadius()
    height = win.getHeight()

    if center.getY() <= rad:
        return True
    if center.getY() >= height - rad:
        return True
    return False


def get_random_color():
    color = color_rgb(randint(0, 255), randint(0, 255), randint(0, 255))
    return color


if __name__ == '__main__':
    main()
