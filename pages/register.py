from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *


class RegisterPage(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('Register')
        self.window().setStyleSheet('background-color: #232931')

        with open('styles/register_page.css') as f:
            css = f.read()
            self.setStyleSheet(css)

        v_layout = QVBoxLayout(self)
        
        frame = QFrame()
        frame.setFixedSize(300, 50)
        frame.setObjectName('root2')

        h_layout = QHBoxLayout(frame)
        h_layout.setSpacing(15)

        btn = QPushButton()
        btn.setObjectName('btn2')
        btn.setIcon(QIcon('icons/book.svg'))
        h_layout.addWidget(btn)
        
        input = QLineEdit()
        input.setObjectName('input2')
        input.setPlaceholderText('Name')
        h_layout.addWidget(input)

        v_layout.addWidget(frame, alignment=Qt.AlignmentFlag.AlignCenter)
        frame2= QFrame()
        frame2.setFixedSize(300, 50)
        frame2.setObjectName('root2')

        h_layout = QHBoxLayout(frame2)
        h_layout.setSpacing(15)

        btn2 = QPushButton()
        btn2.setObjectName('btn2')
        btn2.setIcon(QIcon('icons/book.svg'))
        h_layout.addWidget(btn2)
        
        input2 = QLineEdit()
        input2.setObjectName('input2')
        input2.setPlaceholderText('Email')
        h_layout.addWidget(input2)

        v_layout.addWidget(frame2, alignment=Qt.AlignmentFlag.AlignCenter)
        frame3= QFrame()
        frame3.setFixedSize(300, 50)
        frame3.setObjectName('root2')

        h_layout = QHBoxLayout(frame3)
        h_layout.setSpacing(15)

        btn3 = QPushButton()
        btn3.setObjectName('btn2')
        btn3.setIcon(QIcon('icons/book.svg'))
        h_layout.addWidget(btn3)
        
        input3 = QLineEdit()
        input3.setObjectName('input2')
        input3.setPlaceholderText('Phone')
        h_layout.addWidget(input3)

        v_layout.addWidget(frame3, alignment=Qt.AlignmentFlag.AlignCenter)
        frame4= QFrame()
        frame4.setFixedSize(300, 50)
        frame4.setObjectName('root2')

        h_layout = QHBoxLayout(frame4)
        h_layout.setSpacing(15)

        btn4 = QPushButton()
        btn4.setObjectName('btn2')
        btn4.setIcon(QIcon('icons/book.svg'))
        h_layout.addWidget(btn4)
        
        input4 = QLineEdit()
        input4.setObjectName('input2')
        input4.setPlaceholderText('Password')
        input4.setEchoMode(QLineEdit.EchoMode.Password)
        h_layout.addWidget(input4)

        v_layout.addWidget(frame4, alignment=Qt.AlignmentFlag.AlignCenter)
        frame5= QFrame()
        frame5.setFixedSize(300, 50)
        frame5.setObjectName('root2')

        h_layout = QHBoxLayout(frame5)
        h_layout.setSpacing(15)

        btn5 = QPushButton()
        btn5.setObjectName('btn2')
        btn5.setIcon(QIcon('icons/book.svg'))
        h_layout.addWidget(btn5)
        
        input5 = QLineEdit()
        input5.setObjectName('input2')
        input5.setPlaceholderText('Confirm password')
        input5.setEchoMode(QLineEdit.EchoMode.Password)
        h_layout.addWidget(input5)

        v_layout.addWidget(frame5, alignment=Qt.AlignmentFlag.AlignCenter)
        button=QPushButton("Register")
        button.setFixedSize(200,50)
        button.setObjectName('register')
        v_layout.addWidget(button, alignment=Qt.AlignmentFlag.AlignCenter)
        b=QWidget()
        ho_lay=QHBoxLayout(b)
        c1=QLabel('Already have an account?')
        c1.setObjectName('down1')
        ho_lay.addWidget(c1, alignment=Qt.AlignmentFlag.AlignCenter)
        c2=QLabel('Login here')
        c2.setObjectName('down2')
        ho_lay.addWidget(c2, alignment=Qt.AlignmentFlag.AlignCenter)
        v_layout.addWidget(b, alignment=Qt.AlignmentFlag.AlignCenter)



