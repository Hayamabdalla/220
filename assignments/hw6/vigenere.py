"""
name: Hayam Abdalla
vigenere.py

problem: write a program to implement the vignere cipher
certification of authenticity:
I certify that this assignment is entirely my own work.
"""

from graphics import GraphWin, Text, Point, Entry, Rectangle


def main():
    win = GraphWin("vigenere", 500, 375)
    win.setCoords(0, 0, 10, 10)
    Text(Point(2, 8), "message to code").draw(win)
    Text(Point(2.3, 7), "enter keyword").draw(win)
    enter_box_1 = Entry(Point(5.6, 8), 30)
    enter_box_2 = Entry(Point(4.5, 7), 15)
    enter_box_1.draw(win)
    enter_box_2.draw(win)
    # draw encode button
    draw_button(Point(4, 3), Point(5.5, 4), "Encode", win)
    message = enter_box_1.getText()
    key = enter_box_2.getText()

    encoded = code(message, key)

    result = Text(Point(4.5, 3.5), "Resulting message\n" + encoded)
    result.draw(win)
    text = Text(Point(5, 1.5), "click anywhere to close")
    text.draw(win)
    win.getMouse()
    win.close()


# draw encode button
def draw_button(point_1, point_2, button_text, win):
    outline = Rectangle(point_1, point_2)
    center = outline.getCenter()
    label = Text(center, button_text)
    outline.draw(win)
    label.draw(win)

    win.getMouse()
    outline.undraw()
    label.undraw()


def code(message, keyword):
    message = message.upper()
    message = message.split()
    message = "".join(message)

    keyword = keyword.upper()

    message = message
    key = keyword
    acc = ""
    for i in range(len(message)):
        character = message[i]
        key = keyword[i % len(keyword)]
        key = ord(key) - 65
        y = ord(character) + key
        if y > 90:
            y -= 26
        z = chr(y)
        acc += z
    return acc


if __name__ == '__main__':
    main()
