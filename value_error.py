import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QMainWindow,
    QPushButton,
    QMessageBox,
    QVBoxLayout,
    QSizePolicy,
)

import sqlite3
from value_error_ui import Ui_Dialog

class _error_window(QDialog, Ui_Dialog):
    def __init__(self, message):
        super(_error_window, self).__init__()
        self.setupUi(self)
        self.error_msg_text.setText(message)
        self.ok_btn.clicked.connect(self.accept)  # Close the dialog when Ok button is clicked




"""
app = QApplication(sys.argv)

widget = QtWidgets.QStackedWidget()
_patient = _error_window()

widget.addWidget(_patient)


widget.setFixedWidth(400)
widget.setFixedHeight(400)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")
# """
