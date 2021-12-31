import db
import sys
from typing import Type
from pages import *
from controllers import auth
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtWidgets import QApplication, QMainWindow, QMenu, QSystemTrayIcon, QWidget, QMessageBox
from widgets.title_bar import TitleBar
from controllers.translator import TranslatorHandler

app = QApplication(sys.argv)
# app remains active even if the window is closed
app.setQuitOnLastWindowClosed(False)

with open('styles/_app.css') as f:
    css = f.read()
    app.setStyleSheet(css)

auto_translation = False


class MainWindow(QMainWindow):

    history = []

    def __init__(self, app: QApplication):
        super().__init__()
        self.setWindowFlags(
            Qt.WindowType.Tool | Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint)
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
        if auth.is_logged_in():
            page = HomePage
        else:
            if auth.is_first_time():
                page = RegisterPage
            else:
                page = LoginPage

        self.navigate_to(page)

    def navigate_to(self, page: Type[QWidget]):
        # add the current centralWidget type to the history
        self.history.append(type(self.centralWidget()))
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


db.init()


def answered(translated: str):
    w = QWidget()
    QMessageBox.warning(w, 'Translation', translated)


def translate():
    if auto_translation:
        transhandler = TranslatorHandler(
            app, 'en', 'ar', app.clipboard().text())
        transhandler.answer.connect(answered)
        transhandler.start()


app.clipboard().dataChanged.connect(translate)

window = MainWindow(app)
window.show()

tray = QSystemTrayIcon()
tray.setIcon(QIcon('icons/tray.svg'))
tray.setVisible(True)

menu = QMenu()

open = QAction("Open")
open.triggered.connect(window.show)
menu.addAction(open)

auto = QAction("Turn on Auto Translation")


def turn_translation():
    global auto_translation
    auto_translation = not auto_translation
    auto.setText(
        "Turn off Auto Translation" if auto_translation else "Turn on Auto Translation")


auto.triggered.connect(turn_translation)
menu.addAction(auto)

quit = QAction("Quit")
quit.triggered.connect(app.quit)
menu.addAction(quit)

tray.setContextMenu(menu)

sys.exit(app.exec())
