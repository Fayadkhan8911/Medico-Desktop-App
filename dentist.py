import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget
from PyQt5.QtGui import QPixmap

import sqlite3


class _dentist_window(QDialog):
    def __init__(self):
        super(_dentist_window, self).__init__()
        loadUi("dentists_window.ui", self)
        self.dentist_table.setColumnWidth(6, 200)

        self.dentist_table.setColumnWidth(7, 200)

        self.dentist_table.setColumnWidth(8, 200)


# """
app = QApplication(sys.argv)

widget = QtWidgets.QStackedWidget()
_patient = _dentist_window()

widget.addWidget(_patient)


widget.setFixedWidth(800)
widget.setFixedHeight(600)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")
# """
