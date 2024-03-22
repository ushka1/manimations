# pylint: disable=C0114, C0115, C0116, C0301

import manim as mn

from utils.board import Board

# mn.config.disable_caching = True
mn.Text.set_default(font="Ubuntu", font_size=18)
mn.Tex.set_default(font_size=32)
mn.MathTex.set_default(font_size=40)


class RookPolynomial3(mn.Scene):
    run_animations = True

    def construct(self):
        # ========== SCENES ==========

        self.first_scene()
        if self.run_animations:
            self.wait(5)
            self.play(mn.FadeOut(*self.mobjects))
        self.remove(*self.mobjects)

        self.second_scene()
        if self.run_animations:
            self.wait(5)
            self.play(mn.FadeOut(*self.mobjects))
        self.remove(*self.mobjects)

    def first_scene(self):
        # ========== TITLE ==========

        title = mn.Text(
            "Wielomiany szachowe - tablice rozłączne", font_size=32)
        title.to_edge(mn.UP)

        if self.run_animations:
            self.play(mn.FadeIn(title))
        else:
            self.add(title)

        # ========== BOARD ==========

        board = Board(self, 4, 4)
        forbidden_squares = [
            (0, 0), (0, 2), (0, 3),
            (1, 2), (1, 3),
            (2, 0), (2, 1),
            (3, 0), (3, 1), (3, 3),
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
            "Załóżmy, że tablica $B$ składa sie z dwóch \"rozłacznych\" tablic $B1$ i $B2$ " +
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

    def second_scene(self):
        # ========== TITLE ==========

        title = mn.Text(
            "Wielomian szachowy przykładowej tablicy B",
            font_size=32
        )
        title.to_edge(mn.UP)

        if self.run_animations:
            self.play(mn.FadeIn(title))
        else:
            self.add(title)

        # ========== BOARD ==========

        board = Board(self, 5, 5)
        forbidden_squares = [
            (0, 0), (0, 1), (0, 3),
            (1, 0), (1, 1),
            (2, 0), (2, 2), (2, 3), (2, 4),
            (3, 2), (3, 3), (3, 4),
            (4, 1), (4, 2), (4, 3), (4, 4),
        ]

        board.get_board().scale(1.25)
        board.fill_squares(forbidden_squares, mn.GREY)

        if self.run_animations:
            self.play(mn.FadeIn(board.get_board()))
            self.wait(1)
        else:
            self.add(board.get_board())

        # ========== SPLITTING ==========

        left, right = board.split_on_y_axis(2)
        left_top, left_bottom = left.split_on_x_axis(2)
        right_top, right_bottom = right.split_on_x_axis(2)

        if self.run_animations:
            self.play(
                *left_bottom.outline_squares_animations(mn.BLUE),
                *right_top.outline_squares_animations(mn.ORANGE),
            )
            self.wait(1)
            self.play(
                left_top.get_board().animate.shift(0.5 * mn.LEFT + 0.5 * mn.UP),
                left_bottom.get_board().animate.shift(0.5 * mn.LEFT + 0.5 * mn.DOWN),
                right_top.get_board().animate.shift(0.5 * mn.RIGHT + 0.5 * mn.UP),
                right_bottom.get_board().animate.shift(0.5 * mn.RIGHT + 0.5 * mn.DOWN)
            )
        else:
            left_bottom.outline_squares(mn.BLUE)
            right_top.outline_squares(mn.ORANGE)
            left_top.get_board().shift(0.5 * mn.LEFT + 0.5 * mn.UP)
            left_bottom.get_board().shift(0.5 * mn.LEFT + 0.5 * mn.DOWN)
            right_top.get_board().shift(0.5 * mn.RIGHT + 0.5 * mn.UP)
            right_bottom.get_board().shift(0.5 * mn.RIGHT + 0.5 * mn.DOWN)

        # ========== FORMULAS ==========

        formula_b1 = mn.MathTex(
            "r_{B1}(x) = 1 + 4x + 3x^2",
            font_size=36
        )
        formula_b1.set_color(mn.BLUE)
        formula_b1.next_to(left_bottom.get_board(), mn.LEFT, buff=0.5)

        formula_b2 = mn.MathTex(
            "r_{B2}(x) = 1 + 5x + 4x^2",
            font_size=36
        )
        formula_b2.set_color(mn.ORANGE)
        formula_b2.next_to(right_top.get_board(), mn.RIGHT, buff=0.5)

        if self.run_animations:
            self.play(mn.FadeIn(formula_b1), mn.FadeIn(formula_b2))
            self.wait(1)
        else:
            self.add(formula_b1, formula_b2)

        # ========== RESULT FORMULA ==========

        formula_result = mn.MathTex(
            "r_B(x) = r_{B1}(x) \\cdot r_{B2}(x) = 1 + 9x + 27x^2 + 31x^3 + 12x^4",
            font_size=40
        )
        formula_result.to_edge(mn.DOWN)
        formula_result[0][6:12].set_color(mn.BLUE)
        formula_result[0][13:19].set_color(mn.ORANGE)

        if self.run_animations:
            self.play(mn.FadeIn(formula_result))
        else:
            self.add(formula_result)
