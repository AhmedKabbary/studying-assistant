from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QPushButton


class IconButton(QPushButton):
    def __init__(self, icon: QIcon, primaryColor, secondaryColor):
        super().__init__()

        self.primaryColor = primaryColor
        self.secondaryColor = secondaryColor

        self.setIcon(icon)
        self.setFixedSize(20, 20)
        self.setIconSize(QSize(15, 15))
        self.setStyleSheet(f"""
            border-radius: 5;
            background-color: {self.primaryColor};
        """)

    def enterEvent(self, event):
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.setStyleSheet(f"""
            border-radius: 5;
            background-color: {self.secondaryColor};
        """)

    def leaveEvent(self, event):
        self.setStyleSheet(f"""
            border-radius: 5;
            background-color: {self.primaryColor};
        """)
