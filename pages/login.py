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

        self.v_layout = QVBoxLayout(self)
        self.v_layout.setSpacing(15)
        self.v_layout.setContentsMargins(25, 0, 25, 15)

        self.v_layout.addStretch()

        lbl = QLabel('Login')
        lbl.setObjectName('title')
        self.v_layout.addWidget(lbl, alignment=Qt.AlignmentFlag.AlignLeft)

        lbl2 = QLabel('sign into your account')
        lbl2.setObjectName('subtitle')
        self.v_layout.addWidget(lbl2, alignment=Qt.AlignmentFlag.AlignLeft)

        self.v_layout.addStretch()

        self.setup_input_fields()

        self.v_layout.addStretch()

        button = QPushButton("Login")
        button.setFixedSize(200, 50)
        button.setObjectName('login')
        self.v_layout.addWidget(button, alignment=Qt.AlignmentFlag.AlignCenter)

        self.setup_register_line()

    def setup_input_fields(self):
        size = QSize(350, 50)

        email = InputField('Email', "icons/email.svg")
        email.setFixedSize(size)
        self.v_layout.addWidget(email, alignment=Qt.AlignmentFlag.AlignHCenter)

        password = InputField('Password', "icons/lock.svg")
        password.setFixedSize(size)
        password.hide_contents(True)
        self.v_layout.addWidget(password, alignment=Qt.AlignmentFlag.AlignHCenter)

    def setup_register_line(self):
        register_widget = QWidget()
        h_layout = QHBoxLayout(register_widget)
        h_layout.setContentsMargins(0, 0, 0, 0)
        h_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        lbl1 = QLabel('Don\'t have an account?')
        lbl1.setObjectName('down')
        h_layout.addWidget(lbl1)

        btn2 = QPushButton('Register here')
        btn2.setObjectName('register')
        btn2.clicked.connect(self.register)
        btn2.setCursor(Qt.CursorShape.PointingHandCursor)
        h_layout.addWidget(btn2)

        self.v_layout.addWidget(register_widget, alignment=Qt.AlignmentFlag.AlignHCenter)

    def login(self):
        print("beshr")

    def register(self):
        from pages.register import RegisterPage
        self.window().navigate_to(RegisterPage)
