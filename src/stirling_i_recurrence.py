# pylint: disable=C0114, C0115, C0116, C0301

import manim as mn

import utils.theme as theme
from utils.animations import color_change

theme.set_theme_defaults()


class StirlingIRecurrence(mn.Scene):
    run_animations = True

    def construct(self):
        # ========== SCENES ==========

        self.first_scene()
        if self.run_animations:
            self.wait(5)
            self.play(mn.FadeOut(*self.mobjects))
        self.remove(*self.mobjects)

    def first_scene(self):
        # ========== TITLE ==========

        title = mn.Text('Liczby Stirlinga I rodzaju - rekurencja',
                        font_size=theme.FONT_LG)
        title.to_edge(mn.UP)

        if self.run_animations:
            self.play(mn.FadeIn(title))
        else:
            self.add(title)

        # ========== TEXT ==========

        text = mn.Paragraph(
            'Przyjmijmy za znaczenie liczb Stirlinga I rodzaju ilość rozmieszczeń n liczb w k cyklach.\n' +
            'Wybierzmy dowolną liczbę i rozpatrzmy ilość pozostałych cykli.',
            alignment='center',
            line_spacing=0.75
        )
        text.next_to(title, mn.DOWN, buff=0.5)

        if self.run_animations:
            self.play(
                mn.FadeIn(text),
            )
        else:
            self.add(text)

        # ========== DESCRIPTION 1 ==========

        desc1 = mn.Paragraph(
            'Jeżeli wybrana liczba jest w cyklu jednoelementowym, to pozostałe n-1 liczb jest\n' +
            'rozmieszczonych w k-1 cyklach. Wybraną liczbę można wstawić na 1 sposób,\n' +
            'poprzez stworzenie jednoelemenotwego cyklu.',
            alignment='center',
            line_spacing=0.75
        )
        desc1.scale(0.75)
        desc1.next_to(text, mn.DOWN, buff=0.75)

        # ========== FORMULA ==========

        formula = mn.MathTex(
            r'\begin{bmatrix} \ n \ \\ \ k \ \end{bmatrix} = \begin{bmatrix} \ n - 1 \ \\ \ k - 1 \ \end{bmatrix} + (n-1) \begin{bmatrix} \ n - 1 \ \\ \ k \ \end{bmatrix}',
        )
        formula.next_to(desc1, mn.DOWN, buff=1)

        # ========== DESCRIPTION 2 ==========

        desc2 = mn.Paragraph(
            'Jeżeli wybrana liczba jest w cyklu wieloelementowym, to pozostałe n-1 liczb jest \n' +
            'rozmieszczonych w k cyklach. Wybraną liczbę można wstawić na n-1 sposobów,\n' +
            'gdyż możemy ją wstawić do dowolnego cyklu na dowolny sposób,\n' +
            'czyli \'obok\' każdej z n-1 pozostałych liczb.',
            alignment='center',
            line_spacing=0.75,
        )
        desc2.scale(0.75)
        desc2.next_to(formula, mn.DOWN, buff=1)

        # ========== ARROWS ==========

        point1 = formula[0][5].get_top()
        point2 = formula[0][19].get_bottom()

        arrow1 = mn.Arrow(
            start=[point1[0], desc1.get_bottom()[1], 0],
            end=point1
        )

        arrow2 = mn.Arrow(
            start=[point2[0], desc2.get_top()[1], 0],
            end=point2
        )

        # ========== ANIMATE 1 ==========

        f1 = formula[0][1]
        t1 = text[0][60:66]
        f2 = formula[0][2]
        t2 = text[0][67:75]
        if self.run_animations:
            self.play(
                mn.FadeIn(formula),
            )
            self.wait(1)
            color_change(self, [f1, t1], mn.BLUE)
            self.wait(1)
            color_change(self, [f2, t2], mn.ORANGE)
            self.wait(5)
        else:
            self.add(formula)
            f1.set_color(mn.BLUE)
            t1.set_color(mn.BLUE)
            f2.set_color(mn.ORANGE)
            t2.set_color(mn.ORANGE)

        # ========== ANIMATE 2 ==========

        d1 = desc1[0][57:65]
        f1 = formula[0][6:9]
        d2 = desc1[1][16:26]
        f2 = formula[0][9:12]
        if self.run_animations:
            self.play(
                mn.FadeIn(desc1),
                mn.FadeIn(arrow1),
            )
            self.wait(1)
            color_change(self, [d1, f1], mn.PINK)
            self.wait(1)
            color_change(self, [d2, f2], mn.RED)
            self.wait(5)
        else:
            self.add(desc1)
            self.add(arrow1)
            d1.set_color(mn.PINK)
            f1.set_color(mn.PINK)
            d2.set_color(mn.RED)
            f2.set_color(mn.RED)

        # ========== ANIMATE 3 ==========

        d1 = desc2[0][57:65]
        f1 = formula[0][20:23]
        d2 = desc2[1][16:24]
        f2 = formula[0][23:24]
        d3 = desc2[1][52:63]
        f3 = formula[0][15:18]
        if self.run_animations:
            self.play(
                mn.FadeIn(desc2),
                mn.FadeIn(arrow2),
            )
            self.wait(1)
            color_change(self, [d1, f1], mn.PINK)
            self.wait(1)
            color_change(self, [d2, f2], mn.RED)
            self.wait(1)
            color_change(self, [d3, f3], mn.YELLOW)
        else:
            self.add(desc2)
            self.add(arrow2)
            d1.set_color(mn.PINK)
            f1.set_color(mn.PINK)
            d2.set_color(mn.RED)
            f2.set_color(mn.RED)
            d3.set_color(mn.YELLOW)
            f3.set_color(mn.YELLOW)
