import db
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
import googletrans
from controllers.translator import TranslatorHandler
from widgets.dropdown import DropDown
import controllers.auth as Auth


class TranslatorPage(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('Google Translator')
        self.window().setStyleSheet('background-color: #232931')

        with open('styles/translator_page.css') as f:
            css = f.read()
            self.setStyleSheet(css)

        self.v_layout = QVBoxLayout(self)
        self.v_layout.setContentsMargins(0, 0, 0, 0)

        self.setup_top_frame()

        self.setup_bottom_frame()

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
        swap.move(340, 250)
        swap.setFixedSize(40, 50)
        swap.setObjectName('swap_button')
        swap.setIcon(QIcon('icons/swap_v.svg'))
        swap.setIconSize(QSize(35, 35))
        swap.setCursor(Qt.CursorShape.PointingHandCursor)
        swap.clicked.connect(self.swap)

    def setup_top_frame(self):
        frame = QFrame()
        frame.setFixedWidth(400)
        frame.setObjectName('top_frame')

        v2_layout = QVBoxLayout(frame)

        self.combo1 = DropDown(size=QSize(200, 40), border=False)
        v2_layout.addWidget(self.combo1)

        v2_layout.addStretch()

        self.enter_line = QLineEdit()
        self.enter_line.setPlaceholderText('Type here...')
        self.enter_line.setObjectName('LineToTranslate')
        self.enter_line.returnPressed.connect(self.translate)
        v2_layout.addWidget(self.enter_line)

        v2_layout.addStretch()

        self.v_layout.addWidget(frame, stretch=1)

    def setup_bottom_frame(self):
        frame = QFrame()
        frame.setFixedWidth(400)
        frame.setObjectName('bottom_frame')

        v2_layout = QVBoxLayout(frame)

        self.combo2 = DropDown(size=QSize(200, 40), border=False)
        v2_layout.addWidget(self.combo2)

        v2_layout.addStretch()

        self.trans_lbl = QLabel("Translation")
        self.trans_lbl.setObjectName('label')
        v2_layout.addWidget(self.trans_lbl)

        v2_layout.addStretch()

        history = QPushButton(self)
        history.setText('SHOW HISTORY')
        history.setObjectName('show_history')
        history.setCursor(Qt.CursorShape.PointingHandCursor)
        history.clicked.connect(self.show_history)
        v2_layout.addWidget(history)

        self.v_layout.addWidget(frame, stretch=1)

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
        transhandler = TranslatorHandler(self, self.combo1.currentText(), self.combo2.currentText(), self.enter_line.text())
        transhandler.answer.connect(self.answered)
        transhandler.crash.connect(self.crash)
        transhandler.start()

    def answered(self, translated):
        self.trans_lbl.setText(translated)
        db.cursor.execute("INSERT INTO TRANSLATION (SENTENCE, TRANSLATION, ORIGIN, DESTINATION, USER_ID) VALUES (?, ?, ?, ?, ?)",
                          (self.enter_line.text(), translated, self.combo1.currentText(), self.combo2.currentText(), Auth.user[0]))
        db.cursor.commit()

    def crash(self):
        pass

    def show_history(self):
        d = QDialog()
        d.setFixedSize(400, 300)
        d.setWindowTitle('Translation history')
        d.setStyleSheet("background-color: #232931;")

        scroll = QScrollArea(d)
        scroll.setWidgetResizable(True)
        scroll.setAlignment(Qt.AlignmentFlag.AlignTop)
        scroll.setFixedSize(400, 300)
        scroll.verticalScrollBar().hide()
        scroll.horizontalScrollBar().hide()
        scroll.setStyleSheet('border: none;')
        w = QWidget()
        self.list_layout = QVBoxLayout(w)
        self.list_layout.setSpacing(15)
        self.list_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        scroll.setWidget(w)

        res = db.cursor.execute('SELECT * FROM TRANSLATION WHERE USER_ID = ?', (Auth.user[0],))
        for row in res:
            l = QLabel(str(row[1]) + '\n' + str(row[2]))
            l.setStyleSheet('color: #EEEEEE;')
            self.list_layout.addWidget(l)

        d.exec()
