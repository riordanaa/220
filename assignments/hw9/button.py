"""
Name: <Aidan Riordan>
program name: <button.py>
I Aidan Riordan certify that this is my own work
"""
from graphics import Text


class Button:
    """This class will allow construction of doors with properties to have a shape and text"""
    def __init__(self, rectangle_shape, string_label):
        """This makes the button class"""
        self.shape = rectangle_shape
        self.text = string_label

    def get_label(self):
        """This returns the label from the button object"""
        return self.text

    def draw(self, win):
        """This draws the door on the screen"""

        center = self.shape.getCenter()
        self.text = Text(center, self.text)
        self.shape.draw(win)
        self.text.draw(win)


    def undraw(self):
        """Undraw function undraws the objects shape and text"""
        self.text.undraw()
        self.shape.undraw()

    def is_clicked(self, point):
        """Returns true if clikced within shape bounds returns false otherwise"""
        p_1 = self.shape.getP1()
        p_2 = self.shape.getP2()
        width = abs(p_1.getX() - p_2.getX())
        height = abs(p_1.getY() - p_2.getY())
        x_1 = point.getX()
        y_1 = point.getY()
        d_x = abs(self.shape.getCenter().getX() - x_1)
        d_y = abs(self.shape.getCenter().getY() - y_1)
        if d_x <= width/2 and d_y <= height/2:
            return True
        return False

    def color_button(self, color):
        """allows to change fill color of shape"""
        self.shape.setFill(color)

    def set_label(self, label):
        """changes label of button"""
        self.text.setText(label)
