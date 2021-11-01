from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *


class LoginPage(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('Login')
        self.window().setStyleSheet('background-color: #232931')
        v_layout = QVBoxLayout(self)
        lbl = QLabel('Login')
        lbl.setStyleSheet("color: white")
        v_layout.addWidget(lbl, alignment=Qt.AlignmentFlag.AlignCenter)
