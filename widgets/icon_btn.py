from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QColor, QIcon
from PyQt6.QtWidgets import QGraphicsDropShadowEffect, QPushButton


class IconButton(QPushButton):
    def __init__(self, icon: QIcon, primaryColor, secondaryColor):
        super().__init__()

        self.primaryColor = primaryColor
        self.secondaryColor = secondaryColor

        self.setIcon(icon)
        self.setFixedSize(20, 20)
        self.setIconSize(QSize(15, 15))
        self.setStyleSheet(f"""
            QPushButton {{
                border-radius: 5;
                background-color: {self.primaryColor};
            }}

            QPushButton::hover {{
                background-color: {self.secondaryColor};
            }}
        """)
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.setup_shadow()

    def setup_shadow(self):
        shadow = QGraphicsDropShadowEffect()
        shadow.setOffset(0, 2)
        shadow.setBlurRadius(4)
        shadow_color = QColor('black')
        shadow_color.setAlpha(65)
        shadow.setColor(shadow_color)
        self.setGraphicsEffect(shadow)
