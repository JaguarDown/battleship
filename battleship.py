# battleship.py

# TODO: Implement colors in the grid for readability, such as a blue ocean, red
# hits, white misses, and gray ships.

# TODO: Implement multiple squares for ships

# TODO:  Validate input coordinates to make sure they're not off of the
#        board or on top of other ships. Check for situations like trying to place the first
#        sector of a carrier at the far right of the board horizontally which
#        is impossible since the ship can't hang off the edge. You should correct
#        by checking the squares to the left and moving the ship left.

from random import randint

from numpy import can_cast
from Ship import Ship
from ConsoleColor import ConsoleColor
from Board import Board

colors = ConsoleColor()

player_board = Board("Player Grid", False)

target_board = Board("Target Grid", True)

# We don't define boards for the computer because it doesn't need to look at
# one. When the computer fires I think we will just check it against the main
# board for now becasue they will be random. We can add logic later. The
# computer's ship locations are stored in themselves.

# P. S. However, if you want
# to model it after the real world, the ships could just keep track of their
# hits and the computer's board could keep track of the locations. Food for
# thought. -ZP 1/22/2020

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

def print_boards():
    target_board.print()
    player_board.print()

def random_position(grid):
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
        if not ship.is_placed:
            while True:
                can_place = True
                coordinates = get_valid_coordinates(ship)
                y, x = coordinates[0], coordinates[1]
                orientation = get_valid_orientation(ship)
            
                for sector in ship.get_occupied_sectors(y, x, orientation):
                    if sector.y > 10 or sector.x > 10:
                        can_place = False
                        error = "That will hang off the map!"
                        break
                    elif player_board.grid[sector.y][sector.x] != colors.blue("*"):
                        can_place = False
                        error = "There's a ship in the way!"
                        break
                
                if can_place:
                    ship.place(y, x, orientation)
                    for sector in ship.occupied_sectors:
                        player_board.grid[sector.y][sector.x] = ship.name[0]
                    break
                else:
                    print(error, " Please try again.")
                    continue



def place_computer_ships():
    print("Placing computer ships...")
    for ship in computer_ships:
        if not ship.is_placed:
            while True:
                can_place = True
                # Generate random positions
                y = random_position(target_board.grid)
                x = random_position(target_board.grid)
                orientation = random_orientation()

                # TODO: Extend this loop to shift the ship left or up if part of it will be off the grid
                # and then recheck until conditions are satisfied.

                # Check all sqaures the ship will be on
                for sector in ship.get_occupied_sectors(y, x, orientation):
                    # Make sure it's not off the map
                    if sector.y > 10 or sector.x > 10:
                        can_place = False
                        break
                    # Make sure there's not a ship there
                    elif target_board.grid[sector.y][sector.x] != colors.blue("*"):
                        can_place = False
                        break
                
                if can_place:
                    print("\nPlacing the computer's", ship.name, "at a random locatoin.")
                    ship.place(y, x, orientation)
                    # Rename sectors to ship letter
                    for sector in ship.occupied_sectors:
                        target_board.grid[sector.y][sector.x] = ship.name[0]
                    break
                else:
                    continue

player_board.initialize()
target_board.initialize()
print_boards()
player_ships = create_ships()
computer_ships = create_ships()
place_player_ships()
place_computer_ships()
print_boards()