import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget
from PyQt5.QtGui import QPixmap

import sqlite3


class _patient_window(QDialog):
    def __init__(self):
        super(_patient_window, self).__init__()
        loadUi("patients_window.ui", self)


"""
app = QApplication(sys.argv)

widget = QtWidgets.QStackedWidget()
_patient = _patient_window()

widget.addWidget(_patient)


widget.setFixedWidth(800)
widget.setFixedHeight(600)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")
# """
