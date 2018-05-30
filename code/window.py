import tkinter as tk
from grid import Grid


class MainWindow:

    def __init__(self, master, rows, columns):
        self.rows = rows
        self.columns = columns

        self.dead_cell_color = "White"
        self.alive_cell_color = "Light Green"
        
        self.grid = Grid(rows, columns) # This window's associated grid

        self.master = master
        self.main_frame = tk.Frame(self.master) # The main frame of this window
        self.main_frame.pack()

        self.buttons_frame = tk.Frame(self.main_frame)  # Frame holding buttons in this window
        self.buttons_frame.grid(row=0, sticky="w")

        self.cell_grid_frame = tk.Frame(self.main_frame)  # Frame displaying all the cells in the grid
        self.cell_grid_frame.grid(row=1)

        self.next_gen_button = tk.Button(self.buttons_frame,
                                         text="Next",
                                         bg="Green",
                                         activebackground="Dark Green",
                                         command=self.next_gen)

        self.next_gen_button.grid(row=0, column=0)

        # Button the when pressed clears the board of cells - i.e. resets them all to dead cells
        self.clear_button = tk.Button(self.buttons_frame,
                                      text="Clear",
                                      bg="Red",
                                      activebackground="Dark Red",
                                      command=self.clear)

        self.clear_button.grid(row=0, column=1)

        # 2d grid holding all "tile buttons" which represent some associated cell in this window's grid
        self.cell_grid = []

        for i in range(rows):
            cell_row = []
            for j in range(columns):
                self.cell_frame = tk.Frame(self.cell_grid_frame, height=15, width=15)
                self.cell = tk.Button(self.cell_frame,
                                      bg=self.dead_cell_color,
                                      command=lambda i=i, j=j : self.change_color(i, j))

                self.cell_frame.grid_propagate(False)  # Disables frame resizing
                self.cell_frame.columnconfigure(0, weight=1)  # Allows cell to fill frame
                self.cell_frame.rowconfigure(0, weight=1)

                self.cell_frame.grid(row=j+1, column=i)
                self.cell.grid(sticky="nesw")
                cell_row.append(self.cell)

            self.cell_grid.append(cell_row)

    def change_color(self, i, j):
        button = self.cell_grid[i][j]

        if button.cget("bg") == self.dead_cell_color:
            button.config(bg=self.alive_cell_color)
        else:
            button.config(bg=self.dead_cell_color)

        self.grid.change_cell(j + 1, i + 1)

    def update_cell(self, i, j, num):
        button = self.cell_grid[i][j]
        if num == 1:
            button.config(bg=self.alive_cell_color)
        elif num == 0:
            button.config(bg=self.dead_cell_color)


    def next_gen(self):
        self.grid.next_gen()

        for row in range(self.rows):
            for col in range(self.columns):
                self.update_cell(row, col, self.grid.get_cell(col + 1, row + 1))

    def clear(self):
        for row in self.cell_grid:
            for button in row:
                button.config(bg=self.dead_cell_color)

        self.grid.clear()


if __name__ == "__main__":
    root = tk.Tk()
    mw = MainWindow(root, 40, 40)
    root.mainloop()
