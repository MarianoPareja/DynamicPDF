from reportlab.platypus import (
    BaseDocTemplate,
    FrameBreak,
    NextPageTemplate,
    PageTemplate,
)

from CustomPageDesigns.CustomPage_001 import page_001_content
from CustomPageDesigns.CustomPage_002 import page_002_content
from utils import generate_content, setBackgroundColor

PAGE_WIDTH, PAGE_HEIGHT = (595, 842)
page_size = (PAGE_WIDTH, PAGE_HEIGHT)

page_001_frames, page_001_stories = [], []
generate_content(page_001_content, page_001_frames, page_001_stories)

page_002_frames, page_002_stories = [], []
generate_content(page_002_content, page_002_frames, page_002_stories)

page_1 = PageTemplate(id="Page_1", frames=page_001_frames, pagesize=page_size)
page_2 = PageTemplate(
    id="Page_2", frames=page_002_frames, pagesize=page_size, onPage=setBackgroundColor
)

stories = []
stories.extend(page_001_stories)
stories.append(NextPageTemplate("Page_2"))
stories.extend(page_002_stories)

doc = BaseDocTemplate(
    filename="Document.pdf",
    leftMargin=0,
    rightMargin=0,
    topMargin=0,
    bottomMargin=0,
)
doc.addPageTemplates(page_1)
doc.addPageTemplates(page_2)

doc.build(stories)
