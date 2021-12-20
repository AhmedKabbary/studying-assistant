from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from widgets.input_field import InputField


class LoginPage(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('Login')
        self.window().setStyleSheet('background-color: #232931')

        with open('styles/login_page.css') as f:
            css = f.read()
            self.setStyleSheet(css)

        v_layout = QVBoxLayout(self)
        lbl = QLabel('Login')
        lbl.setObjectName('title')
        v_layout.addWidget(lbl, alignment=Qt.AlignmentFlag.AlignLeft)
        v_layout.setContentsMargins(16,16,16,16)

        lbl2 = QLabel('sign into your account')
        lbl2.setObjectName('title2')
        v_layout.addWidget(lbl2, alignment=Qt.AlignmentFlag.AlignLeft)

        email = InputField('Email', False,"icons/email.svg")
        v_layout.addWidget(email, alignment=Qt.AlignmentFlag.AlignCenter)

        password = InputField('Password', True,"icons/lock.svg")
        v_layout.addWidget(password, alignment=Qt.AlignmentFlag.AlignCenter)

        button=QPushButton("Login")
        button.setFixedSize(200,50)
        button.setObjectName('login')
        v_layout.addWidget(button, alignment=Qt.AlignmentFlag.AlignCenter)

        b=QWidget()
        ho_lay=QHBoxLayout(b)
        c1=QLabel("Don't have an account?")
        c1.setObjectName('down1')
        ho_lay.addWidget(c1, alignment=Qt.AlignmentFlag.AlignCenter)
        c2=QLabel('Register here')
        c2.setObjectName('down2')
        ho_lay.addWidget(c2, alignment=Qt.AlignmentFlag.AlignCenter)
        v_layout.addWidget(b, alignment=Qt.AlignmentFlag.AlignCenter)


