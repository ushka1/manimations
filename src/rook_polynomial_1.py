# pylint: disable=C0114, C0115, C0116, C0301

import manim as mn

from utils.board import Board

# mn.config.disable_caching = True


def get_available_configurations(
        m: int,
        n: int,
        forbidden_squares: list[tuple[int, int]],
        size: int,
):
    return get_available_configurations_helper(
        0,
        0,
        m,
        n,
        forbidden_squares,
        [],
        [],
        size,
    )


def get_available_configurations_helper(
        i: int,
        j: int,
        m: int,
        n: int,
        forbidden_squares: list[tuple[int, int]],
        reserved_rows: list[int],
        reserved_cols: list[int],
        size: int,
) -> list[list[tuple[int, int]]] | None:
    # configuration of given size found
    if size == 0:
        return []

    # configuration of given size cannot be found
    if i >= m:
        return None

    next_i = i
    next_j = (j + 1) % n
    if next_j == 0:
        next_i += 1

    # skip forbidden squares and reserved rows and columns
    if i in reserved_rows or j in reserved_cols or (i, j) in forbidden_squares:
        return get_available_configurations_helper(
            next_i,
            next_j,
            m,
            n,
            forbidden_squares,
            reserved_rows,
            reserved_cols,
            size,
        )

    res = []

    # include current square
    if size == 1:
        res = [[(i, j)]]
    else:
        included = get_available_configurations_helper(
            next_i,
            next_j,
            m,
            n,
            forbidden_squares,
            reserved_rows + [i],
            reserved_cols + [j],
            size - 1,
        )

        if included is not None:
            for conf in included:
                res.append([(i, j)] + conf)

    # exclude current square
    excluded = get_available_configurations_helper(
        next_i,
        next_j,
        m,
        n,
        forbidden_squares,
        reserved_rows,
        reserved_cols,
        size,
    )

    if excluded is not None:
        res += excluded

    return res


class RookPolynomial1(mn.Scene):
    run_animations = False

    def construct(self):
        # ========== CONFIG ==========

        mn.Text.set_default(font="Roboto", font_size=16)
        mn.Tex.set_default(font_size=32)

        # ========== SCENES ==========

        # self.first_scene()
        # if self.run_animations:
        #     self.wait(5)
        #     self.play(mn.FadeOut(*self.mobjects))
        # self.remove(*self.mobjects)

        self.second_scene()
        if self.run_animations:
            self.wait(5)
            self.play(mn.FadeOut(*self.mobjects))
        # self.remove(*self.mobjects)

    def first_scene(self):
        # ========== TITLE ==========

        title = mn.Text("Wielomiany szachowe", font_size=36)
        title.to_edge(mn.UP)

        if self.run_animations:
            self.play(mn.FadeIn(title))
        else:
            self.add(title)

        # ========== DEFINITION ==========

        tex1 = mn.Tex(
            "Wielomianem szachowym tablicy $B$ (o wymiarach $m \\times n$) nazywamy:"
        )
        tex1.next_to(title, mn.DOWN, buff=1)

        formula = mn.MathTex(
            "r_B(x) = 1 + {r_1}x + {r_2}x^2 + {r_3}x^3 + \\ldots" +
            "+ {r_{min\\{m,n\\}}}x^{min\\{m,n\\}}",
            font_size=48,
        )
        formula.next_to(tex1, mn.DOWN, buff=1)

        tex2 = mn.Tex(
            "$r_k$ to liczba możliwych ustawień $k$ wież na tablicy $B$ (na dozwolonych polach), " +
            "tak aby wzajemnie sie nie atakowały."
        )
        tex2.next_to(formula, mn.DOWN, buff=1)

        tex3 = mn.Tex(
            "$x^k$ to znacznik informujacy o liczbie wież do rozstawienia, " +
            "gdzie $k$ to liczba wież."
        )
        tex3.next_to(tex2, mn.DOWN, buff=0.5)

        if self.run_animations:
            self.play(
                mn.FadeIn(tex1),
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
            for _ in range(3):
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
            self.wait(3)
        else:
            self.add(tex2)
            formula[0][6:7].set_color(mn.BLUE)
            formula[0][8:10].set_color(mn.BLUE)
            formula[0][12:14].set_color(mn.BLUE)
            formula[0][17:19].set_color(mn.BLUE)
            formula[0][26:35].set_color(mn.BLUE)
            tex2.set_color(mn.BLUE)

        if self.run_animations:
            self.play(mn.FadeIn(tex3))
            for _ in range(3):
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
        # ========== BOARD ==========

        animations: list[mn.FadeIn | None] = []

        board = Board(self, 5, 4)
        board.fill_squares([
            (0, 1), (0, 2),
            (1, 0), (1, 3),
            (2, 1),
            (3, 0), (3, 2),
            (4, 1),
        ],
            mn.GREY,
        )
        board.get_board().to_edge(mn.UP).shift(1.5 * mn.DOWN)
        animations.append(mn.FadeIn(board.get_board()))

        n_labels = ["Ann", "Ed", "Joe", "Leo", "Sue"]
        n_labels_mobjects = [mn.Text(label) for label in n_labels]
        for i, mob in enumerate(n_labels_mobjects):
            mob.next_to(board.get_square_at(board.cols * i), mn.LEFT)
            animations.append(mn.FadeIn(mob))

        m_labels = ["Frontend", "Backend", "Testing", "AI"]
        m_labels_mobjects = [mn.Text(label) for label in m_labels]
        for i, mob in enumerate(m_labels_mobjects):
            mob.rotate(-90 * mn.DEGREES)
            mob.next_to(board.get_square_at(i), mn.UP)
            animations.append(mn.FadeIn(mob))

        if self.run_animations:
            self.play(*animations)
            self.wait(1)
        else:
            for a in animations:
                if a is not None:
                    self.add(a.mobject)

        # ========== FORMULA ==========

        formula = mn.MathTex(
            "r_B(x) = 1 + {r_1}x + {r_2}x^2 + {r_3}x^3 + {r_4}x^4",
            font_size=48,
        )
        formula.next_to(board.get_board(), mn.DOWN, buff=1)

        if self.run_animations:
            self.play(mn.FadeIn(formula))
            self.wait(1)
        else:
            self.add(formula)

        res = get_available_configurations(
            5,
            4,
            [
                (0, 1), (0, 2),
                (1, 0), (1, 3),
                (2, 1),
                (3, 0), (3, 2),
                (4, 1),
            ],
            3,
        )
        if res is not None:
            for r in res:
                board.place_rooks(r)
                self.wait(1)
                board.remove_all_rooks()

        # self.play(
        #     formula.animate.become(mn.MathTex(
        #         "r_B(x) = 1 + 1x + {r_2}x^2 + {r_3}x^3 + {r_4}x^4").next_to(board.get_board(), mn.DOWN, buff=1))
        # )
        # self.play(
        #     formula.animate.become(mn.MathTex(
        #         "r_B(x) = 1 + 2x + {r_2}x^2 + {r_3}x^3 + {r_4}x^4").next_to(board.get_board(), mn.DOWN, buff=1))
        # )

        # formula.become(mn.MathTex(
        # "r_B(x) = 1 + 5x + 8x^2 + 5x^3 + x^4").next_to(board.get_board(), mn.DOWN, buff=1))
