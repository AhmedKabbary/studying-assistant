from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from widgets.dropdown import DropDown
import json


class ConverterPage(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('Units Converter')
        self.window().setStyleSheet('background-color: #232931')

        with open("styles/converter_page.css") as f:
            css = f.read()
            self.setStyleSheet(css)

        with open("units.json", "r") as s:
            self.units: dict = json.loads(s.read())

        v_layout = QVBoxLayout(self)

        self.type_combo = DropDown(self, QSize(120, 30))
        self.type_combo.move(145, 100)
        self.type_combo.addItems(list(self.units.keys()))
        self.type_combo.currentIndexChanged.connect(self.Typeselected)

        s = self.units[self.type_combo.currentText()]["units"].keys()
        self.combobox1 = QComboBox(self)
        self.combobox1.setGeometry(20, 270, 100, 50)
        self.combobox1.addItems(s)
        self.combobox1.setEditable(False)
        self.comboboxx = QComboBox(self)
        self.comboboxx.setGeometry(280, 270, 100, 50)
        self.comboboxx.addItems(s)
        self.comboboxx.setEditable(False)

        button = QPushButton(self)
        button.setGeometry(170, 270, 50, 40)
        button.clicked.connect(self.choose)
        button.setStyleSheet("""
            border-radius:10;
            background-color:#00ADB5;
            color:white;
            font-size:18 px;
            font-weight :bold;
        """)
        button.setIcon(QIcon('icons/swap_h.svg'))
        button.setIconSize(QSize(30, 30))

        frame2 = QFrame(self)
        frame2.setGeometry(100, 200, 250, 40)
        frame2.setStyleSheet("""
            QFrame{
                padding: 8px;
                color: #EEEEEE;
                border-radius:5;
                background-color: #393E46;
            }
        """)

        self.line_edit = QLineEdit(self)
        self.line_edit.setGeometry(100, 200, 250, 40)
        self.line_edit.textChanged.connect(self.do_action)
        self.line_edit.setStyleSheet("""
            QLineEdit{
                border: none;
                color: #EEEEEE;
                padding: 8px;
                background-color: transparent;
            }
        """)

        self.result = QLabel(self)
        self.result.setGeometry(100, 400, 250, 40)
        self.result.setStyleSheet("""
            QLabel{
                padding: 8px;
                color: #EEEEEE;
                border-radius:5;
                background-color: #393E46;
            }
        """)

    def Typeselected(self):
        self.combobox1.clear()
        b = self.units[self.type_combo.currentText()]["units"].keys()
        self.combobox1.addItems(b)
        self.comboboxx.clear()
        d = self.units[self.type_combo.currentText()]["units"].keys()
        self.comboboxx.addItems(d)

    def choose(self):
        g = self.combobox1.currentIndex()
        self.combobox1.setCurrentIndex(self.comboboxx.currentIndex())
        self.comboboxx.setCurrentIndex(g)
        self.do_action()

    def do_action(self):
        if self.line_edit.text().isdigit():

            d = self.line_edit.text()
            formula_from = self.units[self.type_combo.currentText(
            )]["units"][self.combobox1.currentText()]["formula_from"]

            eq = formula_from.format(self.line_edit.text())
            r = eval(eq)

            formula_to = self.units[self.type_combo.currentText(
            )]["units"][self.comboboxx.currentText()]["formula_to"]
            eqq = formula_to.format(r)
            q = eval(eqq)
            self.result.setText(str(q))
