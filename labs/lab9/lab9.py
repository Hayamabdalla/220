"""
Name: Hayam Abdalla
<ProgramName>.py
"""


from graphics import *
import math


def addTens(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] + 10
    # print(nums)


def squareEach(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] ** 2
    # print(nums)


def sumList (nums):
    acc = 0
    for i in range(len(nums)):
        acc += nums[i]
    # print(acc)
    return acc


def toNumbers(strList):
    for i in range(len(strList)):
        strList[i] = float(strList[i])
    # print(strList)

def writesumOfSquares():
    file = input("enter the file name?")
    infile = open(file, "r")
    outfile = open("output.txt", "w+")
    for line in infile:
        num = line.split()
        toNumbers(num)
        squareEach(num)
        s = sumList(num)
        outfile.write("Sum of squares= " + str(s))

def starter():
    weight = float(input("enter your weight:"))
    numWins = eval(input("enter the number of wins "))

    if 160 > weight >= 150:
        if numWins > 5 :
            print("player has earned starter position")
    elif weight > 199 or numWins > 20 :
        print("player has earned starter position")
    else:
        print("player has not earned starter position ")

def leapYear(year):
    if year % 4 == 0:
        if year % 100 != 0 or year % 400 == 0:
            print(str(year) + "it is a leap year")

    else:
        print(str(year) + "it is not a leap year")


def circle():
    win = GraphWin("Circle", 400, 400)
    p1 = win.getMouse()
    p2 = win.getMouse()
    radius = math.sqrt((p2.getX()-p1.getX())**2 +(p2.getY()- p1.getY()) ** 2)
    circle = Circle(p1, radius)
    circle.draw(win)
    p3 = win.getMouse()
    p4 = win.getMouse()
    radius2 = math.sqrt((p3.getX()-p4.getX()) ** 2 + (p3.getY() - p4.getY()) ** 2)
    circle = Circle(p3, radius2)
    circle.draw(win)
    distance = math.sqrt((p3.getX()-p1.getX()) ** 2 + (p3.getY() - p1.getY()) ** 2)
    if distance <= (radius + radius2):
        msg = Text(Point(200,200), "the circles overlap.")
        msg.draw(win)

    else:
        msg = Text(Point(200, 200),"the circles do not overlap.")
        msg.draw(win)


    win.getMouse()
    win.close()

def main():
    x = [3,4,5]
    y = ["3","4","5"]
    # writesumOfSquares()
    # toNumbers(y)
    # sumList(x)
    # squareEach(x)
    # addTens(x)
    circle()


