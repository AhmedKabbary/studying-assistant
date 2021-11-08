from typing import Type
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QColor, QIcon
from PyQt6.QtWidgets import QGraphicsDropShadowEffect, QLabel, QPushButton, QVBoxLayout, QWidget


class HomeButton(QPushButton):
    def __init__(self, text: str, icon: QIcon, page: Type[QWidget]):
        super().__init__()
        self.page = page
        self.setObjectName('page_button')

        self.setFixedSize(100, 110)
        self.clicked.connect(self.go_to)
        self.setCursor(Qt.CursorShape.PointingHandCursor)

        self.setup_shadow()

        v_layout = QVBoxLayout(self)
        v_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        btn = QPushButton()
        btn.setIcon(icon)
        btn.setIconSize(QSize(50, 50))
        btn.clicked.connect(self.go_to)
        v_layout.addWidget(btn)

        v_layout.setSpacing(12)

        lbl = QLabel(text)
        lbl.setObjectName('page_button_caption')
        lbl.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        v_layout.addWidget(lbl)

    def go_to(self):
        self.window().navigate_to(self.page)

    def setup_shadow(self):
        shadow = QGraphicsDropShadowEffect()
        shadow.setOffset(0, 5)
        shadow.setBlurRadius(25)
        shadow_color = QColor('black')
        shadow_color.setAlpha(65)
        shadow.setColor(shadow_color)
        self.setGraphicsEffect(shadow)
