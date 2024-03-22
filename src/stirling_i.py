# pylint: disable=C0114, C0115, C0116, C0301

import manim as mn

import utils.constants as consts
from utils.create_balls import create_balls
from utils.cycle import Cycle

consts.set_defaults()

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

        title = mn.Text("Liczby Stirlinga I rodzaju", font_size=consts.FONT_LG)
        title.to_edge(mn.UP)

        if self.run_animations:
            self.play(mn.FadeIn(title))
        else:
            self.add(title)

        # ========== FORMULA TEXT ==========

        formula = mn.MathTex(
            r"\begin{bmatrix} \ n \ \\ \ k \ \end{bmatrix} = c(n,k)",
            font_size=consts.FONT_XL,
        )
        formula.next_to(title, mn.DOWN, buff=0.5)

        text = mn.Text(
            "Jest to liczba sposobów zorganizowania n rozróżnialnych kul" +
            "w k nierozróżnialnych cyklach.",
            font_size=consts.FONT_SM,
        )
        text.next_to(formula, mn.DOWN, buff=0.5)

        if self.run_animations:
            self.play(mn.FadeIn(formula))
            self.play(mn.FadeIn(text))
        else:
            self.add(formula)
            self.add(text)

        # ========== HIGHLIGHT BALLS TEXT ==========

        if self.run_animations:
            for _ in range(5):
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

        # ========== BALLS ==========

        balls = create_balls([mn.RED, mn.ORANGE, mn.YELLOW,
                              mn.GREEN, mn.BLUE, mn.PURPLE])
        balls.next_to(text, direction=mn.DOWN, buff=1)

        if self.run_animations:
            self.play(mn.FadeIn(balls))
        else:
            self.add(balls)

        # ========== HIGHLIGHT CYCLES TEXT ==========

        if self.run_animations:
            for _ in range(5):
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

        cycles_group = mn.VGroup(cycle1.get_cycle(), cycle2.get_cycle())
        cycles_group.arrange(mn.RIGHT, buff=2)
        cycles_group.next_to(balls, direction=mn.DOWN, buff=0.5)

        if self.run_animations:
            self.play(mn.FadeIn(cycles_group))
            self.wait(1)
        else:
            self.add(cycles_group)

        # ========== BALLS PLACEMENT ==========

        cells1 = cycle1.get_cell_coords(4)
        cells2 = cycle2.get_cell_coords(2)

        if self.run_animations:
            self.play(
                mn.AnimationGroup(
                    balls[0].animate.move_to(cells1[0]),
                    balls[1].animate.move_to(cells1[1]),
                    balls[2].animate.move_to(cells2[0]),
                    balls[3].animate.move_to(cells1[2]),
                    balls[4].animate.move_to(cells2[1]),
                    balls[5].animate.move_to(cells1[3]),
                    lag_ratio=0.1
                )
            )
            self.wait(1)
        else:
            balls[0].move_to(cells1[0])
            balls[1].move_to(cells1[1])
            balls[2].move_to(cells2[0])
            balls[3].move_to(cells1[2])
            balls[4].move_to(cells2[1])
            balls[5].move_to(cells1[3])

        # ========== CYCLES SHIFT ROTATE SHIFT ==========

        cycle1.get_cycle().add(balls[0])  # type: ignore
        cycle1.get_cycle().add(balls[1])  # type: ignore
        cycle2.get_cycle().add(balls[2])  # type: ignore
        cycle1.get_cycle().add(balls[3])  # type: ignore
        cycle2.get_cycle().add(balls[4])  # type: ignore
        cycle1.get_cycle().add(balls[5])  # type: ignore

        if self.run_animations:
            self.play(
                cycle1.get_cycle().animate.shift(
                    mn.RIGHT * (cycle1.get_cycle().radius * 2 + 2)
                ),
                cycle2.get_cycle().animate.shift(
                    mn.LEFT * (cycle2.get_cycle().radius * 2 + 2)
                ))
            self.play(
                mn.Rotate(cycle2.get_cycle(), 2 * mn.PI, run_time=2),
                mn.Rotate(cycle1.get_cycle(), 2 * mn.PI, run_time=2),
            )
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
            self.wait(1)
        else:
            self.add(title)

        # ========== BALLS CYCLES ==========

        group = mn.VGroup()
        data: list[tuple[Cycle, Cycle, mn.VGroup]] = []
        for _ in range(11):
            cycle1 = Cycle(1)
            cycle2 = Cycle(1)
            balls = create_balls(
                [mn.RED,  mn.YELLOW, mn.GREEN, mn.BLUE]
            )
            data.append((
                cycle1,
                cycle2,
                balls,
            ))

            b_group = mn.VGroup(
                cycle1.get_cycle(),
                cycle2.get_cycle()
            )
            b_group.arrange(mn.RIGHT, buff=1)
            bc_group = mn.VGroup(balls, b_group)
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

        # ========== BALLS PLACEMENT ==========

        animations: list[mn.Animation] = []
        for x in zip(data, stirling_partitions):
            part1 = x[1][0]
            part2 = x[1][1]
            i1 = 0
            i2 = 0

            cycle1 = x[0][0]
            cycle2 = x[0][1]
            balls = x[0][2]
            cells1 = cycle1.get_cell_coords(len(part1))
            cells2 = cycle2.get_cell_coords(len(part2))

            for (i, b) in enumerate(balls):
                if i in part1:
                    animations.append(
                        b.animate.move_to(cells1[i1])
                    )
                    i1 += 1
                else:
                    animations.append(
                        b.animate.move_to(cells2[i2])
                    )
                    i2 += 1

        if self.run_animations:
            self.play(mn.AnimationGroup(*animations, lag_ratio=0.025))
        else:
            for a in animations:
                a.mobject.move_to(a.mobject.target)
