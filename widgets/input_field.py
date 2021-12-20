from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QFrame, QHBoxLayout, QLineEdit, QPushButton


class InputField(QFrame):
    def __init__(self, placeholder, is_password,icon):
        super().__init__()

        self.setFixedSize(300, 50)
        self.setObjectName('root')

        h_layout = QHBoxLayout(self)
        h_layout.setSpacing(15)

        btn = QPushButton()
        btn.setObjectName('btn')
        btn.setIcon(QIcon(icon))
        h_layout.addWidget(btn)
        
        input = QLineEdit()
        input.setObjectName('input')
        input.setPlaceholderText(placeholder)
        if is_password == True:
            input.setEchoMode(QLineEdit.EchoMode.Password)
        h_layout.addWidget(input)