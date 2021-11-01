from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QHBoxLayout, QLabel, QWidget
from widgets.icon_btn import IconButton


class TitleBar(QWidget):
    def __init__(self):
        super().__init__()

        layout = QHBoxLayout(self)
        layout.setSpacing(8)
        layout.setContentsMargins(12, 12, 12, 12)

        self.back_btn = IconButton(QIcon('icons/arrow_back.svg'), '#185ADB', '#188BDB')
        self.show_back_btn(False)
        self.back_btn.clicked.connect(self.back)
        layout.addWidget(self.back_btn, alignment=Qt.AlignmentFlag.AlignLeft)

        layout.addStretch()

        title_lbl = QLabel(self.windowTitle())
        title_lbl.setStyleSheet("""
            color: #DDDDDD;
            font-size: 18px;
            font-weight: bold;
        """)
        self.windowTitleChanged.connect(title_lbl.setText)
        layout.addWidget(title_lbl, alignment=Qt.AlignmentFlag.AlignLeft)

        layout.addStretch()

        min_btn = IconButton(QIcon('icons/minimize.svg'), '#185ADB', '#188BDB')
        min_btn.clicked.connect(self.minimize)
        layout.addWidget(min_btn, alignment=Qt.AlignmentFlag.AlignRight)

    def show_back_btn(self, state: bool):
        if state:
            self.back_btn.show()
        else:
            self.back_btn.hide()

    def back(self):
        self.window().back()

    def minimize(self):
        self.window().close()
