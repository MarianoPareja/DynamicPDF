from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.platypus import Frame, Paragraph

from Frames.CustomFrame import CustomFrame


class Content_001(CustomFrame):
    def __init__(
        self,
        text,
        num_cols,
        gap,
        *args,
        **kwargs,
    ):
        super().__init__(*args, **kwargs)
        self.text = text
        self.num_cols = num_cols
        self.gap = gap

    def distribute_words(self):
        """

        (UPDATE):param threhold(int): Number of words to seach for the closest "\n"

        return text_paragraph(list): List of str containing the differerent paragraphs
        """
        threshold = 30

        total_words = len(self.text[0])
        ratio = 1 / self.num_cols
        key_words = [int((total_words) * (i * ratio)) for i in range(1, self.num_cols)]

        for i, word_index in enumerate(key_words):
            new_index = self.text[0][
                word_index - threshold : word_index + threshold
            ].find("<br/>")
            if new_index != -1:
                key_words[i] = word_index - threshold + new_index - 1
        key_words.append(total_words)
        text_paragraph = []
        cur_index = 0
        for word in key_words:
            text_paragraph.append(self.text[0][cur_index : word + 1])
            cur_index = word + 1

        for i, text in enumerate(text_paragraph):
            while text[:5] == "<br/>":
                text = text[5:]
                text_paragraph[i] = text

        return text_paragraph

    def handle_content(self):

        # Visualize area
        # canvas.setFillColor(colors.Color(0.1, 0.6, 0.1, 0.3))
        # canvas.rect(self._x1, self._y1, self._width, self._height, fill=True)

        x, y = self._x1p, self._y1p

        para_text = self.distribute_words()

        para_width = (self._aW - (self.gap * (self.num_cols - 1))) / self.num_cols

        for text in para_text:
            para = Paragraph(text, self.text[1])
            _, h = para.wrap(availWidth=para_width, availHeight=self._aH)

            # para.drawOn(canvas, x, y + (self._aH - h))
            self.addFrame(
                Frame(
                    x1=x,
                    y1=y + (self._aH - h),
                    width=para_width,
                    height=h,
                    topPadding=0,
                    rightPadding=0,
                    bottomPadding=0,
                    leftPadding=0,
                    showBoundary=0,
                    id=f"content",
                )
            )
            self.addFlowable(para)

            x += para_width + self.gap

        return (self._frames, self._framesContent[:-1])
