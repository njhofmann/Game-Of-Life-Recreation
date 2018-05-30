import copy

# Represents a grid of cells where:
# - 1 = a live cell
# - 0 = a dell cell
class Grid:
    def __init__(self, row, col):
        # Adds a one-layer cell border of inaccessible dead cells around the grid for computation purposes
        # So if user wants a 5x5 grid, this grid will actually by a 7x7 grid, but the user can only access the inner
        # 5x5 grid will be
        self.row = row + 2
        self.col = col + 2
        self.grid = [[0 for i in range(self.col)] for j in range(self.row)]

    # Returns if the given row and column coordinates are accessible - i.e. they are within the "inner grid"
    def accessible_coordinates(self, row, col):
        return 0 < row < (self.row - 1) and 0 < col < (self.col - 1)

    # Given the given coordinates are accessible, returns the value of the associated cell within the grid
    def get_cell(self, row, col):
        if self.accessible_coordinates(row, col):
            return self.grid[row][col]

    # If the given coordinates are accessible, "flips" the value of the associated cell s- i.e. if the value is 1
    # becomes 0, or if the value is 0 it becomes 1
    def change_cell(self, row, col):
        if self.accessible_coordinates(row, col):
            cell = self.grid[row][col]
            if cell == 0:
                self.grid[row][col] = 1
            elif cell == 1:
                self.grid[row][col] = 0

    # Produces the next generation of this grid
    def next_gen(self):
        # Makes an exact copy of the the grid, not aliased
        new_grid = copy.deepcopy(self.grid)

        # Runs each cell in the grid through next_item() based on its
        # row and column position, the sets the result to the same
        # location in new_grid
        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):
                new_grid[row][col] = self.next_item(row, col)

        # Sets this grid as new_grid
        self.grid = new_grid

    # Given the row and col of a cell in this grid, based on its
    # adjacent cells - determines if that cell will "live" or "die"
    # in the next generation
    def next_item(self, r, c):
        # Border cells are always dead cells
        if not self.accessible_coordinates(r, c):
            return 0

        item = self.grid[r][c]

        adjc = [self.grid[r - 1][c - 1], self.grid[r - 1][c + 1],
                self.grid[r - 1][c], self.grid[r][c + 1],
                self.grid[r][c - 1], self.grid[r + 1][c],
                self.grid[r + 1][c - 1], self.grid[r + 1][c + 1]]

        # Number of adjacent cells that are alive
        live_adjc = 0
        for neighbor in adjc:
            if neighbor == 1:
                live_adjc += 1

        # Conditions for determining if cell will live or die in the
        # next generation
        if item == 0:
            if live_adjc == 3:
                return 1
            else:
                return 0
        elif item == 1:
            if live_adjc == 2 or live_adjc == 3:
                return 1
            else:
                return 0

    # Performs a hard reset on this grid, makes every cell a dead cell - i.e. changes it value to 0
    def clear(self):
        self.grid = [[0 for i in range(self.col)] for j in range(self.row)]

    # Prints out all cells in this grid
    def print_grid(self):
        for row in self.grid:
            cells = ""
            for cell in row:
                cells += str(cell) + " "
            print(cells)
        print("\n")



if __name__ == '__main__':
    my_grid = Grid(5, 5)
    my_grid.print_grid()
    my_grid.change_cell(1, 1)
    my_grid.print_grid()
