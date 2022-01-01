from PyQt6.QtCore import QRectF, Qt, pyqtSignal
from PyQt6.QtGui import QImage, QMouseEvent, QPaintEvent, QPainter, QPainterPath
from PyQt6.QtWidgets import QWidget


class ImageWidget(QWidget):

    clicked = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.radius = 0
        self.image = None

    def set_radius(self, radius):
        self.radius = radius

    def set_image(self, path):
        self.image = QImage(path)
        self.repaint()

    def mousePressEvent(self, a0: QMouseEvent):
        if a0.button() == Qt.MouseButton.LeftButton:
            self.clicked.emit()

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
