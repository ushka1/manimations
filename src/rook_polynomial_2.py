# pylint: disable=C0114, C0115, C0116, C0301

import manim as mn

import utils.constants as consts
from utils.board import Board

consts.set_defaults()


class RookPolynomial2(mn.Scene):
    run_animations = True

    def construct(self):
        # ========== SCENES ==========

        self.first_scene()
        if self.run_animations:
            self.wait(5)
            self.play(mn.FadeOut(*self.mobjects))
        self.remove(*self.mobjects)

    def first_scene(self):
        # ========== TITLE ==========

        title = mn.Text(
            "Wielomiany szachowe - zamiana kolumn i wierszy",
            font_size=consts.FONT_LG
        )
        title.to_edge(mn.UP)

        if self.run_animations:
            self.play(mn.FadeIn(title))
        else:
            self.add(title)

        # ========== TEXT ==========

        text1 = mn.Text(
            "W wielomianach szachowych, kolejność wierszy i kolumn można zmieniać bez wpływu na wynik końcowy.")
        text1.next_to(title, mn.DOWN, buff=0.5)

        if self.run_animations:
            self.play(mn.FadeIn(text1))
        else:
            self.add(text1)

        # ========== BOARD ==========

        animations: list[mn.FadeIn | None] = []

        board = Board(self, 5, 4)
        board.get_board().next_to(text1, mn.DOWN, buff=1).shift(mn.DOWN * 1.5)
        board.fill_squares([
            (0, 1), (0, 2),
            (1, 0), (1, 3),
            (2, 1),
            (3, 0), (3, 2),
            (4, 1),
        ],
            mn.GREY
        )
        board.get_board().scale(1.25)

        if self.run_animations:
            animations.append(mn.FadeIn(board.get_board()))
        else:
            self.add(board.get_board())

        y_labels = ["Ann", "Ed", "Joe", "Leo", "Sue"]
        board.set_y_labels(y_labels)
        if self.run_animations:
            animations.append(mn.FadeIn(board.get_y_labels()))
        else:
            self.add(board.get_y_labels())

        x_labels = ["Frontend", "Backend", "Testing", "AI"]
        board.set_x_labels(x_labels)
        if self.run_animations:
            animations.append(mn.FadeIn(board.get_x_labels()))
        else:
            self.add(board.get_x_labels())

        if self.run_animations:
            self.play(*animations)
            self.wait(5)

        # ========== SWAPPING ==========

        if self.run_animations:
            self.play(*board.swap_cols_animations(0, 2))
            self.wait(1)
            self.play(*board.swap_rows_animations(1, 4))
            self.wait(1)
            self.play(*board.swap_cols_animations(0, 1))
            self.wait(1)
            self.play(*board.swap_rows_animations(0, 2))
        else:
            board.swap_cols(0, 2)
            board.swap_rows(1, 4)
            board.swap_cols(0, 1)
            board.swap_rows(0, 2)
