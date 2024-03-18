# pylint: disable=C0114, C0115, C0116, C0301

import manim as mn

from utils.board import Board

# mn.config.disable_caching = True
mn.Text.set_default(font="Ubuntu", font_size=16)


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

        title = mn.Text("Konfiguracje zabronione", font_size=24)
        title.to_edge(mn.UP)

        if self.run_animations:
            self.play(mn.FadeIn(title))
        else:
            self.add(title)

        # ========== TEXT ==========

        text1 = mn.Text(
            "Załóżmy, że mamy m osób, o różnych kwalifikacjach, oraz n stanowisk, które muszą zostać obsadzone.",
            font_size=18
        )
        text2 = mn.Text(
            "Ile jest sposobów na obsadzenie stanowisk (szare pole oznacza brak kwalifikacji)?",
            font_size=18
        )
        text1.next_to(title, mn.DOWN).shift(mn.DOWN * 0.25)
        text2.next_to(text1, mn.DOWN)

        if self.run_animations:
            self.play(mn.FadeIn(text1), mn.FadeIn(text2))
        else:
            self.add(text1, text2)

        if self.run_animations:
            self.wait(5)

        # ========== BOARD ==========

        animations: list[mn.FadeIn | None] = []

        board = Board(self, 5, 4)
        board.get_board().next_to(text2, mn.DOWN).shift(mn.DOWN * 1.5)
        animations.append(mn.FadeIn(board.get_board()))

        m_labels = ["Ann", "Ed", "Joe", "Leo", "Sue"]
        m_labels_mobjects = [mn.Text(label) for label in m_labels]
        for i, mob in enumerate(m_labels_mobjects):
            mob.next_to(board.get_square_at(board.cols * i), mn.LEFT)
            animations.append(mn.FadeIn(mob))

        n_labels = ["Frontend", "Backend", "Testing", "AI"]
        n_labels_mobjects = [mn.Text(label) for label in n_labels]
        for i, mob in enumerate(n_labels_mobjects):
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

        # ========== HIGHLIGHT ==========

        if self.run_animations:
            for _ in range(3):
                self.play(text1[14:20].animate.set_color(mn.WHITE),
                          *[mob.animate.set_color(mn.WHITE)
                            for mob in m_labels_mobjects],
                          run_time=0.2)
                self.play(text1[14:20].animate.set_color(mn.BLUE),
                          *[mob.animate.set_color(mn.BLUE)
                            for mob in m_labels_mobjects],
                          run_time=0.2)
        else:
            text1[14:20].set_color(mn.BLUE)
            for mob in m_labels_mobjects:
                mob.set_color(mn.BLUE)

        if self.run_animations:
            self.wait(1)

        if self.run_animations:
            for _ in range(3):
                self.play(text1[46:56].animate.set_color(mn.WHITE),
                          *[mob.animate.set_color(mn.WHITE)
                            for mob in n_labels_mobjects],
                          run_time=0.2)
                self.play(text1[46:56].animate.set_color(mn.ORANGE),
                          *[mob.animate.set_color(mn.ORANGE)
                            for mob in n_labels_mobjects],
                          run_time=0.2)
        else:
            text1[46:56].set_color(mn.ORANGE)
            for mob in n_labels_mobjects:
                mob.set_color(mn.ORANGE)

        if self.run_animations:
            self.wait(1)

        # ========== HIGHLIGHT BOARD ==========

        if self.run_animations:
            for _ in range(3):
                self.play(
                    text2[36:69].animate.set_color(mn.WHITE),
                    *board.fill_squares_animations([
                        (0, 1), (0, 2),
                        (1, 0), (1, 3),
                        (2, 1),
                        (3, 0), (3, 2),
                        (4, 1),
                    ],
                        mn.GREY,
                        opacity=0
                    ),
                    run_time=0.2
                )
                self.play(
                    text2[36:69].animate.set_color(mn.GREY_A),
                    *board.fill_squares_animations([
                        (0, 1), (0, 2),
                        (1, 0), (1, 3),
                        (2, 1),
                        (3, 0), (3, 2),
                        (4, 1),
                    ],
                        mn.GREY
                    ),
                    run_time=0.2
                )
        else:
            text2[36:69].set_color(mn.GREY_A)
            board.fill_squares([
                (0, 1), (0, 2),
                (1, 0), (1, 3),
                (2, 1),
                (3, 0), (3, 2),
                (4, 1),
            ],
                mn.GREY
            )

        if self.run_animations:
            self.wait(1)

        # ========== TEXT ==========

        text3 = mn.Text(
            "Powyższy problem jest równoważny znalezieniu wszystkich możliwości rozmieszczenia czterech wież",
            font_size=18,
        )
        text3.next_to(board.get_board(), mn.DOWN).shift(mn.DOWN * 0.25)

        text4 = mn.Text(
            "na szachownicy, tak aby się wzajemnie nie atakowały.",
            font_size=18,
        )
        text4.next_to(text3, mn.DOWN)

        if self.run_animations:
            self.play(mn.FadeIn(text3), mn.FadeIn(text4))
        else:
            self.add(text3, text4)
