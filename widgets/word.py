from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *


class WordWidget(QFrame):
    def __init__(self, text, difficulty):
        super().__init__()

        self.setFixedSize(170, 45)
        self.setStyleSheet("""
            background-color: #393E46;
            border-radius: 5;
        """)

        layout = QHBoxLayout(self)
        layout.setSpacing(15)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)

        band = QFrame()
        band.setFixedSize(4, 45)
        if difficulty == 0:
            band.setStyleSheet("""
                background-color: #0BDA51;
                border-top-left-radius: 5;
                border-bottom-left-radius: 5;
            """)
        elif difficulty == 1:
            band.setStyleSheet("""
                background-color: #E4D00A;
                border-top-left-radius: 5;
                border-bottom-left-radius: 5;
            """)
        elif difficulty == 2:
            band.setStyleSheet("""
                background-color: red;
                border-top-left-radius: 5;
                border-bottom-left-radius: 5;
            """)
        layout.addWidget(band)
        
        label = QLabel(text)
        label.setStyleSheet("""
            color: #EEEEEE;
            font-size: 18px;
        """)
        layout.addWidget(label)

