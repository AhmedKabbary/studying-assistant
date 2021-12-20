import db
import sys
from typing import Type
from pages import *
from controllers import auth
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtWidgets import QApplication, QMainWindow, QMenu, QSystemTrayIcon, QWidget
from widgets.title_bar import TitleBar

app = QApplication(sys.argv)
app.setQuitOnLastWindowClosed(False)  # app remains active even if the window is closed

with open('styles/_app.css') as f:
    css = f.read()
    app.setStyleSheet(css)


class MainWindow(QMainWindow):

    history = []

    def __init__(self, app: QApplication):
        super().__init__()
        self.setWindowFlags(Qt.WindowType.Tool | Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint)
        self.adjust_to_bottom_left_side(app)
        self.title_bar = TitleBar()
        self.setMenuWidget(self.title_bar)
        self.setup_content()

    def adjust_to_bottom_left_side(self, app: QApplication):
        w, h = 400, 600
        available_geometry = app.primaryScreen().availableGeometry()
        x = available_geometry.x() + int(available_geometry.width() - w)
        y = available_geometry.y() + int(available_geometry.height() - h)
        self.move(x, y)
        self.setFixedSize(w, h)

    def setup_content(self):
        page = None
        if auth.get_current_user() is None:
            if auth.is_first_time():
                page = RegisterPage
            else:
                page = LoginPage
        else:
            page = HomePage
        self.navigate_to(page)

    def navigate_to(self, page: Type[QWidget]):
        self.history.append(type(self.centralWidget()))  # add the current centralWidget type to the history
        instance = page(self)
        self.setCentralWidget(instance)  # then navigate to the new page
        if instance.__class__ not in [HomePage, LoginPage, RegisterPage]:
            self.title_bar.setWindowTitle(instance.windowTitle())
            self.title_bar.show_back_btn(True)
        else:
            self.title_bar.setWindowTitle(None)
            self.title_bar.show_back_btn(False)

    def back(self):
        page = self.history.pop()  # get and remove the last page from the history
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
tray.setIcon(QIcon('icons/tray.svg'))
tray.setVisible(True)

menu = QMenu()

open = QAction("Open")
open.triggered.connect(window.show)
menu.addAction(open)

quit = QAction("Quit")
quit.triggered.connect(app.quit)
menu.addAction(quit)

tray.setContextMenu(menu)

db.init()

sys.exit(app.exec())
