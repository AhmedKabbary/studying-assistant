from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
import googletrans
import textblob
from textblob import TextBlob



class TranslatorPage(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('Google Translator')
        self.window().setStyleSheet('background-color: #232931')

        with open('styles/translator_page.css') as f:
            css = f.read()
            self.setStyleSheet(css)
    

        v_layout = QVBoxLayout(self)
        
        self.combo1=QComboBox()
        self.combo1.setObjectName('combo')
        self.combo1.setFixedSize(150,40)
        v_layout.addWidget(self.combo1, alignment=Qt.AlignmentFlag.AlignTop)
        v_layout.setContentsMargins(0,0,0,0)


        self.enter_line = QTextEdit('type here')
        # enter_line.move(100,105)
        self.enter_line.setObjectName('LineToTranslate')
        v_layout.addWidget(self.enter_line, alignment=Qt.AlignmentFlag.AlignTop)


        frame = QFrame()
        frame.setFixedSize(400,300)
        frame.setObjectName('button_frame')
        v_layout.addWidget(frame, alignment=Qt.AlignmentFlag.AlignBottom)

        v2_layout = QVBoxLayout(frame)
        self.combo2=QComboBox()
        self.combo2.setObjectName('combo')

        self.combo2.setFixedSize(150,40)
        v2_layout.addWidget(self.combo2, alignment=Qt.AlignmentFlag.AlignTop)
        
        self.tRanslation=QLabel("Translation")
        self.tRanslation.setObjectName('label')
        # translation.setFixedSize(400,300)
        v2_layout.addWidget(self.tRanslation, alignment=Qt.AlignmentFlag.AlignTop)
        
    

        #Add languages to ComboBox
        self.languages=googletrans.LANGUAGES
        self.languages_list = list(self.languages.values())
        self.combo1.addItems(self.languages_list)
        self.combo2.addItems(self.languages_list)

        # set current language
        self.combo1.setCurrentText("english")
        self.combo2.setCurrentText("arabic")

    

        swap=QPushButton(self)
        swap.move(340,225)
        swap.setFixedSize(40,50)
        swap.setObjectName('swap_button')
        swap.setIcon(QIcon('icons/swap_v.svg'))
        swap.setIconSize(QSize(35, 35))
        swap.setCursor(Qt.CursorShape.PointingHandCursor)
        swap.clicked.connect(self.choose)

    def choose(self):
        z = self.combo1.currentIndex()
        self.combo1.setCurrentIndex(self.combo2.currentIndex())
        self.combo2.setCurrentIndex(z)
    # def translate(self):
        
    #     for key,value in self.languages.items():
    #         if (value==self.combo1.currentText()):
    #             from_language_key=key
    #     for key,value in self.languages.items():
    #         if (value==self.combo2.currentText()):
    #             to_language_key=key
    #     words=textblob.TextBlob(self.enter_line.toPlainText())
    #     words=words.translate(from_lang=from_language_key, to=to_language_key)                   
    #     self.tRanslation.setText(str(words))
        

   


   
