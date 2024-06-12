# pylint: disable=C0114, C0115, C0116, C0301

import math

import manim as mn
import numpy as np

import utils.theme as theme
from utils.stirling import get_stirling_first_kind

theme.set_theme_defaults()


class StirlingZoomTest(mn.ThreeDScene):
    run_animations = False

    def construct(self):
        self.set_camera_orientation(
            phi=60 * mn.DEGREES, theta=-60 * mn.DEGREES
        )

        x_max = mn.ValueTracker(3)
        y_max = mn.ValueTracker(3)
        z_max = mn.ValueTracker(3)

        axes = mn.always_redraw(lambda: mn.ThreeDAxes(
            x_range=[0, x_max.get_value(), 1],
            y_range=[0, y_max.get_value(), 1],
            z_range=[0, z_max.get_value(), 1],
            x_axis_config={"include_numbers": True},
            y_axis_config={"include_numbers": True},
            z_axis_config={"include_numbers": True},
        ).scale(0.5).center().shift(mn.OUT))

        if self.run_animations:
            self.play(
                mn.FadeIn(axes),
            )
        else:
            self.add(axes)

        if self.run_animations:
            self.play(
                x_max.animate.set_value(10),
                y_max.animate.set_value(10),
                z_max.animate.set_value(10),
            )
        else:
            x_max.set_value(10)
            y_max.set_value(10)
            z_max.set_value(10)
            axes.update()
