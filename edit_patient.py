import sys
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog, QApplication
import sqlite3
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QPushButton, QStackedWidget, QLabel
from PyQt5.QtCore import QDate



class _edit_patient_details(QDialog):
    def __init__(self, patientID):
        super(_edit_patient_details, self).__init__()
        loadUi("patients_edit_window.ui", self)

            
"""             
app = QApplication(sys.argv)

widget = QtWidgets.QStackedWidget()
_patient_edit = _edit_patient_details()

widget.addWidget(_patient_edit)


widget.setFixedWidth(800)
widget.setFixedHeight(600)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting") """