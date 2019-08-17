#!/usr/bin/python

# TODO: implement colors in the grid for readability, such as a blue ocean, red
# hits, white misses, and gray ships.

from random import randint
from Ship import Ship

main_board = [[" ", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10",]]

tracking_board = [[" ", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10",]]

# We don't define boards for the computer because it doesn't need to look at
# one. When the computer fires I think we will just check it against the main
# board for now becasue they will be random. We can add logic later. The
# computer's ship locations are stored in themselves.

x_coords = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

def initialize_grid(grid):
    index = 0
    for row in range(1, 11):
        grid.append(["O"] * 10)
        grid[row].insert(0, x_coords[index])
        index += 1

def print_m_board(board):
    print "Main grid:" + "\n"
    counter = 0
    for row in board:
        if counter == 1:
            print " "
        print "  ".join(row)
        counter += 1

def print_t_board(board):
    print "Tracking grid: " + "\n"
    for row in board:
        print " ".join(row)

def print_boards():
    print_t_board(tracking_board)
    print_m_board(main_board)

def random_row(grid):
    return randint(1, len(grid) - 1)

def random_col(grid):
    return randint(1, len(grid) - 1)

def create_ships():
    carrier = Ship("Carrier", 5)
    battleship = Ship("Battleship", 4)
    cruiser = Ship("Cruiser", 3)
    submarine = Ship("Submarine", 3)
    destroyer = Ship("Destroyer", 2)
    ships = [carrier, battleship, cruiser, submarine, destroyer]
    return ships

def place_player_ships():
    print "Please place your ships on the board."
    for ship in player_ships:
        if ship.is_placed == False:
            print "Please enter coordinates for your", ship.name
            x = input("X:")
            y = input("Y:")
            ship.place(x, y)
            main_board[x][y] = ship.name[0]


def place_computer_ships():
    print "Placing computer ships..."
    for ship in computer_ships:
        if ship.is_placed == False:
            print "Placing the computer's", ship.name, "at a random location."
            ship.place(random_row(tracking_board), random_col(tracking_board))

initialize_grid(main_board)
initialize_grid(tracking_board)
print_boards()
player_ships = create_ships()
computer_ships = create_ships()
place_player_ships()
place_computer_ships()
print_boards()
