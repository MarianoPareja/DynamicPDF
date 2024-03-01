import os

from reportlab.lib.colors import Color
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.pdfmetrics import getAscentDescent, registerFontFamily
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import FrameBreak

FONTS_PATH = os.path.join(os.path.abspath("./"), "Fonts/")


def load_fonts(fonts_dir=FONTS_PATH):
    """
    Loads all the fonts file in give directory. Expects the following naming convention "FamilyName-Type.ttf"

    param fonts_dir: Directory containing all the fonts files
    """

    fonts_list = os.listdir(fonts_dir)
    fonts_list.sort()

    while fonts_list:

        # Clear variables
        family_name = None
        normal = None
        bold = None
        italic = None
        boldItalic = None

        cond = True

        while cond:
            font_file = fonts_list.pop(0)
            family_name = font_file.split("-")[0]
            font_name = font_file.split(".")[0]

            font_type = font_name.split("-")[1].lower()
            if font_type == "normal":
                normal = font_name
            elif font_type == "bold":
                bold = font_name
            elif font_type == "italic":
                italic = font_name
            elif font_type == "boldItalic":
                boldItalic = font_name

            pdfmetrics.registerFont(
                TTFont(font_name, os.path.join(fonts_dir, font_file))
            )

            if not fonts_list or fonts_list[0].split("-")[0] != family_name:
                cond = False
                registerFontFamily(
                    family=family_name,
                    normal=normal,
                    bold=bold,
                    italic=italic,
                    boldItalic=boldItalic,
                )


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


def generate_content(content_list: list, frames: list, stories: list):
    for i, obj in enumerate(content_list):
        obj_frames, obj_flowables = obj.handle_content()
        frames.extend(obj_frames)
        stories.extend(obj_flowables)

        if i != len(content_list) - 1:
            stories.append(FrameBreak)

    return (frames, stories)


def setBackgroundColor(canvas, doc):
    color = Color(35 / 255, 49 / 255, 55 / 255)
    canvas.setFillColor(color)
    canvas.rect(
        0,
        0,
        doc.width + doc.leftMargin + doc.rightMargin,
        doc.height + doc.topMargin + doc.bottomMargin,
        fill=True,
        stroke=False,
    )
