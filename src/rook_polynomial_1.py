# pylint: disable=C0114, C0115, C0116, C0301

import manim as mn

import utils.theme as theme
from utils.board import Board
from utils.rook_polynomials import get_available_rook_configs

theme.set_theme_defaults()

# ========== CONFIG ==========

ROWS = 3
COLS = 3
FORBIDDEN_POSITIONS = [
    (0, 1),
    (1, 0), (1, 2),
    (2, 0)
]


class RookPolynomial1(mn.Scene):
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

        title = mn.Text("Wielomiany szachowe", font_size=theme.FONT_LG)
        title.to_edge(mn.UP)

        if self.run_animations:
            self.play(mn.FadeIn(title))
        else:
            self.add(title)

        # ========== DEFINITION ==========

        tex1 = mn.Tex(
            "Wielomianem szachowym tablicy $B$ (o wymiarach $m \\times n$) nazywamy:",
            tex_template=theme.TEX_TEMPLATE,
        )
        tex1.next_to(title, mn.DOWN, buff=1)

        formula = mn.MathTex(
            "r_B(x) = 1 + {r_1}x + {r_2}x^2 + {r_3}x^3 + \\ldots" +
            "+ {r_{min\\{m,n\\}}}x^{min\\{m,n\\}}",
        )
        formula.next_to(tex1, mn.DOWN, buff=1)

        tex2 = mn.Tex(
            "$r_k$ to liczba możliwych ustawień $k$ wież na tablicy $B$ (na dozwolonych polach), " +
            "tak aby wzajemnie się nie atakowały.",
            tex_template=theme.TEX_TEMPLATE,
        )
        tex2.next_to(formula, mn.DOWN, buff=1)

        tex3 = mn.Tex(
            "$x^k$ to znacznik informujący o liczbie wież do rozstawienia, " +
            "gdzie $k$ to liczba wież.",
            tex_template=theme.TEX_TEMPLATE,
        )
        tex3.next_to(tex2, mn.DOWN, buff=0.5)

        if self.run_animations:
            self.play(
                mn.FadeIn(tex1),
            )
            self.play(
                mn.FadeIn(formula),
            )
            self.wait(3)
        else:
            self.add(
                tex1,
                formula,
            )

        # ========== HIGHLIGHT ==========

        if self.run_animations:
            self.play(mn.FadeIn(tex2))
            for _ in range(5):
                self.play(
                    formula[0][6:7].animate.set_color(mn.WHITE),
                    formula[0][8:10].animate.set_color(mn.WHITE),
                    formula[0][12:14].animate.set_color(mn.WHITE),
                    formula[0][17:19].animate.set_color(mn.WHITE),
                    formula[0][26:35].animate.set_color(mn.WHITE),
                    tex2.animate.set_color(mn.WHITE),
                    run_time=0.2
                )
                self.play(
                    formula[0][6:7].animate.set_color(mn.BLUE),
                    formula[0][8:10].animate.set_color(mn.BLUE),
                    formula[0][12:14].animate.set_color(mn.BLUE),
                    formula[0][17:19].animate.set_color(mn.BLUE),
                    formula[0][26:35].animate.set_color(mn.BLUE),
                    tex2.animate.set_color(mn.BLUE),
                    run_time=0.2
                )
        else:
            self.add(tex2)
            formula[0][6:7].set_color(mn.BLUE)
            formula[0][8:10].set_color(mn.BLUE)
            formula[0][12:14].set_color(mn.BLUE)
            formula[0][17:19].set_color(mn.BLUE)
            formula[0][26:35].set_color(mn.BLUE)
            tex2.set_color(mn.BLUE)

        if self.run_animations:
            self.wait(1)

        if self.run_animations:
            self.play(mn.FadeIn(tex3))
            for _ in range(5):
                self.play(
                    formula[0][10:11].animate.set_color(mn.WHITE),
                    formula[0][14:16].animate.set_color(mn.WHITE),
                    formula[0][19:21].animate.set_color(mn.WHITE),
                    formula[0][35:45].animate.set_color(mn.WHITE),
                    tex3.animate.set_color(mn.WHITE),
                    run_time=0.2
                )
                self.play(
                    formula[0][10:11].animate.set_color(mn.ORANGE),
                    formula[0][14:16].animate.set_color(mn.ORANGE),
                    formula[0][19:21].animate.set_color(mn.ORANGE),
                    formula[0][35:45].animate.set_color(mn.ORANGE),
                    tex3.animate.set_color(mn.ORANGE),
                    run_time=0.2
                )
        else:
            self.add(tex3)
            formula[0][10:11].set_color(mn.ORANGE)
            formula[0][14:16].set_color(mn.ORANGE)
            formula[0][19:21].set_color(mn.ORANGE)
            formula[0][35:45].set_color(mn.ORANGE)
            tex3.set_color(mn.ORANGE)

    def second_scene(self):
        # ========== TITLE ==========

        title = mn.Text(
            "Wielomian szachowy przykładowej tablicy B",
            font_size=theme.FONT_LG
        )
        title.to_edge(mn.UP)

        if self.run_animations:
            self.play(mn.FadeIn(title))
        else:
            self.add(title)

        # ========== BOARD ==========

        animations: list[mn.FadeIn | None] = []

        board = Board(self, ROWS, COLS)
        board.fill_squares(FORBIDDEN_POSITIONS, mn.GREY)
        board.get_board().scale(1.5).next_to(title, mn.DOWN, buff=1.5)
        animations.append(mn.FadeIn(board.get_board()))

        if self.run_animations:
            self.play(*animations)
        else:
            for a in animations:
                if a is not None:
                    self.add(a.mobject)

        # ========== FORMULA ==========

        def render_r(r: list[int], n: int):
            if r[n] == 0:
                return "{r_" + str(n + 1) + "}"
            else:
                return str(r[n])

        formula = mn.MathTex(
            "r_B(x) = 1 + {r_1}x + {r_2}x^2 + {r_3}x^3",
        )
        formula.next_to(board.get_board(), mn.DOWN, buff=1.5)

        if self.run_animations:
            self.play(mn.FadeIn(formula))
            self.wait(1)
        else:
            self.add(formula)

        r = [0, 0, 0]
        for rooks_count in range(1, min(ROWS, COLS) + 1):
            configs = get_available_rook_configs(
                ROWS, COLS, FORBIDDEN_POSITIONS, rooks_count
            )
            if configs is not None:
                for c in configs:
                    if self.run_animations:
                        remove_animations = board.remove_all_rooks_animations()
                        if len(remove_animations) > 0:
                            self.play(*remove_animations, run_time=0.25)

                        self.play(*board.place_rooks_animations(c),
                                  run_time=0.25)

                    r[rooks_count-1] += 1

                    if self.run_animations:
                        self.play(
                            formula.animate.become(mn.MathTex(
                                f"r_B(x) = 1 + {render_r(r,0)}x + {render_r(r,1)}x^2 + {render_r(r,2)}x^3",
                            ).next_to(board.get_board(), mn.DOWN, buff=1.5))
                        )

        if self.run_animations:
            self.wait(1)
            remove_animations = board.remove_all_rooks_animations()
            if len(remove_animations) > 0:
                self.play(*remove_animations, run_time=0.25)
        else:
            formula.become(
                mn.MathTex(
                    f"r_B(x) = 1 + {render_r(r,0)}x + {render_r(r,1)}x^2 + {render_r(r,2)}x^3",
                ).next_to(board.get_board(), mn.DOWN, buff=1.5)
            )
