# A single cell in a grid
class Cell:
    def __init__(self, x_index, y_index):
        self.x_index = x_index
        self.y_index = y_index
        self.north = None
        self.south = None
        self.east = None
        self.west = None
        self.links = {}

    def link(self, cell, bidirectional: bool = True):
        self.links[cell] = True
        if bidirectional:
            cell.link(self, False)

    def unlink(self, cell, bidirectional: bool = True):
        self.links.pop(cell)
        if bidirectional:
            cell.unlink(self, False)

    def links(self):
        return list(self.links.keys())

    def is_linked(self, cell) -> bool:
        return cell in self.links

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

    def __str__(self):
        return f"({self.x_index}, {self.y_index})"
