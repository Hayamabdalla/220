from button import Button
from random import randint
from graphics import GraphWin, Rectangle, Point


def main():
    win = Graphwin(" ", 500,500)

    text = Text(Point(250, 100),"I have a secret door")
    instruction = text(Point(250,400), "click to choose my door")
    text.draw(win)
    instruction.draw(win)

    door_1_rect = Rectangle(Point(50, 300), Point(150, 350))
    door_1 = Button(door_1_rect, "Door 1")
    door_1.draw(win)

    door_2_rect = Rectangle(Point(200, 300), Point(300, 350))
    door_2 = Button(door_2_rect, "Door 2")
    door_2.draw(win)

    door_3_rect = Rectangle(Point(350, 300), Point(450, 350))
    door_3 = Button(door_3_rect, "Door 3")
    door_3.draw(win)


    win.getMous()
    win.close()


def get_random():
    random = randint(1, 3)
    return random

def did_win(cl_button):
    win_door = get_random()

    if int(cl_button.get_label()[-1]) == win_door:
        return "yay! you Win!"
    else:
        return "sorry, you lose! " + str(win_door) + "was the secret door"



    door_1 = Button(Rectangle())

# rect = Rectangle(Point(50,50), Point(100,100))

