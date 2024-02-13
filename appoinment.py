import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QCalendarWidget
from PyQt5.QtCore import QDate
import sqlite3


class appointment_window(QDialog):
    def __init__(self):
        super(appointment_window, self).__init__()
        loadUi("appointment_window.ui", self)
        """self.v_name = ""
        self.v_time = ""
        self.phone = ""
        self.v_date = ""
"""
        self.appointment_table.setColumnWidth(0, 150)

        self.appointment_table.setColumnWidth(1, 150)

        self.load_table()

        # self._appointment.add_btn.clicked.connect(self.save_appointment)
        self.add_btn.clicked.connect(self.save_appointment)

    def save_appointment(self):
        v_name_input = self.vname_edit.toPlainText()
        phone_input = self.phone_edit.toPlainText()
        v_time_input = self.visit_time_edit.toPlainText()
        v_date_input = self.visit_date_edit.toPlainText()
        conn = sqlite3.connect("medico.db3")
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO appointments (appnt_date,visitor_name,visitor_phone,visit_time,visit_date)
            VALUES (DATE('now'), ?, ?, ?,?)
        """,
            (v_name_input, phone_input, v_time_input, v_date_input),
        )
        conn.commit()
        conn.close()

    def load_table(self):
        _connect = sqlite3.connect("MEDICO.db3")
        _cur = _connect.cursor()
        _query = "SELECT * FROM appointments"
        # data = _cur.fetchall()  # Fetch data
        _tablerow = 0
        self.appointment_table.setRowCount(50)

        for col in _cur.execute(_query):
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
