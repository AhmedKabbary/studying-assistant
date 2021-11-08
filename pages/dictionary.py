from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *


class DictionaryPage(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('My Dictionary')
        self.window().setStyleSheet('background-color: #232931')

        with open('styles/dictionary_page.css') as f:
            css = f.read()
            self.setStyleSheet(css)

        v_layout = QVBoxLayout(self)
        lbl = QLabel('Hello World!')
        lbl.setObjectName('hello_world')
        v_layout.addWidget(lbl, alignment=Qt.AlignmentFlag.AlignCenter)
