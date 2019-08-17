#!/usr/bin/python

class Ship:

    x = 0
    y = 0
    size = 0
    is_sunk = False

    def __init__(self, size):
        self.size = size
