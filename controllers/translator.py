from PyQt6.QtCore import QThread, pyqtSignal
import googletrans


class TranslatorHandler(QThread):
    answer = pyqtSignal(str)
    crash = pyqtSignal()

    def __init__(self, parent, origin: str, destination: str, sentence: str):
        QThread.__init__(self, parent)
        self.origin = origin
        self.destination = destination
        self.sentence = sentence
        self.translator = googletrans.Translator()

    def run(self):
        try:
            if self.sentence != '':
                t_from = self.origin
                t_to = self.destination
                res = self.translator.translate(self.sentence, dest=t_to, src=t_from)
                self.answer.emit(res.text)
        except:
            self.crash.emit()
