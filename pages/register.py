from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from widgets.image import ImageWidget
from widgets.input_field import InputField


class RegisterPage(QWidget):

    pic = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('Register')
        self.window().setStyleSheet('background-color: #232931')

        with open('styles/register_page.css') as f:
            css = f.read()
            self.setStyleSheet(css)

        self.v_layout = QVBoxLayout(self)
        self.v_layout.setSpacing(10)
        self.v_layout.setContentsMargins(25, 0, 25, 15)

        image = ImageWidget()
        image.setFixedSize(100, 100)
        image.set_radius(50)
        image.set_image('pic.jpg')
        self.v_layout.addWidget(image, alignment=Qt.AlignmentFlag.AlignHCenter)

        self.v_layout.addStretch()

        self.setup_input_fields()

        self.v_layout.addStretch()

        register = QPushButton("Register")
        register.setFixedSize(200, 50)
        register.setObjectName('register')
        register.clicked.connect(self.register)
        register.setCursor(Qt.CursorShape.PointingHandCursor)
        self.v_layout.addWidget(register, alignment=Qt.AlignmentFlag.AlignHCenter)

        self.v_layout.addSpacing(5)

        self.setup_login_line()

    def setup_input_fields(self):
        size = QSize(350, 50)

        self.name = InputField('Name', "icons/person.svg")
        self.name.setFixedSize(size)
        self.v_layout.addWidget(self.name, alignment=Qt.AlignmentFlag.AlignHCenter)

        self.email = InputField('Email', "icons/email.svg")
        self.email.setFixedSize(size)
        self.v_layout.addWidget(self.email, alignment=Qt.AlignmentFlag.AlignHCenter)

        self.phone = InputField('Phone', "icons/phone.svg")
        self.phone.setFixedSize(size)
        self.v_layout.addWidget(self.phone, alignment=Qt.AlignmentFlag.AlignHCenter)

        self.password = InputField('Password', "icons/lock.svg")
        self.password.setFixedSize(size)
        self.password.hide_contents(True)
        self.v_layout.addWidget(self.password, alignment=Qt.AlignmentFlag.AlignHCenter)

        self.password2 = InputField('Confirm Password', "icons/lock.svg")
        self.password2.setFixedSize(size)
        self.password2.hide_contents(True)
        self.v_layout.addWidget(self.password2, alignment=Qt.AlignmentFlag.AlignHCenter)

    def setup_login_line(self):
        login_widget = QWidget()
        h_layout = QHBoxLayout(login_widget)
        h_layout.setContentsMargins(0, 0, 0, 0)
        h_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        lbl1 = QLabel('Already have an account?')
        lbl1.setObjectName('down')
        h_layout.addWidget(lbl1)

        btn2 = QPushButton('Login here')
        btn2.setObjectName('login')
        btn2.clicked.connect(self.login)
        btn2.setCursor(Qt.CursorShape.PointingHandCursor)
        h_layout.addWidget(btn2)

        self.v_layout.addWidget(login_widget, alignment=Qt.AlignmentFlag.AlignHCenter)

    def register(self):
        import controllers.auth as Auth
        #try:
        Auth.register(self.pic, self.name.text(),  self.email.text(), self.phone.text(), self.password.text(), self.password2.text())
        #except Exception as e:
        #    QMessageBox.critical(self, 'An error occurred', e.args[0])

    def login(self):
        from pages.login import LoginPage
        self.window().navigate_to(LoginPage)
