from reportlab.lib.colors import Color
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    FrameBreak,
    PageTemplate,
    Paragraph,
)

from CustomPageDesigns.CustomPage_001 import header
from utils import get_bottom_location

header_frames, header_flowables = header.handle_content()

PAGE_WIDTH, PAGE_HEIGHT = (595, 842)
page_size = (PAGE_WIDTH, PAGE_HEIGHT)

frame_1 = Frame(
    x1=26, y1=get_bottom_location(16, 30), width=543, height=30, showBoundary=1
)

frame_2 = Frame(
    x1=26, y1=get_bottom_location(86, 13), width=91, height=13, showBoundary=1
)

frame_3 = Frame(
    x1=26, y1=get_bottom_location(109, 40), width=174, height=40, showBoundary=1
)

frame_4 = Frame(
    x1=210, y1=get_bottom_location(109, 12), width=174, height=12, showBoundary=1
)

frame_5 = Frame(
    x1=210, y1=get_bottom_location(131, 338), width=359, height=338, showBoundary=1
)

frame_6 = Frame(
    x1=26, y1=get_bottom_location(630, 171), width=543, height=171, showBoundary=1
)

page_1 = PageTemplate(frames=[frame_1, frame_2, frame_3, frame_4, frame_5, frame_6])

stories = [FrameBreak] * 6

doc = BaseDocTemplate("Document.pdf")
doc.addPageTemplates(page_1)
doc.build(stories)
