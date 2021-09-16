"""
Name: <Hayam Abdalla>
lab3.py
"""

def average():
    grades = eval(input("how many grades do you have?"))
    acc =0
    for i in range(grades):
        x = eval(input("enter your grades on hw" + str(i+1)))
        acc = acc + x
    answer = acc/grades
    print(answer)

average()

def tip_jar():
    acc =0
    for i in range(5):
        total = eval(input("how much do you want to donate?"))
        acc = total + acc
    print(acc)

tip_jar()

def newton():
    x = eval(input("what is the x number is"))
    refine = eval(input("how many times to improve the approximation?"))
    approximation = x/2
    for i in range(refine):
        approximation = (approximation + (x/approximation))/2
    print(approximation)

newton()

def sequence():
    x= eval(input("enter the number of terms in a series"))
    for i in range(1, x+1):
        print(1+(i//2*2))

sequence()

def pi():
    acc = 1
    x= eval(input("enter the number of terms in the series"))
    for i in range (x):
        num = 2 + (i//2*2)
        denom = 1+ ((i+1)//2*2)
        acc = acc * (num / denom)
    print(acc * 2)

pi()


