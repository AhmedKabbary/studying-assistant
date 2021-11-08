from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from pdfplumber.pdf import PDF


class DropPDF(QFrame):

    name = None
    dropped = pyqtSignal(PDF)

    def __init__(self):
        super().__init__()
        self.setObjectName('root')
        self.setFixedSize(350, 250)

        with open('styles/drop_pdf.css') as f:
            css = f.read()
            self.setStyleSheet(css)

        v_layout = QVBoxLayout(self)
        v_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.btn = QPushButton()
        self.btn.setIcon(QIcon('icons/drop.svg'))
        self.btn.setIconSize(QSize(50, 50))
        v_layout.addWidget(self.btn)

        v_layout.addSpacerItem(QSpacerItem(0, 30))

        self.drop_lbl = QLabel('Drop PDF file here')
        self.drop_lbl.setObjectName('description')
        self.drop_lbl.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        v_layout.addWidget(self.drop_lbl)

        self.or_lbl = QLabel('or')
        self.or_lbl.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        v_layout.addWidget(self.or_lbl)

        self.browse_btn = QPushButton()
        self.browse_btn.setObjectName('browse')
        self.browse_btn.setText('Browse files')
        self.browse_btn.clicked.connect(self.browse_files)
        self.browse_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        v_layout.addWidget(self.browse_btn)

        self.setAcceptDrops(True)

    def dragEnterEvent(self, event: QDragEnterEvent):
        if event.mimeData().hasUrls:
            event.setDropAction(Qt.DropAction.CopyAction)
            event.accept()
            self.or_lbl.hide()
            self.browse_btn.hide()
            self.drop_lbl.setText('Release PDF file here')
            self.btn.setIcon(QIcon('icons/drop.svg'))
        else:
            event.ignore()

    def dragLeaveEvent(self, event: QDragLeaveEvent):
        self.refresh_ui()
        return super().dragLeaveEvent(event)

    def dropEvent(self, event: QDropEvent):
        if event.mimeData().hasUrls:
            event.setDropAction(Qt.DropAction.CopyAction)
            event.accept()
            for url in event.mimeData().urls():
                self.proccess_pdf(url)
                return
        else:
            event.ignore()

    def browse_files(self):
        url, _ = QFileDialog.getOpenFileUrl(self, caption="Select PDF file", filter="PDF Files (*.pdf)")
        if url:
            self.proccess_pdf(url)

    def proccess_pdf(self, url: QUrl):
        import pdfplumber
        try:
            self.pdf = pdfplumber.open(url.toLocalFile())
            self.name = url.fileName()
            self.dropped.emit(self.pdf)
        except:
            QMessageBox.critical(self, 'An error occurred', 'Please provie a valid PDF file')
        finally:
            self.refresh_ui()

    def refresh_ui(self):
        self.or_lbl.show()
        if self.name == None:
            self.browse_btn.show()
            self.drop_lbl.setText('Drop PDF file here')
            self.btn.setIcon(QIcon('icons/drop.svg'))
        else:
            self.browse_btn.hide()
            self.drop_lbl.setText(self.name)
            self.or_lbl.setText('({} pages)'.format(len(self.pdf.pages)))
            self.btn.setIcon(QIcon('icons/file.svg'))
