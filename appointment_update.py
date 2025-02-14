import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QCalendarWidget
from PyQt5.QtCore import QDate
import sqlite3
from appointment_update_ui import Ui_Dialog  # Import your UI class


class appointment_update(QDialog, Ui_Dialog):
    def __init__(self, v_name, v_phone):
        super(appointment_update, self).__init__()
        self.setupUi(self)  # Initialize the UI

        self.v_name = v_name
        self.v_phone = v_phone
        self.appointment_table.setColumnWidth(0, 150)
        self.appointment_table.setColumnWidth(1, 150)

        self.load_table()
        self.v_date = self.calendar.selectedDate()

        # self._appointment.add_btn.clicked.connect(self.save_appointment)
        # self.add_appointment_btn.clicked.connect(self.save_appointment)
        # self.search_btn.clicked.connect(self.search_date)
        # self

    def load_table(self):
        print(f"v_name = {self.v_name}")
        _connect = sqlite3.connect("MEDICO.db3")
        _cur = _connect.cursor()

        _tablerow = 0
        self.appointment_table.setRowCount(50)
        self.appointment_table.setColumnWidth(4, 200)
        self.appointment_table.setColumnWidth(3, 200)

        for col in _cur.execute(
            "SELECT reg_date,visitor_name,visitor_phone,visit_time,dentist_name FROM appointments WHERE visitor_date=? ",
            (self.v_date,),
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
