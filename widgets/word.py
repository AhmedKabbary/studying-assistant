from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *


class WordWidget(QFrame):

    deleted = pyqtSignal()

    def __init__(self, id, text, difficulty):
        super().__init__()
        self.id = id

        self.setFixedSize(170, 45)
        self.setObjectName('root')
        self.setStyleSheet("""
            QFrame#root {
                border-radius: 50;
                background-color: #393E46;
            }
        """)
        self.setCursor(Qt.CursorShape.PointingHandCursor)

        layout = QHBoxLayout(self)
        layout.setSpacing(15)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)

        band = QFrame()
        band.setFixedSize(4, 45)
        if difficulty == 0:
            band.setStyleSheet("""
                background-color: #0BDA51;
                border-top-left-radius: 5;
                border-bottom-left-radius: 5;
            """)
        elif difficulty == 1:
            band.setStyleSheet("""
                background-color: #E4D00A;
                border-top-left-radius: 5;
                border-bottom-left-radius: 5;
            """)
        elif difficulty == 2:
            band.setStyleSheet("""
                background-color: red;
                border-top-left-radius: 5;
                border-bottom-left-radius: 5;
            """)
        layout.addWidget(band)

        label = QLabel(text)
        label.setStyleSheet("""
            color: #EEEEEE;
            font-size: 18px;
            background-color: transparent;
        """)
        layout.addWidget(label)

    def mousePressEvent(self, a0: QMouseEvent):
        if a0.button() == Qt.MouseButton.RightButton:
            menu = QMenu()
            delete = QAction('Delete')
            delete.triggered.connect(self.delete_word)
            menu.addAction(delete)
            menu.exec(QPoint(int(a0.globalPosition().x()), int(a0.globalPosition().y())))

    def delete_word(self):
        import db
        db.cursor.execute('DELETE FROM DICTIONARY WHERE ID = ' + str(self.id))
        db.cursor.commit()
        self.deleted.emit()
