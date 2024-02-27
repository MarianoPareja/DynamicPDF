from reportlab.lib import colors
from reportlab.platypus import Frame, Paragraph, Table, TableStyle


class Table_001(Frame):
    def __init__(
        self, table_data, colsContentWidth, headerFormat, contentFormat, *args, **kwargs
    ):
        super().__init__(*args, **kwargs)
        self.table_data = table_data
        self.colsContentWidth = colsContentWidth
        self.headerFormat = headerFormat
        self.contentFormat = contentFormat
        self.headerUpper = True

        self.colsWidth = self._aW / len(self.table_data[0])

    def generate_paragraph_data(self):
        """
        Applies ParagraphSyle to all text in the table

        :return table_para_data(list): List containing all the Paragraph instances

        """
        table_para_data = []

        if self.headerUpper:
            self.table_data[0] = [text.upper() for text in self.table_data[0]]

        table_para_data.append(
            [Paragraph(text, self.headerFormat) for text in self.table_data[0]]
        )

        for row in range(1, len(self.table_data)):
            table_para_data.append(
                [Paragraph(text, self.contentFormat) for text in self.table_data[row]]
            )

        return table_para_data

    def add_grid(self, table_style):
        for row in range(len(self.table_data)):
            if row == len(self.table_data) - 1:
                table_style.add(
                    "LINEBELOW", (0, row), (-1, row), 1, colors.Color(1, 1, 1, 0.2)
                )
                return

            table_style.add(
                "LINEBELOW", (0, row), (-1, row), 1, colors.Color(1, 1, 1, 0.1)
            )

    def handle_data(self, canvas):

        # # Visualize area
        # canvas.setFillColor(colors.Color(1, 0.1, 0.1, 0.3))
        # canvas.rect(self._x1, self._y1, self._width, self._height, fill=True)

        table_style = TableStyle(
            [
                ("WORDWRAP", (0, 0), (-1, -1), "NORMAL"),
                ("ALIGNMENT", (0, 0), (-1, -1), "LEFT"),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("TOPPADDING", (0, 0), (-1, -1), 6),
                ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
            ]
        )
        self.add_grid(table_style)

        # CREATE PARAGRAPHS INSTANCES FOR TEXT
        table_data = self.generate_paragraph_data()

        #     ('FONTNAME', (0,0), (0,-1), ),
        #     ('FONTSIZE', (0,0), (0,-1), self.header_format.get('fontsize')),
        # ])

        t = Table(table_data, colWidths=self.colsWidth)
        t.setStyle(table_style)

        w, h = t.wrap(availWidth=self._aW, availHeight=self._aH)
        print(self._aH, h)
        t.drawOn(canvas, self._x1, self._y1)
