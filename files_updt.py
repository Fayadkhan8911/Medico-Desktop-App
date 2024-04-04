import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QStackedWidget
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
import value_error


class _add_file_window(QDialog):
    def __init__(self):
        super(_add_file_window, self).__init__()
        loadUi("files_updt.ui", self)

    


"""
app = QApplication(sys.argv)

widget = QtWidgets.QStackedWidget()
_app = _add_file_window()

widget.addWidget(_app)


widget.setFixedWidth(740)
widget.setFixedHeight(636)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")
# """
