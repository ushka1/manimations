# pylint: disable=C0114, C0115, C0116

import manim as mn
import numpy as np

mn.config.disable_caching = True


class Cycle():
    def __init__(self, r: int):
        self.circle = mn.Circle(radius=r, color=mn.WHITE)

    def get_cycle(self):
        return self.circle

    def get_cell_coords(self, n: int):
        x, y, _ = self.circle.get_center()
        cells = []
        angle = 2 * np.pi / n

        for i in range(n):
            dx = self.circle.width / 2 * np.cos(i * angle)
            dy = self.circle.width / 2 * np.sin(i * angle)
            cells.append((round(x + dx, 2), round(y + dy, 2), 0))

        return cells


def create_circles(colors: list[mn.ManimColor]):
    circles = mn.VGroup()
    for (i, c) in enumerate(colors):
        circle = mn.Circle(
            radius=0.3,
        ).set_fill(c, 1).set_stroke(width=0)

        # put label in the center of circle
        label = mn.Text(str(i + 1), font_size=36, color=mn.BLACK)
        label.move_to(circle)

        circle_group = mn.VGroup(circle, label)
        circle_group.set_z_index(1)
        circles.add(circle_group)

    circles.arrange(mn.RIGHT)
    return circles


stirling_partitions = [
    [[0], [1, 2, 3]],
    [[0], [1, 3, 2]],

    [[1], [0, 2, 3]],
    [[1], [0, 3, 2]],

    [[2], [0, 1, 3]],
    [[2], [0, 3, 1]],

    [[3], [0, 1, 2]],
    [[3], [0, 2, 1]],

    [[0, 1], [2, 3]],
    [[0, 2], [1, 3]],
    [[0, 3], [1, 2]],
]


