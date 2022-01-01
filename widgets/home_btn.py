from typing import Type
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QColor, QIcon
from PyQt6.QtWidgets import QGraphicsDropShadowEffect, QLabel, QPushButton, QVBoxLayout, QWidget


class HomeButton(QPushButton):
    def __init__(self, text: str, icon: QIcon, page: Type[QWidget], enabled: bool = True):
        super().__init__()
        self.page = page
        self.enabled = enabled

        with open('styles/home_button.css') as f:
            css = f.read()
            self.setStyleSheet(css)

        if enabled:
            self.setObjectName('page_button')
        else:
            self.setObjectName('page_button_disabled')
        self.setFixedSize(100, 110)
        self.clicked.connect(self.go_to)
        self.setCheckable(False)
        if enabled:
            self.setCursor(Qt.CursorShape.PointingHandCursor)

        self.setup_shadow()

        v_layout = QVBoxLayout(self)
        v_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        btn = QPushButton()
        if enabled:
            btn.setIcon(icon)
        else:
            btn.setIcon(QIcon('icons/lock.svg'))
        btn.setIconSize(QSize(50, 50))
        btn.setCheckable(False)
        btn.clicked.connect(self.go_to)
        v_layout.addWidget(btn)

        v_layout.setSpacing(12)

        lbl = QLabel()
        if enabled:
            lbl.setText(text)
        else:
            lbl.setText('Locked')
        lbl.setObjectName('page_button_caption')
        lbl.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        v_layout.addWidget(lbl)

    def go_to(self):
        if self.enabled:
            self.window().navigate_to(self.page)

    def setup_shadow(self):
        shadow = QGraphicsDropShadowEffect()
        shadow.setOffset(0, 5)
        shadow.setBlurRadius(25)
        shadow_color = QColor('black')
        shadow_color.setAlpha(65)
        shadow.setColor(shadow_color)
        self.setGraphicsEffect(shadow)
