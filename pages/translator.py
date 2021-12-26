from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
import googletrans
from widgets.dropdown import DropDown


class TranslatorPage(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('Google Translator')
        self.window().setStyleSheet('background-color: #232931')

        with open('styles/translator_page.css') as f:
            css = f.read()
            self.setStyleSheet(css)

        v_layout = QVBoxLayout(self)
        v_layout.setContentsMargins(0, 0, 0, 0)

        self.combo1 = DropDown(size=QSize(200, 40), border=False)
        v_layout.addWidget(self.combo1, alignment=Qt.AlignmentFlag.AlignTop)

        self.enter_line = QLineEdit()
        self.enter_line.setPlaceholderText('Type here...')
        self.enter_line.setObjectName('LineToTranslate')
        self.enter_line.textChanged.connect(self.translate)
        v_layout.addWidget(
            self.enter_line, alignment=Qt.AlignmentFlag.AlignTop)

        frame = QFrame()
        frame.setFixedSize(400, 300)
        frame.setObjectName('button_frame')
        v_layout.addWidget(frame, alignment=Qt.AlignmentFlag.AlignBottom)

        v2_layout = QVBoxLayout(frame)

        self.combo2 = DropDown(size=QSize(200, 40), border=False)
        v2_layout.addWidget(self.combo2, alignment=Qt.AlignmentFlag.AlignTop)

        self.trans_lbl = QLabel("Translation")
        self.trans_lbl.setObjectName('label')
        # translation.setFixedSize(400,300)
        v2_layout.addWidget(
            self.trans_lbl, alignment=Qt.AlignmentFlag.AlignTop)

        # add languages to ComboBox
        languages = list(googletrans.LANGUAGES.values())
        languages_with_auto = ['auto']
        languages_with_auto.extend(languages)
        self.combo1.addItems(languages_with_auto)
        self.combo2.addItems(languages)

        # set current language
        self.combo1.setCurrentIndex(0)
        self.combo2.setCurrentIndex(3)

        swap = QPushButton(self)
        swap.move(340, 225)
        swap.setFixedSize(40, 50)
        swap.setObjectName('swap_button')
        swap.setIcon(QIcon('icons/swap_v.svg'))
        swap.setIconSize(QSize(35, 35))
        swap.setCursor(Qt.CursorShape.PointingHandCursor)
        swap.clicked.connect(self.swap)

        self.translator = googletrans.Translator()

    def swap(self):
        if self.combo1.currentIndex() == 0:
            temp = 21
        else:
            temp = self.combo1.currentIndex() - 1
        self.combo1.setCurrentIndex(self.combo2.currentIndex() + 1)
        self.combo2.setCurrentIndex(temp)

        temp = self.enter_line.text()
        self.enter_line.setText(self.trans_lbl.text())
        self.trans_lbl.setText(temp)

        del temp

    def translate(self):
        if self.enter_line.text() != '':
            t_from = self.combo1.currentText()
            t_to = self.combo2.currentText()
            res = self.translator.translate(
                self.enter_line.text(), dest=t_to, src=t_from)
            self.trans_lbl.setText(res.text)
