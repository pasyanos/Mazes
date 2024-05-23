from cell import Cell


# A grid of cells
class Grid:
    def __init__(self, rows: int, columns: int):
        self.rows = rows
        self.columns = columns
        self.grid = self.prepare_grid()
        self.configure_cells()

    def each_cell(self):
        for row in self.grid:
            for cell in row:
                yield cell if cell else None

    def each_row(self):
        for row in self.grid:

            yield row

    def __getitem__(self, index):
        x, y = index
        if x < 0 or x >= self.rows:
            return None
        if y < 0 or y >= self.columns:
            return None
        return self.grid[x][y]

    def prepare_grid(self):
        return [[Cell(x, y) for x in range(self.rows)] for y in range(self.columns)]

    def configure_cells(self):
        for cell in self.each_cell():
            x, y = cell.x_index, cell.y_index
            cell.north = self[x, y - 1]
            # print("cell north of ", cell, " is ", cell.north)
            cell.south = self[x, y + 1]
            # print("cell south of ", cell, " is ", cell.south)
            cell.west = self[x - 1, y]
            # print("cell west of ", cell, " is ", cell.west)
            cell.east = self[x + 1, y]
            # print("cell east of ", cell, " is ", cell.east)

    def __str__(self):
        output = "+" + "---+" * self.columns + "\n"
        for row in self.each_row():
            top = "|"
            bottom = "+"
            for cell in row:
                body = "   "
                east_boundary = " " if cell.is_linked(cell.east) else "|"
                top += body + east_boundary
                south_boundary = "   " if cell.is_linked(cell.south) else "---"
                corner = "+"
                bottom += south_boundary + corner
            output += top + "\n"
            output += bottom + "\n"
        return output
