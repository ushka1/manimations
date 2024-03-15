# pylint: disable=C0114, C0115, C0116

import manim as mn

# mn.config.disable_caching = True


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


def create_balls(colors: list[mn.ManimColor]):
    balls = mn.VGroup()
    for (i, color) in enumerate(colors):
        ball = mn.Circle(
            radius=0.3,
        ).set_fill(color, 1).set_stroke(width=0)

        label = mn.Text(str(i + 1), font_size=36, color=mn.BLACK)
        label.move_to(ball)

        group = mn.VGroup(ball, label)
        group.set_z_index(1)
        balls.add(group)

    balls.arrange(mn.RIGHT)
    return balls


stirling_partitions = [
    [[0], [1, 2, 3, 4]],
    [[1], [0, 2, 3, 4]],
    [[2], [0, 1, 3, 4]],
    [[3], [0, 1, 2, 4]],
    [[4], [0, 1, 2, 3]],

    [[0, 1], [2, 3, 4]],
    [[0, 2], [1, 3, 4]],
    [[0, 3], [1, 2, 4]],
    [[0, 4], [1, 2, 3]],

    [[1, 2], [0, 3, 4]],
    [[1, 3], [0, 2, 4]],
    [[1, 4], [0, 2, 3]],

    [[2, 3], [0, 1, 4]],
    [[2, 4], [0, 1, 3]],

    [[3, 4], [0, 1, 2]],
]


class StirlingII(mn.Scene):
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

        title = mn.Text("Liczby Stirlinga II rodzaju", font_size=24)
        title.to_edge(mn.UP)

        if self.run_animations:
            self.play(mn.FadeIn(title))
        else:
            self.add(title)

        # ========== FORMULA TEXT ==========

        formula = mn.MathTex(
            r"\left\{ {n \atop k} \right\} = S(n,k)",
            font_size=36,
        )
        formula.next_to(title, mn.DOWN).shift(mn.DOWN * 0.5)

        text = mn.Text(
            "Jest to liczba rozmieszczeń n rozróżnialnych kul na k nierozróżnialnych stosach.",
            font_size=18
        )
        text.next_to(formula, mn.DOWN)

        if self.run_animations:
            self.play(mn.FadeIn(formula))
            self.play(mn.FadeIn(text))
        else:
            self.add(formula)
            self.add(text)

        # ========== HIGHLIGHT BALLS TEXT ==========

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

        # ========== BALLS ==========

        balls = create_balls([mn.RED, mn.ORANGE, mn.YELLOW,
                              mn.GREEN, mn.BLUE, mn.PURPLE])
        balls.next_to(text, direction=mn.DOWN,).shift(mn.DOWN * 0.5)

        if self.run_animations:
            self.play(mn.FadeIn(balls))
        else:
            self.add(balls)

        # ========== HIGHLIGHT BUCKETS ==========

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
        bucket_group.next_to(balls, direction=mn.DOWN).shift(mn.DOWN * 0.5)

        if self.run_animations:
            self.play(mn.FadeIn(bucket_group))
        else:
            self.add(bucket_group)

        # ========== BALLS PLACEMENT ==========

        if self.run_animations:
            self.play(
                mn.AnimationGroup(
                    balls[0].animate.move_to(
                        bucket1.get_cell_coords(0, 0)
                    ),
                    balls[1].animate.move_to(
                        bucket1.get_cell_coords(0, 1)
                    ),
                    balls[2].animate.move_to(
                        bucket2.get_cell_coords(0, 0)
                    ),
                    balls[3].animate.move_to(
                        bucket1.get_cell_coords(0, 2)
                    ),
                    balls[4].animate.move_to(
                        bucket2.get_cell_coords(0, 1)
                    ),
                    balls[5].animate.move_to(
                        bucket1.get_cell_coords(0, 3)
                    ),
                    lag_ratio=0.1
                )
            )
            self.wait(1)
        else:
            balls[0].move_to(bucket1.get_cell_coords(0, 0))
            balls[1].move_to(bucket1.get_cell_coords(0, 1))
            balls[2].move_to(bucket2.get_cell_coords(0, 0))
            balls[3].move_to(bucket1.get_cell_coords(0, 2))
            balls[4].move_to(bucket2.get_cell_coords(0, 1))
            balls[5].move_to(bucket1.get_cell_coords(0, 3))

        # ========== BUCKETS SHIFT ==========

        bucket1.get_bucket().add(balls[0])  # type: ignore
        bucket1.get_bucket().add(balls[1])  # type: ignore
        bucket2.get_bucket().add(balls[2])  # type: ignore
        bucket1.get_bucket().add(balls[3])  # type: ignore
        bucket2.get_bucket().add(balls[4])  # type: ignore
        bucket1.get_bucket().add(balls[5])  # type: ignore

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

    def second_scene(self):
        # ========== TITLE ==========

        title = mn.MathTex(
            r"\left\{ {5 \atop 2} \right\} = 15",
            font_size=36,
        )
        title.to_edge(mn.UP)

        if self.run_animations:
            self.play(mn.FadeIn(title))
        else:
            self.add(title)

        # ========== BUCKETS ==========

        group = mn.VGroup()
        data: list[tuple[Bucket, Bucket, mn.VGroup]] = []
        for _ in range(15):
            bucket1 = Bucket(2, 4)
            bucket2 = Bucket(2, 4)
            balls = create_balls(
                [mn.RED, mn.ORANGE, mn.YELLOW, mn.GREEN, mn.BLUE]
            )
            data.append((
                bucket1,
                bucket2,
                balls,
            ))

            b_group = mn.VGroup(
                bucket1.get_bucket(),
                bucket2.get_bucket()
            )
            b_group.arrange(mn.RIGHT, buff=1)
            bc_group = mn.VGroup(balls, b_group)
            bc_group.arrange(mn.DOWN, buff=0.5)
            group.add(bc_group)

        group.scale(0.3)
        group.arrange_in_grid(5, 3, buff=(2, 0.3))
        group.next_to(title, mn.DOWN)

        if self.run_animations:
            self.play(mn.FadeIn(group))
            self.wait(1)
        else:
            self.add(group)

        # ========== BALLS PLACEMENT ==========

        animations: list[mn.Animation] = []
        for e in zip(data, stirling_partitions):
            part1 = e[1][0]
            # part2 = e[1][1]
            i1 = 0
            i2 = 0

            bucket1 = e[0][0]
            bucket2 = e[0][1]
            balls = e[0][2]

            for (i, b) in enumerate(balls):
                if i in part1:
                    animations.append(
                        b.animate.move_to(bucket1.get_cell_coords(0, i1))
                    )
                    i1 += 1
                else:
                    animations.append(
                        b.animate.move_to(bucket2.get_cell_coords(0, i2))
                    )
                    i2 += 1

        if self.run_animations:
            self.play(mn.AnimationGroup(*animations, lag_ratio=0.025))
        else:
            for a in animations:
                a.mobject.move_to(a.mobject.target)
