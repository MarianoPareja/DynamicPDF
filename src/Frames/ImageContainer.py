from reportlab.lib import colors
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.platypus import Frame, Paragraph


class ImageContainer_001(Frame):
    def __init__(self, text, images_file, gap, *args, **kwargs):
        """
        :param text(tuple): Tuple containing (text, ParagraphStyle)
        :param images_file(list): List of images files path
        """

        super().__init__(*args, **kwargs)
        self.text = (text[0].upper(), text[1])
        self.images_file = images_file
        self.gap = gap

        self.content_width = (self._aW - (self.gap * len(self.images_file))) / (
            len(self.images_file) + 1
        )

    def handle_content(self, canvas):
        """ """
        # Visualize container area
        # canvas.setFillColor(colors.Color(0.4, 0.4, 0.4, 0.1))
        # canvas.rect(self._x1, self._y1, self._width, self._height, fill=True)

        xP = self._x1 + self.leftPadding
        yP = self._y1 + self.bottomPadding

        x, y = xP, yP

        para = Paragraph(self.text[0], self.text[1])
        w, h = para.wrap(availWidth=self.content_width, availHeight=self._aH)
        para.drawOn(canvas, x, y)

        # cur_y = self.height - f.fontSize

        x += self.content_width

        for img_file in self.images_file:
            x += self.gap
            aux = round(self._x2 - x, 5)
            if round(self.content_width, 5) <= aux:
                _, _ = canvas.drawImage(
                    img_file,
                    x,
                    y,
                    self.content_width,
                    self._aH,
                    mask="auto",
                    anchor="c",
                )
                x += self.content_width

            else:
                print("No enough spaces to insert all images")
                break
