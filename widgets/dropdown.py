from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import QFrame, QHBoxLayout, QLabel, QMenu, QPushButton


class DropDown(QFrame):

    currentIndexChanged = pyqtSignal()
    currentTextChanged = pyqtSignal()

    def __init__(self, parent=None, size: QSize = QSize(150, 50), border: bool = True):
        super().__init__(parent=parent)
        self.items = []
        self.setObjectName('root_with_border' if border else 'root_without_border')
        self.setStyleSheet("""
            QFrame#root_with_border {
                border-radius: 5;
                background-color: #232931;
                border: 1px solid #00ADB5;
            }

            QFrame#root_without_border {
                border-radius: 5;
                background-color: #232931;
                border: none;
            }

            QLabel#lbl {
                color: #EEEEEE;
                font-size: 18px;
                font-weight: bold;
            }

            QPushButton#btn {
                border: none;
                background-color: transparent;
            }

            QMenu{
                background-color: #393E46;
                color: #EEEEEE;
            }

            QMenu::item{
                background-color: #393E46;
                color: #EEEEEE;
            }

            QMenu::item:selected{
                background-color: #00ADB5;
                color: #EEEEEE;
            }
        """)
        self.setFixedSize(size)
        self.setCursor(Qt.CursorShape.PointingHandCursor)

        l = QHBoxLayout(self)
        l.setContentsMargins(16, 16, 8, 16)
        l.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.lbl = QLabel()
        self.lbl.setObjectName('lbl')
        l.addWidget(self.lbl)

        l.addStretch()

        btn = QPushButton()
        btn.setObjectName('btn')
        btn.setIcon(QIcon('icons/arrow_drop.svg'))
        btn.setIconSize(QSize(26, 26))
        btn.clicked.connect(self.mousePressEvent)
        l.addWidget(btn)

    def addItems(self, items):
        self.items.extend(items)
        self.currentIndex = 0
        self.lbl.setText(items[0])

    def clear(self):
        self.items.clear()

    def currentIndex(self):
        return self.currentIndex

    def currentText(self):
        return self.items[self.currentIndex]

    def mousePressEvent(self, event):
        contextMenu = QMenu(self)
        contextMenu.setFixedWidth(self.size().width())

        for index, item in enumerate(self.items):
            action = QAction(item, self)
            action.triggered.connect(lambda _, i=index: self._setCurrentIndex(i))
            contextMenu.addAction(action)

        contextMenu.exec(self.window().geometry().topLeft() + self.geometry().bottomLeft())

    def _setCurrentIndex(self, index):
        self.currentIndex = index
        self.lbl.setText(self.items[index])
        self.currentIndexChanged.emit()
        self.currentTextChanged.emit()
