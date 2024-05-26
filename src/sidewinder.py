from mazeRecipe import MazeRecipe
import random


# Implementation of the sidewinder algorithm for generating mazes.
class Sidewinder(MazeRecipe):
    @staticmethod
    def on(maze, horizontal_bias=0.5):
        for row in maze.each_row():
            # a run is a sequence of horizontally linked cells (it can be a single cell)
            run = []
            for cell in row:
                # add the current cell
                run.append(cell)

                # check if we are at the eastern or northern boundary, which are special cases
                at_eastern_boundary = cell.east is None
                at_northern_boundary = cell.north is None

                # close out the run if we are at the eastern boundary,
                # or by random choice (with bias) if we are NOT at the northern boundary
                should_close_out = at_eastern_boundary or (not at_northern_boundary
                                                           and random.random() > horizontal_bias)

                # if we are closing out the run, link a random cell from the run
                # to its northern neighbor
                if should_close_out:
                    member = random.choice(run)
                    if member.north:
                        member.link(member.north)
                    run.clear()
                # otherwise, link it to the east and continue with the same run
                else:
                    cell.link(cell.east)
        return maze
