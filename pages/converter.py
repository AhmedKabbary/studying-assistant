from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *


class ConverterPage(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('Units Converter')
        self.window().setStyleSheet('background-color: #232931')

        with open('styles/converter_page.css') as f:
            css = f.read()
            self.setStyleSheet(css)

        v_layout = QVBoxLayout(self)
        lbl = QLabel('Hello World!')
        lbl.setObjectName('hello_world')
        v_layout.addWidget(lbl, alignment=Qt.AlignmentFlag.AlignCenter)
