import manim as mn

# mn.config.disable_caching = True


class StirlingII(mn.Scene):
    def construct(self):
        # ========== CONFIG ==========

        mn.Text.set_default(font="Roboto", font_size=16)

        # ========== TITLE ==========

        title = mn.Text("Liczby Stirlinga II rodzaju", font_size=24)
        title.to_edge(mn.UP)
        # self.play(mn.FadeIn(title))
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

        # self.play(mn.FadeIn(formula))
        self.add(formula)

        # self.play(mn.FadeIn(text))
        self.add(text)

        # ========== COLORING ==========

        formula[0][1].set_color(mn.BLUE)
        formula[0][7].set_color(mn.BLUE)
        text[24:42].set_color(mn.BLUE)

        # for _ in range(5):
        #     self.play(formula[0][1].animate.set_color(mn.WHITE),
        #               formula[0][7].animate.set_color(mn.WHITE),
        #               text[24:42].animate.set_color(mn.WHITE),
        #               run_time=0.2)
        #     self.play(formula[0][1].animate.set_color(mn.BLUE),
        #               formula[0][7].animate.set_color(mn.BLUE),
        #               text[24:42].animate.set_color(mn.BLUE),
        #               run_time=0.2)

        formula[0][2].set_color(mn.ORANGE)
        formula[0][9].set_color(mn.ORANGE)
        text[44:69].set_color(mn.ORANGE)

        # for _ in range(5):
        #     self.play(formula[0][2].animate.set_color(mn.WHITE),
        #               formula[0][9].animate.set_color(mn.WHITE),
        #               text[44:69].animate.set_color(mn.WHITE),
        #               run_time=0.2)
        #     self.play(formula[0][2].animate.set_color(mn.ORANGE),
        #               formula[0][9].animate.set_color(mn.ORANGE),
        #               text[44:69].animate.set_color(mn.ORANGE),
        #               run_time=0.2)

        # self.wait(1)

        # ========== CIRCLES ==========

        circle_colors = [mn.RED, mn.ORANGE, mn.YELLOW,
                         mn.GREEN, mn.BLUE, mn.PURPLE]
        circles = mn.VGroup()
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

        self.add(circles)

        # ========== BUCKETS ==========

        buckets = mn.VGroup()
        for _ in range(2):
            bucket = self.create_bucket()
            buckets.add(bucket)

        buckets.arrange(mn.RIGHT, buff=1)
        buckets.next_to(circles, direction=mn.DOWN).shift(mn.DOWN * 0.5)
        self.add(buckets)

        # ========== MOVE CIRCLES INTO BUCKETS ==========

    def create_bucket(self):
        width = 4
        height = 2
        points = [
            [-width / 2, height / 2, 0],
            [-width / 2, -height / 2, 0],
            [width / 2, -height / 2, 0],
            [width / 2, height / 2, 0],
        ]

        bucket = mn.VGroup()
        for i in range(len(points)-1):
            line = mn.Line(
                points[i],  # type: ignore
                points[i+1],  # type: ignore
                color=mn.WHITE,
            )
            bucket.add(line)

        return bucket
