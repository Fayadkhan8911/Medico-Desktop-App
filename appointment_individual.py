import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QCalendarWidget
from PyQt5.QtCore import QDate
import sqlite3
from appointment_individual_ui import Ui_Dialog  # Import your UI class


class appointment_individual(QDialog, Ui_Dialog):
    def __init__(self, v_name, v_phone, p_id):
        super(appointment_individual, self).__init__()
        self.setupUi(self)  # Initialize the UI

        self.v_name = v_name
        self.v_phone = v_phone
        self.p_id = p_id
        self.appointment_table.setColumnWidth(0, 150)
        self.appointment_table.setColumnWidth(1, 150)
        self.load_table(self.v_name, self.v_phone, self.p_id)

        self.cancel_btn.clicked.connect(
            lambda: self.cancel_appointment(self.v_name, self.v_phone)
        )

    def cancel_appointment(self, v_name, v_phone):
        v_name = self.v_name
        v_phone = self.v_phone
        p_id = self.p_id
        _connect = sqlite3.connect("MEDICO.db3")
        _cur = _connect.cursor()

        if p_id == "":
            _cur.execute(
                """
                UPDATE appointments  
                SET Status='Cancelled' 
                WHERE visit_date=(SELECT visit_date FROM appointments WHERE visitor_name=? AND visitor_phone=? ORDER BY visit_date DESC LIMIT 1)""",
                (v_name, v_phone),
            )
            _connect.commit()
        else:
            _cur.execute(
                """
                UPDATE appointments  
                SET Status='Cancelled' 
                WHERE visit_date=(SELECT visit_date FROM appointments WHERE p_id=?  ORDER BY visit_date DESC LIMIT 1)""",
                (p_id,),
            )
            _connect.commit()
        self.load_table(self.v_name, self.v_phone, self.p_id)

    def load_table(self, v_name, v_phone, p_id):
        v_name = self.v_name
        v_phone = self.v_phone
        p_id = self.p_id

        _connect = sqlite3.connect("MEDICO.db3")
        _cur = _connect.cursor()

        _tablerow = 0
        self.appointment_table.setRowCount(50)
        self.appointment_table.setColumnWidth(4, 150)
        self.appointment_table.setColumnWidth(3, 150)
        self.appointment_table.setColumnWidth(5, 100)
        self.appointment_table.setColumnWidth(6, 150)

        if p_id == "":
            for col in _cur.execute(
                "SELECT reg_date,p_id,visitor_name,visitor_phone,visit_date,visit_time,dentist_name,status FROM appointments WHERE visitor_name=? AND visitor_phone=? ORDER BY visit_date ",
                (v_name, v_phone),
            ):
                self.appointment_table.setItem(
                    _tablerow, 0, QtWidgets.QTableWidgetItem(QDate.fromString(col[0], "yyyy-MM-dd").toString("dd-MM-yyyy"))
                )
                self.appointment_table.setItem(
                    _tablerow, 1, QtWidgets.QTableWidgetItem(col[1])
                )
                self.appointment_table.setItem(
                    _tablerow, 2, QtWidgets.QTableWidgetItem(col[2])
                )
                self.appointment_table.setItem(
                    _tablerow, 3, QtWidgets.QTableWidgetItem(col[3])
                )
                self.appointment_table.setItem(
                    _tablerow, 4, QtWidgets.QTableWidgetItem(QDate.fromString(col[4], "yyyy-MM-dd").toString("dd-MM-yyyy"))
                )
                self.appointment_table.setItem(
                    _tablerow, 5, QtWidgets.QTableWidgetItem(col[5])
                )
                self.appointment_table.setItem(
                    _tablerow, 6, QtWidgets.QTableWidgetItem(col[6])
                )
                self.appointment_table.setItem(
                    _tablerow, 7, QtWidgets.QTableWidgetItem(col[7])
                )
                _tablerow += 1

        else:
            for col in _cur.execute(
                "SELECT appointments.reg_date,appointments.p_id, patients.f_name, patients.phone,appointments.visit_date,appointments.visit_time,appointments.dentist_name,appointments.status FROM appointments INNER JOIN patients ON appointments.p_id = patients.p_id WHERE appointments.p_id=? ORDER BY appointments.visit_date ",
                (p_id,),
            ):
                self.appointment_table.setItem(
                    _tablerow, 0, QtWidgets.QTableWidgetItem(QDate.fromString(col[0], "yyyy-MM-dd").toString("dd-MM-yyyy"))
                )
                self.appointment_table.setItem(
                    _tablerow, 1, QtWidgets.QTableWidgetItem(col[1])
                )
                self.appointment_table.setItem(
                    _tablerow, 2, QtWidgets.QTableWidgetItem(col[2])
                )
                self.appointment_table.setItem(
                    _tablerow, 3, QtWidgets.QTableWidgetItem(col[3])
                )
                self.appointment_table.setItem(
                    _tablerow, 4, QtWidgets.QTableWidgetItem(QDate.fromString(col[4], "yyyy-MM-dd").toString("dd-MM-yyyy"))
                )
                self.appointment_table.setItem(
                    _tablerow, 5, QtWidgets.QTableWidgetItem(col[5])
                )
                self.appointment_table.setItem(
                    _tablerow, 6, QtWidgets.QTableWidgetItem(col[6])
                )
                self.appointment_table.setItem(
                    _tablerow, 7, QtWidgets.QTableWidgetItem(col[7])
                )
                _tablerow += 1



"""
app = QApplication(sys.argv)

widget = QtWidgets.QStackedWidget()
_patient = appointment_window()

widget.addWidget(_patient)


widget.setFixedWidth(800)
widget.setFixedHeight(600)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")
# """
