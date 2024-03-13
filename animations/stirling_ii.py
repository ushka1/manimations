# pylint: disable=C0114, C0115, C0116
# mn.config.disable_caching = True

import manim as mn


class Bucket():
    def __init__(self, width: int, height: int):
        self.group = mn.VGroup()
        self.width = width
        self.height = height

        points = [
            [-self.width / 2, self.height / 2, 0],
            [-self.width / 2, -self.height / 2, 0],
            [self.width / 2, -self.height / 2, 0],
            [self.width / 2, self.height / 2, 0],
        ]
        for i in range(len(points)-1):
            line = mn.Line(
                points[i],  # type: ignore
                points[i+1],  # type: ignore
                color=mn.WHITE,
            )
            self.group.add(line)

    def get_bucket(self):
        return self.group

    def get_cell_coords(self, row: int, col: int):
        x = self.group.get_left()[0] + col + 1/2
        y = self.group.get_bottom()[1] + row + 1/2
        return (x, y, 0)


class StirlingII(mn.Scene):
    run_animations = True

    def construct(self):
        # ========== CONFIG ==========

        mn.Text.set_default(font="Roboto", font_size=16)

        # ========== TITLE ==========

        title = mn.Text("Liczby Stirlinga II rodzaju", font_size=24)
        title.to_edge(mn.UP)

        if self.run_animations:
            self.play(mn.FadeIn(title))
        else:
            self.add(title)

        # ========== TEXT ==========

        formula = mn.MathTex(
            r"\left\{ {n \atop k} \right\} = S(n,k)",
            font_size=36,
        )

        text = mn.Text(
            "Jest to liczba rozmieszczeń n rozróżnialnych kul na k nierozróżnialnych stosach.",
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

        # ========== COLORING ==========

        if self.run_animations:
            for _ in range(3):
                self.play(formula[0][1].animate.set_color(mn.WHITE),
                          formula[0][7].animate.set_color(mn.WHITE),
                          text[24:42].animate.set_color(mn.WHITE),
                          run_time=0.2)
                self.play(formula[0][1].animate.set_color(mn.BLUE),
                          formula[0][7].animate.set_color(mn.BLUE),
                          text[24:42].animate.set_color(mn.BLUE),
                          run_time=0.2)

            for _ in range(3):
                self.play(formula[0][2].animate.set_color(mn.WHITE),
                          formula[0][9].animate.set_color(mn.WHITE),
                          text[44:69].animate.set_color(mn.WHITE),
                          run_time=0.2)
                self.play(formula[0][2].animate.set_color(mn.ORANGE),
                          formula[0][9].animate.set_color(mn.ORANGE),
                          text[44:69].animate.set_color(mn.ORANGE),
                          run_time=0.2)

            self.wait(1)
        else:
            formula[0][1].set_color(mn.BLUE)
            formula[0][7].set_color(mn.BLUE)
            text[24:42].set_color(mn.BLUE)

            formula[0][2].set_color(mn.ORANGE)
            formula[0][9].set_color(mn.ORANGE)
            text[44:69].set_color(mn.ORANGE)

        # ========== CIRCLES ==========

        circles = mn.VGroup()
        circle_colors = [mn.RED, mn.ORANGE, mn.YELLOW,
                         mn.GREEN, mn.BLUE, mn.PURPLE]
        for color in circle_colors:
            circle = mn.Circle(
                radius=0.3,
            ).set_fill(color, 1).set_stroke(width=0)
            circles.add(circle)

        circles.arrange(mn.RIGHT)
        circles.next_to(
            group,
            direction=mn.DOWN,
        ).shift(mn.DOWN * 0.5)

        if self.run_animations:
            self.play(mn.FadeIn(circles))
        else:
            self.add(circles)

        # ========== BUCKETS ==========

        bucket1 = Bucket(4, 2)
        bucket2 = Bucket(4, 2)

        bucket_group = mn.VGroup(bucket1.get_bucket(), bucket2.get_bucket())
        bucket_group.arrange(mn.RIGHT, buff=1)
        bucket_group.next_to(circles, direction=mn.DOWN).shift(mn.DOWN * 0.5)

        if self.run_animations:
            self.play(mn.FadeIn(bucket_group))
        else:
            self.add(bucket_group)

        # ========== MOVE CIRCLES INTO BUCKETS ==========

        self.play(circles[0].animate.move_to(bucket1.get_cell_coords(0, 0)))
        self.play(circles[1].animate.move_to(bucket1.get_cell_coords(0, 1)))
        self.play(circles[2].animate.move_to(bucket2.get_cell_coords(0, 0)))
        self.play(circles[3].animate.move_to(bucket1.get_cell_coords(0, 2)))
        self.play(circles[4].animate.move_to(bucket2.get_cell_coords(0, 1)))
        self.play(circles[5].animate.move_to(bucket1.get_cell_coords(0, 3)))

        # XXX
        self.run_animations = True
        # XXX