class StirlingI(mn.Scene):
    run_animations = True

    def construct(self):
        # ========== CONFIG ==========

        mn.Text.set_default(font="Roboto", font_size=16)

        # ========== SCENES ==========

        self.first_scene()
        if self.run_animations:
            self.wait(2)
            self.play(mn.FadeOut(*self.mobjects))
        self.remove(*self.mobjects)

        self.second_scene()
        if self.run_animations:
            self.wait(5)
            self.play(mn.FadeOut(*self.mobjects))
        self.remove(*self.mobjects)

    def first_scene(self):
        # ========== TITLE ==========

        title = mn.Text("Liczby Stirlinga I rodzaju", font_size=24)
        title.to_edge(mn.UP)

        if self.run_animations:
            self.play(mn.FadeIn(title))
        else:
            self.add(title)

        # ========== TEXT ==========

        formula = mn.MathTex(
            r"\begin{bmatrix} \ n \ \\ \ k \ \end{bmatrix} = c(n,k)",
            font_size=36,
        )

        text = mn.Text(
            "Jest to liczba sposobów zorganizowania n rozróżnialnych kul w k nierozróżnialnych cyklach.",
            font_size=18
        )
        text.next_to(formula, mn.DOWN)

        group = mn.VGroup(formula, text)
        group.next_to(title, mn.DOWN).shift(mn.DOWN * 0.5)

        if self.run_animations:
            self.play(mn.FadeIn(formula))
            self.play(mn.FadeIn(text))
        else:
            self.add(formula)
            self.add(text)

        # ========== HIGHLIGHT - CIRCLES ==========

        if self.run_animations:
            for _ in range(3):
                self.play(formula[0][1].animate.set_color(mn.WHITE),
                          formula[0][7].animate.set_color(mn.WHITE),
                          text[34:52].animate.set_color(mn.WHITE),
                          run_time=0.2)
                self.play(formula[0][1].animate.set_color(mn.BLUE),
                          formula[0][7].animate.set_color(mn.BLUE),
                          text[34:52].animate.set_color(mn.BLUE),
                          run_time=0.2)
        else:
            formula[0][1].set_color(mn.BLUE)
            formula[0][7].set_color(mn.BLUE)
            text[34:52].set_color(mn.BLUE)

        # ========== CIRCLES ==========

        circles = create_circles([mn.RED, mn.ORANGE, mn.YELLOW,
                                  mn.GREEN, mn.BLUE, mn.PURPLE])
        circles.next_to(
            group,
            direction=mn.DOWN,
        ).shift(mn.DOWN * 0.5)

        if self.run_animations:
            self.play(mn.FadeIn(circles))
        else:
            self.add(circles)

        # ========== HIGHLIGHT - CYCLES ==========

        if self.run_animations:
            for _ in range(3):
                self.play(formula[0][2].animate.set_color(mn.WHITE),
                          formula[0][9].animate.set_color(mn.WHITE),
                          text[53:78].animate.set_color(mn.WHITE),
                          run_time=0.2)
                self.play(formula[0][2].animate.set_color(mn.ORANGE),
                          formula[0][9].animate.set_color(mn.ORANGE),
                          text[53:78].animate.set_color(mn.ORANGE),
                          run_time=0.2)
        else:
            formula[0][2].set_color(mn.ORANGE)
            formula[0][9].set_color(mn.ORANGE)
            text[53:78].set_color(mn.ORANGE)

        # ========== CYCLES ==========

        cycle1 = Cycle(1)
        cycle2 = Cycle(1)

        cycle_group = mn.VGroup(cycle1.get_cycle(), cycle2.get_cycle())
        cycle_group.arrange(mn.RIGHT, buff=2)
        cycle_group.next_to(circles, direction=mn.DOWN).shift(mn.DOWN * 0.5)

        if self.run_animations:
            self.play(mn.FadeIn(cycle_group))
        else:
            self.add(cycle_group)

        # # ========== PLACEMENT ==========

        cells1 = cycle1.get_cell_coords(4)
        cells2 = cycle2.get_cell_coords(2)

        print(cells1)

        if self.run_animations:
            self.play(
                mn.AnimationGroup(
                    circles[0].animate.move_to(cells1[0]),
                    circles[1].animate.move_to(cells1[1]),
                    circles[2].animate.move_to(cells2[0]),
                    circles[3].animate.move_to(cells1[2]),
                    circles[4].animate.move_to(cells2[1]),
                    circles[5].animate.move_to(cells1[3]),
                    lag_ratio=0.1
                )
            )
            self.wait(1)
        else:
            circles[0].move_to(cells1[0])
            circles[1].move_to(cells1[1])
            circles[2].move_to(cells2[0])
            circles[3].move_to(cells1[2])
            circles[4].move_to(cells2[1])
            circles[5].move_to(cells1[3])

        # # ========== CYCLES SHIFT ==========

        cycle1.get_cycle().add(circles[0])  # type: ignore
        cycle1.get_cycle().add(circles[1])  # type: ignore
        cycle2.get_cycle().add(circles[2])  # type: ignore
        cycle1.get_cycle().add(circles[3])  # type: ignore
        cycle2.get_cycle().add(circles[4])  # type: ignore
        cycle1.get_cycle().add(circles[5])  # type: ignore

        if self.run_animations:
            self.play(
                cycle1.get_cycle().animate.shift(
                    mn.RIGHT * (cycle1.get_cycle().radius * 2 + 2)
                ),
                cycle2.get_cycle().animate.shift(
                    mn.LEFT * (cycle2.get_cycle().radius * 2 + 2)
                ))
            self.wait(0.5)
            self.play(
                mn.AnimationGroup(
                    mn.Rotate(cycle2.get_cycle(), 2*np.pi, run_time=2),
                    mn.Rotate(cycle1.get_cycle(), 2*np.pi, run_time=2),
                    lag_ratio=0.5
                )
            )
            self.wait(0.5)
            self.play(
                cycle2.get_cycle().animate.shift(
                    mn.RIGHT * (cycle2.get_cycle().radius * 2 + 2)
                ),
                cycle1.get_cycle().animate.shift(
                    mn.LEFT * (cycle1.get_cycle().radius * 2 + 2)
                ))

    def second_scene(self):
        # ========== TITLE ==========

        title = mn.MathTex(
            r"\begin{bmatrix} \ 4 \ \\ \ 2 \ \end{bmatrix} = 11",
            font_size=36,
        )
        title.to_edge(mn.UP)

        if self.run_animations:
            self.play(mn.FadeIn(title))
        else:
            self.add(title)

        # ========== SHOW BUCKETS ==========

        group = mn.VGroup()
        data: list[tuple[Cycle, Cycle, mn.VGroup]] = []
        for _ in range(11):
            bucket1 = Cycle(1)
            bucket2 = Cycle(1)
            circles = create_circles(
                [mn.RED,  mn.YELLOW, mn.GREEN, mn.BLUE]
            )
            data.append((
                bucket1,
                bucket2,
                circles,
            ))

            b_group = mn.VGroup(
                bucket1.get_cycle(),
                bucket2.get_cycle()
            )
            b_group.arrange(mn.RIGHT, buff=1)
            bc_group = mn.VGroup(circles, b_group)
            bc_group.arrange(mn.DOWN, buff=0.5)
            group.add(bc_group)

        group.scale(0.4)
        group.arrange_in_grid(5, 3, buff=(2, 0.3))
        group.next_to(title, mn.DOWN)

        if self.run_animations:
            self.play(mn.FadeIn(group))
            self.wait(1)
        else:
            self.add(group)

        # ========== PLACEMENT ==========

        animations: list[mn.Animation] = []
        for e in zip(data, stirling_partitions):
            circles = e[0][2]
            part1 = e[1][0]
            part2 = e[1][1]
            cells1 = e[0][0].get_cell_coords(len(part1))
            cells2 = e[0][1].get_cell_coords(len(part2))
            i1 = 0
            i2 = 0
            for (i, c) in enumerate(circles):
                if i in part1:
                    animations.append(
                        c.animate.move_to(cells1[i1])
                    )
                    i1 += 1
                else:
                    animations.append(
                        c.animate.move_to(cells2[i2])
                    )
                    i2 += 1

        if self.run_animations:
            self.play(mn.AnimationGroup(*animations, lag_ratio=0.025))
        else:
            for a in animations:
                a.mobject.move_to(a.mobject.target)
