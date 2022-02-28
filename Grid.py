# Grid.py
# TODO: All code was copy and pasted from battleship.py, please eval, refactor, and finish building.

from ConsoleColor import ConsoleColor

class Grid:
    
    colors = ConsoleColor()

    def __init__(self, grid_name, is_target_grid):
        self.is_target_grid = is_target_grid
        self.grid_name = grid_name
        self.x_axis = [[" ", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10",]]
        self.y_axis = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

    def initialize(self):
        index = 0
        for row in range(1, 11):
            self.x_axis.append([self.colors.blue("*")] * 10)
            self.x_axis[row].insert(0, self.y_axis[index])
            index += 1

    def print(self):
        if self.is_target_grid:

            print("\n" + self.grid_name + "\n")
            for row in self.x_axis:
                print(" ".join(row))
        else:
            print("\n" + self.grid_name + "\n")
            counter = 0
            for row in self.x_axis:
                if counter == 1:
                    print(" ")
                print("  ".join(row) + "\n")
                counter += 1
