import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QCalendarWidget
from PyQt5.QtCore import QDate
import sqlite3
import appt_success
import error
import re


class appointment_window(QDialog):
    def __init__(self, appt_callback_fnc):
        super(appointment_window, self).__init__()
        loadUi("gui/appointment_window.ui", self)
        
        self.vname_edit.setTabChangesFocus(True)
        self.phone_edit.setTabChangesFocus(True)
        self.dname_edit.setTabChangesFocus(True)
        self.pat_id_edit.setTabChangesFocus(True)
        self.search_name_edit.setTabChangesFocus(True)
        self.search_phone_edit.setTabChangesFocus(True)
        self.search_pat_id_edit.setTabChangesFocus(True)
        
        self.current_date = QDate.currentDate()
        self.reg_date = self.current_date.toString('yyyy-MM-dd')
        
        """self.v_name = ""
        self.v_time = ""
        self.phone = ""
        self.v_date = ""
"""
        self.appt_callback_fnc = appt_callback_fnc
        self.appointment_table.setColumnWidth(0, 150)

        self.appointment_table.setColumnWidth(1, 150)

        self.load_table()

        # self._appointment.add_btn.clicked.connect(self.save_appointment)
        self.add_appointment_btn.clicked.connect(self.save_appointment)
        
        
    def match_mobile_pattern(self, phone_input):
        phone_pattern = re.compile(r'^(?:\+8801[3-9]\d{8}|01[3-9]\d{8})$')
        # Check if the input matches the phone number pattern
        if phone_pattern.match(phone_input):
            return True
        else:
            return False
        
        

    #    self.search_btn.clicked.connect(self.search_date)
    def show_error_window(self, message):
        error_window = error._error_window(message)  # Adjusted to use the error module
        #error_window.ok_btn.clicked.connect(self.trigger_callback)
        error_window.exec_()

    def save_appointment(self):
        p_id = self.pat_id_edit.toPlainText()
        v_name_input = self.vname_edit.toPlainText()
        phone_input = self.phone_edit.toPlainText()
        v_time_input = self.timeEdit.time().toString()
        v_date_input = self.calendar.selectedDate().toString("yyyy-MM-dd")
        print(v_date_input)
        dr_input = self.dname_edit.toPlainText()
        conn = sqlite3.connect("medico.db3")
        cursor = conn.cursor()
        cur1 = conn.cursor()
        if p_id == "":
            
            if not v_name_input or not phone_input:
                message = "Please Input both Name and Phone Number"
                self.show_error_window(message)
                return
            
            elif not self.match_mobile_pattern(phone_input):
                message = "Please Input valid Phone Number"
                self.show_error_window(message)
                return
            
            cursor.execute(
                """
                INSERT INTO appointments (reg_date,visitor_name,visitor_phone,visit_time,visit_date,status,dentist_name)
                VALUES (?, ?, ?, ?, ?, ?,?)
             """,
                (
                    self.reg_date,
                    v_name_input,
                    phone_input,
                    v_time_input,
                    v_date_input,
                    "Active",
                    dr_input,
                ),
            )
            conn.commit()
            conn.close()
            self.show_appt_success_dialog()
        else:
            cur1.execute(
                """
                           SELECT f_name , phone FROM patients WHERE p_id =?
                           """,
                (p_id,),
            )
            d = cur1.fetchone()

            # _name = data[0]
            # _phone = data[1]
            # print(type(data))
            if d:
                data = list(d)
                _name = data[0]
                _phone = data[1]
                print("testing")
                cursor.execute(
                    """
                    INSERT INTO appointments (reg_date,visitor_name,visitor_phone,visit_time,visit_date,status,dentist_name,p_id)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """,
                    (
                        self.reg_date,
                        _name,
                        _phone,
                        v_time_input,
                        v_date_input,
                        "Active",
                        dr_input,
                        p_id,
                    ),
                )
                conn.commit()
                conn.close()
                self.show_appt_success_dialog()
            #     print("testing")
            else:
                print("testing 2")
                self.show_error_window("No patient found with Patient ID")
                print("No patient found with Patient ID")

    def show_appt_success_dialog(self):
        success_dialog = appt_success._error_window("Appointment Success")
        success_dialog.ok_btn.clicked.connect(self.trigger_callback)
        success_dialog.exec_()

    def trigger_callback(self):
        self.appt_callback_fnc()

    def load_table(self):
        current_date = self.current_date.toString("yyyy-MM-dd")
        _connect = sqlite3.connect("MEDICO.db3")
        _cur = _connect.cursor()
        _cur.execute(("""SELECT reg_date, p_id , visitor_name, visitor_phone, visit_date, visit_time, dentist_name, status FROM appointments WHERE visit_date >= ? ORDER BY visit_date DESC"""), (current_date,))
        
        rows = _cur.fetchall()
        print(rows)
        
        _tablerow = 0
        self.appointment_table.setRowCount(50)
        self.appointment_table.setColumnWidth(4, 130)
        self.appointment_table.setColumnWidth(3, 120)
        self.appointment_table.setColumnWidth(1, 130)
        self.appointment_table.setColumnWidth(0, 100)
        self.appointment_table.setColumnWidth(2, 130)
        

        for col in rows:
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
            pass
        
        self.appointment_table.resizeColumnsToContents()


"""
    def search_date(self):
        self.date_input = self.search_date_edit.toPlainText()

        _connect = sqlite3.connect("MEDICO.db3")
        _cur = _connect.cursor()
        _query = "SELECT * FROM appointments WHERE appnt_date=?"  # Correct query syntax
        _cur.execute(_query, (self.date_input,))  # Pass parameters correctly

        _tablerow = 0
        self.appointment_table.setRowCount(50)

        for col in _cur.fetchall():
            for col_index, col_data in enumerate(col):
                self.appointment_table.setItem(
                    _tablerow, col_index, QtWidgets.QTableWidgetItem(str(col_data))
                )
            _tablerow += 1

        _connect.close()
"""

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
