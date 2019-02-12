from graphics import *


class Button:
    """button in a graphic window
    Methods: activate(), deactivate(), clicked(point), getLabel(), setLabel(),
    setColor(), setValue(), getValue(), undraw()"""
    def __init__(self, win, center, width, height, label):
        """creates a rectangular button centered at center,
        having the width, height and label."""
        p1 = Point(center.getX()-width/2 , center.getY()-height/2)
        p2 = Point(center.getX()+width/2 , center.getY()+height/2)
        self.xmin, self.ymin = p1.getX(), p1.getY()
        self.xmax, self.ymax = p2.getX(), p2.getY()
        self.rect = Rectangle(p1, p2)
        self.rect.setFill("lightgrey")
        self.rect.setWidth(1)
        self.rect.draw(win)
        self.label = Text(center, label)
        self.label.draw(win)
        self.active = False
        self.value = ""

    def activate(self):
        """returns the state of the button(colored and bolded)"""
        self.rect.setFill("green")
        self.rect.setWidth(2)
        self.active = True

    def deactivate(self):
        """returns the state of the button(grey and thin outline)"""
        self.rect.setFill("lightgrey")
        self.rect.setWidth(1)
        self.active = False

    def clicked(self,p):
        """checks if the button was active, and if the click was on it."""
        return (self.active and
                self.xmin <= p.getX() <= self.xmax and
                self.ymin <= p.getY() <= self.ymax)

    def getLabel(self):
        """returns a string with the label name."""
        return self.label

    def setLabel(self, newLabel):
        """sets a custom label name."""
        self.label.setText(newLabel)

    def setColor(self, color):
        """sets a custom color."""
        self.rect.setFill(color)

    def setValue(self, value):
        """sets a custom value."""
        self.value = value

    def getValue(self):
        """returns the value."""
        return self.value

    def undraw(self):
        """undraws the button"""
        self.rect.undraw()
        self.label.undraw()
