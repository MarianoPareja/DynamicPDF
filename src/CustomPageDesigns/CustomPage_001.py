import os

from reportlab.lib import colors
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfgen import canvas
from reportlab.platypus import PageTemplate

# FRAMES TEMPLATES
from Frames.Content import Content_001
from Frames.Grids import ContentGrid, HeaderGrid
from Frames.Headers import Header_001
from Frames.Headings import Heading_001, Heading_002
from Frames.ImageContainer import ImageContainer_001
from Frames.Tags import Tag_001
from utils import generate_content, get_bottom_location, load_fonts

load_fonts()

IMAGES_PATH = os.path.join(os.path.dirname(os.path.abspath("./")), "Images/")

PAGE_WIDTH, PAGE_HEIGHT = (595, 842)

# DECLARE STYLES
# ------------------------------------------------

style_1 = ParagraphStyle(
    name="style_1",
    fontName="NeueMontreal-Light",
    fontSize=10,
    leading=12,
    textColor=colors.Color(0.07, 0.07, 0.07, 0.5),
)

style_2 = ParagraphStyle(
    name="style_2",
    fontName="NeueMontreal-Light",
    fontSize=10,
    leading=12,
    textColor=colors.Color(0.07, 0.07, 0.07, 1),
)

style_3 = ParagraphStyle(
    name="style_3",
    fontName="NeueMontreal-Regular",
    fontSize=15,
    leading=18,
)

style_4 = ParagraphStyle(
    name="style_4",
    fontName="F37ZagmaMonoTrial-Light",
    fontSize=8,
    leading=8.72,
)

style_5 = ParagraphStyle(
    name="style_5",
    fontName="NeueMontreal-Medium",
    fontSize=40,
    leading=40,
    textColor=colors.Color(0.07, 0.07, 0.07, 1),
)

style_6 = ParagraphStyle(
    name="style_6",
    fontName="NeueMontreal-Regular",
    fontSize=10,
    leading=12,
    textColor=colors.Color(0.07, 0.07, 0.07, 1),
)

style_7 = ParagraphStyle(
    name="style_7",
    fontFamily="F37ZagmaMonoTrial-Light",
    fontSize=8,
    leading=9.6,
    textColor=colors.Color(0.07, 0.07, 0.07, 0.5),
)

style_8 = ParagraphStyle(
    name="style-8",
    fontName="NeueMontreal-Light",
    fontSize=10,
    leading=13,
    alignment=TA_JUSTIFY,
    textColor=colors.Color(0.07, 0.07, 0.07, 1),
    splitLongWords=False,
)

style_9 = ParagraphStyle(
    name="style-9",
    fontName="F37ZagmaMonoTrial-Book",
    fontSize=8,
    leading=9.6,
    textColor=colors.Color(0.07, 0.07, 0.07, 0.5),
)

# GENERATE INPUT DATA
# ------------------------------------------------

header_texts = [
    "Preliminary",
    "Dismorphism",
    "Assessment",
]
header_styles = [style_1, style_1, style_2]
header_data = [(text, style) for text, style in zip(header_texts, header_styles)]

page_number_data = ("01", style_3)

tag_data = ("SEXUAL DISMORPHISM", style_4)

heading_01_data = ("Theory", style_5)

heading_02_title_data = ("What Is It?", style_6)
headin_02_page_data = ("01/", style_7)

content_text = """Humans have long been fascinated by facial proportions as ultimately these proportions make up the geometry of one’s face. In short, you are your proportions, measurements and ratios.

Following this, it is easy to understand why proportions are so closely linked to beauty. An attractive face by definition would have to have different proportions to an unattractive one as they inherently look different and have different forms. While this idea has held true for millennia, our application of facial proportions has changed.

In the early BC years, Ancient Greeks believed in divine proportions and canons of beauty. Think of the ‘Golden Ratio’, ‘Perfect Thirds,’ or similar and we can link them back to the works of early Hellenistic philosophers. In fact, most famous renaissance works such as Michalengo’s ‘David’ statue followed these proportions of beauty..

However, modern science shows us these proportions of beauty are misguided. They are simply too idealistic to be realistic. Schmid Et al’s research found only a weak link between these Golden Ratios and Neoclassical canons, meaning they are not as closely linked to beauty as humans once thought.

Instead, in contemporary science, plastic surgeons and orthodontists use ‘Modern Anthropometry,’ where instead of relying on arbitrary proportions and one-size-fits-all shapes, we use demographic data of populations to establish the actual proportions that contribute to attractiveness for that group.

For example, the features that makes a <b>White Male</b> of <u>30 years</u> age attractive, may not necessarily be the same proportions that make a <u>Black Woman</u> of <u>20 years age</u> attractive, which is why Modern Anthropometry is needed. Clincians must compare apples to apples to be precise."""
content_text = content_text.replace("\n", "<br/>")
content_data = (content_text, style_8)

