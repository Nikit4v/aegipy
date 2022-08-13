import numpy as np

from src.style import Style, BorderStyle


def test_style_validation():
    s = Style(
        name="test_style",
        fontname="fontname",
        fontsize=12,
        primary_color=(255, 255, 0),
        secondary_colour=(255, 255, 0),
        outline_colour=(255, 255, 0),
        background_colour=(255, 255, 0),
        italic=False,
        bold=False,
        underline=False,
        strike_out=False,
        scale=(1., 0.5),
        spacing=0,
        angle=0,
        border_style=BorderStyle.Normal
    )
