from reportlab.platypus import PageTemplate

from src.CustomPageDesigns.CustomPage_001 import header

pageTemplate = PageTemplate(id="pageTemplate001")

# Header Frames
data = header.handle_content()

print(data)
