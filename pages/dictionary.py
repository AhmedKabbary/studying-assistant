import db
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from widgets.word import WordWidget
import controllers.auth as Auth


class DictionaryPage(QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('My Dictionary')
        self.window().setStyleSheet('background-color: #232931')

        with open('styles/dictionary_page.css') as f:
            css = f.read()
            self.setStyleSheet(css)

        v_layout = QVBoxLayout(self)
        v_layout.setContentsMargins(20, 20, 20, 30)

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setAlignment(Qt.AlignmentFlag.AlignTop)
        scroll.setFixedSize(350, 400)
        scroll.horizontalScrollBar().hide()
        scroll.setStyleSheet('border: none;')

        w = QWidget()
        self.grid_layout = QGridLayout(w)
        self.grid_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        v_layout.addWidget(scroll)
        scroll.setWidget(w)

        btn = QPushButton()
        btn.setText("ADD WORD")
        btn.setFixedSize(200, 50)
        btn.setObjectName('add')
        btn.clicked.connect(self.add_word)
        btn.setCursor(Qt.CursorShape.PointingHandCursor)
        v_layout.addWidget(btn, alignment=Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignBottom)

        self.load_grid()

    def load_grid(self):
        # delete all widgets in the grid
        for i in reversed(range(self.grid_layout.count())):
            self.grid_layout.itemAt(i).widget().deleteLater()

        result = db.cursor.execute('SELECT * FROM DICTIONARY WHERE USER_ID = ?', (Auth.user[0],))
        for index, item in enumerate(result):
            r = (index // 2)
            c = 0 if (index % 2 == 0) else 1
            w = WordWidget(item[0], item[1], item[2])
            w.deleted.connect(self.load_grid)
            self.grid_layout.addWidget(w, r, c)

    def add_word(self):
        d = InputWordDialog()
        d.word_added.connect(self.word_added)
        d.exec()

    def word_added(self, word, difficulty):
        db.cursor.execute("INSERT INTO DICTIONARY (WORD, DIFFICULTY, USER_ID) VALUES (?, ?, ?)", (word, difficulty, Auth.user[0]))
        db.cursor.commit()
        self.load_grid()


class InputWordDialog(QDialog):

    word_added = pyqtSignal(str, int)

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Add a word')
        self.setFixedWidth(300)
        self.setStyleSheet("""
            QDialog {
                background-color: #232931;
            
            }

            QLineEdit {
                border: none;
                background-color: #393E46;
                border-radius: 5;
                padding: 8px;
                color: #EEEEEE;
            }

            QGroupBox {
                border: 1px solid #646464;
                border-radius: 5;
                color : #EEEEEE;
            }

            QPushButton {
                border: none;
                border-radius: 5;
                font-size: 20;
                font-weight: bold;
                background-color: #393E46;
                color : #EEEEEE;
            }

            QRadioButton {
                color: #EEEEEE;
            }
        """)

        v_layout = QVBoxLayout(self)
        v_layout.setSpacing(24)

        self.word = QLineEdit()
        self.word.setPlaceholderText('Enter a word')
        v_layout.addWidget(self.word)

        group = QGroupBox()
        group.setTitle('Select difficulty')
        group_layout = QVBoxLayout(group)

        self.easy = QRadioButton('easy', group)
        group_layout.addWidget(self.easy)
        self.normal = QRadioButton('normal', group)
        self.normal.setChecked(True)
        group_layout.addWidget(self.normal)
        self.hard = QRadioButton('hard', group)
        group_layout.addWidget(self.hard)

        v_layout.addWidget(group)

        # qwidget with horizontal layout
        # put two buttons in the horizontal layout
        # add the qwidget in the main v_layout
        widget = QWidget()
        h_layout = QHBoxLayout(widget)
        h_layout.setContentsMargins(0, 0, 0, 0)

        btn1 = QPushButton()
        btn1.setText("SAVE")
        btn1.setFixedHeight(30)
        btn1.clicked.connect(self.okay)
        btn1.setCursor(Qt.CursorShape.PointingHandCursor)
        h_layout.addWidget(btn1, stretch=1)

        btn2 = QPushButton()
        btn2.setText("CANCEL")
        btn2.setFixedHeight(30)
        btn2.setCursor(Qt.CursorShape.PointingHandCursor)
        btn2.clicked.connect(self.close)

        h_layout.addWidget(btn2, stretch=1)

        v_layout.addWidget(widget)

    def okay(self):
        w = self.word.text()

        d = 0
        if self.easy.isChecked():
            d = 0
        elif self.normal.isChecked():
            d = 1
        elif self.hard.isChecked():
            d = 2

        self.word_added.emit(w, d)
        self.close()
