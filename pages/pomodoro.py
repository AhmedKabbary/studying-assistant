from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from widgets.timer import pomo_timer

class button(QPushButton):
    def __init__(self):
        super().__init__()
        self.setFixedSize(50,50)
        self.setIconSize(QSize(28,28))
        self.setCursor(Qt.CursorShape.PointingHandCursor)

class PomodorosPage(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('My Pomodoros')
        self.window().setStyleSheet('background-color: #232931')
        self.num = 0
        with open('styles/pomodoro_page.css') as f:
            css = f.read()
            self.setStyleSheet(css)

        
        widget_po = QWidget()
        hbox_po = QHBoxLayout()
        po = pomo_timer()
        hbox_po.addWidget(po)
        hbox_po.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignCenter)
        widget_po.setLayout(hbox_po)

        widget_lb = QWidget()
        hbox_lb = QHBoxLayout()
        self.label_pomos = QLabel("My Pomodoros")
        self.label_pomos.setObjectName('l')
        self.label_pomos.setFixedSize(200,35)
        self.btn_addpomo = QPushButton()
        self.btn_addpomo.clicked.connect(self.add_tasks)
        self.btn_addpomo.setObjectName('b')
        self.btn_addpomo.setFixedSize(28,28)
        self.btn_addpomo.setIcon(QIcon('icons/add.svg'))
        self.btn_addpomo.setIconSize(QSize(22,22))
        self.btn_addpomo.setCursor((Qt.CursorShape.PointingHandCursor))
        hbox_lb.addWidget(self.label_pomos)
        hbox_lb.addStretch(3)
        hbox_lb.addWidget(self.btn_addpomo)
        hbox_lb.setAlignment(Qt.AlignmentFlag.AlignTop)
        widget_lb.setLayout(hbox_lb)

        self.scrl = QScrollArea()
        self.bar = QScrollBar()
        self.bar.setFixedSize(10,190)
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
        self.btn_playpause.setFixedSize(150,50)
        self.btn_playpause.setCheckable(True)
        self.btn_playpause.setIcon(QIcon('icons/play.svg'))
        self.btn_playpause.clicked.connect(self.playpause)
        self.btn_playpause.clicked.connect(po.display)
        self.btn_stop = button()
        self.btn_stop.setIcon(QIcon('icons/stop.svg'))
        self.btn_stop.clicked.connect(po.stop)
        self.btn_stop.clicked.connect(self.spp)
        self.btn_replay = button()
        self.btn_replay.setIcon(QIcon('icons/replay.svg'))
        self.btn_replay.clicked.connect(po.replay)
        self.btn_replay.clicked.connect(self.rpp)
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

    def add_tasks(self):
        self.num +=1
        self.lbl_task = QLabel("Task #"+str(self.num))
        self.lbl_task.setObjectName('sl')
        self.lbl_task.setFixedHeight(50)
        self.vbox_scrl.addWidget(self.lbl_task)

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