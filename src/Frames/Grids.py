from reportlab.platypus import Frame


class HeaderGrid(Frame):
    def __init__(self, color, lineWidth, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.color = color
        self.lineWidth = lineWidth

    def drawGrid(self, canvas):
        canvas.setStrokeColor(self.color)
        canvas.setLineWidth(self.lineWidth)
        canvas.line(self._x1, self._y1, self._x2, self._y1)
        canvas.line(self._x1, self._y2, self._x2, self._y2)


class ContentGrid(Frame):
    def __init__(self, color, lineWidth, gapWidth, numCols, numRows, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.color = color
        self.lineWidth = lineWidth
        self.gapWidth = gapWidth
        self.numRows = numRows
        self.numCols = numCols

    def drawGrid(self, canvas):

        xP, yP = self._x1 + self._leftPadding, self._y1 + self._bottomPadding
        x, y = xP, yP

        aW = self._aW - (self.gapWidth * (self.numCols + 1))
        colWidth = aW / self.numCols

        aH = self._aH - (self.gapWidth * (self.numRows + 1))
        rowHeight = aH / self.numRows

        canvas.setStrokeColor(self.color)
        canvas.setLineWidth(self.lineWidth)

        for row in range(self.numRows):
            if row == 0:
                canvas.line(self._x1, y, self._x2, y)
                y += self.gapWidth

            canvas.line(self._x1, y, self._x2, y)
            y += rowHeight
            canvas.line(self._x1, y, self._x2, y)
            y += self.gapWidth

            if row == self.numRows - 1:
                canvas.line(self._x1, y, self._x2, y)

        for col in range(self.numCols):
            if col == 0:
                canvas.line(x, self._y1, x, self._y2)
                x += self.gapWidth

            canvas.line(x, self._y1, x, self._y2)
            x += colWidth
            canvas.line(x, self._y1, x, self._y2)
            x += self.gapWidth

            if col == self.numCols - 1:
                canvas.line(x, self._y1, x, self._y2)
