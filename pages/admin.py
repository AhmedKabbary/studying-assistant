from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
import db


class AdminPage(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('Admin Panel')
        self.window().setStyleSheet('background-color: #232931')

        with open('styles/admin_page.css') as f:
            css = f.read()
            self.setStyleSheet(css)

        v_layout = QVBoxLayout(self)
        v_layout.setSpacing(15)
        v_layout.setContentsMargins(20, 10, 20, 20)

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setAlignment(Qt.AlignmentFlag.AlignTop)
        scroll.setFixedSize(350, 500)
        scroll.verticalScrollBar().hide()
        scroll.horizontalScrollBar().hide()
        scroll.setStyleSheet('border: none;')

        w = QWidget()
        self.list_layout = QVBoxLayout(w)
        self.list_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        v_layout.addWidget(scroll, alignment=Qt.AlignmentFlag.AlignTop)
        scroll.setWidget(w)

        self.load_list()

    def load_list(self):
        for i in reversed(range(self.list_layout.count())):
            self.list_layout.itemAt(i).widget().deleteLater()

        result = db.cursor.execute('SELECT * FROM USER')
        for row in result:
            t = Account(row)
            t.update_list.connect(self.load_list)
            self.list_layout.addWidget(t)


class Account(QLabel):

    update_list = pyqtSignal()

    def __init__(self, user):
        super().__init__()
        self.user = user
        self.setText(user[4])
        self.setFixedSize(350, 50)
        self.setObjectName('account_lbl')
        self.setCursor(Qt.CursorShape.PointingHandCursor)

    def mousePressEvent(self, ev: QMouseEvent):
        if ev.button() == Qt.MouseButton.LeftButton:
            import controllers.auth as Auth
            if self.user[0] != Auth.user[0]:
                d = AccountDialog(self.user)
                d.update_list.connect(self.update_list.emit)
                d.exec()


class AccountDialog(QDialog):

    update_list = pyqtSignal()

    def __init__(self, user):
        super().__init__()
        self.user = user

        self.setWindowTitle('Setup account')
        self.setFixedWidth(250)
        self.setStyleSheet("""
            QDialog {
                background-color: #232931;
            }

            QLineEdit {
                border: none;
                background-color: #393E46;
                border-radius: 5;
                padding: 8px;
                color: #EEEEEE;
            }

            QPushButton {
                border: none;
                border-radius: 5;
                font-size: 20;
                font-weight: bold;
                background-color: #393E46;
                color : #EEEEEE;
            }

            QCheckBox {
                color: #EEEEEE;
            }

            QCheckBox::indicator {
                color: black;
            }
        """)

        v_layout = QVBoxLayout(self)

        permissions = user[7]

        self.p_t = QCheckBox('Tasks')
        self.p_t.setChecked('T' in permissions)
        v_layout.addWidget(self.p_t)
        self.p_p = QCheckBox('Pomodoro')
        self.p_p.setChecked('P' in permissions)
        v_layout.addWidget(self.p_p)
        self.p_c = QCheckBox('Units Converter')
        self.p_c.setChecked('C' in permissions)
        v_layout.addWidget(self.p_c)
        self.p_d = QCheckBox('Dictionary')
        self.p_d.setChecked('D' in permissions)
        v_layout.addWidget(self.p_d)
        self.p_a = QCheckBox('AI Answerer')
        self.p_a.setChecked('A' in permissions)
        v_layout.addWidget(self.p_a)
        self.p_g = QCheckBox('Google Translate')
        self.p_g.setChecked('G' in permissions)
        v_layout.addWidget(self.p_g)

        v_layout.addSpacerItem(QSpacerItem(15, 15))

        widget = QWidget()
        h_layout = QHBoxLayout(widget)
        h_layout.setContentsMargins(0, 0, 0, 0)

        btn1 = QPushButton()
        btn1.setText("SAVE")
        btn1.setFixedHeight(30)
        btn1.clicked.connect(self.save)
        btn1.setCursor(Qt.CursorShape.PointingHandCursor)
        h_layout.addWidget(btn1, stretch=1)

        btn2 = QPushButton()
        btn2.setText("DELETE")
        btn2.setFixedHeight(30)
        btn2.setCursor(Qt.CursorShape.PointingHandCursor)
        btn2.clicked.connect(self.delete)

        h_layout.addWidget(btn2, stretch=1)

        v_layout.addWidget(widget)

    def save(self):
        permissions = []

        if self.p_t.isChecked():
            permissions.append('T')
        elif self.p_p.isChecked():
            permissions.append('P')
        elif self.p_c.isChecked():
            permissions.append('C')
        elif self.p_d.isChecked():
            permissions.append('D')
        elif self.p_a.isChecked():
            permissions.append('A')
        elif self.p_g.isChecked():
            permissions.append('G')

        import db
        db.cursor.execute('UPDATE USER SET PERMISSIONS = ? WHERE ID = ?', (','.join(permissions), self.user[0]))
        db.cursor.commit()
        self.update_list.emit()
        self.close()

    def delete(self):
        import db
        db.cursor.execute('DELETE FROM USER WHERE ID = ?', (self.user[0],))
        db.cursor.commit()
        self.update_list.emit()
        self.close()
