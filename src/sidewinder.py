from mazeRecipe import MazeRecipe
import random


class Sidewinder(MazeRecipe):
    @staticmethod
    def on(maze, horizontal_bias=0.5):
        for row in maze.each_row():
            run = []
            for cell in row:
                run.append(cell)

                at_eastern_boundary = cell.east is None
                at_northern_boundary = cell.north is None

                should_close_out = at_eastern_boundary or (not at_northern_boundary
                                                           and random.random() > horizontal_bias)

                if should_close_out:
                    member = random.choice(run)
                    if member.north:
                        member.link(member.north)
                    run.clear()
                else:
                    cell.link(cell.east)
        return maze
