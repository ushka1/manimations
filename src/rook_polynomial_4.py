# pylint: disable=C0114, C0115, C0116, C0301

import manim as mn

import utils.theme as theme
from utils.board import Board

theme.set_theme_defaults()


class RookPolynomial4(mn.Scene):
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
            "Wielomiany szachowe - usunięcie wiersza i kolumny",
            font_size=theme.FONT_LG
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
        board.place_symbol_rooks([(1, 0)], "s")

        board_label = mn.MathTex("B", font_size=theme.FONT_LG)
        board_label.next_to(board.get_board(), mn.DOWN, buff=0.5)

        if self.run_animations:
            self.play(
                mn.FadeIn(board.get_board()),
                mn.FadeIn(board_label),
            )
        else:
            self.add(board.get_board(), board_label)

        # ========== TEXT ==========

        formula = mn.MathTex(
            "r_B(x) = r_{B1}(x) + x \\cdot r_{B2}(x)",
        )
        formula.to_edge(mn.DOWN)

        tex1 = mn.Tex(
            "Niech $B$ będzie tablicą oraz $s$ pewnym jej polem dopuszczalnym. Dalej, " +
            "niech $B1$ oznacza tablicę otrzymaną z $B$, w której $s$ jest polem " +
            "zabronionym (pozostałe bez zmian), a $B2$ tablicę otrzymaną z $B$ przez " +
            "usunięcie wiersza i kolumny zawierających pole s. Wówczas:",
            tex_template=theme.TEX_TEMPLATE
        )
        tex1.next_to(formula, mn.UP)

        if self.run_animations:
            self.play(mn.FadeIn(tex1))
            self.play(mn.FadeIn(formula))
            self.wait(5)
        else:
            self.add(tex1, formula)

        # ========== HIGHLIGHT S ==========

        if self.run_animations:
            self.play(
                board.get_rook(1, 0).animate.set_color(mn.YELLOW),
                tex1[0][23].animate.set_color(mn.YELLOW),
                tex1[0][98].animate.set_color(mn.YELLOW),
                tex1[0][206].animate.set_color(mn.YELLOW),
            )
        else:
            board.get_rook(1, 0).set_color(mn.YELLOW)
            tex1[0][23].set_color(mn.YELLOW)
            tex1[0][98].set_color(mn.YELLOW)
            tex1[0][206].set_color(mn.YELLOW),

        if self.run_animations:
            for _ in range(3):
                self.play(
                    mn.Circumscribe(board.get_rook(1, 0)),
                    mn.Circumscribe(tex1[0][23]),
                    mn.Circumscribe(tex1[0][98]),
                    mn.Circumscribe(tex1[0][206]),
                )

        # ========== BOARD 1 ==========

        board_1 = Board(self, 3, 4)
        board_1.place_symbol_rooks([(1, 0)], "s")
        board_1.fill_squares(forbidden_squares, mn.GREY)
        board_1.get_rook(1, 0).set_color(mn.YELLOW)
        board_1.get_board().move_to(board.get_board())

        if self.run_animations:
            self.play(
                mn.FadeIn(board_1.get_board()),
                board_1.get_board().animate.next_to(
                    board.get_board(), mn.DOWN, buff=-0.5
                ).shift(3.5 * mn.LEFT)
            )
        else:
            board_1.get_board().next_to(
                board.get_board(), mn.DOWN, buff=-0.5
            ).shift(3.5 * mn.LEFT)
            self.add(board_1.get_board())

        # ========== BOARD 1 LABELS ==========

        board_1_label = mn.MathTex("B1", font_size=theme.FONT_LG)
        board_1_label.next_to(board_1.get_board(), mn.LEFT, buff=0.5)
        arrow_1 = mn.Arrow(
            board.get_board().get_left(),
            board_1.get_board().get_right(),
            stroke_width=5,
            buff=0.5
        )

        if self.run_animations:
            self.play(
                mn.FadeIn(arrow_1),
                mn.FadeIn(board_1_label),
            )
            self.wait(1)
        else:
            self.add(arrow_1, board_1_label)

        if self.run_animations:
            self.play(
                board_1_label.animate.set_color(color=mn.BLUE),
                tex1[0][63:65].animate.set_color(color=mn.BLUE),
                formula[0][6:12].animate.set_color(color=mn.BLUE),
                *board_1.fill_squares_animations([(1, 0)], mn.GRAY),
            )
            for _ in range(3):
                self.play(
                    mn.Circumscribe(board_1_label, color=mn.BLUE),
                    mn.Circumscribe(tex1[0][63:65], color=mn.BLUE),
                    mn.Circumscribe(formula[0][6:12], color=mn.BLUE),
                )
        else:
            board_1_label.set_color(color=mn.BLUE)
            tex1[0][63:65].set_color(color=mn.BLUE)
            formula[0][6:12].set_color(color=mn.BLUE)
            board_1.fill_squares([(1, 0)], mn.GRAY)

        # ========== MIDDLE WAIT ==========

        if self.run_animations:
            self.wait(1)

        # ========== BOARD 2 ==========

        board_2 = Board(self, 3, 4)
        board_2.place_symbol_rooks([(1, 0)], "s")
        board_2.fill_squares(forbidden_squares, mn.GREY)
        board_2.get_rook(1, 0).set_color(mn.YELLOW)
        board_2.get_board().move_to(board.get_board())

        if self.run_animations:
            self.play(
                mn.FadeIn(board_2.get_board()),
                board_2.get_board().animate.next_to(
                    board.get_board(), mn.DOWN, buff=-0.5
                ).shift(3.5 * mn.RIGHT)
            )
        else:
            board_2.get_board().next_to(
                board.get_board(), mn.DOWN, buff=-0.5
            ).shift(3.5 * mn.RIGHT)
            self.add(board_2.get_board())

        # ========== BOARD 2 LABELS ==========

        arrow_2 = mn.Arrow(
            board.get_board().get_right(),
            board_2.get_board().get_left(),
            stroke_width=5,
            buff=0.5
        )

        board_2_label = mn.MathTex("B2", font_size=theme.FONT_LG)
        board_2_label.next_to(board_2.get_board(), mn.RIGHT, buff=0.5)
        if self.run_animations:
            self.play(
                mn.FadeIn(board_2_label),
                mn.FadeIn(arrow_2)
            )
            self.wait(1)
        else:
            self.add(board_2_label, arrow_2)

        # ========== BOARD 2 ACTION ==========

        vert_line = mn.DashedLine(
            board_2.get_square_at(0).get_center() + 0.5 * mn.UP,
            board_2.get_square_at(8).get_center() + 0.5 * mn.DOWN,
            color=mn.PURE_RED,
            dash_length=0.25,
            dashed_ratio=0.75
        )
        vert_line.set_stroke(width=5)

        hor_line = mn.DashedLine(
            board_2.get_square_at(4).get_center() + 0.5 * mn.LEFT,
            board_2.get_square_at(7).get_center() + 0.5 * mn.RIGHT,
            color=mn.PURE_RED,
            dash_length=0.25,
            dashed_ratio=0.75
        )
        hor_line.set_stroke(width=5)

        if self.run_animations:
            self.play(
                board_2_label.animate.set_color(mn.ORANGE),
                tex1[0][140:142].animate.set_color(mn.ORANGE),
                formula[0][15:21].animate.set_color(mn.ORANGE),
                mn.Create(vert_line),
                mn.Create(hor_line),
            )
            for _ in range(3):
                self.play(
                    mn.Circumscribe(board_2_label, color=mn.ORANGE),
                    mn.Circumscribe(tex1[0][140:142], color=mn.ORANGE),
                    mn.Circumscribe(formula[0][15:21], color=mn.ORANGE),
                )
        else:
            self.add(vert_line, hor_line)
            board_2_label.set_color(mn.ORANGE)
            tex1[0][140:142].set_color(mn.ORANGE)
            formula[0][15:21].set_color(mn.ORANGE)
