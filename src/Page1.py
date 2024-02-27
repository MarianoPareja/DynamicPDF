from reportlab.lib import colors
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas

from Frames.Content import Content_001
from Frames.Grids import ContentGrid, HeaderGrid
from Frames.Headers import Header_001
from Frames.Headings import Heading_001, Heading_002
from Frames.ImageContainer import ImageContainer_001
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
    textColor=colors.Color(0.07, 0.07, 0.07, 0.5),
)
text_style_2 = ParagraphStyle(
    name="style_header_2",
    fontName="NeueMontreal-Light",
    fontSize=10,
    leading=12,
)

texts = ["Preliminary", "Dismorphism", "Theory"]
styles = [text_style_1, text_style_1, text_style_2]
data = [(word, style) for word, style in zip(texts, styles)]

page_style = ParagraphStyle(
    name="page_style_1",
    fontName="NeueMontreal-Regular",
    fontSize=15,
    leading=18,
)
page = ("01", page_style)

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
heading_1_text = "Theory"
heading_1_style = ParagraphStyle(
    name="heading_1_style",
    fontName="NeueMontreal-Medium",
    fontSize=40,
    leading=40,
    textColor=colors.Color(0.07, 0.07, 0.07, 1),
)
heading_1_data = (heading_1_text, heading_1_style)

# HEADING 2 DATA
heading_2_text = "What Is It?"
heading_2_text_style = ParagraphStyle(
    name="heading_2_style",
    fontName="NeueMontreal-Regular",
    fontSize=10,
    leading=12,
    textColor=colors.Color(0.07, 0.07, 0.07, 1),
)
heading_2_data = (heading_2_text, heading_2_text_style)

heading_2_page_text = "01/"
heading_2_page_style = ParagraphStyle(
    name="heading_2_page",
    fontFamily="F37ZagmaMonoTrial-Light",
    fontSize=8,
    leading=9.6,
    textColor=colors.Color(0.07, 0.07, 0.07, 1),
)
page_data = (heading_2_page_text, heading_2_page_style)

# PARAGRAPH DATA
content_text = """Humans have long been fascinated by facial proportions as ultimately these proportions make up the geometry of one’s face. In short, you are your proportions, measurements and ratios.

Following this, it is easy to understand why proportions are so closely linked to beauty. An attractive face by definition would have to have different proportions to an unattractive one as they inherently look different and have different forms. While this idea has held true for millennia, our application of facial proportions has changed.

In the early BC years, Ancient Greeks believed in divine proportions and canons of beauty. Think of the ‘Golden Ratio’, ‘Perfect Thirds,’ or similar and we can link them back to the works of early Hellenistic philosophers. In fact, most famous renaissance works such as Michalengo’s ‘David’ statue followed these proportions of beauty..

However, modern science shows us these proportions of beauty are misguided. They are simply too idealistic to be realistic. Schmid Et al’s research found only a weak link between these Golden Ratios and Neoclassical canons, meaning they are not as closely linked to beauty as humans once thought.

Instead, in contemporary science, plastic surgeons and orthodontists use ‘Modern Anthropometry,’ where instead of relying on arbitrary proportions and one-size-fits-all shapes, we use demographic data of populations to establish the actual proportions that contribute to attractiveness for that group.

For example, the features that makes a <strong>White Male</strong> of <strong>30 years</strong> age attractive, may not necessarily be the same proportions that make a Black Woman of 20 years age attractive, which is why Modern Anthropometry is needed. Clincians must compare apples to apples to be precise."""

content_text = content_text.replace("\n", "<br/>")

content_style = ParagraphStyle(
    name="content-style",
    fontName="NeueMontreal-Light",
    fontSize=10,
    leading=13,
    alignment=TA_JUSTIFY,
    textColor=colors.Color(0.07, 0.07, 0.07, 1),
    splitLongWords=True,
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


def get_bottom_location(top, height, pageHeight=842):
    return pageHeight - height - top


if __name__ == "__main__":
    c = canvas.Canvas("Page1.pdf", bottomup=True, pagesize=(595, 842))

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
        background=colors.Color(0.93, 0.93, 0.93, 1),
        x1=26,
        y1=get_bottom_location(86, 13),
        width=91,
        height=13,
        topPadding=4,
        bottomPadding=4,
        leftPadding=6,
        rightPadding=6,
    )
    tag.handle_content(c)

    heading_1 = Heading_001(
        text=heading_1_data,
        x1=26,
        y1=get_bottom_location(109, 40),
        width=174,
        height=40,
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
        x1=210,
        y1=get_bottom_location(109, 12),
        width=174,
        height=12,
        topPadding=0,
        rightPadding=0,
        bottomPadding=0,
        leftPadding=0,
    )
    heading_2.handle_content(c)

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
    content.handle_content(c)

    image = ImageContainer_001(
        text=image_data,
        images_file=[
            "./Images/6e17f9cce757f63a4d822adc336ea5f6.jpeg",
            "./Images/6e17f9cce757f63a4d822adc336ea5f6.jpeg",
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
    image.handle_content(c)

    # Grids

    headerGrid = HeaderGrid(
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
    headerGrid.drawGrid(c)

    contentGrid = ContentGrid(
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
    contentGrid.drawGrid(c)

    c.save()
