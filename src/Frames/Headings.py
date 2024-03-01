from reportlab.lib import colors
from reportlab.pdfbase.pdfmetrics import getFont, stringWidth
from reportlab.platypus import Frame, Paragraph

from Frames.CustomFrame import CustomFrame
from utils import align_text


class Heading_001(CustomFrame):
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

    def handle_content(self):
        """
        Heading 001 Style
        """
        # Visualize area
        # canvas.setFillColor(colors.Color(0.4, 0.2, 0.2, 0.3))
        # canvas.rect(self._x1, self._y1, self._width, self._height, fill=True)

        x, y = self._x1p, self._y1p

        # Align to descent line
        y = self._y1p - align_text(
            self.text[1].fontName,
            self.text[1].fontSize,
            self._aH,
            alignment="CENTERLINE",
        )

        para = Paragraph(self.text[0], self.text[1])
        w, h = para.wrap(availWidth=self._width, availHeight=self._height)
        self.addFrame(
            Frame(
                x1=x,
                y1=y,
                width=w,
                height=h,
                topPadding=0,
                rightPadding=0,
                bottomPadding=0,
                leftPadding=0,
                showBoundary=0,
                id=f"main_heading",
            )
        )
        self.addFlowable(para)

        # para.drawOn(canvas, x, y)

        return (self._frames, self._framesContent[:-1])


class Heading_002(CustomFrame):
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

    def handle_content(self):
        """ """
        # Visualize area
        # canvas.setFillColor(colors.Color(1, 0.1, 0.1, 0.3))
        # canvas.rect(self._x1, self._y1, self._width, self._height, fill=True)

        x, y = self._x1p, self._y1p

        y = self._y1p + align_text(
            self.number[1].fontName,
            self.number[1].fontSize,
            self._aH,
            alignment="CENTERLINE",
        )

        para = Paragraph(self.number[0], self.number[1])
        w, h = para.wrap(availWidth=self._aW, availHeight=self._aH)

        self.addFrame(
            Frame(
                x1=x,
                y1=y,
                width=w,
                height=h,
                topPadding=0,
                rightPadding=0,
                bottomPadding=0,
                leftPadding=0,
                showBoundary=0,
                id=f"main_heading",
            )
        )
        self.addFlowable(para)

        # para.drawOn(canvas, x, y)

        x += (
            stringWidth(
                self.number[0], self.number[1].fontName, self.number[1].fontSize
            )
            + self.gap
        )

        y = self._y1p - align_text(
            self.text[1].fontName,
            self.text[1].fontSize,
            self._aH,
            alignment="CENTERLINE",
        )

        para = Paragraph(self.text[0], self.text[1])
        w, h = para.wrap(availWidth=self._aW, availHeight=self._aH)

        self.addFrame(
            Frame(
                x1=x,
                y1=y,
                width=w,
                height=h,
                topPadding=0,
                rightPadding=0,
                bottomPadding=0,
                leftPadding=0,
                showBoundary=0,
                id=f"second_heading",
            )
        )
        self.addFlowable(para)

        # para.drawOn(canvas, x, y)

        return (self._frames, self._framesContent[:-1])
