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
        button.clicked.connect(self.login)
        button.setCursor(Qt.CursorShape.PointingHandCursor)
        self.v_layout.addWidget(button, alignment=Qt.AlignmentFlag.AlignCenter)

        self.setup_register_line()

    def setup_input_fields(self):
        size = QSize(350, 50)

        self.email = InputField('Email', "icons/email.svg")
        self.email.setFixedSize(size)
        self.v_layout.addWidget(self.email, alignment=Qt.AlignmentFlag.AlignHCenter)

        self.password = InputField('Password', "icons/lock.svg")
        self.password.setFixedSize(size)
        self.password.hide_contents(True)
        self.v_layout.addWidget(self.password, alignment=Qt.AlignmentFlag.AlignHCenter)

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
        import controllers.auth as Auth
        try:
            Auth.login(self.email.text(), self.password.text())
            from pages.home import HomePage
            self.window().navigate_to(HomePage)
        except Exception as e:
            QMessageBox.critical(self, 'An error occurred', e.args[0])

    def register(self):
        from pages.register import RegisterPage
        self.window().navigate_to(RegisterPage)
