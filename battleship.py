#!/usr/bin/python

from random import randint
from Ship import Ship

grid1 = [[" ", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10",]]

grid2 = [[" ", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10",]]

x_coords = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

def initialize_grid(grid):
    index = 0
    for row in range(1, 11):
        grid.append(["O"] * 10)
        grid[row].insert(0, x_coords[index])
        index += 1

def print_board(grid, message, space):
    print message + "\n"
    if space:
        counter = 0
        for row in grid:
            if counter == 1:
                print " "
            print "  ".join(row)
            counter += 1
    else:
        for row in grid:
            print " ".join(row)

initialize_grid(grid1)
initialize_grid(grid2)
print_board(grid2, "Tracking Grid:", False)
print_board(grid1, "\nMain Grid:", True)

def random_row(grid):
    return randint(1, len(grid) - 1)

def random_col(grid):
    return randint(1, len(grid) - 1)

carrier = Ship(5)
carrier.x = raw_input("Enter carrier X coordinate:")
carrier.y = random_col(grid1)

print "Carrier X:", carrier.x
print "Carrier Y:", carrier.y
