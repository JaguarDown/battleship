# Ship.py

# TODO: Get coordinates function

from Coordinate import Coordinate
from enum import Enum

class Ship:

    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.is_sunk = False
        self.is_placed = False
        self.location = None
        self.occupied_sectors = []

    def place(self, y, x, orientation):
        self.location = Coordinate(y, x)
        self.occupied_sectors = self.get_sectors(y, x, orientation)
        self.is_placed = True

    def get_sectors(self, y, x, orientation):
        squares = []
        if orientation == "H":
            squares.insert(0, Coordinate(y, x))
            for i in range(1, self.size):
                squares.insert(i, Coordinate(y, x + i))
            return squares
        else:
            squares.insert(0, Coordinate(y, x))
            for i in range(1, self.size):
                squares.insert(i, Coordinate(y + i, x))
            return squares
    
