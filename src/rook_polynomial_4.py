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

        board.fill_squares(forbidden_squares, mn.GREY)
        board.get_board().next_to(title, mn.DOWN, buff=1)

        if self.run_animations:
            self.play(mn.FadeIn(board.get_board()))
        else:
            self.add(board.get_board())

        # ========== PREPARE BOARD B1 ==========

        board_1 = Board(self, 3, 4)
        forbidden_squares = [
            (0, 0), (0, 2),
            (1, 1), (1, 2),
            (2, 0), (2, 3),
        ]

        board_1.fill_squares(forbidden_squares, mn.GREY)
        board_1.get_board().next_to(board.get_board(), mn.DOWN,
                                    buff=-0.5).shift(3.5 * mn.LEFT)

        # ========== PREPARE BOARD B2 ==========

        board_2 = Board(self, 3, 4)
        forbidden_squares = [
            (0, 0), (0, 2),
            (1, 1), (1, 2),
            (2, 0), (2, 3),
        ]

        board_2.fill_squares(forbidden_squares, mn.GREY)
        board_2.get_board().next_to(board.get_board(), mn.DOWN,
                                    buff=-0.5).shift(3.5 * mn.RIGHT)

        # ========== TEXT ==========

        formula = mn.MathTex(
            "r_B(x) = r_{B1}(x) + x \\cdot r_{B2}(x)",
        )
        formula.to_edge(mn.DOWN)

        tex1 = mn.Tex(
            "Niech B bedzie tablica oraz s pewnym jej pole dopuszczalnym. Dalej, " +
            "niech B1 oznacza tablice otrzymana z B, w której s jest polem " +
            "zabronionym (pozostałe bez zmian), a B2 tablice otrzymana z B przez " +
            "usuniecie wiersza i kolumny zawierajacych pole s. Wówczas:"
        )
        tex1.next_to(formula, mn.UP)

        if self.run_animations:
            self.play(mn.FadeIn(tex1))
            self.play(mn.FadeIn(formula))
            self.wait(5)
        else:
            self.add(tex1, formula)

        # ========== HIGHLIGHT ==========

        if self.run_animations:
            pass
        else:
            formula[0][6:12].set_color(mn.BLUE)
            formula[0][13:19].set_color(mn.ORANGE)

        if self.run_animations:
            self.play(mn.FadeIn(board_1.get_board()))
        else:
            self.add(board_1.get_board())

        if self.run_animations:
            self.play(mn.FadeIn(board_2.get_board()))
        else:
            self.add(board_2.get_board())
