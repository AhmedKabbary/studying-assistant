from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *


class TasksPage(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('My Tasks')
        self.window().setStyleSheet('background-color: #232931')

        with open('styles/tasks_page.css') as f:
            css = f.read()
            self.setStyleSheet(css)

        v_layout = QVBoxLayout(self)
        lbl = QLabel('Hello World!')
        lbl.setObjectName('hello_world')
        v_layout.addWidget(lbl, alignment=Qt.AlignmentFlag.AlignCenter)
