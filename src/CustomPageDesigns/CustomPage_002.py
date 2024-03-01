from reportlab.lib import colors
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfgen import canvas
from reportlab.platypus import PageTemplate

from Frames.Content import Content_001
from Frames.Headers import Header_001
from Frames.Headings import Heading_001, Heading_002
from Frames.Tables import Table_001
from Frames.Tags import Tag_001
from utils import get_bottom_location, load_fonts

load_fonts()

PAGE_WIDTH, PAGE_HEIGHT = (595, 842)


# DECLARE STYLES
# ------------------------------------------------

style_1 = ParagraphStyle(
    name="style_1",
    fontName="NeueMontreal-Light",
    fontSize=10,
    leading=12,
    textColor=colors.Color(1, 1, 1, 0.5),
)

style_2 = ParagraphStyle(
    name="style_2",
    fontName="NeueMontreal-Light",
    fontSize=10,
    leading=12,
    textColor=colors.Color(1, 1, 1, 1),
)

style_3 = ParagraphStyle(
    name="style_3",
    fontName="NeueMontreal-Regular",
    fontSize=15,
    leading=18,
    textColor=colors.Color(1, 1, 1, 1),
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
    textColor=colors.Color(1, 1, 1, 1),
    splitLongWords=0,
)

style_6 = ParagraphStyle(
    name="style_6",
    fontName="NeueMontreal-Regular",
    fontSize=10,
    leading=12,
    textColor=colors.Color(1, 1, 1, 1),
)

style_7 = ParagraphStyle(
    name="style_7",
    fontFamily="F37ZagmaMonoTrial-Light",
    fontSize=8,
    leading=9.6,
    textColor=colors.Color(1, 1, 1, 0.5),
)

style_8 = ParagraphStyle(
    name="style-8",
    fontName="NeueMontreal-Regular",
    fontSize=20,
    leading=20,
    alignment=TA_JUSTIFY,
    textColor=colors.Color(1, 1, 1, 1),
    splitLongWords=True,
    firstLineIndent=60,
)

style_9 = ParagraphStyle(
    name="style-9",
    fontName="F37ZagmaMonoTrial-Book",
    fontSize=8,
    leading=9.6,
    textColor=colors.Color(0.07, 0.07, 0.07, 0.5),
)

style_10 = ParagraphStyle(
    name="style-10",
    fontName="F37ZagmaMonoTrial-Book",
    fontSize=8,
    leading=9.6,
    textColor=colors.Color(1, 1, 1, 0.5),
)

style_11 = ParagraphStyle(
    name="style-11",
    fontName="NeueMontreal-Light",
    fontSize=8,
    leading=9.6,
    textColor=colors.Color(1, 1, 1, 1),
)

style_12 = ParagraphStyle(
    name="style-11",
    fontName="NeueMontreal-Regular",
    fontSize=8,
    leading=9.6,
    textColor=colors.Color(1, 1, 1, 1),
)


# GENERATE INPUT DATA
# ------------------------------------------------

header_texts = ["Preliminary", "Dismorphism", "Assessment"]
header_styles = [style_1, style_1, style_2]
header_data = [(text, style) for text, style in zip(header_texts, header_styles)]

page_number_data = ("01", style_3)

tag_data = ("SEXUAL DISMORPHISM", style_4)

heading_01_data = ("Assessment Overview", style_5)

heading_02_title_data = ("Next Few Pages", style_6)
headin_02_page_data = ("02/", style_7)

content_text = """Our main goal with Facial
Proportions is to take an overall look at your facial configuration and dimensions. Later in chapter 2 we look into individual proportions, feature-by-feature."""
content_text = content_text.replace("\n", "<br/>")
content_data = (content_text, style_8)

tabledesc_text = "Summary of tests"
tabledesc_data = (tabledesc_text, style_12)

image_text = """FIG 2 : Ratios greater than 1.10 <br/> (i.e. there is a 110% difference between you and the most extreme comparisons) are shown here as they are dimorphic traits."""
image_data = (image_text, style_9)

table_data = [
    ["Table iii", "Raw Result", "Explanation"],
    [
        "Euclidean Matrix Analysis",
        "Saller and colleagues [22]",
        "The subject has a moderately juvenile face.",
    ],
    [
        "Dimorphism Analysis",
        "Edmondson and colleagues [23]",
        "Measuring changes of the face as as masculinity is artificially increased or decreased",
    ],
]

# GENERATE FRAMES
# ------------------------------------------------

header = Header_001(
    text=header_data,
    page=page_number_data,
    separator_gap=8,
    separator_color=colors.Color(1, 1, 1, 0.5),
    line_gap=16,
    line_color=colors.Color(1, 1, 1, 0.1),
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
    bg=colors.Color(0.68, 0.76, 0.79, 1),
    x1=26,
    y1=get_bottom_location(86, 13),
    width=91,
    height=13,
    topPadding=4,
    rightPadding=6,
    bottomPadding=4,
    leftPadding=6,
)

heading_1 = Heading_001(
    text=heading_01_data,
    x1=26,
    y1=get_bottom_location(109, 80),
    width=208,
    height=80,
    topPadding=0,
    rightPadding=0,
    bottomPadding=0,
    leftPadding=0,
)

heading_2 = Heading_002(
    number=headin_02_page_data,
    text=heading_02_title_data,
    gap=10,
    x1=26,
    y1=get_bottom_location(245, 12),
    width=359,
    height=12,
    topPadding=0,
    rightPadding=0,
    bottomPadding=0,
    leftPadding=0,
)

content = Content_001(
    text=content_data,
    num_cols=1,
    gap=11,
    x1=26,
    y1=get_bottom_location(267, 100),
    width=359,
    height=100,
    topPadding=0,
    rightPadding=0,
    bottomPadding=0,
    leftPadding=0,
)

table_desc = Content_001(
    text=tabledesc_data,
    num_cols=1,
    gap=0,
    x1=26,
    y1=get_bottom_location(698, 10),
    width=62,
    height=10,
    topPadding=0,
    rightPadding=0,
    bottomPadding=0,
    leftPadding=0,
)

table = Table_001(
    table_data=table_data,
    colsContentWidth=167,
    headerFormat=style_10,
    contentFormat=style_11,
    x1=26,
    y1=get_bottom_location(716, 76),
    width=543,
    height=76,
    topPadding=0,
    rightPadding=0,
    bottomPadding=0,
    leftPadding=0,
)


# CREATE PAGE
# ------------------------------------------------
page_002_content = [
    header,
    tag,
    heading_1,
    heading_2,
    content,
    table_desc,
    table,
]

if __name__ == "__main__":
    pass
