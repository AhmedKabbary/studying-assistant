from PyQt6.QtCore import QRectF
from PyQt6.QtGui import QImage, QPaintEvent, QPainter, QPainterPath
from PyQt6.QtWidgets import QWidget


class ImageWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.radius = 0
        self.image = None

    def set_radius(self, radius):
        self.radius = radius

    def set_image(self, path):
        self.image = QImage(path)
        self.repaint()

    def paintEvent(self, event: QPaintEvent):
        if self.image:
            painter = QPainter(self)
            painter.setRenderHint(QPainter.RenderHint.Antialiasing, True)
            painter.setRenderHint(QPainter.RenderHint.LosslessImageRendering, True)

            path = QPainterPath()
            rect = QRectF(event.rect())
            path.addRoundedRect(rect, self.radius, self.radius)
            painter.setClipPath(path)

            painter.drawImage(rect, self.image)
