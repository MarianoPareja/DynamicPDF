from reportlab.platypus import Frame, FrameBreak


class CustomFrame(Frame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._frames = []
        self._framesContent = []

    def _geom(self):
        self._x2 = self._x1 + self._width
        self._y2 = self._y1 + self._height
        # efficiency
        self._y1p = self._y1 + self._bottomPadding
        self._x1p = self._x1 + self._leftPadding
        # work out the available space
        self._aW = self._x2 - self._x1p - self._rightPadding
        self._aH = self._y2 - self._y1p - self._topPadding

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
        self._framesContent.append(FrameBreak())
