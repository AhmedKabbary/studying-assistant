from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *


class RegisterPage(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('Register')
        self.window().setStyleSheet('background-color: #232931')
        v_layout = QVBoxLayout(self)
        lbl = QLabel('Register')
        lbl.setStyleSheet("color: white")
        v_layout.addWidget(lbl, alignment=Qt.AlignmentFlag.AlignCenter)
