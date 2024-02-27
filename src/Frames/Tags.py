from reportlab.lib import colors
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.platypus import Frame, Paragraph

from Frames.CustomFrame import CustomFrame
from utils import align_text


class Tag_001(CustomFrame):
    def __init__(self, text, background, *args, **kwargs):
        """
        :param text(tuple): Tuple containing (text, ParagraphStyle)
        :param background(reportlab.lib.colors.Color): RGBA values corresponding to the background color
        """

        if not isinstance(background, colors.Color):
            raise ValueError(
                "Expected %s type for background, got %s",
                type(colors.Color),
                type(background),
            )

        super().__init__(*args, **kwargs)
        self.text = text
        self.background = background

    def handle_content(self, canvas):

        canvas.setFillColor(self.background)
        canvas.setLineWidth(0)
        canvas.rect(self._x1, self._y1, self._width, self._height, fill=True)

        xP = self._x1 + self._leftPadding
        yP = self._y1 + self._bottomPadding

        x, y = xP, yP

        y = yP + align_text(
            self.text[1].fontName,
            self.text[1].fontSize,
            self._aH,
            alignment="CENTERLINE",
        )

        para = Paragraph(self.text[0], self.text[1])
        w, h = para.wrap(
            availWidth=stringWidth(
                self.text[0], self.text[1].fontName, self.text[1].fontSize
            ),
            availHeight=self._aH,
        )
        para.drawOn(canvas, x, y)


###
# text = "SEXUAL DISMORPHISM"

# if __name__ == "__main__":
#     c = canvas.Canvas("tesing_heading.pdf", pagesize=letter)

#     width = 40 * mm
#     height = 8 * mm

#     style = ParagraphStyle(
#         name="Style",
#         fontName="Helvetica",
#         fontSize=8,
#         leading=12,
#     )

#     data = (text, style)

#     frame = Tag_001(
#         text=data,
#         background=colors.Color(0.3, 0.3, 0.9, 0.4),
#         x1=100 * mm,
#         y1=100 * mm,
#         width=width,
#         height=height,
#         leftPadding=0,
#         bottomPadding=0,
#         rightPadding=0,
#         topPadding=0,
#     )

#     frame.handle_content(c)
#     c.save()
