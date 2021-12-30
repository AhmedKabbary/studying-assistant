from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QFrame, QHBoxLayout, QLabel, QPushButton


class TaskWidget(QFrame):
    def __init__(self, text, checked):
        super().__init__()
        self.checked = checked

        self.setStyleSheet("""
            QFrame#root{
                background-color: #393E46;
            }

            QLabel#lbl {
                color: #EEEEEE;
                font-size: 16px;
                font-weight: bold;
                background-color: transparent;
            }

            QPushButton#btn {
                border: none;
                background-color: transparent;
            }
        """)

        self.setObjectName('root')
        self.setFixedSize(350, 45)

        h_layout = QHBoxLayout(self)
        h_layout.setContentsMargins(20, 5, 25, 5)
        h_layout.setSpacing(15)

        lbl = QLabel()
        lbl.setObjectName('lbl')
        lbl.setText(text)
        h_layout.addWidget(lbl, alignment=Qt.AlignmentFlag.AlignLeft)

        self.check = QPushButton()
        self.check.setObjectName('btn')
        if self.checked:
            self.check.setIcon(QIcon('icons/checked.svg'))
        else:
            self.check.setIcon(QIcon('icons/unchecked.svg'))
        self.check.setIconSize(QSize(25, 25))
        h_layout.addWidget(self.check, alignment=Qt.AlignmentFlag.AlignRight)

    def clicked(self):
        self.checked = not self.checked
        if self.checked:
            self.check.setIcon(QIcon('icons/checked.svg'))
        else:
            self.check.setIcon(QIcon('icons/unchecked.svg'))
