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

    
        with open('styles/pomodoro_page.css') as f:
            css = f.read()
            self.setStyleSheet(css)


        vbox = QVBoxLayout(self)
        widget = QWidget()
        hbox = QHBoxLayout()
        po = pomo_timer()
        self.btn_playpause = button()
        self.btn_playpause.setText('PLAY')
        self.btn_playpause.setFixedSize(150,50)
        self.btn_playpause.setCheckable(True)
        self.btn_playpause.setIcon(QIcon('icons\play.svg'))
        self.btn_playpause.clicked.connect(self.playpause)
        self.btn_playpause.clicked.connect(po.display)
        self.btn_stop = button()
        self.btn_stop.setIcon(QIcon('icons\stop.svg'))
        self.btn_stop.clicked.connect(po.stop)
        self.btn_stop.clicked.connect(self.spp)
        self.btn_replay = button()
        self.btn_replay.setIcon(QIcon('icons\ereplay.svg'))
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
        vbox.addWidget(po)
        vbox.addWidget(widget)
    
        
    def playpause(self, checked):
        if checked:
            self.btn_playpause.setText('PAUSE')
            self.btn_playpause.setIcon(QIcon('icons\pause.svg'))
        else:
            self.btn_playpause.setText('PLAY')
            self.btn_playpause.setIcon(QIcon('icons\play.svg'))

    def rpp(self):
        self.btn_playpause.setText('PAUSE')
        self.btn_playpause.setIcon(QIcon('icons\pause.svg'))
        self.btn_playpause.setChecked(True)
        
    def spp(self):
        self.btn_playpause.setText('PLAY')
        self.btn_playpause.setIcon(QIcon('icons\play.svg'))
        self.btn_playpause.setChecked(False)