from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import (QFrame, QGridLayout, QHBoxLayout, QLabel, QVBoxLayout, QWidget)
from widgets.home_btn import HomeButton
from widgets.icon_btn import IconButton
from widgets.image import ImageWidget
from pages import *


class HomePage(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('Home')
        self.window().setStyleSheet('background-color: #393E46')

        with open('styles/home_page.css') as f:
            css = f.read()
            self.setStyleSheet(css)

        self.root_layout = QVBoxLayout(self)
        self.root_layout.setSpacing(0)
        self.root_layout.setContentsMargins(0, 0, 0, 0)

        self.setup_profile()
        self.setup_bottom_sheet()

    def setup_profile(self):
        profile_root = QWidget()
        profile_root.setFixedWidth(self.parentWidget().width())
        self.root_layout.addWidget(profile_root, alignment=Qt.AlignmentFlag.AlignCenter)

        v_layout = QVBoxLayout(profile_root)
        v_layout.setSpacing(8)
        v_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        image = ImageWidget()
        image.setFixedSize(100, 100)
        image.set_radius(20)
        image.set_image('pic.jpg')
        v_layout.addWidget(image, alignment=Qt.AlignmentFlag.AlignHCenter)

        v_layout.addSpacing(16)

        w1 = QWidget()
        h_layout = QHBoxLayout(w1)
        h_layout.setContentsMargins(0, 0, 0, 0)
        h_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        name = QLabel('Ahmed Kabbary')
        name.setObjectName('name')
        h_layout.addWidget(name)
        h_layout.addSpacing(8)
        edit_btn = IconButton(QIcon('icons/edit.svg'), '#188BDB', '#185ADB')
        h_layout.addWidget(edit_btn)
        v_layout.addWidget(w1, alignment=Qt.AlignmentFlag.AlignHCenter)

        email = QLabel('ahmed@example.com')
        email.setObjectName('email')
        v_layout.addWidget(email, alignment=Qt.AlignmentFlag.AlignHCenter)

        role = QLabel('admin')
        role.setObjectName('role')
        v_layout.addWidget(role, alignment=Qt.AlignmentFlag.AlignHCenter)

    def setup_bottom_sheet(self):
        frame = QFrame()
        frame.setObjectName('bottom_container')
        frame.setFixedSize(self.parentWidget().width(), 320)
        self.root_layout.addWidget(frame, alignment=Qt.AlignmentFlag.AlignBottom)

        g_layout = QGridLayout(frame)
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
