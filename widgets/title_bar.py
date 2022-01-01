from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QFrame, QHBoxLayout, QLabel
from pages.login import LoginPage
from widgets.icon_btn import IconButton


class TitleBar(QFrame):
    def __init__(self):
        super().__init__()

        self.setObjectName('title_bar')

        layout = QHBoxLayout(self)
        layout.setSpacing(8)
        layout.setContentsMargins(12, 12, 12, 14)

        self.back_btn = IconButton(QIcon('icons/arrow_back.svg'), '#188BDB', '#185ADB')
        self.back_btn.clicked.connect(self.back)
        layout.addWidget(self.back_btn, alignment=Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)

        self.logout_btn = IconButton(QIcon('icons/logout.svg'), '#188BDB', '#185ADB')
        self.logout_btn.clicked.connect(self.logout)
        layout.addWidget(self.logout_btn, alignment=Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)

        self.show_back_btn(False)
        self.show_logout_btn(False)

        layout.addStretch()

        title_lbl = QLabel(self.windowTitle())
        title_lbl.setStyleSheet("""
            color: #EEEEEE;
            font-size: 16px;
            font-weight: bold;
        """)
        self.windowTitleChanged.connect(title_lbl.setText)
        layout.addWidget(title_lbl, alignment=Qt.AlignmentFlag.AlignCenter)

        layout.addStretch()

        min_btn = IconButton(QIcon('icons/minimize.svg'), '#188BDB', '#185ADB')
        min_btn.clicked.connect(self.minimize)
        layout.addWidget(min_btn, alignment=Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)

    def show_back_btn(self, state: bool):
        if state:
            self.back_btn.show()
            self.setStyleSheet("""
                QFrame#title_bar {
                    border-bottom: 1px solid #393E46;
                }
            """)
        else:
            self.back_btn.hide()
            self.setStyleSheet("""
                QFrame#title_bar {
                    border-bottom: none;
                }
            """)

    def show_logout_btn(self, state: bool):
        if state:
            self.logout_btn.show()
            self.setStyleSheet("""
                QFrame#title_bar {
                    border-bottom: 1px solid #393E46;
                }
            """)
        else:
            self.logout_btn.hide()
            self.setStyleSheet("""
                QFrame#title_bar {
                    border-bottom: none;
                }
            """)

    def back(self):
        self.window().back()

    def logout(self):
        import controllers.auth as Auth
        Auth.logout()
        self.window().navigate_to(LoginPage)

    def minimize(self):
        self.window().close()
