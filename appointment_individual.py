import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QCalendarWidget
from PyQt5.QtCore import QDate
import sqlite3


class appointment_individual(QDialog):
    def __init__(self):
        super(appointment_individual, self).__init__()
        loadUi("appointment_individual.ui", self)
        """self.v_name = ""
        self.v_time = ""
        self.phone = ""
        self.v_date = ""
"""
        self.appointment_table.setColumnWidth(0, 150)

        self.appointment_table.setColumnWidth(1, 150)

        # self.load_table()

        # self._appointment.add_btn.clicked.connect(self.save_appointment)
        # self.add_appointment_btn.clicked.connect(self.save_appointment)
        # self.search_btn.clicked.connect(self.search_date)

    def load_table(self, v_name, v_phone):
        _connect = sqlite3.connect("MEDICO.db3")
        _cur = _connect.cursor()
        # _query = "SELECT appointment_date , visitor_name, visitor_phone,visit_date,visit_time FROM appointments ORDER BY visit_date DESC"
        # data = _cur.fetchall()  # Fetch data
        _tablerow = 0
        self.appointment_table.setRowCount(50)
        self.appointment_table.setColumnWidth(4, 200)
        self.appointment_table.setColumnWidth(3, 200)

        for col in _cur.execute(
            "SELECT reg_date,visitor_name,visitor_phone,visit_date,visit_time,dentist_name FROM appointments WHERE visitor_name=? AND visitor_phone=?",
            (v_name, v_phone),
        ):
            self.appointment_table.setItem(
                _tablerow, 0, QtWidgets.QTableWidgetItem(col[0])
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
                _tablerow, 4, QtWidgets.QTableWidgetItem(col[4])
            )
            _tablerow += 1
            pass


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
