from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

from widgets.input_field import InputField


class RegisterPage(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('Register')
        self.window().setStyleSheet('background-color: #232931')

        with open('styles/register_page.css') as f:
            css = f.read()
            self.setStyleSheet(css)

        v_layout = QVBoxLayout(self)

        name = InputField('Name', False,"icons/person.svg")
        v_layout.addWidget(name, alignment=Qt.AlignmentFlag.AlignCenter)

        email = InputField('Email', False,"icons/email.svg")
        v_layout.addWidget(email, alignment=Qt.AlignmentFlag.AlignCenter)

        phone = InputField('Phone', False,"icons/phone.svg")
        v_layout.addWidget(phone, alignment=Qt.AlignmentFlag.AlignCenter)

        password = InputField('Password', True,"icons/lock.svg")
        v_layout.addWidget(password, alignment=Qt.AlignmentFlag.AlignCenter)

        password2 = InputField('Confirm Password', True,"icons/lock.svg")
        v_layout.addWidget(password2, alignment=Qt.AlignmentFlag.AlignCenter)

        button=QPushButton("Register")
        button.setFixedSize(200,50)
        button.setObjectName('register')
        button.clicked.connect(self.register)
        v_layout.addWidget(button, alignment=Qt.AlignmentFlag.AlignCenter)

        b=QWidget()
        ho_lay=QHBoxLayout(b)
        c1=QLabel('Already have an account?')
        c1.setObjectName('down1')
        ho_lay.addWidget(c1, alignment=Qt.AlignmentFlag.AlignCenter)
        c2=QLabel('Login here')
        c2.setObjectName('down2')
        ho_lay.addWidget(c2, alignment=Qt.AlignmentFlag.AlignCenter)
        v_layout.addWidget(b, alignment=Qt.AlignmentFlag.AlignCenter)
    def register(self):
        print("beshr")

