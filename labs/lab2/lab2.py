"""
Name: <Hayam Abdalla>
<ProgramName>.py
"""
import math
def sum_of_threes():
    bound=eval(input("enter the bound"))
    acc=0
    for i in range(0,bound+1,3):
        acc=i+acc
    print(acc)

sum_of_threes()

def multiplication_table():
    for h in range(1,11):
        for l in range (1,11):
            print (h * l, end =" ")
        print()

multiplication_table()

def triangle_area():
    a=eval(input("a"))
    b=eval(input("b"))
    c=eval(input("c"))
    s=(a+b+c)/2
    A=s*((s-a)*(s-b)*(s-c))
    A=math.sqrt(A)
    print(A)

triangle_area()

def sum_of_squares():
    low = eval(input('low'))
    upper =eval(input("upper"))
    acc=0
    for x in range (low,upper+1):
        acc=acc+x**2
    print(acc)

sum_of_squares()

def power():
    base=eval(input("base"))
    exponent=eval(input("exponent"))
    acc=1
    for x in range(exponent):
        acc = acc*base
    print(acc)

power()
