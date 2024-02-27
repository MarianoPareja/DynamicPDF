from reportlab.lib import colors
from reportlab.pdfbase.pdfmetrics import getFont, stringWidth
from reportlab.platypus import Frame, Paragraph

from utils import align_text


class Heading_001(Frame):
    def __init__(
        self,
        text,
        *args,
        **kwargs,
    ):
        """
        Headind Model 001

        """
        super().__init__(*args, **kwargs)
        self.text = text

    def handle_content(self, canvas):
        """
        Heading 001 Style
        """
        # Visualize area
        # canvas.setFillColor(colors.Color(0.4, 0.2, 0.2, 0.3))
        # canvas.rect(self._x1, self._y1, self._width, self._height, fill=True)

        xP = self._x1 + self.leftPadding
        yP = self._y1 + self.bottomPadding

        x, y = xP, yP

        # Align to descent line
        y = yP - align_text(
            self.text[1].fontName,
            self.text[1].fontSize,
            self._aH,
            alignment="CENTERLINE",
        )

        para = Paragraph(self.text[0], self.text[1])
        _, _ = para.wrap(availWidth=self._width, availHeight=self._height)
        para.drawOn(canvas, x, y)


class Heading_002(Frame):
    def __init__(
        self,
        number,
        text,
        gap,
        *args,
        **kwargs,
    ):
        super().__init__(*args, **kwargs)
        self.number = number
        self.text = text
        self.gap = gap

    def handle_content(self, canvas):
        """ """
        # Visualize area
        # canvas.setFillColor(colors.Color(1, 0.1, 0.1, 0.3))
        # canvas.rect(self._x1, self._y1, self._width, self._height, fill=True)

        xP = self._x1 + self.leftPadding
        yP = self._y1 + self.bottomPadding

        x, y = xP, yP

        y = yP + align_text(
            self.number[1].fontName,
            self.number[1].fontSize,
            self._aH,
            alignment="CENTERLINE",
        )

        para = Paragraph(self.number[0], self.number[1])
        _, _ = para.wrap(availWidth=self._aW, availHeight=self._aH)
        para.drawOn(canvas, x, y)

        x += (
            stringWidth(
                self.number[0], self.number[1].fontName, self.number[1].fontSize
            )
            + self.gap
        )

        y = yP - align_text(
            self.text[1].fontName,
            self.text[1].fontSize,
            self._aH,
            alignment="CENTERLINE",
        )

        para = Paragraph(self.text[0], self.text[1])
        _, _ = para.wrap(availWidth=self._aW, availHeight=self._aH)
        para.drawOn(canvas, x, y)
