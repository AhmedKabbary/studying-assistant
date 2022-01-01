import db
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from widgets.timer import pomo_timer
from datetime import datetime
import controllers.auth as Auth


class Item(QLabel):

    clicked = pyqtSignal()
    deleted = pyqtSignal()
    emptytasks = pyqtSignal()

    def __init__(self, id):
        super().__init__()
        self.id = id

    def mousePressEvent(self, ev):
        if ev.button() == Qt.MouseButton.LeftButton:
            self.clicked.emit()
        if ev.button() == Qt.MouseButton.RightButton:
            menu = QMenu()
            delete = QAction('Delete')
            delete.triggered.connect(self.delete_task)
            menu.addAction(delete)
            menu.exec(QPoint(int(ev.globalPosition().x()), int(ev.globalPosition().y())))

    def delete_task(self):
        db.cursor.execute('DELETE FROM POMODOROS WHERE ID = ' + str(self.id))
        db.cursor.execute("UPDATE sqlite_sequence SET seq=0 WHERE name=? ",("POMODOROS",))
        db.cursor.commit()
        self.deleted.emit()
        self.emptytasks.emit()


class button(QPushButton):
    def __init__(self):
        super().__init__()
        self.setFixedSize(50, 50)
        self.setIconSize(QSize(28, 28))
        self.setCursor(Qt.CursorShape.PointingHandCursor)
          
