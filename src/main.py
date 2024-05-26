from grid import Grid
from binaryTree import BinaryTree
from sidewinder import Sidewinder
from display import displayGrid
import argparse


def main(model: str, rows: int, columns: int, sw_bias: float):
    grid = Grid(rows, columns)

    if model == "sidewinder":
        Sidewinder.on(grid, sw_bias)
    elif model == "binary_tree":
        BinaryTree.on(grid)
    else:
        raise ValueError(f"Unknown model: {model}")

    displayGrid(grid)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a maze")
    parser.add_argument("--rows", type=int, help="Number of rows in the maze", default=4)
    parser.add_argument("--columns", type=int, help="Number of columns in the maze", default=4)

    sub_parser = parser.add_subparsers(dest="algorithm", required=True)
    sub_parser.add_parser("binary_tree", help="Run binary tree algorithm")
    sidewinder = sub_parser.add_parser("sidewinder", help="Run sidewinder algorithm")
    sidewinder.add_argument("--bias", type=float, help="Bias for sidewinder algorithm", default=0.5)

    main(parser.parse_args().algorithm, parser.parse_args().rows, parser.parse_args().columns,
         parser.parse_args().bias if hasattr(parser.parse_args(), "bias") else 0.5)
