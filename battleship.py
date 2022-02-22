# battleship.py

# TODO: Just let the user type letter coordinates and use a dictionary of
# letters that map to numbers to interpret the coordinates. It'll be much
# easier to just let the program deal with coordinates in integers. I couldn't
# figure out how to make my list of dictionaries work, apparently dictionaries
# assume a different order than you put them in which is terrible for grids.

# TODO: Implement colors in the grid for readability, such as a blue ocean, red
# hits, white misses, and gray ships.

# TODO:  Validate input coordinates to make sure they're not off of the
#        board or on top of other ships. After adding orientation occupying
#        multiple squares, check for situations like trying to place the first
#        square of a carrier at the far right of the board horizontally which
#        is impossible since the ship can't hang off the edge. You should correct
#        by checking the squares to the left and moving the ship left.

from random import randint
from Ship import Ship
from Vector import Vector
from ConsoleColor import ConsoleColor

colors = ConsoleColor()

main_board = [[" ", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10",]]

tracking_board = [[" ", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10",]]

# We don't define boards for the computer because it doesn't need to look at
# one. When the computer fires I think we will just check it against the main
# board for now becasue they will be random. We can add logic later. The
# computer's ship locations are stored in themselves.

# P. S. However, if you want
# to model it after the real world, the ships could just keep track of their
# hits and the computer's board could keep track of the locations. Food for
# thought. -ZP 1/22/2020

y_axis = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

letter_coordinates = {
    "A": 1,
    "B": 2,
    "C": 3,
    "D": 4,
    "E": 5,
    "F": 6,
    "G": 7,
    "H": 8,
    "I": 9,
    "J": 10,
}

def initialize_grid(grid):
    index = 0
    for row in range(1, 11):
        grid.append([colors.blue("*")] * 10)
        grid[row].insert(0, y_axis[index])
        index += 1

def print_m_board(board):
    print("\nMain grid:" + "\n")
    counter = 0
    for row in board:
        if counter == 1:
            print(" ")
        print("  ".join(row))
        counter += 1

def print_t_board(board):
    print("Tracking grid: " + "\n")
    for row in board:
        print(" ".join(row))

def print_boards():
    print_t_board(tracking_board)
    print_m_board(main_board)

def random_row(grid):
    return randint(1, len(grid) - 1)

def random_col(grid):
    return randint(1, len(grid) - 1)

def random_orientation():
    orientations = ["H", "V"]
    choice = orientations[randint(0, 1)]
    return choice

def create_ships():
    carrier = Ship("Carrier", 5)
    battleship = Ship("Battleship", 4)
    cruiser = Ship("Cruiser", 3)
    submarine = Ship("Submarine", 3)
    destroyer = Ship("Destroyer", 2)
    ships = [carrier, battleship, cruiser, submarine, destroyer]
    return ships

def get_valid_coordinates(ship):
    while True:
        print("\nPlease enter coordinates for your " + ship.name + ".")
        user_input = str(input())
        if user_input[0].upper() not in ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J",]:
            print("\nInvalid y coordinate.")
            continue
        elif len(user_input) > 3:
            print("\nYour input is too long.")
            continue
        else:
            try:
                x = int(user_input[1:len(user_input)])
            except ValueError:
                print("\nMalformed coordinate.")
                continue
            if x < 0 or x > 10:
                print("\nX coordinate out of range")
                continue
            y = user_input[0].upper()
            coordinates = [letter_coordinates[y], x]
            return coordinates
            

def get_valid_orientation(ship):
    while True:
        print("\nPlease enter an orientation for your " + ship.name + ".\n" \
        "H/h = horizontal, V/v = vertical: ")
        orientation = input()
        if orientation.upper() not in ["V", "H",]:
            print("Orientation must be entered as H or h for horizontal " \
            "and V or v for vertical.")
            continue
        else:
            orientation = orientation.upper()
            return orientation

def place_player_ships():
    print("\nPlease place your ships on the board.")
    for ship in player_ships:
        if ship.is_placed == False:
            coordinates = get_valid_coordinates(ship)
            y = coordinates[0]
            x = coordinates[1]
            orientation = get_valid_orientation(ship)
            # Before placing the next ship,
            # we should compare the coordinates to the main board to see if a ship is there.
            ship.place(y, x, orientation)
            for square in ship.occupied_squares:
                main_board[square.y][square.x] = ship.name[0]


def place_computer_ships():
    print("Placing computer ships...")
    for ship in computer_ships:
        if ship.is_placed == False:
            print("Placing the computer's", ship.name, "at a random location.")
            ship.place(random_row(tracking_board), random_col(tracking_board), random_orientation())

initialize_grid(main_board)
initialize_grid(tracking_board)
print_boards()
player_ships = create_ships()
computer_ships = create_ships()
place_player_ships()
place_computer_ships()
print_boards()
