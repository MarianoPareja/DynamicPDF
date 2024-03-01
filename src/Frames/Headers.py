from reportlab.lib import colors
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.platypus import Frame, FrameBreak, Paragraph

from FlowablesShapes.Circle import FlowableCircle, FlowableLine
from Frames.CustomFrame import CustomFrame
from utils import align_text


class Header_001(CustomFrame):
    def __init__(
        self,
        text,
        page,
        separator_gap,
        separator_color,
        line_gap,
        line_color,
        *args,
        **kwargs,
    ):
        """
        This function generates a custom Heading with the following structure:
        Word - separator_gap - word - line_gap - vector_line - page_number

        :param page(tuple): (text, style) corresponding to the page number
        :param text(list): List of tuples containing the words to be shown in order (text, style)
        :param x(int): X Coordinate of the heading
        :param y(int): Y Coordinate of the heading
        :param separator_gap: Gap in pixels between words and separator shape
        :param line_gap: Gap in pixels between vector line and heading text

        """
        super().__init__(*args, **kwargs)
        self.text = text
        self.page = page
        self.separator_gap = separator_gap
        self.separator_color = separator_color
        self.line_gap = line_gap
        self.line_color = line_color

    def get_vector_line_length(self, actual_x):
        """
        Gets the lenght of the vector line

        :param actual_x: X coordinate of the last word (inclusive)
        """

        return (
            self._aW
            - actual_x
            - (self.line_gap * 2)
            - stringWidth(self.page[0], self.page[1].fontName, self.page[1].fontSize)
        )

    def handle_content(self):

        # To visualize the area
        # canvas.setFillColor(colors.Color(1, 0, 1, 0.1))
        # canvas.rect(self._x1, self._y1, self._width, self._height, fill=True)

        x, y = self._x1p, self._y1p

        for i, (text, style) in enumerate(self.text):

            # Alignment: CenterLine
            y = self._y1p + align_text(
                style.fontName, style.fontSize, self._aH, alignment="CENTERLINE"
            )

            para = Paragraph(text, style)
            w = stringWidth(text, style.fontName, style.fontSize)
            _, h = para.wrap(availWidth=w, availHeight=self._aH)

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
                    id=f"header_para_{i}",
                )
            )
            self.addFlowable(para)

            x += w
            if i < len(self.text) - 1:
                x += self.separator_gap
                y = self._y1p + self._aH / 2

                circle = FlowableCircle(
                    x=self.separator_gap,
                    y=-self._aH / 2 + 2,
                    r=1,
                    strokeColor=self.separator_color,
                    strokeWidth=0,
                )

                self.addFrame(
                    Frame(
                        x1=x - self.separator_gap,
                        y1=y - self._aH / 2,
                        width=2 * self.separator_gap,
                        height=self._aH,
                        topPadding=0,
                        rightPadding=0,
                        bottomPadding=0,
                        leftPadding=0,
                        showBoundary=0,
                        id=f"header_figure_{i}",
                    )
                )
                self.addFlowable(circle)

                x += self.separator_gap

        line_length = self.get_vector_line_length(x - self._x1p)
        x += self.line_gap

        # Dine Line Values
        y = self._y1p + self._aH / 2

        line = FlowableLine(
            x1=0,
            y1=-self._aH / 2,
            x2=line_length,
            y2=-self._aH / 2,
            strokeColor=self.line_color,
            lineWidth=1,
        )

        self.addFrame(
            Frame(
                x1=x,
                y1=y - self._aH / 2,
                width=line_length,
                height=self._aH,
                topPadding=0,
                rightPadding=0,
                bottomPadding=0,
                leftPadding=0,
                showBoundary=0,
                id="header-line",
            )
        )
        self.addFlowable(line)

        x += line_length + self.line_gap

        y = self._y1p + align_text(
            self.page[1].fontName,
            self.page[1].fontSize,
            self._aH,
            alignment="CENTERLINE",
        )

        para = Paragraph(self.page[0], self.page[1])
        w, h = para.wrap(
            availWidth=stringWidth(
                self.page[0], self.page[1].fontName, self.page[1].fontSize
            ),
            availHeight=self._aH,
        )

        self.addFrame(
            Frame(
                x,
                y,
                w,
                height=h,
                topPadding=0,
                rightPadding=0,
                bottomPadding=0,
                leftPadding=0,
                showBoundary=0,
                id="header_pagenumber",
            )
        )
        self.addFlowable(para)

        return (self._frames, self._framesContent[:-1])
