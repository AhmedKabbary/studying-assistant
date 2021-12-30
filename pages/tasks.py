from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from widgets.dropdown import DropDown
from widgets.task import TaskWidget


class TasksPage(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('My Tasks')
        self.window().setStyleSheet('background-color: #232931')

        with open('styles/tasks_page.css') as f:
            css = f.read()
            self.setStyleSheet(css)

        v_layout = QVBoxLayout(self)
        v_layout.setSpacing(15)
        v_layout.setContentsMargins(20, 10, 20, 20)

        self.type_combo = DropDown(size=QSize(175, 50))
        entries = ["Shopping", "Home", "Work", "University"]
        self.type_combo.addItems(entries)
        v_layout.addWidget(self.type_combo, alignment=Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setAlignment(Qt.AlignmentFlag.AlignTop)
        scroll.setFixedSize(350, 400)
        scroll.verticalScrollBar().hide()
        scroll.horizontalScrollBar().hide()
        scroll.setStyleSheet('border: none;')

        w = QWidget()
        self.list_layout = QVBoxLayout(w)
        self.list_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        v_layout.addWidget(scroll)
        scroll.setWidget(w)

        def add_task():
            d = InputTaskDialog()
            d.task_added.connect(self.shahd)
            d.exec()

        btn = QPushButton()
        btn.setText("ADD TASK")
        btn.setFixedSize(200, 50)
        btn.setObjectName('add')
        btn.clicked.connect(add_task)
        btn.setCursor(Qt.CursorShape.PointingHandCursor)
        v_layout.addWidget(
            btn, alignment=Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignBottom)

    def shahd(self, task, type):
        t = TaskWidget(task, False)
        self.list_layout.addWidget(t)


class InputTaskDialog(QDialog):

    task_added = pyqtSignal(str, str)

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Add a task')
        self.setStyleSheet("""
            QDialog {
                background-color: #232931;
            }

            QLineEdit {
                border: none;
                background-color: #393E46;
                border-radius: 5;
                padding: 8px;
            }

            QGroupBox {
                border: 1px solid #646464;
                border-radius: 5;
                color : #EEEEEE;
            }

            QPushButton {
                border: none;
                border-radius: 5;
                font-size: 20;
                font-weight: bold;
                background-color: #393E46;
                color : #EEEEEE;
            }

            QRadioButton {
                color: #EEEEEE;
            }

            QLineEdit {
                color: #EEEEEE;
            }
        """)

        v_layout = QVBoxLayout(self)
        v_layout.setSpacing(24)

        self.task = QLineEdit()
        self.task.setPlaceholderText('Enter a task')
        v_layout.addWidget(self.task)

        group = QGroupBox()
        group.setTitle('Select Type')
        group_layout = QVBoxLayout(group)

        self.work = QRadioButton('work', group)
        group_layout.addWidget(self.work)
        self.home = QRadioButton('home', group)
        self.home.setChecked(True)
        group_layout.addWidget(self.home)
        self.shopping = QRadioButton('shopping', group)
        group_layout.addWidget(self.shopping)
        self.university = QRadioButton('university', group)
        group_layout.addWidget(self.university)

        v_layout.addWidget(group)

        widget = QWidget()
        h_layout = QHBoxLayout(widget)
        h_layout.setContentsMargins(0, 0, 0, 0)

        btn1 = QPushButton()
        btn1.setText("OK")
        btn1.setFixedHeight(30)
        btn1.clicked.connect(self.okay)
        btn1.setCursor(Qt.CursorShape.PointingHandCursor)
        h_layout.addWidget(btn1, stretch=1)

        btn2 = QPushButton()
        btn2.setText("CANCEL")
        btn2.setFixedHeight(30)
        btn2.setCursor(Qt.CursorShape.PointingHandCursor)
        btn2.clicked.connect(self.close)

        h_layout.addWidget(btn2, stretch=1)

        v_layout.addWidget(widget)

    def okay(self):
        task = self.task.text()
        type = 'home'
        if self.work.isChecked():
            type = 'work'
        elif self.home.isChecked():
            type = 'home'
        elif self.shopping.isChecked():
            type = 'shopping'
        elif self.university.isChecked():
            type = 'university'
        self.task_added.emit(task, type)
        self.close()
