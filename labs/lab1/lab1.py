"""
Name: < Hayam Abdalla>
lab1.py
problem: This function calculates the area of a rectagle
"""
def calc_area():
    length= 20
    width= 5
    area= length * width
    print ("area =", area)


def calc_rec_area():
    length=eval(input("enter the length"))
    width=eval(input("enter the width:"))
    area=length* width
    print("area=",area)

def calc_volum():
    length=eval(input("enter the length"))
    width=eval(input("enter the width"))
    hight=eval(input("enter the hight"))
    volum=length*width*hight
    print("volum=",volum)

def shooting_percentage():
    made=eval(input("enter the made shots"))
    took=eval(input("enter the took shots"))
    percent=made/took*100
    print("percent=", percent)

def coffee():
    pound=eval(input("enter the coffe pound"))
    coffee=10.50*pound+0.86*pound+1.50
    print("coffee",coffee)

def kilometers_to_miles():
    kilometer=eval(input("enter the kilometer"))
    mile=kilometer/1.61
    print("mile",mile)







