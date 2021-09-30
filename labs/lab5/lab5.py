"""
Name: <Hayam Abdalla>
<ProgramName>.py
"""

from graphics import *
import math


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
    p1 = win.getMouse()
    p2 = win.getMouse()
    p3 = win.getMouse()
    triangle = Polygon (p1, p2, p3)
    triangle.draw(win)
    dx1 = (p1.getX() - p2.getX())
    dy1 = (p1.getY() - p2.getY())
    dx2 = (p2.getX() - p3.getX())
    dy2 = (p2.getY() - p3.getY())
    dx3 = (p1.getX() - p3.getX())
    dy3 = (p2.getY() - p3.getY())
    a = math.sqrt((dx1**2) + (dy1**2))
    b = math.sqrt((dx2**2) + (dy2**2))
    c = math.sqrt((dx3**2) + (dy3**2))
    premiter = a + b + c
    s = (a + b + c)/2
    area = math.sqrt(s * (s -a)*(s -b)*(s -c))
    inst_pt = Point(win_width / 2, win_height - 30)
    area_txt = Text(inst_pt, "the area is : " + str(area))
    area_txt.draw(win)
    inst_pt = Point(win_width / 2, win_height - 60)
    premiter_txt = Text(inst_pt, "the premiter is : " + str(premiter))
    premiter_txt.draw(win)




    # Add code here to accept the mouse clicks, draw the triangle.
    # and display its area in the graphics window.

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
    point1 = Point (win_width/2, win_height/2 + 40)
    red_box = Entry(point1, 5)
    red_box.draw(win)
    point2 = Point(win_width / 2, win_height / 2 + 70)
    green_box = Entry(point2, 5)
    green_box.draw(win)
    point3= Point(win_width / 2, win_height / 2 + 100)
    blue_box = Entry(point3, 5)
    blue_box.draw(win)
    for _ in range(5):
        win.getMouse()
        red = int(red_box.getText())
        green = int(green_box.getText())
        blue = int (blue_box.getText())
        color = color_rgb(red,green,blue)
        shape.setFill(color)






    # Wait for another click to exit
    win.getMouse()
    win.close()

def process_string():
    s = input("please enter the string")
    first_character = s[0]
    print(first_character)
    the_last_character = s[-1]
    print(the_last_character)
    inclusive_character = s[2:6]
    print(inclusive_character)
    concatenation =s [0]+s[-1]
    print(concatenation)
    step5 = s[0:3]*10
    print(step5)
    for i in range(len(s)):
        c = s[i]
        print(c)
    step7 = len(s)
    print(step7)

def list_processing():
    pt = Point(5, 10)
    value = [5, "hi" , 2.5,"there", pt, '7.2']
    step1 = value[1] + value[3]
    step2 = value[0] + value[2]
    step3 = value[1] * 5
    step4 = [value[2] , value[3],value[4]]
    step5 = [value[2] ,value[3],value[0]]
    step6 = [value[2], value[0],float(value[-1])]
    step7 = value[2]+ value[0]+ float(value[-1])
    step8 = len(value)
    print(step1)
    print(step2)
    print(step3)
    print(step4)
    print(step5)
    print(step6)
    print(step7)
    print(step8)


def another_series():
    x = eval(input("enter the number of terms:"))
    acc = 0
    for i in range(x):
        y = 2+2*(i % 3)
        print(y, end="")
        acc+= y
        print()
        print(acc)










def main():
    # target()
    # triangle()
    # color_shape()
    # process_string()
    list_processing()
    another_series()



main()
