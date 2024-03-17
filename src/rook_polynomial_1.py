# 1. Pokaż szachy.
# 1. Wielomian szachowy - definicja.
# 1. Wielomian szachowy - przykład:
#   - podświetlenie r_x i render wież na tablicy.


# pylint: disable=C0114, C0115, C0116

import manim as mn

from utils.board import Board

# mn.config.disable_caching = True


class RookPolynomial1(mn.Scene):
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
