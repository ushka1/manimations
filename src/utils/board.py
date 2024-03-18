# pylint: disable=C0114, C0115, C0116

import manim as mn


class Board():
    def __init__(self, scene: mn.Scene, rows: int, cols: int):
        self.scene = scene
        self.rows = rows
        self.cols = cols
        self.group = mn.VGroup()

        for _ in range(rows):
            for _ in range(cols):
                square = mn.Square()
                square.set_width(0.5)
                self.group.add(square)

        self.group.arrange_in_grid(rows, cols, buff=0)

    def get_board(self):
        return self.group

    def fill_squares(self, positions, color: mn.ManimColor, opacity=1):
        for (row, col) in positions:
            i = row * self.cols + col
            if len(self.group) <= i:
                continue

            square = self.group[i]
            square.set_fill(color, opacity)

    def fill_squares_animations(self, positions, color: mn.ManimColor, opacity=1):
        animations = []
        for (row, col) in positions:
            i = row * self.cols + col
            if len(self.group) <= i:
                continue

            square = self.group[i]
            animations.append(square.animate.set_fill(color, opacity))
        return animations

    def place_rooks(self, positions):
        for (row, col) in positions:
            i = row * self.cols + col
            if len(self.group) <= i:
                continue

            square = self.group[i]
            if len(square) > 1:
                continue

            rook = mn.Circle(radius=square.width / 3, color=mn.WHITE)
            rook.move_to(square)
            square.add(rook)

    def place_rooks_animations(self, positions):
        animations = []
        for (row, col) in positions:
            i = row * self.cols + col
            if len(self.group) <= i:
                continue

            square = self.group[i]
            if len(square) > 1:
                continue

            rook = mn.Circle(radius=square.width / 3, color=mn.WHITE)
            rook.move_to(square)
            square.add(rook)
            animations.append(mn.FadeIn(rook))
        return animations

    def remove_rooks(self, positions):
        for (row, col) in positions:
            i = row * self.cols + col
            square = self.group[i]

            if len(square) > 1:
                circle = square[1]
                square.remove(circle)
                self.scene.remove(circle)

    def remove_rooks_animations(self, positions):
        animations = []
        for (row, col) in positions:
            i = row * self.cols + col
            if len(self.group) <= i:
                continue

            square = self.group[i]
            if len(square) > 1:
                rook = square[1]
                square.remove(rook)
                animations.append(mn.FadeOut(rook))
        return animations

    def remove_all_rooks(self):
        self.remove_rooks([
            (row, col)
            for row in range(self.rows)
            for col in range(self.cols)
        ])

    def remove_all_rooks_animations(self):
        return self.remove_rooks_animations([
            (row, col)
            for row in range(self.rows)
            for col in range(self.cols)
        ])

    def swap_rows(self, i, j):
        row1 = self.group[i * self.cols:(i + 1) * self.cols]
        row2 = self.group[j * self.cols:(j + 1) * self.cols]

        self.group[i * self.cols:(i + 1) * self.cols] = row2
        self.group[j * self.cols:(j + 1) * self.cols] = row1

        self.group.arrange_in_grid(self.rows, self.cols, buff=0)

    def swap_cols(self, i, j):
        col1 = self.group[i::self.cols]
        col2 = self.group[j::self.cols]

        self.group[i::self.cols] = col2
        self.group[j::self.cols] = col1

        self.group.arrange_in_grid(self.rows, self.cols, buff=0)

    def split_on_y_axis(self, y):
        group1 = mn.VGroup()
        group2 = mn.VGroup()
        for (i, square) in enumerate(self.group):
            if i % self.cols < y:
                group1.add(square.copy())
            else:
                group2.add(square.copy())

        board1 = Board(self.scene, self.rows, y)
        board1.group = group1
        board2 = Board(self.scene, self.rows, self.cols - y)
        board2.group = group2

        self.group.remove(*self.group)
        self.scene.remove(self.group)
        self.scene.add(board1.get_board(), board2.get_board())
        return (board1, board2)

    def split_on_x_axis(self, x):
        group1 = mn.VGroup()
        group2 = mn.VGroup()
        for (i, square) in enumerate(self.group):
            if i // self.cols < x:
                group1.add(square.copy())
            else:
                group2.add(square.copy())

        board1 = Board(self.scene, x, self.cols)
        board1.group = group1
        board2 = Board(self.scene, self.rows - x, self.cols)
        board2.group = group2

        self.group.remove(*self.group)
        self.scene.remove(self.group)
        self.scene.add(board1.get_board(), board2.get_board())
        return (board1, board2)

    def get_square_at(self, i):
        return self.group[i]
