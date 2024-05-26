from PIL import Image, ImageDraw


PADDING_PX = 20
CELL_SIZE = 15
LINE_WIDTH = 2


def displayGrid(grid):
    # print(grid)

    width = grid.columns * CELL_SIZE + PADDING_PX * 2
    height = grid.rows * CELL_SIZE + PADDING_PX * 2
    img = Image.new("RGB", (width, height), "white")

    draw = ImageDraw.Draw(img)

    for cell in grid.each_cell():
        x1 = cell.x_index * CELL_SIZE + PADDING_PX
        y1 = cell.y_index * CELL_SIZE + PADDING_PX
        x2 = (cell.x_index + 1) * CELL_SIZE + PADDING_PX
        y2 = (cell.y_index + 1) * CELL_SIZE + PADDING_PX

        if not cell.north:
            draw.line([(x1, y1), (x2 + LINE_WIDTH//2, y1)], width=LINE_WIDTH, fill="black")
        if not cell.west:
            draw.line([(x1, y1), (x1, y2)], width=LINE_WIDTH, fill="black")
        if not cell.is_linked(cell.east):
            draw.line([(x2, y1), (x2, y2 + LINE_WIDTH//2)], width=LINE_WIDTH, fill="black")
        if not cell.is_linked(cell.south):
            draw.line([(x1, y2), (x2, y2)], width=LINE_WIDTH, fill="black")

    img.show()

