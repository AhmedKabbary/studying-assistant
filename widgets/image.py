from PyQt6.QtCore import QRectF
from PyQt6.QtGui import QImage, QPaintEvent, QPainter, QPainterPath
from PyQt6.QtWidgets import QWidget


class ImageWidget(QWidget):
    def __init__(self, w, h, url: str, radius):
        super().__init__()
        self.setFixedSize(w, h)
        self.radius = radius
        self._image = QImage(url)

    def paintEvent(self, event: QPaintEvent):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing, True)
        painter.setRenderHint(QPainter.RenderHint.LosslessImageRendering, True)

        path = QPainterPath()
        rect = QRectF(event.rect())
        path.addRoundedRect(rect, self.radius, self.radius)
        painter.setClipPath(path)

        painter.drawImage(rect, self._image)
