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
        self.load_patients_table()

    def load_patients_table(self):
        _connect = sqlite3.connect("MEDICO.db3")
        _cur = _connect.cursor()
        # _query = ("SELECT * FROM appointments WHERE appnt_date = ?",(self.current_date,),)

        # data = _cur.fetchall()  # Fetch data
        _tablerow = 0
        self.patient_table.setRowCount(50)
        # cursor.execute("SELECT * FROM patientss WHERE appnt_date = ?", (self.current_date,))
        self.patient_table.setColumnWidth(5, 200)
        self.patient_table.setColumnWidth(1, 200)
        self.patient_table.setColumnWidth(2, 200)
        for col in _cur.execute(
            "SELECT p_id,f_name,l_name,sex,age,phone FROM patients"
        ):
            # self.patient_table.setItem(_tablerow, 0, QtWidgets.QTableWidgetItem(col[0]))
            item = str(col[0])
            self.patient_table.setItem(_tablerow, 0, QtWidgets.QTableWidgetItem(item))
            self.patient_table.setItem(_tablerow, 1, QtWidgets.QTableWidgetItem(col[1]))
            self.patient_table.setItem(_tablerow, 2, QtWidgets.QTableWidgetItem(col[2]))
            self.patient_table.setItem(_tablerow, 3, QtWidgets.QTableWidgetItem(col[3]))
            self.patient_table.setItem(_tablerow, 4, QtWidgets.QTableWidgetItem(col[4]))
            self.patient_table.setItem(_tablerow, 5, QtWidgets.QTableWidgetItem(col[5]))
            _tablerow += 1
            pass


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
