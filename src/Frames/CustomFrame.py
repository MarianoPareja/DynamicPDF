from reportlab.lib.colors import Color
from reportlab.platypus import Frame, FrameBreak

from FlowablesShapes.Circle import FlowableRect


class CustomFrame(Frame):

    def __init__(self, bg: Color = None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._frames = []
        self._framesContent = []
        self.bg = bg
        self._autoBreak = True

        if bg is not None and isinstance(bg, Color):
            self._setBackground()

    def _geom(self):
        self._x2 = self._x1 + self._width
        self._y2 = self._y1 + self._height
        # efficiency
        self._y1p = self._y1 + self._bottomPadding
        self._x1p = self._x1 + self._leftPadding
        # work out the available space
        self._aW = self._x2 - self._x1p - self._rightPadding
        self._aH = self._y2 - self._y1p - self._topPadding

    def _setBackground(self):
        self.addFrame(
            Frame(
                x1=self._x1,
                y1=self._y1,
                width=self._width,
                height=self._height,
                leftPadding=0,
                bottomPadding=0,
                rightPadding=0,
                topPadding=0,
                showBoundary=1,
            )
        )
        self.addFlowable(
            FlowableRect(
                x=0,
                y=-self.height,
                width=self._width,
                height=self._height,
                strokeColor=self.bg,
                fillColor=self.bg,
                fill=1,
            )
        )

    def addFrame(self, frame: Frame):
        """
        Adds a frame to the self._frames list
        """
        self._frames.append(frame)

    def addFlowable(self, flowable):
        """
        Add a flowabled to the self._frame list.
        :param flowable[Flowable]: Flowable like object Paragraph, Table, Image, Spacer
        """
        self._framesContent.append(flowable)
        # Automatically add Framebreak
        if self._autoBreak:
            self._framesContent.append(FrameBreak())
