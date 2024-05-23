from mazeRecipe import MazeRecipe
import random


class BinaryTree(MazeRecipe):
    @staticmethod
    def on(maze):
        for cell in maze.each_cell():
            # print("cell is ", cell)
            neighbors = []
            if cell.south:
                neighbors.append(cell.south)
            if cell.east:
                neighbors.append(cell.east)

            if neighbors:
                index = random.randint(0, len(neighbors) - 1)
                neighbor = neighbors[index]
                # print("choosing neighbor ", neighbor)
                cell.link(neighbor)
