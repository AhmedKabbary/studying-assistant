from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

class pomo_timer(QFrame):
    def __init__(self):
        super().__init__()
        self.setObjectName("f")
        self.setFixedSize(190,190)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.min_30)
        self.timer_reset = QTimer(self)
        self.lbl = QLabel(self)
        self.lbl.move(50, 55)
        self.lbl.setFixedSize(95, 80)
        self.set_values()
        self.set_text()

    def set_text(self):
        text = str(self.minutes).zfill(2)+":"+str(self.seconds).zfill(2)
        self.lbl.setText(text)

    def set_values(self):
        self.seconds = 0
        self.minutes = 25
        self.work_value = 300
        self.rest_value = 60
        self.count = 0
        self.set_text()

    def display(self):
        if self.timer.isActive():
            self.timer.stop()
        else:
            self.timer.start(1000)

    def replay(self):
        self.timer.stop()
        self.timer_reset.timeout.connect(self.replay_reset)
        self.timer_reset.start(1)
        
    def stop(self):
        if self.work_value < 300:
           self.timer.stop()
           self.timer_reset.timeout.connect(self.stop_reset)
           self.timer_reset.start(1)
        
    def reset(self):
        if self.rest_value < 60:
            self.rest_value += 0.2
            self.repaint()
        elif self.work_value < 300:
            self.work_value += 0.2
            self.repaint()
        
    def replay_reset(self):
        self.reset()
        if self.work_value == 300:
            self.set_values()
            self.timer_reset.stop()
            self.timer_reset.disconnect()
            self.timer.start(1000)

    def stop_reset(self):
        self.reset()
        if self.work_value == 300:
            self.set_values()
            self.timer_reset.stop()
            self.timer_reset.disconnect()

    def min_30(self):
        self.seconds -= 1
        if self.seconds == -1:
            self.seconds = 59
            self.minutes -= 1
            if self.minutes == -1 and self.count == 0:
               self.seconds = 0
               self.minutes = 5
               self.count = 1
        elif self.seconds == 0 and self.minutes == 0 and self.count == 1:
            self.rest_value = 0
            self.repaint()
            self.timer.stop()
        self.set_text()
        if self.count == 0:
           self.work_value -= 0.2
           self.repaint()
        elif self.count == 1 and self.rest_value > 0.21:
           self.rest_value -= 0.2
           self.repaint()
    
    def paintEvent(self, e):
        cg = QConicalGradient()
        cg.setCenter(QPointF(self.rect().center()))
        cg.setAngle(250)
        cg.setColorAt(0.3, QColor(197, 0, 0))
        cg.setColorAt(1, QColor(255, 230, 0))
        
        cg2 = QConicalGradient()
        cg2.setCenter(QPointF(self.rect().center()))
        cg2.setAngle(120)
        cg2.setColorAt(0.3, QColor(0, 70, 0))
        cg2.setColorAt(0.7, QColor(0, 255, 0))

        painter = QPainter(self)
        painter.setPen(QPen(QBrush(cg), 17, Qt.PenStyle.SolidLine, Qt.PenCapStyle.RoundCap))
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.drawArc(QRect(15, 15, 160, 160), 300*16, self.work_value*16)

        painter2 = QPainter(self)
        painter2.setPen(QPen(QBrush(cg2), 17,Qt.PenStyle.SolidLine, Qt.PenCapStyle.RoundCap))
        painter2.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter2.drawArc(QRect(15, 15, 160, 160), 240*16, self.rest_value*16)
