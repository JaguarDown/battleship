# Ship.py

# TODO: Get coordinates function

from Coordinates import Coordinates
from enum import Enum

class Ship:

    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.is_sunk = False
        self.is_placed = False
        self.location = None
        self.occupied_sectors = []

    # Place the ship on the grid by storing some location and status data.
    def place(self, y, x, orientation):
        self.location = Coordinates(y, x)
        self.occupied_sectors = self.get_occupied_sectors(y, x, orientation)
        self.is_placed = True

    # Calculate the ship's space on the grid and return a list of sectors (Coordinate objects)
    def get_occupied_sectors(self, y, x, orientation):
        squares = []
        if orientation == "H":
            squares.insert(0, Coordinates(y, x))
            for i in range(1, self.size):
                squares.insert(i, Coordinates(y, x + i))
            return squares
        else:
            squares.insert(0, Coordinates(y, x))
            for i in range(1, self.size):
                squares.insert(i, Coordinates(y + i, x))
            return squares
    
