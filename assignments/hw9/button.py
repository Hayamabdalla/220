from graphics import Text


class Button:

    def __init__(self, shape, label):
        self.shape = shape
        self.txt = Text(shape.getCenter(), label)

    def get_label(self):
        return self.text.getText()

    def draw(self, win):
        self.text.draw(win)
        self.shape.draw(win)


    def undraw(self):
        self.text.undraw()
        self.shape.undraw()

    def is_clicked(self, Point):
        click_x = Point.getX()
        click_y = Point.getY()

        point_1_x = self.shape.getP1().getX()
        point_1_y = self.shape.getP1().getY()

        point_2_x = self.shape.getP2().getX()
        point_2_y = self.shape.getP2().getY()


        if point_1_x <= click_x >= point_2_x and point_1_y <= click_y >= point_2_y:
            return True
        return False

    def color_button(self, color):
        self.shape.setfill(color)

    def set_label(self, label):
        self.text.setText(label)




