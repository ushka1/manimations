# pylint: disable=C0114, C0115, C0116, C0301

import manim as mn


class Bucket():
    def __init__(self, rows: int, cols: int):
        self.rows = rows
        self.cols = cols

        width = cols
        height = rows
        points = [
            [-width / 2, height / 2, 0],
            [-width / 2, -height / 2, 0],
            [width / 2, -height / 2, 0],
            [width / 2, height / 2, 0],
            [width / 2, -height / 2, 0],
            [-width / 2, -height / 2, 0],
            [-width / 2, height / 2, 0],
        ]
        self.polygon = mn.Polygon(*points, color=mn.WHITE)  # type: ignore

    def get_bucket(self):
        return self.polygon

    def get_cell_coords(self, row: int, col: int):
        col_width = self.polygon.width / self.cols
        row_height = self.polygon.height / self.rows
        x = self.polygon.get_left()[0] + (col + 1/2) * col_width
        y = self.polygon.get_bottom()[1] + (row + 1/2) * row_height
        return (x, y, 0)
