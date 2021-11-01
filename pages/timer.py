from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *


class TimerPage(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('Pomodoros')
        self.window().setStyleSheet('background-color: #232931')
        v_layout = QVBoxLayout(self)
        lbl = QLabel('Timer')
        lbl.setStyleSheet("color: white")
        v_layout.addWidget(lbl, alignment=Qt.AlignmentFlag.AlignCenter)
