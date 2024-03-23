# pylint: disable=C0114, C0116


import manim as mn

FONT_SM = 20
FONT_MD = 24
FONT_LG = 32
FONT_XL = 40


TEX_TEMPLATE = mn.TexTemplate()
TEX_TEMPLATE.add_to_preamble(r"\PassOptionsToPackage{T1}{fontenc}")
TEX_TEMPLATE.add_to_preamble(r"\PassOptionsToPackage{polish}{babel}")
TEX_TEMPLATE.add_to_preamble(r"\PassOptionsToPackage{utf8}{inputenc}")
TEX_TEMPLATE.add_to_preamble(r"\usepackage{fontenc}")
TEX_TEMPLATE.add_to_preamble(r"\usepackage{babel}")
TEX_TEMPLATE.add_to_preamble(r"\usepackage{inputenc}")


def set_theme_defaults():
    mn.Text.set_default(font="Ubuntu", font_size=FONT_SM)
    mn.Tex.set_default(font_size=FONT_LG)
    mn.MathTex.set_default(font_size=FONT_XL)
