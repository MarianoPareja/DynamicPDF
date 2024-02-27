import os

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.pdfmetrics import getAscentDescent
from reportlab.pdfbase.ttfonts import TTFont

FONTS_PATH = os.path.join(os.path.dirname(os.path.abspath("./")), "Fonts/")
# FONTS_PATH = os.path.join(os.path.abspath("./"), "Fonts/")


def load_fonts():
    for font_file in os.listdir(FONTS_PATH):
        font_name = font_file.split(".")[0]
        pdfmetrics.registerFont(TTFont(font_name, os.path.join(FONTS_PATH, font_file)))


def align_text(fontName, fontSize, windowHeight, alignment):
    """
    Get Y Coordinate of the text baseline considering the baseline is at left-bottom corner (0,0)

    :param alignment: Where the text will be aligned ("TOPLINE","CENTERLINE","DESCENTLINE")
    :return y: Coordinate of the baseline
    """
    ascent, descent = getAscentDescent(fontName, fontSize)
    font_height = ascent - descent

    if alignment == "TOPLINE":
        y = windowHeight - font_height
    elif alignment == "CENTERLINE":
        y = (windowHeight - font_height) / 2
    elif alignment == "DESCENTLINE":
        y = descent
    else:
        raise ValueError("Invalid alignment position, got %s", alignment)

    return y


def get_bottom_location(top, height, pageHeight=842):
    return pageHeight - height - top
