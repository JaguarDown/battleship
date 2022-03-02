# Board.py
# TODO: All code was copy and pasted from battleship.py, please eval, refactor, and finish building.

from ConsoleColor import ConsoleColor

class Board:
    
    colors = ConsoleColor()

    def __init__(self, board_name, is_target_grid):
        # String for printing
        self.board_name = board_name

        # Multi-dimensional list to form the grid later. Could probably generate the whole thing in a loop
        # but I'm just hacking it together first
        self.grid = [["  ", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10",]]

        # List for the y axis coordinates
        self.y_axis = ["A ", "B ", "C ", "D ", "E ", "F ", "G ", "H ", "I ", "J "]

    def initialize(self):
        # Build the grid
        index = 0
        # Append 10 more lists of 10 asterisks
        for row in range(1, 11):
            self.grid.append([self.colors.blue("*")] * 10)

            # On each appended row, insert the corresponding y axis coordinate (A, B, C, etc.) to index 0
            self.grid[row].insert(0, self.y_axis[index])
            index += 1

    def print(self):
        print("\n" + self.board_name + "\n")
        counter = 0
        for row in self.grid:
            if counter == 1:
                print(" ")
            print("  ".join(row))
            counter += 1
