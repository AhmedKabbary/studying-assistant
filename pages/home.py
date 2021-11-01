from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *


class HomePage(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('Home')
        self.window().setStyleSheet('background-color: #393E46')

        v_layout = QVBoxLayout(self)
        v_layout.setSpacing(0)
        v_layout.setContentsMargins(0, 0, 0, 0)

        frame1 = QFrame()
        frame1.setStyleSheet('background-color: #393E46')
        frame1.setFixedWidth(self.parentWidget().width())
        v_layout.addWidget(frame1, stretch=2)

        frame2 = QFrame()
        frame2.setStyleSheet("""
            background-color: #232931;
            border-top-left-radius: 30px;
            border-top-right-radius: 30px;
        """)
        frame2.setFixedWidth(self.parentWidget().width())
        v_layout.addWidget(frame2, stretch=3)
