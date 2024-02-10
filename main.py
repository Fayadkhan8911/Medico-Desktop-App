import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget
from PyQt5.QtGui import QPixmap

import sqlite3

import add_patients
import patients
import add_pat_med
import pat_detailed


class _main_window(QDialog):
    def __init__(self):
        super(_main_window, self).__init__()
        loadUi("main_window.ui", self)
        self.patient_btn.clicked.connect(self._go_patient_window)
        self.add_patient_btn.clicked.connect(self._go_add_pat)

    def _go_dash(self):
        _dash = _main_window()
        widget.addWidget(_dash)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def _go_patient_window(self):
        self._patients = patients._patient_window()
        widget.addWidget(self._patients)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        self._patients.dash_btn.clicked.connect(self._go_dash)
        self._patients.add_patient_btn.clicked.connect(self._go_add_pat)
        self._patients.search_btn.clicked.connect(self._go_pat_det)

    def _go_add_pat(self):
        self._add_pat = add_patients._add_patient_window()
        widget.addWidget(self._add_pat)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        self._add_pat.dash_btn.clicked.connect(self._go_dash)
        self._add_pat.patient_btn.clicked.connect(self._go_patient_window)
        self._add_pat.next_btn.clicked.connect(self._go_med_hist)

    def _go_med_hist(self):
        self._med_hist = add_pat_med._add_med_hist_win()
        widget.addWidget(self._med_hist)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        self._med_hist.restart_btn.clicked.connect(self._go_add_pat)

    def _go_pat_det(self):
        self._details = pat_detailed._pat_detailed_win()
        widget.addWidget(self._details)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        self._details.return_pat.clicked.connect(self._go_patient_window)


"""     this was for 'only one main.py' file format

class _patient_window(QDialog):
    def __init__(self):
        super(_patient_window, self).__init__()
        loadUi("patients_window.ui", self)
        self.dash_btn.clicked.connect(self._go_dash)

    def _go_dash(self):
        _dash = _main_window()
        widget.addWidget(_dash)
        widget.setCurrentIndex(widget.currentIndex() + 1)

"""

# main
app = QApplication(sys.argv)

widget = QtWidgets.QStackedWidget()
_main = _main_window()

widget.addWidget(_main)


widget.setFixedWidth(800)
widget.setFixedHeight(600)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")
