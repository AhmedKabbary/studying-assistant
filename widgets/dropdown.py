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
                border: 1px solid #188bdb;
            }

            QFrame#root_without_border {
                border-radius: 5;
                background-color: transparent;
                border: none;
            }

            QLabel#lbl {
                color: #EEEEEE;
                font-size: 18px;
                font-weight: bold;
                background-color: transparent;
            }

            QPushButton#btn {
                border: none;
                background-color: transparent;
            }
        """)
        self.setFixedSize(size)
        self.setCursor(Qt.CursorShape.PointingHandCursor)

        l = QHBoxLayout(self)
        l.setContentsMargins(16, 0, 8, 0)
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
        self._currentIndex = 0
        self.lbl.setText(items[0])

    def clear(self):
        self.items.clear()

    def currentIndex(self):
        return self._currentIndex

    def currentText(self):
        return self.items[self._currentIndex]

    def mousePressEvent(self, event):
        contextMenu = QMenu(self)
        contextMenu.setFixedWidth(self.size().width())

        for index, item in enumerate(self.items):
            action = QAction(item, self)
            action.triggered.connect(lambda _, i=index: self.setCurrentIndex(i))
            contextMenu.addAction(action)

        contextMenu.exec(self.mapToGlobal(QPoint(0, self.height())))

    def setCurrentIndex(self, index):
        self._currentIndex = index
        self.lbl.setText(self.items[index])
        self.currentIndexChanged.emit()
        self.currentTextChanged.emit()
