# pylint: disable=C0114, C0116


import manim as mn

FONT_SM = 20
FONT_MD = 24
FONT_LG = 32
FONT_XL = 40


def set_defaults():
    mn.Text.set_default(font="Ubuntu", font_size=FONT_SM)
    mn.Tex.set_default(font_size=FONT_LG)
    mn.MathTex.set_default(font_size=FONT_XL)

    # tex polish support
    mn.TexTemplate.add_to_preamble(txt=r"\usepackage{polski}")
    mn.TexTemplate.add_to_preamble(txt=r"\usepackage[utf8]{inputenc}")
    mn.TexTemplate.add_to_preamble(txt=r"\usepackage[T1]{fontenc}")
