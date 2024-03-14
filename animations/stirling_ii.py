# pylint: disable=C0114, C0115, C0116
# mn.config.disable_caching = True

import manim as mn


class Bucket():
    def __init__(self, rows: int, cols: int):
        self.rows = rows
        self.cols = cols

        width = cols
        height = rows
        points = [
            [-width / 2, height / 2, 0],
            [-width / 2, -height / 2, 0],
            [width / 2, -height / 2, 0],
            [width / 2, height / 2, 0],
            [width / 2, -height / 2, 0],
            [-width / 2, -height / 2, 0],
            [-width / 2, height / 2, 0],
        ]
        self.polygon = mn.Polygon(*points, color=mn.WHITE)  # type: ignore

    def get_bucket(self):
        return self.polygon

    def get_cell_coords(self, row: int, col: int):
        col_width = self.polygon.width / self.cols
        row_height = self.polygon.height / self.rows
        x = self.polygon.get_left()[0] + (col + 1/2) * col_width
        y = self.polygon.get_bottom()[1] + (row + 1/2) * row_height
        return (x, y, 0)


class StirlingII(mn.Scene):
    run_animations = False

    def construct(self):
        # ========== CONFIG ==========

        mn.Text.set_default(font="Roboto", font_size=16)

        # ========== SCENES ==========

        # self.first_scene()

        # if self.run_animations:
        #     self.wait(3)
        #     self.play(mn.FadeOut(*self.mobjects))

        # self.remove(*self.mobjects)

        self.second_scene()

    def second_scene(self):

        # ========== TITLE ==========

        title = mn.MathTex(
            r"\left\{ {5 \atop 2} \right\}",
            font_size=36,
        )
        title.to_edge(mn.UP)

        if self.run_animations:
            self.play(mn.FadeIn(title))
        else:
            self.add(title)

        # ========== BUCKETS ==========

        all_buckets: list[Bucket] = []
        group = mn.VGroup()
        for _ in range(15):
            bucket1 = Bucket(2, 4)
            bucket2 = Bucket(2, 4)
            all_buckets.append(bucket1)
            all_buckets.append(bucket2)

            buckets = mn.VGroup(bucket1.get_bucket(), bucket2.get_bucket())
            buckets.arrange(mn.RIGHT, buff=1)
            buckets.scale(0.25)
            group.add(buckets)

        group.arrange_in_grid(5, 3, buff=(2, 0.75))
        group.next_to(title, mn.DOWN).shift(mn.DOWN * 0.5)
        self.add(group)

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
            title,
            direction=mn.DOWN,
        ).shift(mn.DOWN * 0.5)
        self.add(circles)

        circles.scale(0.25)

        circles[0].move_to(all_buckets[0].get_cell_coords(0, 0))
        circles[1].move_to(all_buckets[0].get_cell_coords(0, 1))
        circles[2].move_to(all_buckets[0].get_cell_coords(0, 2))
        circles[3].move_to(all_buckets[0].get_cell_coords(0, 3))
        circles[4].move_to(all_buckets[0].get_cell_coords(1, 0))
        circles[5].move_to(all_buckets[0].get_cell_coords(1, 1))

    def first_scene(self):
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

        # ========== HIGHLIGHT - CIRCLES ==========

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
        else:
            formula[0][1].set_color(mn.BLUE)
            formula[0][7].set_color(mn.BLUE)
            text[24:42].set_color(mn.BLUE)

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

        # ========== HIGHLIGHT - BUCKETS ==========

        if self.run_animations:
            for _ in range(3):
                self.play(formula[0][2].animate.set_color(mn.WHITE),
                          formula[0][9].animate.set_color(mn.WHITE),
                          text[44:69].animate.set_color(mn.WHITE),
                          run_time=0.2)
                self.play(formula[0][2].animate.set_color(mn.ORANGE),
                          formula[0][9].animate.set_color(mn.ORANGE),
                          text[44:69].animate.set_color(mn.ORANGE),
                          run_time=0.2)
        else:
            formula[0][2].set_color(mn.ORANGE)
            formula[0][9].set_color(mn.ORANGE)
            text[44:69].set_color(mn.ORANGE)

        # ========== BUCKETS ==========

        bucket1 = Bucket(2, 4)
        bucket2 = Bucket(2, 4)

        bucket_group = mn.VGroup(bucket1.get_bucket(), bucket2.get_bucket())
        bucket_group.arrange(mn.RIGHT, buff=1)
        bucket_group.next_to(circles, direction=mn.DOWN).shift(mn.DOWN * 0.5)

        if self.run_animations:
            self.play(mn.FadeIn(bucket_group))
        else:
            self.add(bucket_group)

        # ========== PLACEMENT ==========

        if self.run_animations:
            self.play(circles[0].animate.move_to(
                bucket1.get_cell_coords(0, 0)
            ))
            self.play(circles[1].animate.move_to(
                bucket1.get_cell_coords(0, 1)
            ))
            self.play(circles[2].animate.move_to(
                bucket2.get_cell_coords(0, 0)
            ))
            self.play(circles[3].animate.move_to(
                bucket1.get_cell_coords(0, 2)
            ))
            self.play(circles[4].animate.move_to(
                bucket2.get_cell_coords(0, 1)
            ))
            self.play(circles[5].animate.move_to(
                bucket1.get_cell_coords(0, 3)
            ))
        else:
            circles[0].move_to(bucket1.get_cell_coords(0, 0))
            circles[1].move_to(bucket1.get_cell_coords(0, 1))
            circles[2].move_to(bucket2.get_cell_coords(0, 0))
            circles[3].move_to(bucket1.get_cell_coords(0, 2))
            circles[4].move_to(bucket2.get_cell_coords(0, 1))
            circles[5].move_to(bucket1.get_cell_coords(0, 3))

        # ========== BUCKETS SHIFT ==========

        bucket1.get_bucket().add(circles[0])  # type: ignore
        bucket1.get_bucket().add(circles[1])  # type: ignore
        bucket2.get_bucket().add(circles[2])  # type: ignore
        bucket1.get_bucket().add(circles[3])  # type: ignore
        bucket2.get_bucket().add(circles[4])  # type: ignore
        bucket1.get_bucket().add(circles[5])  # type: ignore

        if self.run_animations:
            self.play(bucket1.get_bucket().animate.shift(
                mn.RIGHT * (bucket1.get_bucket().width + 1)
            ),
                bucket2.get_bucket().animate.shift(
                mn.LEFT * (bucket1.get_bucket().width + 1)
            ))
            self.wait(0.5)
            self.play(bucket2.get_bucket().animate.shift(
                mn.RIGHT * (bucket1.get_bucket().width + 1)
            ),
                bucket1.get_bucket().animate.shift(
                mn.LEFT * (bucket1.get_bucket().width + 1)
            ))
