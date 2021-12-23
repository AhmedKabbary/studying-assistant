from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *


class TranslatorPage(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('Google Translator')
        self.window().setStyleSheet('background-color: #232931')

        with open('styles/translator_page.css') as f:
            css = f.read()
            self.setStyleSheet(css)

        v_layout = QVBoxLayout(self)
        
        combo=QComboBox()
        combo.setFixedSize(150,40)
        v_layout.addWidget(combo, alignment=Qt.AlignmentFlag.AlignTop)
        v_layout.setContentsMargins(0,0,0,0)

        enter_line = QLineEdit()
        enter_line.setFixedSize(200,300)
        enter_line.setObjectName('LineToTranslate')
        v_layout.addWidget(enter_line, alignment=Qt.AlignmentFlag.AlignTop)


        frame = QFrame()
        frame.setFixedSize(400,300)
        frame.setObjectName('button_frame')
        v_layout.addWidget(frame, alignment=Qt.AlignmentFlag.AlignBottom)

        v2_layout = QVBoxLayout(frame)
        combo2=QComboBox()
        combo2.setFixedSize(150,40)
        v2_layout.addWidget(combo2, alignment=Qt.AlignmentFlag.AlignTop)
        
        translation=QLabel("Translation")
        translation.setFixedSize(400,300)
        v2_layout.addWidget(translation, alignment=Qt.AlignmentFlag.AlignTop)
        

        swap=QPushButton(self)
        swap.move(340,225)
        swap.setFixedSize(40,50)
        swap.setObjectName('swap_button')
        swap.setIcon(QIcon('icons/swap.svg'))
        swap.setIconSize(QSize(35, 35))