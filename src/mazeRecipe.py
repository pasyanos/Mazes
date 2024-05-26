from src import grid


# A class for generating mazes. Each algorithm should implement this class,
# and override the static on method.
# This class does nothing to the grid, but extensions of this class should modify it
# and create a maze.
class MazeRecipe:
    @staticmethod
    def on(maze: grid.Grid):
        pass
