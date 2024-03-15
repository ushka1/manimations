# 1. Pokaż szachy.
# 1. Wielomian szachowy - definicja.
# 1. Wielomian szachowy - przykład:
#   - podświetlenie r_x i render wież na tablicy.


# pylint: disable=C0114, C0115, C0116

import manim as mn

# mn.config.disable_caching = True


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

    def forbid_squares(self, positions):
        for (row, col) in positions:
            i = row * self.cols + col
            if len(self.group) <= i:
                continue

            square = self.group[i]
            square.set_fill(mn.GREY, 1)

    def unforbid_squares(self, positions):
        for (row, col) in positions:
            i = row * self.cols + col
            if len(self.group) <= i:
                continue

            square = self.group[i]
            square.set_fill(opacity=0)

    def unforbid_all_squares(self):
        self.unforbid_squares([
            (row, col)
            for row in range(self.rows)
            for col in range(self.cols)
        ])

    def remove_rooks(self, positions):
        for (row, col) in positions:
            i = row * self.cols + col
            square = self.group[i]

            if len(square) > 1:
                circle = square[1]
                square.remove(circle)
                self.scene.remove(circle)

    def remove_all_rooks(self):
        self.remove_rooks([
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


class RookPolynomialI(mn.Scene):
    run_animations = False

    def construct(self):
        # ========== CONFIG ==========

        mn.Text.set_default(font="Roboto", font_size=16)

        # ========== SCENES ==========

        self.first_scene()
        # if self.run_animations:
        #     self.wait(2)
        #     self.play(mn.FadeOut(*self.mobjects))
        # self.remove(*self.mobjects)

    def first_scene(self):
        # ========== TITLE ==========

        title = mn.Text("Konfiguracje zabronione", font_size=24)
        title.to_edge(mn.UP)

        if self.run_animations:
            self.play(mn.FadeIn(title))
        else:
            self.add(title)

        # ========== FORMULA TEXT ==========

        text1 = mn.Text(
            "Załóżmy, że mamy n osób, o różnych kwalifikacjach, oraz m stanowisk, które muszą zostać obsadzone.",
            font_size=18
        )
        text2 = mn.Text(
            "Ile jest sposobów na obsadzenie stanowisk?",
            font_size=18
        )
        text1.next_to(title, mn.DOWN).shift(mn.DOWN * 0.5)
        text2.next_to(text1, mn.DOWN)

        if self.run_animations:
            self.play(mn.FadeIn(text1))
        else:
            self.add(text1, text2)

        # ========== HIGHLIGHT BALLS TEXT ==========

        board = Board(self, 8, 8)
        self.add(board.get_board())
        board.get_board().next_to(text2, direction=mn.DOWN,).shift(mn.DOWN * 0.5)

        board.forbid_squares([(0, 0), (0, 1), (1, 0), (1, 1)])

        board.place_rooks([(0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7)])

        board.swap_rows(0, 4)
        board.swap_cols(0, 4)

        board.place_rooks([(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5)])

        # if self.run_animations:
        #     for _ in range(3):
        #         self.play(formula[0][1].animate.set_color(mn.WHITE),
        #                   formula[0][7].animate.set_color(mn.WHITE),
        #                   text[34:52].animate.set_color(mn.WHITE),
        #                   run_time=0.2)
        #         self.play(formula[0][1].animate.set_color(mn.BLUE),
        #                   formula[0][7].animate.set_color(mn.BLUE),
        #                   text[34:52].animate.set_color(mn.BLUE),
        #                   run_time=0.2)
        # else:
        #     formula[0][1].set_color(mn.BLUE)
        #     formula[0][7].set_color(mn.BLUE)
        #     text[34:52].set_color(mn.BLUE)

        # # ========== BALLS ==========

        # balls = create_balls([mn.RED, mn.ORANGE, mn.YELLOW,
        #                       mn.GREEN, mn.BLUE, mn.PURPLE])
        # balls.next_to(text, direction=mn.DOWN,).shift(mn.DOWN * 0.5)

        # if self.run_animations:
        #     self.play(mn.FadeIn(balls))
        # else:
        #     self.add(balls)

        # # ========== HIGHLIGHT CYCLES TEXT ==========

        # if self.run_animations:
        #     for _ in range(3):
        #         self.play(formula[0][2].animate.set_color(mn.WHITE),
        #                   formula[0][9].animate.set_color(mn.WHITE),
        #                   text[53:78].animate.set_color(mn.WHITE),
        #                   run_time=0.2)
        #         self.play(formula[0][2].animate.set_color(mn.ORANGE),
        #                   formula[0][9].animate.set_color(mn.ORANGE),
        #                   text[53:78].animate.set_color(mn.ORANGE),
        #                   run_time=0.2)
        # else:
        #     formula[0][2].set_color(mn.ORANGE)
        #     formula[0][9].set_color(mn.ORANGE)
        #     text[53:78].set_color(mn.ORANGE)
