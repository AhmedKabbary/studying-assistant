from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QFrame, QGridLayout, QVBoxLayout, QWidget
from widgets.home_btn import HomeButton
from PyQt6.QtCore import Qt
from pages import *


class HomePage(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('Home')
        self.window().setStyleSheet('background-color: #393E46')

        with open('styles/home_page.css') as f:
            css = f.read()
            self.setStyleSheet(css)

        v_layout = QVBoxLayout(self)
        v_layout.setSpacing(0)
        v_layout.setContentsMargins(0, 0, 0, 0)

        frame1 = QFrame()
        frame1.setFixedWidth(self.parentWidget().width())
        v_layout.addWidget(frame1, alignment=Qt.AlignmentFlag.AlignCenter)

        frame2 = QFrame()
        frame2.setObjectName('bottom_container')
        frame2.setFixedSize(self.parentWidget().width(), 320)
        v_layout.addWidget(frame2, alignment=Qt.AlignmentFlag.AlignBottom)

        g_layout = QGridLayout(frame2)
        g_layout.setContentsMargins(25, 10, 25, 25)
        g_layout.setSpacing(25)
        g_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        line = QFrame()
        line.setFixedHeight(2)
        line.setObjectName('line')

        g_layout.addWidget(line, 0, 1)
        g_layout.addWidget(HomeButton('Tasks', QIcon('icons/tasks.svg'), TasksPage), 1, 0)
        g_layout.addWidget(HomeButton('Pomodoro', QIcon('icons/timer.svg'), PomodorosPage), 1, 1)
        g_layout.addWidget(HomeButton('Converter', QIcon('icons/ruler.svg'), ConverterPage), 1, 2)
        g_layout.addWidget(HomeButton('Dictionary', QIcon('icons/bookmark.svg'), DictionaryPage), 2, 0)
        g_layout.addWidget(HomeButton('AI Answerer', QIcon('icons/book.svg'), AIPage), 2, 1)
        g_layout.addWidget(HomeButton('Translator', QIcon('icons/g_translate.svg'), TranslatorPage), 2, 2)
