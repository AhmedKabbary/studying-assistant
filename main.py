import sys
import auth
from typing import List
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from pages.home import HomePage
from pages.login import LoginPage
from pages.register import RegisterPage
from pages.timer import TimerPage
from widgets.title_bar import TitleBar

app = QApplication(sys.argv)
app.setQuitOnLastWindowClosed(False)


class MainWindow(QMainWindow):

    history = []

    def __init__(self, app: QApplication):
        super().__init__()
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint)
        self.adjust_to_side(app)
        self.title_bar = TitleBar()
        self.setMenuWidget(self.title_bar)
        self.setup_content()

    def adjust_to_side(self, app: QApplication):
        w, h = 400, 600
        available_geometry = app.primaryScreen().availableGeometry()
        self.setGeometry(int(available_geometry.width() - (w)), int(available_geometry.height() - (h)), w, h)

    def setup_content(self):
        page = None
        if auth.get_current_user() is None:
            if auth.is_first_time():
                page = RegisterPage
            else:
                page = LoginPage
        else:
            page = HomePage
        self.navigate_to(page(self))

    def navigate_to(self, page: QWidget):
        self.history.append(type(self.centralWidget()))
        self.setCentralWidget(page)
        if page.__class__ not in [HomePage, LoginPage, RegisterPage]:
            self.title_bar.setWindowTitle(page.windowTitle())
            self.title_bar.show_back_btn(True)
        else:
            self.title_bar.setWindowTitle(None)
            self.title_bar.show_back_btn(False)

    def back(self):
        page = self.history.pop()
        instance = page(self)
        self.setCentralWidget(instance)
        if instance.__class__ not in [HomePage, LoginPage, RegisterPage]:
            self.title_bar.setWindowTitle(page.windowTitle())
            self.title_bar.show_back_btn(True)
        else:
            self.title_bar.setWindowTitle(None)
            self.title_bar.show_back_btn(False)


window = MainWindow(app)
window.show()

tray = QSystemTrayIcon()
tray.setIcon(QIcon('icons/minimize.svg'))
tray.setVisible(True)

menu = QMenu()

open = QAction("Open")
open.triggered.connect(window.show)
menu.addAction(open)


def test_navigate():
    window.navigate_to(TimerPage(window))


test = QAction("Navigate")
test.triggered.connect(test_navigate)
menu.addAction(test)

quit = QAction("Quit")
quit.triggered.connect(app.quit)
menu.addAction(quit)

tray.setContextMenu(menu)

sys.exit(app.exec())
