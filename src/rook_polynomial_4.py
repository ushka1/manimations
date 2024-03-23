# pylint: disable=C0114, C0115, C0116, C0301

import manim as mn

import utils.constants as consts
from utils.board import Board

consts.set_defaults()


class RookPolynomial4(mn.Scene):
    run_animations = False

    def construct(self):
        # ========== SCENES ==========

        self.first_scene()
        # if self.run_animations:
        #     self.wait(5)
        #     self.play(mn.FadeOut(*self.mobjects))
        # self.remove(*self.mobjects)

    def first_scene(self):
        # ========== TITLE ==========

        title = mn.Text(
            "Wielomiany szachowe - usunięcie wiersza i kolumny",
            font_size=consts.FONT_LG
        )
        title.to_edge(mn.UP)

        if self.run_animations:
            self.play(mn.FadeIn(title))
        else:
            self.add(title)

        # ========== BOARD ==========

        board = Board(self, 3, 4)
        forbidden_squares = [
            (0, 0), (0, 2),
            (1, 1), (1, 2),
            (2, 0), (2, 3),
        ]
        board.get_board().scale(1.25)

        board.fill_squares(forbidden_squares, mn.GREY)
        board.get_board().next_to(title, mn.DOWN, buff=1)

        if self.run_animations:
            self.play(mn.FadeIn(board.get_board()))
        else:
            self.add(board.get_board())

        # ========== TEXT ==========

        tex1 = mn.Tex(
            "Załóżmy, że tablica $B$ składa sie z dwóch \"rozłącznych\" tablic $B1$ i $B2$ " +
            "(tzn. o rozłacznych wierszach i kolumnach), a poza tym wyłacznie z pól " +
            "zabronionych. Wówczas:"
        )
        tex1.next_to(board.get_board(), mn.DOWN, buff=1)

        if self.run_animations:
            self.play(mn.FadeIn(tex1))
        else:
            self.add(tex1)

        formula = mn.MathTex(
            "r_B(x) = r_{B1}(x) \\cdot r_{B2}(x)",
        )
        formula.next_to(tex1, mn.DOWN, buff=0.5)

        if self.run_animations:
            self.play(mn.FadeIn(formula))
            self.wait(5)
        else:
            self.add(formula)

        # ========== HIGHLIGHT ==========

        left, right = board.split_on_y_axis(2)
        left_top, _ = left.split_on_x_axis(2)
        _, right_bottom = right.split_on_x_axis(2)

        label_b1 = mn.Tex("$B1$")
        label_b2 = mn.Tex("$B2$")
        label_b1.next_to(left_top.get_board(), mn.LEFT, buff=0.5)
        label_b2.next_to(right_bottom.get_board(), mn.RIGHT, buff=0.5)

        if self.run_animations:
            self.play(mn.FadeIn(label_b1))
            for _ in range(5):
                self.play(
                    *left_top.outline_squares_animations(mn.WHITE),
                    formula[0][6:12].animate.set_color(mn.WHITE),
                    label_b1.animate.set_color(mn.WHITE),
                    tex1[0][59:61].animate.set_color(mn.WHITE),
                    run_time=0.2
                )
                self.play(
                    *left_top.outline_squares_animations(mn.BLUE),
                    formula[0][6:12].animate.set_color(mn.BLUE),
                    label_b1.animate.set_color(mn.BLUE),
                    tex1[0][59:61].animate.set_color(mn.BLUE),
                    run_time=0.2
                )
            self.wait(1)
            self.play(mn.FadeIn(label_b2))
            for _ in range(5):
                self.play(
                    *right_bottom.outline_squares_animations(mn.WHITE),
                    formula[0][13:19].animate.set_color(mn.WHITE),
                    label_b2.animate.set_color(mn.WHITE),
                    tex1[0][62:64].animate.set_color(mn.WHITE),
                    run_time=0.2
                )
                self.play(
                    *right_bottom.outline_squares_animations(mn.ORANGE),
                    formula[0][13:19].animate.set_color(mn.ORANGE),
                    label_b2.animate.set_color(mn.ORANGE),
                    tex1[0][62:64].animate.set_color(mn.ORANGE),
                    run_time=0.2
                )
        else:
            self.add(label_b1, label_b2)

            left_top.outline_squares(mn.BLUE)
            formula[0][6:12].set_color(mn.BLUE)
            label_b1.set_color(mn.BLUE)
            tex1[0][59:61].set_color(mn.BLUE)

            right_bottom.outline_squares(mn.ORANGE)
            formula[0][13:19].set_color(mn.ORANGE)
            label_b2.set_color(mn.ORANGE)
            tex1[0][62:64].set_color(mn.ORANGE)
