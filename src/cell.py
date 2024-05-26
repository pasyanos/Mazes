# A single cell of a grid. Each cell can have a north, south, east, and west neighbor.
class Cell:
    def __init__(self, x_index, y_index):
        self.x_index = x_index
        self.y_index = y_index
        self.north = None
        self.south = None
        self.east = None
        self.west = None
        self.links = {}

    # Link this cell to another cell.
    # If bidirectional is True, link the other cell back to this one.
    def link(self, cell, bidirectional: bool = True):
        self.links[cell] = True
        if bidirectional:
            cell.link(self, False)

    # Unlink this cell from another cell.
    # If bidirectional is True, unlink the other cell from this one as well
    def unlink(self, cell, bidirectional: bool = True):
        self.links.pop(cell)
        if bidirectional:
            cell.unlink(self, False)

    # Return a list of all cells linked to this one
    def links(self):
        return list(self.links.keys())

    # Check if another cell is linked to this one
    def is_linked(self, cell) -> bool:
        return cell in self.links

    # Return a list of all neighbors of this cell (whether or not they are linked)
    def neighbors(self):
        neighbors = []
        if self.north:
            neighbors.append(self.north)
        if self.south:
            neighbors.append(self.south)
        if self.east:
            neighbors.append(self.east)
        if self.west:
            neighbors.append(self.west)
            
        return neighbors

    # String representation of the cell, for debugging
    def __str__(self):
        return f"({self.x_index}, {self.y_index})"
