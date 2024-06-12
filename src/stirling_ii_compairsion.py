# pylint: disable=C0114, C0115, C0116, C0301

import math

import manim as mn
import numpy as np

import utils.theme as theme
from utils.stirling import get_stirling_second_kind

theme.set_theme_defaults()


class StirlingIICompairsion(mn.ThreeDScene):
    run_animations = True

    def construct(self):
        self.first_scene()
        if self.run_animations:
            self.wait(5)
            self.play(mn.FadeOut(*self.mobjects))
        self.remove(*self.mobjects)

    def first_scene(self):
        self.set_camera_orientation(
            phi=60 * mn.DEGREES, theta=-60 * mn.DEGREES
        )

        n_max = 8
        k_max = 8
        scaler = 250

        N = np.arange(0, n_max + 1, 1)
        K = np.arange(0, k_max + 1, 1)

        N_grid, K_grid = np.meshgrid(N, K)
        S = np.vectorize(get_stirling_second_kind)(N_grid, K_grid)
        S = S / scaler

        axes = mn.ThreeDAxes(
            x_range=[0, n_max + 1, 1],
            y_range=[0, k_max + 1, 1],
            z_range=[0, math.ceil(S.max()), 1],
        )

        labels = axes.get_axis_labels(
            x_label=mn.MathTex("k").scale(3),
            y_label=mn.MathTex("n").scale(3),
            z_label=mn.MathTex("S(n, k)").scale(3)
        )

        ticks = mn.VGroup()
        for n in N:
            x, y, _ = axes.coords_to_point(n, 0, 0)
            tick = mn.Text(str(n)).scale(2)
            tick.move_to((x, y, 0))
            tick.shift(mn.DOWN * 1)
            ticks.add(tick)
        for k in K:
            x, y, _ = axes.coords_to_point(0, k, 0)
            tick = mn.Text(str(k)).scale(2)
            tick.move_to((x, y, 0))
            tick.shift(mn.LEFT * 1)
            ticks.add(tick)
        for s in range(math.ceil(S.max())):
            x, y, z = axes.coords_to_point(0, 0, s)
            tick = mn.Text(str(s * scaler)).scale(2)
            tick.move_to((x, y, z))
            tick.rotate(90 * mn.DEGREES, axis=mn.X_AXIS)
            tick.rotate(45 * mn.DEGREES, axis=mn.Z_AXIS)
            tick.shift(mn.LEFT * 1 + mn.DOWN * 1)
            ticks.add(tick)

        bars = mn.VGroup()
        for n in N:
            for k in K:
                s = S[n][k]
                b = mn.Prism(
                    dimensions=(0.75, 0.75, s),
                    fill_opacity=0.5,
                )
                x, y, _ = axes.coords_to_point(n, k, 0)
                z = s / 2
                b.move_to((x, y, z))
                bars.add(b)

        labels[1].shift(mn.UP * 3)
        labels[2].rotate(45 * mn.DEGREES, axis=mn.Z_AXIS)

        group = mn.VGroup(axes, labels, bars, ticks)
        group.scale(0.5)
        group.center()
        group.shift(mn.OUT * 1)

        if self.run_animations:
            self.play(
                mn.Create(axes),
                run_time=3,
            )
            self.play(
                mn.Create(labels),
                run_time=3,
            )
            self.play(
                mn.Create(ticks),
                run_time=3,
            )
            self.play(
                mn.Create(bars),
                run_time=6,
            )
        else:
            self.add(group)

        if self.run_animations:
            rate = -0.5
            deg = 360 * mn.DEGREES
            self.begin_ambient_camera_rotation(
                rate=rate
            )
            self.wait(deg / abs(rate))
            self.stop_ambient_camera_rotation()