class PomodorosPage(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('My Pomodoros')
        self.window().setStyleSheet('background-color: #232931')

        with open('styles/pomodoro_page.css') as f:
            css = f.read()
            self.setStyleSheet(css)

        widget_po = QWidget()
        hbox_po = QHBoxLayout()
        self.po = pomo_timer()
        hbox_po.addWidget(self.po)
        hbox_po.setAlignment(Qt.AlignmentFlag.AlignTop |
                             Qt.AlignmentFlag.AlignCenter)
        widget_po.setLayout(hbox_po)

        widget_lb = QWidget()
        hbox_lb = QHBoxLayout()
        self.label_pomos = QLabel("My Pomodoros")
        self.label_pomos.setObjectName('l')
        self.label_pomos.setFixedSize(200, 35)
        self.btn_addpomo = QPushButton()
        self.btn_addpomo.clicked.connect(self.add_tasks)
        self.btn_addpomo.setObjectName('b')
        self.btn_addpomo.setFixedSize(28, 28)
        self.btn_addpomo.setIcon(QIcon('icons/add.svg'))
        self.btn_addpomo.setIconSize(QSize(22, 22))
        self.btn_addpomo.setCursor((Qt.CursorShape.PointingHandCursor))
        hbox_lb.addWidget(self.label_pomos)
        hbox_lb.addStretch(3)
        hbox_lb.addWidget(self.btn_addpomo)
        hbox_lb.setAlignment(Qt.AlignmentFlag.AlignTop)
        widget_lb.setLayout(hbox_lb)

        self.scrl = QScrollArea()
        self.bar = QScrollBar()
        self.bar.setFixedSize(10, 190)
        self.widget_scrl = QWidget()
        self.vbox_scrl = QVBoxLayout()
        self.vbox_scrl.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.widget_scrl.setLayout(self.vbox_scrl)
        self.scrl.setWidget(self.widget_scrl)
        self.scrl.setFrameStyle(0)
        self.scrl.setWidgetResizable(True)
        self.scrl.setVerticalScrollBar(self.bar)

        widget = QWidget()
        hbox = QHBoxLayout()
        self.btn_playpause = button()
        self.btn_playpause.setText('PLAY')
        self.btn_playpause.setFixedSize(150, 50)
        self.btn_playpause.setCheckable(True)
        self.btn_playpause.setIcon(QIcon('icons/play.svg'))
        self.btn_playpause.clicked.connect(self.playpause)
        self.btn_playpause.clicked.connect(self.po.display)
        self.btn_playpause.clicked.connect(self.checkframe)
        self.btn_stop = button()
        self.btn_stop.setIcon(QIcon('icons/stop.svg'))
        self.btn_stop.clicked.connect(self.po.stop)
        self.btn_stop.clicked.connect(self.spp)
        self.btn_stop.clicked.connect(self.checkframe)
        self.btn_replay = button()
        self.btn_replay.setIcon(QIcon('icons/replay.svg'))
        self.btn_replay.clicked.connect(self.po.replay)
        self.btn_replay.clicked.connect(self.rpp)
        self.btn_replay.clicked.connect(self.checkframe)
        hbox.addStretch()
        hbox.addWidget(self.btn_stop)
        hbox.addStretch()
        hbox.addWidget(self.btn_playpause)
        hbox.addStretch()
        hbox.addWidget(self.btn_replay)
        hbox.addStretch()
        hbox.setAlignment(Qt.AlignmentFlag.AlignBottom)
        widget.setLayout(hbox)

        vbox = QVBoxLayout(self)
        vbox.addWidget(widget_po)
        vbox.addWidget(widget_lb)
        vbox.addWidget(self.scrl)
        vbox.addWidget(widget)

        self.po.transf.connect(self.autoframe)
        self.load_list()

        if self.vbox_scrl.count() == 0:
            self.btn_playpause.setEnabled(False)
            self.btn_replay.setEnabled(False)
            self.btn_stop.setEnabled(False) 
 
    def exploit(self):
        self.po.stop()
        self.spp()

    def checkemptytasks(self):
        if self.vbox_scrl.count() == 1:
            self.btn_playpause.setEnabled(False)
            self.btn_replay.setEnabled(False)
            self.btn_stop.setEnabled(False)


    def enableButtons(self):
        self.btn_playpause.setEnabled(True)
        self.btn_replay.setEnabled(True)
        self.btn_stop.setEnabled(True)

    def load_list(self):
        for i in reversed(range(self.vbox_scrl.count())):
            self.vbox_scrl.itemAt(i).widget().deleteLater()
            
        result = db.cursor.execute('SELECT * FROM POMODOROS WHERE USER_ID = ?', (Auth.user[0],))
        for row in result:
            lbl_task = Item(row[0])
            lbl_task.setText(row[1])
            lbl_task.clicked.connect(lambda w=lbl_task: self.addframe(w))
            lbl_task.deleted.connect(self.load_list)
            lbl_task.emptytasks.connect(self.checkemptytasks)
            lbl_task.emptytasks.connect(self.exploit)
            lbl_task.setObjectName("sl")
            lbl_task.setFixedHeight(50)
            self.vbox_scrl.addWidget(lbl_task)

    def addframe(self, item):
        if self.po.timer.isActive():
           pass
        else:
            self.po.stop()
            for i in range(self.vbox_scrl.count()):
               self.vbox_scrl.itemAt(i).widget().setObjectName("sl")
               self.vbox_scrl.itemAt(i).widget().setStyleSheet("")
            item.setObjectName("slf")
            item.setStyleSheet("")

    def autoframe(self):
        for i in range(self.vbox_scrl.count()):
            if (self.vbox_scrl.itemAt(i).widget().objectName() == "slf") and (i != self.vbox_scrl.count()-1):
                self.vbox_scrl.itemAt(i).widget().setObjectName("sl")
                self.vbox_scrl.itemAt(i+1).widget().setObjectName("slf")
                self.vbox_scrl.itemAt(i).widget().setStyleSheet("")
                self.vbox_scrl.itemAt(i+1).widget().setStyleSheet("")
                break
            if (i == self.vbox_scrl.count()-1):
                self.po.stop()
                self.spp()

    def checkframe(self):
        for i in range(self.vbox_scrl.count()):
            if (self.vbox_scrl.itemAt(i).widget().objectName() == "slf"):
                break
        else:
            self.po.replay()
            self.vbox_scrl.itemAt(0).widget().setObjectName('slf')
            self.vbox_scrl.itemAt(0).widget().setStyleSheet('')
            

    def add_tasks(self):
        d = AddPomodoroDialog()
        d.enablebtns.connect(self.enableButtons)
        d.enablebtns.connect(self.exploit)
        d.task_added.connect(self.task_added)
        d.exec()

    def task_added(self, task):
        db.cursor.execute("INSERT INTO POMODOROS (DESCRIPTION, CREATION_DATE, USER_ID) VALUES (?, ?, ?)",
                          (task, datetime.now().isoformat(), Auth.user[0]))
        db.cursor.commit()
        self.load_list()

    def playpause(self, checked):
        if checked:
            self.btn_playpause.setText('PAUSE')
            self.btn_playpause.setIcon(QIcon('icons/pause.svg'))
        else:
            self.btn_playpause.setText('PLAY')
            self.btn_playpause.setIcon(QIcon('icons/play.svg'))

    def rpp(self):
        self.btn_playpause.setText('PAUSE')
        self.btn_playpause.setIcon(QIcon('icons/pause.svg'))
        self.btn_playpause.setChecked(True)

    def spp(self):
        self.btn_playpause.setText('PLAY')
        self.btn_playpause.setIcon(QIcon('icons/play.svg'))
        self.btn_playpause.setChecked(False)


class AddPomodoroDialog(QDialog):

    task_added = pyqtSignal(str)
    enablebtns = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Add a task')
        self.setFixedWidth(250)
        self.setStyleSheet("""
            QDialog {
                background-color: #232931;
            }

            QLineEdit {
                color: #EEEEEE;
                border: none;
                background-color: #393E46;
                border-radius: 5;
                padding: 8px;
            }

            QPushButton {
                border: none;
                border-radius: 5;
                font-size: 20;
                font-weight: bold;
                background-color: #393E46;
                color : #EEEEEE;
            }
        """)

        v_layout = QVBoxLayout(self)
        v_layout.setSpacing(24)

        self.task = QLineEdit()
        self.task.setPlaceholderText('Enter a task')
        v_layout.addWidget(self.task)

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
        btn2.setText("CANCEL")
        btn2.setFixedHeight(30)
        btn2.setCursor(Qt.CursorShape.PointingHandCursor)
        btn2.clicked.connect(self.close)

        h_layout.addWidget(btn2, stretch=1)

        v_layout.addWidget(widget)

    def save(self):
        self.enablebtns.emit()
        t = self.task.text()
        self.task_added.emit(t)
        self.close()
