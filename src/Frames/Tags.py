from reportlab.lib import colors
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.platypus import Frame, Paragraph

from Frames.CustomFrame import CustomFrame
from utils import align_text


class Tag_001(CustomFrame):
    def __init__(self, text, bg, *args, **kwargs):
        """
        :param text(tuple): Tuple containing (text, ParagraphStyle)
        :param background(reportlab.lib.colors.Color): RGBA values corresponding to the background color
        """

        super().__init__(bg, *args, **kwargs)
        self.text = text

    def handle_content(self):

        x = self._x1p
        y = self._y1p

        y = self._y1p + align_text(
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
        # para.drawOn(canvas, x, y)
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
                id="tag",
            )
        )
        self.addFlowable(para)

        return (self._frames, self._framesContent[:-1])
