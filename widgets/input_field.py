from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QFrame, QHBoxLayout, QLineEdit, QPushButton


class InputField(QFrame):
    def __init__(self, placeholder, icon):
        super().__init__()

        self.setStyleSheet("""
            QFrame#root{
                background-color:#393E46;
                border-radius: 10;
            }

            QLineEdit#input {
                border: none;
                color: #EEEEEE;
                background-color: transparent;
            }

            QPushButton#btn {
                border: none;
                background-color: transparent;
            }
        """)

        self.setObjectName('root')

        h_layout = QHBoxLayout(self)
        h_layout.setSpacing(15)
        h_layout.setContentsMargins(16, 0, 16, 0)

        btn = QPushButton()
        btn.setObjectName('btn')
        btn.setIcon(QIcon(icon))
        btn.setCheckable(False)
        h_layout.addWidget(btn)

        self.input = QLineEdit()
        self.input.setObjectName('input')
        self.input.setPlaceholderText(placeholder)
        h_layout.addWidget(self.input)

    def hide_contents(self, state: bool):
        if state == True:
            self.input.setEchoMode(QLineEdit.EchoMode.Password)
        else:
            self.input.setEchoMode(QLineEdit.EchoMode.Normal)

    def text(self):
        return self.input.text()
