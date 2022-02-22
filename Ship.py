# Ship.py

# TODO: Get coordinates function

from Vector import Vector
from enum import Enum

class Ship:

    x = 0
    y = 0
    name = ""
    size = 0
    is_sunk = False
    is_placed = False
    location = None
    occupied_squares = []

    def __init__(self, name, size):
        self.name = name
        self.size = size

    def place(self, y, x, orientation):
        self.location = Vector(y, x)
        self.occupied_squares = self.get_squares(y, x, orientation)
        self.is_placed = True

    def get_squares(self, y, x, orientation):
        squares = []
        if orientation == "H":
            squares.insert(0, Vector(y, x))
            for i in range(1, self.size):
                squares.insert(i, Vector(y, x + i))
            return squares
        else:
            squares.insert(0, Vector(y, x))
            for i in range(1, self.size):
                squares.insert(i, Vector(y + i, x))
            return squares
    
