from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *


class pomo_timer(QWidget):
    def __init__(self):
        super().__init__()

        self.c = 0
        self.count = 60
        self.count2 = 24

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.min_25)
        self.timer
        self.value = 300
        self.value2 = 60

        self.lbl = QLabel("25:00", self)
        self.lbl.move(150, 70)
        self.lbl.setFixedSize(95, 80)


    def display(self):
        if self.timer.isActive():
            self.timer.stop()
        else:
            self.timer.start(1000)

    def replay(self):
        self.count = 60
        self.count2 = 24
        self.lbl.setText("25:00")
        self.value = 300
        self.value2 = 60
        self.c = 0
        self.repaint()
        self.timer.start(1000)

    def stop(self):
        self.count = 60
        self.count2 = 24
        self.lbl.setText("25:00")
        self.value = 300
        self.value2 = 60
        self.c = 0
        self.repaint()
        self.timer.stop()
        
    def min_25(self):
        self.count -= 1
        if self.count == -1:
            self.count = 59
            self.count2 -= 1
            if self.count2 == -1 and self.c == 0:
               self.count = 0
               self.count2 = 5
               self.c = 1
        elif self.count == 0 and self.count2 == 0 and self.c == 1:
            self.value2 = 0
            self.repaint()
            self.timer.stop()
            
        text = str(self.count2).zfill(2)+":"+str(self.count).zfill(2)
        self.lbl.setText(text)
        
        if self.c == 0:
           self.value -= 0.2
           self.repaint()
        elif self.c == 1 and self.value2 > 0.21:
           self.value2 -= 0.2
           self.repaint()
         
    
    def paintEvent(self, e):
        cg = QConicalGradient()
        cg.setCenter(QPointF(self.rect().center()))
        cg.setAngle(270)
        cg.setColorAt(0.3, QColor(197, 0, 0))
        cg.setColorAt(1, QColor(255, 230, 0))
        

        cg2 = QConicalGradient()
        cg2.setCenter(QPointF(self.rect().center()))
        cg2.setAngle(120)
        cg2.setColorAt(0.3, QColor(0, 70, 0))
        cg2.setColorAt(0.7, QColor(0, 255, 0))

        back_circle = QPainter(self)
        back_circle.setPen(Qt.PenStyle.NoPen)
        back_circle.setBrush(QColor(23, 25, 29))
        back_circle.setRenderHint(QPainter.RenderHint.Antialiasing)
        back_circle.drawEllipse(100, 15, 190, 190)

        painter = QPainter(self)
        painter.setPen(
            QPen(QBrush(cg), 17, Qt.PenStyle.SolidLine, Qt.PenCapStyle.RoundCap))
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.drawArc(QRect(115, 30, 160, 160), 300*16, self.value*16)

        painter2 = QPainter(self)
        painter2.setPen(
            QPen(QBrush(cg2), 17,Qt.PenStyle.SolidLine, Qt.PenCapStyle.RoundCap))
        painter2.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter2.drawArc(QRect(115, 30, 160, 160), 240*16, self.value2*16)
