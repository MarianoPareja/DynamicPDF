from reportlab.lib import colors
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph, TableStyle

from Frames.Content import Content_001
from Frames.Grids import ContentGrid, HeaderGrid
from Frames.Headers import Header_001
from Frames.Headings import Heading_001, Heading_002
from Frames.ImageContainer import ImageContainer_001
from Frames.Tables import Table_001
from Frames.Tags import Tag_001
from utils import load_fonts

load_fonts()

# First page
page_width = 595
page_height = 842

### Header 1
text_style_1 = ParagraphStyle(
    name="style_header_1",
    fontName="NeueMontreal-Light",
    fontSize=10,
    leading=12,
    textColor=colors.Color(1, 1, 1, 0.5),
)
text_style_2 = ParagraphStyle(
    name="style_header_2",
    fontName="NeueMontreal-Light",
    fontSize=10,
    leading=12,
    textColor=colors.Color(1, 1, 1, 1),
)

texts = ["Preliminary", "Dismorphism", "Theory"]
styles = [text_style_1, text_style_1, text_style_2]
data = [(word, style) for word, style in zip(texts, styles)]

page_style = ParagraphStyle(
    name="page_style_1",
    fontName="NeueMontreal-Regular",
    fontSize=15,
    leading=18,
    textColor=colors.Color(1, 1, 1, 1),
)
page = ("02", page_style)

## TAG DATA

tag_text = "SEXUAL DISMORPHISM"
tag_style = ParagraphStyle(
    name="tag_style_1",
    fontName="F37ZagmaMonoTrial-Light",
    fontSize=8,
    leading=8.72,
)
tag_data = (tag_text, tag_style)


# HEADING 1 DATA
heading_1_text = "Assesment Overview"
heading_1_style = ParagraphStyle(
    name="heading_1_style",
    fontName="NeueMontreal-Medium",
    fontSize=40,
    leading=40,
    textColor=colors.Color(1, 1, 1, 1),
)
heading_1_data = (heading_1_text, heading_1_style)

# HEADING 2 DATA
heading_2_text = "Next Few Pages"
heading_2_text_style = ParagraphStyle(
    name="heading_2_style",
    fontName="NeueMontreal-Regular",
    fontSize=10,
    leading=12,
    textColor=colors.Color(1, 1, 1, 1),
)
heading_2_data = (heading_2_text, heading_2_text_style)

heading_2_page_text = "02/"
heading_2_page_style = ParagraphStyle(
    name="heading_2_page",
    fontFamily="F37ZagmaMonoTrial-Light",
    fontSize=8,
    leading=9.6,
    textColor=colors.Color(1, 1, 1, 0.5),
)
page_data = (heading_2_page_text, heading_2_page_style)

# PARAGRAPH DATA
content_text = """Our main goal with Facial
Proportions is to take an overall look at your facial configuration and dimensions. Later in chapter 2 we look into individual proportions, feature-by-feature."""

content_text = content_text.replace("\n", "<br/>")

content_style = ParagraphStyle(
    name="content-style",
    fontName="NeueMontreal-Regular",
    fontSize=20,
    leading=20,
    alignment=TA_JUSTIFY,
    textColor=colors.Color(1, 1, 1, 1),
    splitLongWords=True,
    firstLineIndent=60,
)
content_data = (content_text, content_style)

# IMAGES DATA
image_text = """FIG 2 : Ratios greater than 1.10 <br/> (i.e. there is a 110% difference between you and the most extreme comparisons) are shown here as they are dimorphic traits."""
image_style = ParagraphStyle(
    name="image-style",
    fontName="F37ZagmaMonoTrial-Book",
    fontSize=8,
    leading=9.6,
    textColor=colors.Color(0.07, 0.07, 0.07, 0.5),
)
image_data = (image_text, image_style)

# TABLE DATA

header_format = ParagraphStyle(
    name="header-table-style",
    fontName="F37ZagmaMonoTrial-Book",
    fontSize=8,
    leading=9.6,
    textColor=colors.Color(1, 1, 1, 0.5),
)

content_format = ParagraphStyle(
    name="content-style",
    fontName="NeueMontreal-Light",
    fontSize=8,
    leading=9.6,
    textColor=colors.Color(1, 1, 1, 1),
)

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


def get_bottom_location(top, height, pageHeight=842):
    return pageHeight - height - top


if __name__ == "__main__":
    c = canvas.Canvas("Page2.pdf", bottomup=True, pagesize=(595, 842))
    c.setFillColor(colors.Color(0.14, 0.19, 0.22, 1))
    c.rect(0, 0, 595, 842, fill=True)

    header = Header_001(
        text=data,
        page=page,
        separator=".",
        separator_gap=8,
        line_gap=16,
        x1=26,
        y1=get_bottom_location(16, 30),
        width=543,
        height=30,
        topPadding=6,
        bottomPadding=6,
        leftPadding=0,
        rightPadding=0,
    )
    header.handle_content(c)

    tag = Tag_001(
        text=tag_data,
        background=colors.Color(0.68, 0.76, 0.79, 1),
        x1=26,
        y1=get_bottom_location(86, 13),
        width=91,
        height=13,
        topPadding=4,
        rightPadding=6,
        bottomPadding=4,
        leftPadding=6,
    )
    tag.handle_content(c)

    heading_1 = Heading_001(
        text=heading_1_data,
        x1=26,
        y1=get_bottom_location(109, 80),
        width=208,
        height=80,
        topPadding=0,
        rightPadding=0,
        bottomPadding=0,
        leftPadding=0,
    )
    heading_1.handle_content(c)

    heading_2 = Heading_002(
        number=page_data,
        text=heading_2_data,
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
    heading_2.handle_content(c)

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
    content.handle_content(c)

    table = Table_001(
        table_data=table_data,
        colsContentWidth=167,
        headerFormat=header_format,
        contentFormat=content_format,
        x1=26,
        y1=get_bottom_location(716, 76),
        width=543,
        height=76,
        topPadding=0,
        rightPadding=0,
        bottomPadding=0,
        leftPadding=0,
    )
    table.handle_data(c)

    # Grids

    # headerGrid = HeaderGrid(
    #     color=colors.Color(255, 0, 0, 0.5),
    #     lineWidth=0.5,
    #     x1=16,
    #     y1=get_bottom_location(16, 30),
    #     width=563,
    #     height=30,
    #     topPadding=0,
    #     rightPadding=0,
    #     bottomPadding=0,
    #     leftPadding=0,
    # )
    # headerGrid.drawGrid(c)

    # contentGrid = ContentGrid(
    #     color=colors.Color(255, 0, 0, 0.5),
    #     lineWidth=0.5,
    #     gapWidth=10,
    #     numCols=12,
    #     numRows=12,
    #     x1=16,
    #     y1=get_bottom_location(16, 796),
    #     width=563,
    #     height=736,
    #     topPadding=0,
    #     rightPadding=0,
    #     bottomPadding=0,
    #     leftPadding=0,
    # )
    # contentGrid.drawGrid(c)

    c.save()
