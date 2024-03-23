# pylint: disable=C0114, C0115, C0116, C0301


import math

import manim as mn


class Cycle():
    """
    A class to visually represent a cycle.
    """

    def __init__(self, r: int):
        self.circle = mn.Circle(radius=r, color=mn.WHITE)

    def get_cycle(self):
        return self.circle

    def get_cell_coords(self, n: int):
        x, y, _ = self.circle.get_center()
        cells = []
        angle = 2 * mn.PI / n

        for i in range(n):
            dx = self.circle.width / 2 * math.cos(i * angle)
            dy = self.circle.width / 2 * math.sin(i * angle)
            cells.append((round(x + dx, 2), round(y + dy, 2), 0))

        return cells
