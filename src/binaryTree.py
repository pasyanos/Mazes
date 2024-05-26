from mazeRecipe import MazeRecipe
import random


# Implementation of the binary tree algorithm for generating mazes.
class BinaryTree(MazeRecipe):
    @staticmethod
    def on(maze):
        for cell in maze.each_cell():
            # get the north and east neighbors of the cell, if they exist
            neighbors = []
            if cell.north:
                neighbors.append(cell.north)
            if cell.east:
                neighbors.append(cell.east)

            # randomly choose from the existing neighbors and link the cell to it
            if neighbors:
                index = random.randint(0, len(neighbors) - 1)
                neighbor = neighbors[index]

                cell.link(neighbor)
