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

        with open("units.json", "r") as self.units:
            self.units_dict: dict = json.loads(self.units.read())

        self.v_layout = QVBoxLayout(self)

        self.v_layout.addStretch()

        self.type_combo = DropDown(size=QSize(175, 50))
        self.type_combo.addItems(list(self.units_dict.keys()))
        self.type_combo.currentIndexChanged.connect(self.type_selected)
        self.v_layout.addWidget(
            self.type_combo, alignment=Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)

        self.units = self.units_dict[self.type_combo.currentText(
        )]["units"].keys()

        self.v_layout.addStretch()
        self.setup_input()
        self.v_layout.addStretch()
        self.setup_controlls()
        self.v_layout.addStretch()
        self.setup_result()
        self.v_layout.addStretch()

    def setup_controlls(self):
        w = QWidget()
        h_layout = QHBoxLayout(w)

        self.from_combo = DropDown(size=QSize(100, 50))
        self.from_combo.addItems(list(self.units))
        h_layout.addWidget(self.from_combo)

        h_layout.addStretch()

        swap = QPushButton()
        swap.setObjectName('swap')
        swap.setFixedSize(50, 40)
        swap.clicked.connect(self.swap)
        swap.setIcon(QIcon('icons/swap_h.svg'))
        swap.setIconSize(QSize(35, 35))
        swap.setCursor(Qt.CursorShape.PointingHandCursor)    
        h_layout.addWidget(
            swap, alignment=Qt.AlignmentFlag.AlignCenter)

        h_layout.addStretch()

        self.to_combo = DropDown(size=QSize(100, 50))
        self.to_combo.addItems(list(self.units))
        h_layout.addWidget(self.to_combo)

        self.v_layout.addWidget(w)

    def setup_input(self):
        w = QWidget()
        h_layout = QHBoxLayout(w)

        h_layout.addStretch()

        lbl1 = QLabel('Convert :')
        lbl1.setObjectName("lbl")
        h_layout.addWidget(lbl1, alignment=Qt.AlignmentFlag.AlignVCenter)

        h_layout.addStretch()

        self.input = QLineEdit()
        self.input.setObjectName("input")
        self.input.setFixedSize(250, 40)
        self.input.textChanged.connect(self.do_action)
        h_layout.addWidget(self.input)

        h_layout.addStretch()
        self.v_layout.addWidget(w)

    def setup_result(self):
        w = QWidget()
        h_layout = QHBoxLayout(w)

        h_layout.addStretch()

        lbl1 = QLabel('Answer :')
        lbl1.setObjectName("lbl")
        h_layout.addWidget(lbl1, alignment=Qt.AlignmentFlag.AlignVCenter)

        h_layout.addStretch()

        self.result = QLabel()
        self.result.setObjectName("result")
        self.result.setFixedSize(250, 40)
        h_layout.addWidget(self.result)

        h_layout.addStretch()
        self.v_layout.addWidget(w)

    def type_selected(self):
        u = self.units_dict[self.type_combo.currentText()]["units"].keys()
        self.from_combo.clear()
        self.from_combo.addItems(list(u))
        self.to_combo.clear()
        self.to_combo.addItems(list(u))

    def swap(self):
        g = self.from_combo.currentIndex()
        self.from_combo.setCurrentIndex(self.to_combo.currentIndex())
        self.to_combo.setCurrentIndex(g)
        self.do_action()

    def do_action(self):
        if self.input.text().isdigit():

            d = self.input.text()
            formula_from = self.units_dict[self.type_combo.currentText(
            )]["units"][self.from_combo.currentText()]["formula_from"]

            eq = formula_from.format(self.input.text())
            r = eval(eq)

            formula_to = self.units_dict[self.type_combo.currentText(
            )]["units"][self.to_combo.currentText()]["formula_to"]
            eqq = formula_to.format(r)
            q = eval(eqq)
            self.result.setText(str(q))
