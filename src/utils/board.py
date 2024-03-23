# pylint: disable=C0114, C0115, C0116

import manim as mn


class Board():
    def __init__(self, scene: mn.Scene, rows: int, cols: int):
        self.scene = scene
        self.rows = rows
        self.cols = cols
        self.group = mn.VGroup()
        self.x_labels = mn.VGroup()
        self.y_labels = mn.VGroup()

        for _ in range(rows):
            for _ in range(cols):
                square = mn.Square()
                square.set_width(0.5)
                self.group.add(square)

        self.group.arrange_in_grid(rows, cols, buff=0)

    def get_board(self):
        return self.group

    def set_y_labels(self, labels):
        texts = []
        for (i, label) in enumerate(labels):
            texts.append(mn.Text(label))

        max_width = max([text.get_width() for text in texts])
        for (i, text) in enumerate(texts):
            container = mn.Rectangle(height=0.5, width=max_width)
            container.add(text.align_to(container, mn.RIGHT))
            container.set_stroke(width=0)
            self.y_labels.add(container)
            self.y_labels[i].next_to(self.group[i * self.cols], mn.LEFT)

    def get_y_labels(self):
        return self.y_labels

    def set_x_labels(self, labels):
        texts = []
        for (i, label) in enumerate(labels):
            texts.append(mn.Text(label))

        max_width = max([text.get_width() for text in texts])
        for (i, text) in enumerate(texts):
            container = mn.Rectangle(height=0.5, width=max_width)
            container.add(text.align_to(container, mn.RIGHT))
            container.set_stroke(width=0)
            container.rotate(-mn.PI / 2)
            self.x_labels.add(container)
            self.x_labels[i].next_to(self.group[i], mn.UP)

    def get_x_labels(self):
        return self.x_labels

    def outline_squares(self, color: mn.ManimColor, opacity=1):
        for square in self.group:
            square.set_stroke(color, opacity=opacity)

    def outline_squares_animations(self, color: mn.ManimColor, opacity=1):
        animations = []
        for square in self.group:
            animations.append(
                square.animate.set_stroke(color, opacity=opacity))
        return animations

    def fill_squares(self, positions, color: mn.ManimColor, opacity=1):
        for (row, col) in positions:
            i = row * self.cols + col
            if len(self.group) <= i:
                continue

            square = self.group[i]
            rook_color = None
            if len(square) > 1:
                rook_color = square[1].get_fill_color()

            square.set_fill(color, opacity)
            if rook_color is not None:
                square[1].set_fill(rook_color)

    def fill_squares_animations(self, positions, color: mn.ManimColor, opacity=1):
        animations = []
        for (row, col) in positions:
            i = row * self.cols + col
            if len(self.group) <= i:
                continue

            square = self.group[i]
            rook_color = None
            if len(square) > 1:
                rook_color = square[1].get_fill_color()

            animations.append(square.animate.set_fill(color, opacity))
            if rook_color is not None:
                animations.append(square[1].animate.set_fill(rook_color))

        return animations

    def get_rook(self, row, col):
        i = row * self.cols + col
        if len(self.group) <= i:
            return None

        square = self.group[i]
        if len(square) <= 1:
            return None

        return square[1]

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

    def place_symbol_rooks(self, positions, symbol):
        for (row, col) in positions:
            i = row * self.cols + col
            if len(self.group) <= i:
                continue

            square = self.group[i]
            if len(square) > 1:
                continue

            text = mn.Text(symbol)
            text.move_to(square)
            square.add(text)

    def place_symbol_rooks_animations(self, positions, symbol):
        animations = []
        for (row, col) in positions:
            i = row * self.cols + col
            if len(self.group) <= i:
                continue

            square = self.group[i]
            if len(square) > 1:
                continue

            text = mn.Text(symbol)
            text.move_to(square)
            square.add(text)
            animations.append(mn.FadeIn(text))
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
        self.group[i * self.cols:(i + 1) * self.cols] = row2  # type: ignore
        self.group[j * self.cols:(j + 1) * self.cols] = row1  # type: ignore

        label1 = self.y_labels[i]
        label2 = self.y_labels[j]
        self.y_labels[i] = label2  # type: ignore
        self.y_labels[j] = label1  # type: ignore

        self.group.arrange_in_grid(self.rows, self.cols, buff=0)
        label1.next_to(row1, mn.LEFT)
        label2.next_to(row2, mn.LEFT)

    def swap_rows_animations(self, i, j):
        row1 = self.group[i * self.cols:(i + 1) * self.cols]
        row2 = self.group[j * self.cols:(j + 1) * self.cols]
        self.group[i * self.cols:(i + 1) * self.cols] = row2  # type: ignore
        self.group[j * self.cols:(j + 1) * self.cols] = row1  # type: ignore

        label1 = self.y_labels[i]
        label2 = self.y_labels[j]
        self.y_labels[i] = label2  # type: ignore
        self.y_labels[j] = label1  # type: ignore

        group1 = mn.VGroup(*row1, label1)
        group2 = mn.VGroup(*row2, label2)
        return [
            mn.Swap(group1, group2),
        ]

    def swap_cols(self, i, j):
        col1 = self.group[i::self.cols]
        col2 = self.group[j::self.cols]
        self.group[i::self.cols] = col2  # type: ignore
        self.group[j::self.cols] = col1  # type: ignore

        label1 = self.x_labels[i]
        label2 = self.x_labels[j]
        self.x_labels[i] = label2  # type: ignore
        self.x_labels[j] = label1  # type: ignore

        self.group.arrange_in_grid(self.rows, self.cols, buff=0)
        label1.next_to(col1, mn.UP)
        label2.next_to(col2, mn.UP)

    def swap_cols_animations(self, i, j):
        col1 = self.group[i::self.cols]
        col2 = self.group[j::self.cols]
        self.group[i::self.cols] = col2  # type: ignore
        self.group[j::self.cols] = col1  # type: ignore

        label1 = self.x_labels[i]
        label2 = self.x_labels[j]
        self.x_labels[i] = label2  # type: ignore
        self.x_labels[j] = label1  # type: ignore

        group1 = mn.VGroup(*col1, label1)
        group2 = mn.VGroup(*col2, label2)
        return [
            mn.Swap(group1, group2),
        ]

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
