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


class _error_window(QDialog):
    def __init__(self):
        super(_error_window, self).__init__()
        loadUi("error_win.ui", self)
        a = "puta"
        self.error_msg.setText(a)
        self.ok_btn.clicked.connect(self.close)
        layout = QVBoxLayout()
        layout.addWidget(self.ok_btn)
        self.setLayout(layout)


# """
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
