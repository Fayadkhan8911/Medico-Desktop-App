import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QDialog, QApplication, QWidget
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

import sqlite3


class _patient_window(QDialog):
    def __init__(self):
        super(_patient_window, self).__init__()
        loadUi("patients_window.ui", self)
        self.fname_srch_edit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lname_srch_edit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.phone_srch_edit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.patid_srch_edit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.search_btn.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.add_patient_btn.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.dash_btn.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.patient_btn.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.payment_btn.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.expense_btn.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.appointment_btn.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.dentist_btn.setFocusPolicy(QtCore.Qt.StrongFocus)
        
        self.setTabOrder(self.fname_srch_edit, self.lname_srch_edit)
        self.setTabOrder(self.lname_srch_edit, self.phone_srch_edit)
        self.setTabOrder(self.phone_srch_edit, self.patid_srch_edit)
        self.setTabOrder(self.patid_srch_edit, self.search_btn)
        self.setTabOrder(self.search_btn, self.add_patient_btn)
        self.setTabOrder(self.add_patient_btn, self.dash_btn)
        self.setTabOrder(self.dash_btn, self.patient_btn)
        self.setTabOrder(self.patient_btn, self.payment_btn)
        self.setTabOrder(self.payment_btn, self.expense_btn)
        self.setTabOrder(self.expense_btn, self.appointment_btn)
        self.setTabOrder(self.appointment_btn, self.dentist_btn)
        
        self.fname_srch_edit.setTabChangesFocus(True)
        self.lname_srch_edit.setTabChangesFocus(True)
        self.phone_srch_edit.setTabChangesFocus(True)
        self.patid_srch_edit.setTabChangesFocus(True)
        self.patient_btn.setFocus()
        
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
