from typing import Optional

from reportlab.lib import colors
from reportlab.platypus import PageTemplate


class CustomPageTemplate(PageTemplate):
    def __init__(self, bg_color: Optional[colors.Color], *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bg_color = bg_color


    def onPage(self, canvas):


        # LOS FRAMES SOLO DEFINEN LOS ESPACIOS
        