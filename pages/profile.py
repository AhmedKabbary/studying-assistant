from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from widgets.image import ImageWidget
from widgets.input_field import InputField
import controllers.auth as Auth


class ProfilePage(QWidget):

    url = 'pic.jpg'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('Profile')
        self.window().setStyleSheet('background-color: #232931')

        with open('styles/profile_page.css') as f:
            css = f.read()
            self.setStyleSheet(css)

        self.v_layout = QVBoxLayout(self)
        self.v_layout.setSpacing(10)
        self.v_layout.setContentsMargins(25, 25, 25, 25)

        self.setup_pic()

        self.v_layout.addStretch()

        self.setup_input_fields()

        self.v_layout.addStretch()

        register = QPushButton("Save")
        register.setFixedSize(200, 50)
        register.setObjectName('save')
        register.clicked.connect(self.save)
        register.setCursor(Qt.CursorShape.PointingHandCursor)
        self.v_layout.addWidget(register, alignment=Qt.AlignmentFlag.AlignHCenter)

    def setup_pic(self):
        self.image = ImageWidget()
        self.image.setFixedSize(100, 100)
        self.image.set_radius(50)
        self.image.set_image(Auth.user[2])
        self.image.setCursor(Qt.CursorShape.PointingHandCursor)
        self.image.clicked.connect(self.browse_files)
        self.v_layout.addWidget(self.image, alignment=Qt.AlignmentFlag.AlignHCenter)

    def setup_input_fields(self):
        size = QSize(350, 50)

        self.name = InputField('Name', "icons/person.svg")
        self.name.setFixedSize(size)
        self.name.set_text(Auth.user[3])
        self.v_layout.addWidget(self.name, alignment=Qt.AlignmentFlag.AlignHCenter)

        self.email = InputField('Email', "icons/email.svg")
        self.email.setFixedSize(size)
        self.email.set_text(Auth.user[4])
        self.v_layout.addWidget(self.email, alignment=Qt.AlignmentFlag.AlignHCenter)

        self.phone = InputField('Phone', "icons/phone.svg")
        self.phone.setFixedSize(size)
        self.phone.set_text(Auth.user[6])
        self.v_layout.addWidget(self.phone, alignment=Qt.AlignmentFlag.AlignHCenter)

        self.password = InputField('Password', "icons/lock.svg")
        self.password.setFixedSize(size)
        self.password.set_text(Auth.user[5])
        self.password.hide_contents(True)
        self.v_layout.addWidget(self.password, alignment=Qt.AlignmentFlag.AlignHCenter)

        self.password2 = InputField('Confirm Password', "icons/lock.svg")
        self.password2.setFixedSize(size)
        self.password2.set_text(Auth.user[5])
        self.password2.hide_contents(True)
        self.v_layout.addWidget(self.password2, alignment=Qt.AlignmentFlag.AlignHCenter)

    def save(self):
        import controllers.auth as Auth
        try:
            Auth.update(self.url, self.name.text(),  self.email.text(), self.phone.text(), self.password.text(), self.password2.text())
            self.window().back()
        except Exception as e:
            QMessageBox.critical(self, 'An error occurred', e.args[0])

    def browse_files(self):
        url, _ = QFileDialog.getOpenFileUrl(self, caption="Select image", filter="Images (*.jpg *.png)")
        if url.isValid():
            self.image.set_image(url.toLocalFile())
            self.url = url
