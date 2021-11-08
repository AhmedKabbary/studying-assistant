from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from pdfplumber.pdf import PDF
from widgets.drop_pdf import DropPDF
from controllers.ai_answer import AIAnswerHandler


class AIPage(QWidget):

    pdf = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('AI PDF Answer Extractor')
        self.window().setStyleSheet('background-color: #232931')

        with open('styles/ai_page.css') as f:
            css = f.read()
            self.setStyleSheet(css)

        self.v_layout = QVBoxLayout(self)
        self.v_layout.setSpacing(50)
        self.v_layout.setContentsMargins(15, 15, 15, 50)
        self.v_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.setup_question_ui()
        self.setup_drop_file_ui()

    def setup_question_ui(self):
        root = QWidget()
        root.setFixedWidth(370)

        h_layout = QHBoxLayout(root)
        h_layout.setSpacing(15)

        self.input = QLineEdit()
        self.input.setFixedHeight(40)
        self.input.setObjectName('input_field')
        self.input.setPlaceholderText('Ask a question')
        h_layout.addWidget(self.input, 3, alignment=Qt.AlignmentFlag.AlignVCenter)

        self.answer_btn = QPushButton()
        self.answer_btn.setFixedHeight(38)
        self.answer_btn.setObjectName('answer_btn')
        self.answer_btn.setText('Answer')
        self.answer_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        self.answer_btn.clicked.connect(self.answer)
        h_layout.addWidget(self.answer_btn, 1, alignment=Qt.AlignmentFlag.AlignVCenter)

        self.v_layout.addWidget(root, alignment=Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)

    def setup_drop_file_ui(self):
        root = DropPDF()
        root.dropped.connect(self.file_dropped)
        self.v_layout.addWidget(root, alignment=Qt.AlignmentFlag.AlignCenter)

    def file_dropped(self, pdf: PDF):
        self.pdf = pdf

    def answer(self):
        if (self.input.text() == ''):
            QMessageBox.warning(self, 'Bad input', 'Question field cannot be empty')
            return

        if (self.pdf == None):
            QMessageBox.warning(self, 'Bad input', 'Please select a PDF file')
            return

        self.setCursor(Qt.CursorShape.WaitCursor)
        self.answer_btn.setCursor(Qt.CursorShape.WaitCursor)

        answer_handler = AIAnswerHandler(self, self.input.text(), self.pdf)
        answer_handler.answer.connect(self.answered)
        answer_handler.crash.connect(self.crash)
        answer_handler.start()

    def answered(self, answer, accuracy):
        self.unsetCursor()
        self.answer_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        QMessageBox.information(self, 'Answer', f'{answer}\n\nAccuracy: {accuracy}%')

    def crash(self):
        self.unsetCursor()
        self.answer_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        QMessageBox.critical(self, 'An error occurred', 'Please check your internet connection')
