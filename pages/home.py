from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import (QFrame, QGridLayout, QHBoxLayout, QLabel, QPushButton, QVBoxLayout, QWidget)
from widgets.home_btn import HomeButton
from widgets.icon_btn import IconButton
from widgets.image import ImageWidget
from pages import *
import controllers.auth as Auth


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

        Auth.refresh_user()
        self.setup_profile()
        self.setup_bottom_sheet()

    def setup_profile(self):
        profile_root = QWidget()
        profile_root.setFixedWidth(self.parentWidget().width())
        self.root_layout.addWidget(profile_root, alignment=Qt.AlignmentFlag.AlignCenter)

        v_layout = QVBoxLayout(profile_root)
        v_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        image = ImageWidget()
        image.setFixedSize(100, 100)
        image.set_radius(20)
        image.set_image(Auth.user[2])
        v_layout.addWidget(image, alignment=Qt.AlignmentFlag.AlignHCenter)

        v_layout.addSpacing(16)

        w1 = QWidget()
        h_layout = QHBoxLayout(w1)
        h_layout.setContentsMargins(0, 0, 0, 0)
        h_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        name = QLabel(Auth.user[3])
        name.setObjectName('name')
        h_layout.addWidget(name)
        h_layout.addSpacing(8)
        edit_btn = IconButton(QIcon('icons/edit.svg'), '#188BDB', '#185ADB')
        edit_btn.clicked.connect(self.to_profile)
        h_layout.addWidget(edit_btn)
        v_layout.addWidget(w1, alignment=Qt.AlignmentFlag.AlignHCenter)

        email = QLabel(Auth.user[4])
        email.setObjectName('email')
        v_layout.addWidget(email, alignment=Qt.AlignmentFlag.AlignHCenter)

        role = QPushButton()
        if Auth.user[1] == 1:
            role.setText('admin')
            role.setObjectName('role_admin')
            role.setCursor(Qt.CursorShape.PointingHandCursor)
            role.clicked.connect(self.to_admin)
        else:
            role.setText('user')
            role.setObjectName('role_user')
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

        available_buttons = Auth.user[7]

        g_layout.addWidget(line, 0, 1)
        g_layout.addWidget(HomeButton('Tasks', QIcon('icons/tasks.svg'), TasksPage, 'T' in available_buttons), 1, 0)
        g_layout.addWidget(HomeButton('Pomodoro', QIcon('icons/timer.svg'), PomodorosPage, 'P' in available_buttons), 1, 1)
        g_layout.addWidget(HomeButton('Converter', QIcon('icons/ruler.svg'), ConverterPage, 'C' in available_buttons), 1, 2)
        g_layout.addWidget(HomeButton('Dictionary', QIcon('icons/bookmark.svg'), DictionaryPage, 'D' in available_buttons), 2, 0)
        g_layout.addWidget(HomeButton('AI Answerer', QIcon('icons/book.svg'), AIPage, 'A' in available_buttons), 2, 1)
        g_layout.addWidget(HomeButton('Translator', QIcon('icons/g_translate.svg'), TranslatorPage, 'G' in available_buttons), 2, 2)

    def to_admin(self):
        self.window().navigate_to(AdminPage)

    def to_profile(self):
        self.window().navigate_to(ProfilePage)
