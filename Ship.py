#!/usr/bin/python

from Coordinates import Coordinates

class Ship:

    x = 0
    y = 0
    name = ""
    size = 0
    is_sunk = False
    is_placed = False
    occupied_squares = []

    def __init__(self, name, size):
        self.name = name
        self.size = size

    def place(self, x, y):
        """
        To do: validate input coordinates to make sure they're not off of the
        board or on top of other ships. After adding orientation occupying
        multiple squares, check for situations like trying to place the first
        square of a carrier at the far right of the board horizontally which
        is impossible since the ship can't hang off the edge. You should correct
        by checking the squares to the left and moving the ship left.
        """
        square1 = Coordinates(x, y)
        self.occupied_squares.insert(0, square1)
        is_placed = True
