from typing import Tuple
from pdfplumber.pdf import PDF
from PyQt6.QtCore import QObject, QThread, pyqtSignal


class AIAnswerHandler(QThread):
    answer = pyqtSignal(str, int)
    crash = pyqtSignal()

    def __init__(self, parent: QObject, question: str, pdf: PDF):
        QThread.__init__(self, parent)
        self.question = question
        self.pdf = pdf

    def run(self):
        import json
        import requests

        best_answer: Tuple[str, int] = None

        try:
            for page in self.pdf.pages:
                response = requests.post(
                    'https://deepset-electra-base-squad2-ldwkccpswa-ue.a.run.app',
                    json={
                        'question': self.question,
                        'context': page.extract_text()
                    }
                )
                response.raise_for_status()
                res = json.loads(response.text)
                if (best_answer == None) or (round(res['score']*100) > best_answer[1]):
                    best_answer = (res['answer'], round(res['score']*100))

            self.pdf.close()
            self.answer.emit(best_answer[0], best_answer[1])
        except:
            self.crash.emit()
