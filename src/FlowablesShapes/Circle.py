from reportlab.lib.colors import Color
from reportlab.platypus import Flowable


class FlowableCircle(Flowable):
    def __init__(self, x, y, r, strokeColor, strokeWidth, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._x = x
        self._y = y
        self._r = r
        self._strokeColor = strokeColor
        self._strokeWidth = strokeWidth

        self.size = self._r * 2

    def wrap(self, *args):
        return (0, self.size)

    def draw(self):
        canvas = self.canv
        canvas.setStrokeColor(self._strokeColor)
        canvas.setFillColor(self._strokeColor)
        canvas.circle(self._x, self._y, self._r, self._strokeWidth, fill=1)


class FlowableLine(Flowable):
    def __init__(self, x1, y1, x2, y2, strokeColor, lineWidth, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        self._strokeColor = strokeColor
        self._lineWidth = lineWidth

        self.size = 0

    def wrap(self, *args):
        return (0, self.size)

    def draw(self):
        canvas = self.canv
        canvas.setStrokeColor(self._strokeColor)
        canvas.setLineWidth(self._lineWidth)
        canvas.line(self._x1, self._y1, self._x2, self._y2)


class FlowableRect(Flowable):
    def __init__(
        self, x, y, width, height, strokeColor, fillColor, fill, *args, **kwargs
    ):
        super().__init__(*args, **kwargs)

        self._x = x
        self._y = y
        self._width = width
        self._height = height
        self._strokeColor = strokeColor
        self._fillColor = fillColor
        self._fill = fill

        self.size = 0

    def wrap(self, *args):
        return (0, self.size)

    def draw(self):
        canvas = self.canv
        canvas.setStrokeColor(self._strokeColor)
        canvas.setFillColor(self._fillColor)
        canvas.rect(
            x=self._x,
            y=self._y,
            width=self._width,
            height=self._height,
            fill=self._fill,
        )
