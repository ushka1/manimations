from typing import List

import manim as mn


def color_change(scene: mn.Scene, items: List[mn.Group], color: mn.ManimColor):
    scene.play(
        *[i.animate.set_color(color) for i in items],
        *[mn.Circumscribe(i, color=color) for i in items]
    )
