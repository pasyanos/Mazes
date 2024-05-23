from grid import Grid
from mazeRecipe import MazeRecipe
from binaryTree import BinaryTree


def main():
    grid = Grid(5, 5)
    BinaryTree.on(grid)
    print(grid)


if __name__ == "__main__":
    main()
