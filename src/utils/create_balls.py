# pylint: disable=C0114, C0115, C0116, C0301

import manim as mn


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
