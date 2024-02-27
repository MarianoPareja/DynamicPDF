from reportlab.platypus import PageTemplate


class CustomPageTemplate(PageTemplate):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
