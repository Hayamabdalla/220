"""
Name: <Hayam Abdalla>
<ProgramName>.py
"""

from graphics import *
import math


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
    instructions = Text(inst_pt, "Click to move aquare")
    instructions.draw(win)
    inst_pt = Point(width / 2, height - 30)
    instructions = Text(inst_pt, "Click to move aquare")
    instructions.draw(win)

    # builds a circle
    shape = Rectangle(Point(50, 50), Point(70,70))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)

    # allows the user to click multiple times to move the circle
    for i in range(num_clicks):
        p = win.getMouse()
        shape = Rectangle(Point(p.getX() - 10, p.getY() - 10), Point(p.getX() + 10, p.getY()+ 10 ))
        shape.setOutline("red")
        shape.setFill("red")
        shape.draw(win)






    instructions.undraw()
    instructions.setText("click to close")
    instructions.draw(win)

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

    win_width = 400
    win_height = 400
    win = GraphWin("rectangle", win_width, win_height)
    p1 = win.getMouse()
    p2 = win.getMouse()
    r = Rectangle(p1,p2)
    r.draw(win)
    length = abs(p1.getX() - p2.getX())
    width = abs(p1.getY()-p2.getY())
    area= length * width
    perimeter = 2 * length + 2* width


    inst_pt = Point(win_width / 2, win_height - 10)
    instructions = Text(inst_pt, "the area is: " + str (area) )
    instructions.draw(win)

    inst_pt = Point(win_width / 2,win_height - 30)
    instructions = Text(inst_pt, "the perimeter is : " + str(perimeter))
    instructions.draw(win)


    win.getMouse()
    win.close()

def circle():
    win_width = 400
    win_height = 400
    win = GraphWin("circle", win_width, win_height)
    p1 = win.getMouse()
    p2 = win.getMouse()
    X1 = p1.getX()
    X2 = p2.getX()
    Y1 = p1.getY()
    Y2 = p2.getY()
    d = math.sqrt(((X2-X1)**2)+((Y2 -Y1)**2))
    circle_A = Circle(p1,d)
    circle_A.draw(win)


    inst_pt = Point(win_width / 2, win_height - 10)
    instructions = Text(inst_pt, "the radius is : " + str(d))
    instructions.draw(win)

    win.getMouse()
    win.close()

def pi2():
    n= eval(input("number of terms in series:"))
    acc = 0
    for i in range(n):
        num = 4 *((-1)**i)
        denom = 1 + 2*i
        fraction = (num / denom)
        acc = acc + fraction
    print(math.pi-acc)
    print(acc)







def main():
    squares()
    rectangle()
    circle()
    pi2()

main()
