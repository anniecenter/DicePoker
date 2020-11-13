# File Name:     die_view.py
# Programmer:    Annie Center
# Date:          Nov. 18, 2019

from graphics import Point
from graphics import Rectangle
from graphics import Circle
from button import Button


class DieView:
    def __init__(self, win, center, size):
        # Define some standard values
        self.win = win
        self.background = "white"
        self.foreground = "black"
        self.psize = 0.1 * size
        hsize = size / 2.0
        offset = 0.6 * hsize

        # Create a square for the face
        cx, cy = center.getX(), center.getY()
        p1 = Point(cx - hsize, cy - hsize)
        p2 = Point(cx + hsize, cy + hsize)
        rect = Rectangle(p1, p2)
        rect.draw(self.win)
        rect.setFill(self.background)

        # Create 7 circles for standard pip locations
        self.pips = [self.__makePip(cx - offset, cy - offset),
                     self.__makePip(cx - offset, cy),
                     self.__makePip(cx - offset, cy + offset),
                     self.__makePip(cx, cy),
                     self.__makePip(cx + offset, cy - offset),
                     self.__makePip(cx + offset, cy),
                     self.__makePip(cx + offset, cy + offset)]

        # Create a table for which pips are on for each value
        self.onTable = [[], [3], [2, 4], [2, 3, 4], [0, 2, 4, 6], [0, 2, 3, 4, 6], [0, 1, 2, 4, 5, 6]]

        # Draw an initial value
        self.setValue(1)

    def __makePip(self, x, y):
        pip = Circle(Point(x, y), self.psize)
        pip.setFill(self.background)
        pip.setOutline(self.background)
        pip.draw(self.win)
        return pip

    def setValue(self, value):
        # Turn all pips off
        for pip in self.pips:
            pip.setFill(self.background)

        # Turn appropriate pips back on
        for i in self.onTable[value]:
            self.pips[i].setFill(self.foreground)

        self.value = value

    def setColor(self, color):
        self.foreground = color
        self.setValue(self.value)
