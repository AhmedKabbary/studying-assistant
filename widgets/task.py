from PyQt6.QtCore import QPoint, QSize, Qt, pyqtSignal
from PyQt6.QtGui import QAction, QIcon, QMouseEvent
from PyQt6.QtWidgets import QFrame, QHBoxLayout, QLabel, QMenu, QPushButton


class TaskWidget(QFrame):

    deleted = pyqtSignal()

    def __init__(self, id, text, checked):
        super().__init__()
        self.id = id
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
        self.setCursor(Qt.CursorShape.PointingHandCursor)

        h_layout = QHBoxLayout(self)
        h_layout.setContentsMargins(20, 5, 25, 5)
        h_layout.setSpacing(15)

        lbl = QLabel()
        lbl.setObjectName('lbl')
        lbl.setText(text)
        h_layout.addWidget(lbl, alignment=Qt.AlignmentFlag.AlignLeft)

        self.check = QPushButton()
        self.check.setObjectName('btn')
        if self.checked == 1:
            self.check.setIcon(QIcon('icons/checked.svg'))
        else:
            self.check.setIcon(QIcon('icons/unchecked.svg'))
        self.check.setIconSize(QSize(25, 25))
        self.check.clicked.connect(self.clicked)
        h_layout.addWidget(self.check, alignment=Qt.AlignmentFlag.AlignRight)

    def mousePressEvent(self, a0: QMouseEvent) -> None:
        if a0.button() == Qt.MouseButton.LeftButton:
            self.clicked()
        if a0.button() == Qt.MouseButton.RightButton:
            menu = QMenu()
            delete = QAction('Delete')
            delete.triggered.connect(self.delete_word)
            menu.addAction(delete)
            menu.exec(QPoint(int(a0.globalPosition().x()), int(a0.globalPosition().y())))

    def clicked(self):
        # swap the int as a switch (0,1)
        if self.checked == 1:
            self.checked = 0
        else:
            self.checked = 1

        if self.checked == 1:
            self.check.setIcon(QIcon('icons/checked.svg'))
        else:
            self.check.setIcon(QIcon('icons/unchecked.svg'))

        import db
        db.cursor.execute('UPDATE TASKS SET CHECKED = ? WHERE ID = ?', (self.checked, str(self.id)))
        db.cursor.commit()

    def delete_word(self):
        import db
        db.cursor.execute('DELETE FROM TASKS WHERE ID = ' + str(self.id))
        db.cursor.commit()
        self.deleted.emit()