image_text = """FIG 2 : Ratios greater than 1.10 <br/> (i.e. there is a 110% difference between you and the most extreme comparisons) are shown here as they are dimorphic traits."""
image_data = (image_text, style_9)


# GENERATE FRAMES
# ------------------------------------------------
header = Header_001(
    text=header_data,
    page=page_number_data,
    separator_gap=8,
    separator_color=colors.Color(18 / 255, 18 / 255, 18 / 255, 0.2),
    line_gap=16,
    line_color=colors.Color(18 / 255, 18 / 255, 18 / 255, 0.1),
    x1=26,
    y1=get_bottom_location(16, 30),
    width=543,
    height=30,
    topPadding=6,
    bottomPadding=6,
    leftPadding=0,
    rightPadding=0,
)

tag = Tag_001(
    text=tag_data,
    bg=colors.Color(0.93, 0.93, 0.93, 1),
    x1=26,
    y1=get_bottom_location(86, 13),
    width=91,
    height=13,
    topPadding=4,
    bottomPadding=4,
    leftPadding=6,
    rightPadding=6,
)

heading_1 = Heading_001(
    text=heading_01_data,
    x1=26,
    y1=get_bottom_location(109, 40),
    width=174,
    height=40,
    topPadding=0,
    rightPadding=0,
    bottomPadding=0,
    leftPadding=0,
)

heading_2 = Heading_002(
    number=headin_02_page_data,
    text=heading_02_title_data,
    gap=10,
    x1=210,
    y1=get_bottom_location(109, 12),
    width=174,
    height=12,
    topPadding=0,
    rightPadding=0,
    bottomPadding=0,
    leftPadding=0,
)

content = Content_001(
    text=content_data,
    num_cols=2,
    gap=11,
    x1=210,
    y1=get_bottom_location(131, 338),
    width=359,
    height=338,
    topPadding=0,
    rightPadding=0,
    bottomPadding=0,
    leftPadding=0,
)

image = ImageContainer_001(
    text=image_data,
    images_file=[
        os.path.join(IMAGES_PATH, "6e17f9cce757f63a4d822adc336ea5f6.jpeg"),
        os.path.join(IMAGES_PATH, "6e17f9cce757f63a4d822adc336ea5f6.jpeg"),
    ],
    gap=10,
    x1=26,
    y1=get_bottom_location(630, 171),
    width=543,
    height=171,
    topPadding=0,
    rightPadding=0,
    bottomPadding=0,
    leftPadding=0,
)

header_grid = HeaderGrid(
    color=colors.Color(255, 0, 0, 0.5),
    lineWidth=0.5,
    x1=16,
    y1=get_bottom_location(16, 30),
    width=563,
    height=30,
    topPadding=0,
    rightPadding=0,
    bottomPadding=0,
    leftPadding=0,
)

content_grid = ContentGrid(
    color=colors.Color(255, 0, 0, 0.5),
    lineWidth=0.5,
    gapWidth=10,
    numCols=12,
    numRows=12,
    x1=16,
    y1=get_bottom_location(16, 796),
    width=563,
    height=736,
    topPadding=0,
    rightPadding=0,
    bottomPadding=0,
    leftPadding=0,
)

# CREATE PAGE
# ------------------------------------------------
page_001_content = [
    header,
    tag,
    heading_1,
    heading_2,
    content,
    header_grid,
    content_grid,
    image,
]


if __name__ == "__main__":
    pass
