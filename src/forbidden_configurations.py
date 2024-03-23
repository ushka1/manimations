# pylint: disable=C0114, C0115, C0116, C0301

import manim as mn

import utils.theme as theme
from utils.board import Board
from utils.rook_polynomials import get_available_rook_configs

theme.set_theme_defaults()


class ForbiddenConfigurations(mn.Scene):
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

        title = mn.Text("Konfiguracje zabronione", font_size=theme.FONT_LG)
        title.to_edge(mn.UP)

        if self.run_animations:
            self.play(mn.FadeIn(title))
        else:
            self.add(title)

        # ========== TEXT ==========

        text1 = mn.Text(
            "Załóżmy, że mamy m osób, o różnych kwalifikacjach, oraz n stanowisk, które muszą zostać obsadzone."
        )
        text1.next_to(title, mn.DOWN, buff=0.5)

        text2 = mn.Text(
            "Ile jest sposobów na obsadzenie stanowisk (szare pole oznacza brak kwalifikacji)?",
        )
        text2.next_to(text1, mn.DOWN, buff=0.125)

        if self.run_animations:
            self.play(
                mn.FadeIn(text1),
                mn.FadeIn(text2)
            )
        else:
            self.add(text1, text2)

        # ========== BOARD ==========

        animations: list[mn.FadeIn | None] = []

        board = Board(self, 5, 4)
        board.get_board().next_to(text2, mn.DOWN, buff=1.75)
        animations.append(mn.FadeIn(board.get_board()))

        board.set_y_labels(["Ann", "Ed", "Joe", "Leo", "Sue"])
        m_labels_mobjects = board.get_y_labels()
        for label in board.get_y_labels():
            animations.append(mn.FadeIn(label))

        board.set_x_labels(["Frontend", "Backend", "Testing", "AI"])
        n_labels_mobjects = board.get_x_labels()
        for label in board.get_x_labels():
            animations.append(mn.FadeIn(label))

        if self.run_animations:
            self.play(*animations)
            self.wait(5)
        else:
            for a in animations:
                if a is not None:
                    self.add(a.mobject)

        # ========== HIGHLIGHT PEOPLE ==========

        if self.run_animations:
            for _ in range(5):
                self.play(text1[14:20].animate.set_color(mn.WHITE),
                          *[mob.animate.set_color(mn.WHITE)
                            for mob in m_labels_mobjects],
                          run_time=0.2)
                self.play(text1[14:20].animate.set_color(mn.BLUE),
                          *[mob.animate.set_color(mn.BLUE)
                            for mob in m_labels_mobjects],
                          run_time=0.2)
            self.wait(1)
        else:
            text1[14:20].set_color(mn.BLUE)
            for mob in m_labels_mobjects:
                mob.set_color(mn.BLUE)

        # ========== HIGHLIGHT JOBS ==========

        if self.run_animations:
            for _ in range(5):
                self.play(text1[46:56].animate.set_color(mn.WHITE),
                          *[mob.animate.set_color(mn.WHITE)
                            for mob in n_labels_mobjects],
                          run_time=0.2)
                self.play(text1[46:56].animate.set_color(mn.ORANGE),
                          *[mob.animate.set_color(mn.ORANGE)
                            for mob in n_labels_mobjects],
                          run_time=0.2)
            self.wait(1)
        else:
            text1[46:56].set_color(mn.ORANGE)
            for mob in n_labels_mobjects:
                mob.set_color(mn.ORANGE)

        # ========== HIGHLIGHT BOARD ==========

        forbidden_squares = [
            (0, 1), (0, 2),
            (1, 0), (1, 3),
            (2, 1),
            (3, 0), (3, 2),
            (4, 1),
        ]

        if self.run_animations:
            for _ in range(5):
                self.play(
                    text2[36:69].animate.set_color(mn.WHITE),
                    *board.fill_squares_animations(
                        forbidden_squares,
                        mn.GREY,
                        opacity=0
                    ),
                    run_time=0.2
                )
                self.play(
                    text2[36:69].animate.set_color(mn.GREY_A),
                    *board.fill_squares_animations(
                        forbidden_squares,
                        mn.GREY
                    ),
                    run_time=0.2
                )
            self.wait(1)
        else:
            text2[36:69].set_color(mn.GREY_A)
            board.fill_squares(
                forbidden_squares,
                mn.GREY
            )

        # ========== TEXT ==========

        text3 = mn.Text(
            "Powyższy problem jest równoważny znalezieniu wszystkich możliwości rozmieszczenia czterech wież",
        )
        text3.next_to(board.get_board(), mn.DOWN, buff=0.5)

        text4 = mn.Text(
            "na szachownicy, tak aby się wzajemnie nie atakowały.",
        )
        text4.next_to(text3, mn.DOWN, buff=0.125)

        if self.run_animations:
            self.play(
                mn.FadeIn(text3),
                mn.FadeIn(text4)
            )
            self.wait(3)
        else:
            self.add(text3, text4)

        # ========== ROOKS PLACEMENT ==========

        configs = get_available_rook_configs(5, 4, forbidden_squares, 4)

        if configs is None:
            return

        if self.run_animations:
            for c in configs:
                if self.run_animations:
                    remove_animations = board.remove_all_rooks_animations()
                    if len(remove_animations) > 0:
                        self.play(*remove_animations, run_time=0.25)
                    self.play(*board.place_rooks_animations(c),
                              run_time=0.25)
        else:
            board.place_rooks(configs[len(configs) - 1])
