from reportlab.platypus import Frame

from FlowablesShapes.Circle import FlowableLine
from Frames.CustomFrame import CustomFrame


class HeaderGrid(CustomFrame):
    def __init__(self, color, lineWidth, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.color = color
        self.lineWidth = lineWidth

        self._autoBreak = False

    def handle_content(self):
        # canvas.setStrokeColor(self.color)
        # canvas.setLineWidth(self.lineWidth)
        # canvas.line(self._x1, self._y1, self._x2, self._y1)
        # canvas.line(self._x1, self._y2, self._x2, self._y2)

        self.addFrame(
            Frame(
                x1=self._x1,
                y1=self._y1,
                width=self._width,
                height=self._height,
                topPadding=0,
                rightPadding=0,
                bottomPadding=0,
                leftPadding=0,
                showBoundary=0,
                id="header_grid",
            )
        )

        self.addFlowable(FlowableLine(0, 0, self._width, 0, self.color, self.lineWidth))
        self.addFlowable(
            FlowableLine(
                0, -self._height, self._width, -self._height, self.color, self.lineWidth
            )
        )

        return (self._frames, self._framesContent)


class ContentGrid(CustomFrame):
    def __init__(self, color, lineWidth, gapWidth, numCols, numRows, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.color = color
        self.lineWidth = lineWidth
        self.gapWidth = gapWidth
        self.numRows = numRows
        self.numCols = numCols

        self._autoBreak = False

    def handle_content(self):

        x, y = 0, -self._aH

        aW = self._aW - (self.gapWidth * (self.numCols + 1))
        colWidth = aW / self.numCols

        aH = self._aH - (self.gapWidth * (self.numRows + 1))
        rowHeight = aH / self.numRows

        self.addFrame(
            Frame(
                x1=self._x1p,
                y1=self._y1p,
                width=self._width,
                height=self._height,
                topPadding=0,
                rightPadding=0,
                bottomPadding=0,
                leftPadding=0,
                showBoundary=0,
                id="content_grid",
            )
        )

        for row in range(self.numRows):
            if row == 0:

                # canvas.line(self._x1, y, self._x2, y)
                self.addFlowable(
                    FlowableLine(
                        0,
                        y,
                        self._aW,
                        y,
                        self.color,
                        self.lineWidth,
                    )
                )
                y += self.gapWidth

            # canvas.line(self._x1, y, self._x2, y)
            self.addFlowable(
                FlowableLine(
                    0,
                    y,
                    self._aW,
                    y,
                    self.color,
                    self.lineWidth,
                )
            )
            y += rowHeight
            # canvas.line(self._x1, y, self._x2, y)
            self.addFlowable(
                FlowableLine(
                    0,
                    y,
                    self._aW,
                    y,
                    self.color,
                    self.lineWidth,
                )
            )
            y += self.gapWidth

            if row == self.numRows - 1:
                self.addFlowable(
                    FlowableLine(
                        0,
                        y,
                        self._aW,
                        y,
                        self.color,
                        self.lineWidth,
                    )
                )
                # canvas.line(self._x1, y, self._x2, y)

        for col in range(self.numCols):
            if col == 0:
                # canvas.line(x, self._y1, x, self._y2)
                self.addFlowable(
                    FlowableLine(
                        x,
                        0,
                        x,
                        -self._aH,
                        self.color,
                        self.lineWidth,
                    )
                )
                x += self.gapWidth

            # canvas.line(x, self._y1, x, self._y2)
            self.addFlowable(
                FlowableLine(
                    x,
                    0,
                    x,
                    -self._aH,
                    self.color,
                    self.lineWidth,
                )
            )
            x += colWidth
            # canvas.line(x, self._y1, x, self._y2)
            self.addFlowable(
                FlowableLine(
                    x,
                    0,
                    x,
                    -self._aH,
                    self.color,
                    self.lineWidth,
                )
            )
            x += self.gapWidth

            if col == self.numCols - 1:
                self.addFlowable(
                    FlowableLine(
                        x,
                        0,
                        x,
                        -self._aH,
                        self.color,
                        self.lineWidth,
                    )
                )
                # canvas.line(x, self._y1, x, self._y2)

        return (self._frames, self._framesContent)
