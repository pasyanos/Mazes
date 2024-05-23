from grid import Grid
from mazeRecipe import MazeRecipe
from binaryTree import BinaryTree
import argparse


def main(rows: int, columns: int):
    grid = Grid(rows, columns)
    BinaryTree.on(grid)
    print(grid)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a maze")
    parser.add_argument("--rows", type=int, help="Number of rows in the maze", default=4)
    parser.add_argument("--columns", type=int, help="Number of columns in the maze", default=4)
    main(parser.parse_args().rows, parser.parse_args().columns)
