"""
name: Hayam Abdalla
greeting.py

problem: Write a program that displays a heart for a greeting card
certification of authenticity:
I certify that this assignment is entirely my own work.
"""

from graphics import GraphWin, Point, Polygon, Text, Line, time


def main():
    win = GraphWin("Happy Valentin's Day", 500, 500)
    win.setCoords(0, 0, 20, 20)
    point1 = Point(10, 16)
    point2 = Point(16, 19)
    point3 = Point(18, 16)
    point4 = Point(10, 1)
    point5 = Point(10, 1)
    point6 = Point(2, 16)
    point7 = Point(5, 19)
    point8 = Point(10, 16)
    point1.draw(win)
    point2.draw(win)
    point3.draw(win)
    point4.draw(win)
    point5.draw(win)
    point6.draw(win)
    point7.draw(win)
    point8.draw(win)
    heart = Polygon(point1, point2, point3, point4, point5,  point6, point7, point8)
    heart.draw(win)
    heart.setFill("Red")
    text = Text(Point(10, 10), "Happy Valentin's Day!")
    text.setTextColor("purple")
    text.setFace("arial")
    text.setSize(23)
    text.setStyle("italic")
    text.draw(win)
    start_point = Point(1, 1)
    end_point = Point(5, 5)
    arrow = Line(start_point, end_point)
    arrow.setWidth(3)
    arrow.setArrow("last")
    arrow.draw(win)
    for _ in range(20):
        arrow.move(1, 1)
        time.sleep(0.4)
    arrow.undraw()
    text = Text(Point(10, 0.5), "click anywhere to close")
    text.draw(win)
    win.getMouse()
    win.close()


if __name__ == '__main__':
    main()
