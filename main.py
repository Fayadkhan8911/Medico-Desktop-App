import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (
    QDialog,
    QApplication,
    QWidget,
    QTableWidget,
    QTableWidgetItem,
)
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QCalendarWidget
from PyQt5.QtCore import QDate
import sqlite3

import add_patients
import patients
import add_pat_med
import pat_detailed
import error
import expense_window
import payments_window
import pytz
from PyQt5.QtCore import QTimeZone
import view_expense
import appoinment
import dentist
import new_dentist

# import sys


class _main_window(QDialog):
    def __init__(self):
        super(_main_window, self).__init__()
        loadUi("main_window.ui", self)

        self.patient_btn.clicked.connect(self._go_patient_window)
        self.payment_btn.clicked.connect(self._go_make_payment)
        self.expense_btn.clicked.connect(self._go_spend_money)
        self.appointment_btn.clicked.connect(self._go_appoinment)
        self.dentist_btn.clicked.connect(self.get_dentist)
        # self.add_patient_btn.clicked.connect(self._go_add_pat)
        current_day = QDate.currentDate()
        formatted_date = current_day.toString("yyyy-MM-dd")
        print(formatted_date)
        self.load_appointment_table()
        self.load_expense_table()
        # self.show_expenses()
        # Get the current date

    current_date = QDate.currentDate()

    # Convert to 'yyyy-MM-dd' format
    formatted_date = current_date.toString("yyyy-MM-dd")

    def load_expense_table(self):
        _connect = sqlite3.connect("MEDICO.db3")
        _cur = _connect.cursor()
        # _query = ("SELECT * FROM appointments WHERE appnt_date = ?",(self.current_date,),)
        self.expense_table.setColumnWidth(1, 200)
        self.expense_table.setColumnWidth(0, 200)

        # data = _cur.fetchall()  # Fetch data
        tablerow = 0
        self.expense_table.setRowCount(50)
        # cursor.execute("SELECT * FROM appointments WHERE appnt_date = ?", (self.current_date,))

        for col in _cur.execute(
            "SELECT expense_description, expense_remarks, expense_cost FROM expense WHERE expense_date=?",
            (self.formatted_date,),
        ):
            int_cost = str(col[2])
            self.expense_table.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(col[0]))
            self.expense_table.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(col[1]))
            self.expense_table.setItem(
                tablerow, 2, QtWidgets.QTableWidgetItem(int_cost)
            )

            tablerow += 1
            pass

    def load_appointment_table(self):
        _connect = sqlite3.connect("MEDICO.db3")
        _cur = _connect.cursor()
        # _query = ("SELECT * FROM appointments WHERE appnt_date = ?",(self.current_date,),)
        self.appointment_table.setColumnWidth(0, 200)
        self.appointment_table.setColumnWidth(1, 200)
        # data = _cur.fetchall()  # Fetch data
        _tablerow = 0
        self.appointment_table.setRowCount(50)
        # cursor.execute("SELECT * FROM appointments WHERE appnt_date = ?", (self.current_date,))

        for col in _cur.execute(
            "SELECT visitor_name, visitor_phone, visit_time FROM appointments WHERE visit_date=?",
            (self.formatted_date,),
        ):
            # self.appointment_table.setItem(_tablerow, 0, QtWidgets.QTableWidgetItem(col[0]))

            self.appointment_table.setItem(
                _tablerow, 0, QtWidgets.QTableWidgetItem(col[0])
            )
            self.appointment_table.setItem(
                _tablerow, 1, QtWidgets.QTableWidgetItem(col[1])
            )
            self.appointment_table.setItem(
                _tablerow, 2, QtWidgets.QTableWidgetItem(col[2])
            )

            _tablerow += 1
            pass

    def _go_appoinment(self):
        self._appointment = appoinment.appointment_window()
        widget.addWidget(self._appointment)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        self._appointment.dash_btn.clicked.connect(self._go_dash)
        self._appointment.patient_btn.clicked.connect(self._go_patient_window)
        # self._appointment.search_btn.clicked.connect(self._go_pat_det)

        self._appointment.payment_btn.clicked.connect(self._go_make_payment)
        self._appointment.expense_btn.clicked.connect(self._go_spend_money)
        self._appointment.dentist_btn.clicked.connect(self.get_dentist)

    def current_date(self):
        current_date = QDate.currentDate()
        # print(f"Current date is: {current_date.toString()}")
        return f"Today is: {current_date.toString()}"

    def _go_dash(self):
        _dash = _main_window()
        widget.addWidget(_dash)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def _go_patient_window(self):
        self._patients = patients._patient_window()
        widget.addWidget(self._patients)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        self._patients.dash_btn.clicked.connect(self._go_dash)
        self._patients.add_patient_btn.clicked.connect(self._go_add_pat)
        # self._patients.search_btn.clicked.connect(self._go_pat_det)
        self._patients.search_btn.clicked.connect(self.makemegotopat)
        self._patients.payment_btn.clicked.connect(self._go_make_payment)
        self._patients.expense_btn.clicked.connect(self._go_spend_money)
        self._patients.appointment_btn.clicked.connect(self._go_appoinment)
        self._patients.dentist_btn.clicked.connect(self.get_dentist)

    def show_error_window(self, message):
        error_window = error._error_window(message)  # Adjusted to use the error module
        error_window.exec_()

    def makemegotopat(self):
        f_name = self._patients.fname_srch_edit.toPlainText()
        l_name = self._patients.lname_srch_edit.toPlainText()
        phone = self._patients.phone_srch_edit.toPlainText()
        patient_id = self._patients.patid_srch_edit.toPlainText()

        if f_name and phone:
            conn = sqlite3.connect("medico.db3")
            c = conn.cursor()
            c.execute(
                "SELECT * FROM patients WHERE f_name=? AND phone=?", (f_name, phone)
            )
            result = c.fetchone()
            conn.close()
            if result:
                self._go_pat_det()
            else:
                self.show_error_window(
                    "No patient found with First Name and Phone Number."
                )
                print("No patient found with First Name and Phone Number.")

        elif patient_id:

            conn = sqlite3.connect("medico.db3")
            c = conn.cursor()
            c.execute("SELECT * FROM patients WHERE p_id=?", (patient_id,))
            result = c.fetchone()
            conn.close()

            if result:
                self._go_pat_det()
            else:
                self.show_error_window("No patient found with Patient ID")
                print("No patient found with Patient ID")
        else:
            self.show_error_window(
                "Please provide either First Name and Phone Number or Patient ID"
            )
            print("Please provide either first name and phone number or patient ID")

    def _go_add_pat(self):
        self._add_pat = add_patients._add_patient_window()
        widget.addWidget(self._add_pat)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        self._add_pat.dash_btn.clicked.connect(self._go_dash)
        self._add_pat.patient_btn.clicked.connect(self._go_patient_window)
        self._add_pat.next_btn.clicked.connect(self.chkvalid)
        self._add_pat.return_btn.clicked.connect(self._go_patient_window)
        self._add_pat.payment_btn.clicked.connect(self._go_make_payment)
        self._add_pat.expense_btn.clicked.connect(self._go_spend_money)
        self._add_pat.appointment_btn.clicked.connect(self._go_appoinment)
        self._add_pat.dentist_btn.clicked.connect(self.get_dentist)

    def chkvalid(self):
        # CHECK
        f_name_input = self._add_pat.add_fname_edit.toPlainText().strip()
        l_name_input = self._add_pat.add_lname_edit.toPlainText().strip()
        phone_input = self._add_pat.add_phn_edit.toPlainText().strip()
        address_input = self._add_pat.add_address_edit.toPlainText().strip()
        age_input = self._add_pat.add_age_edit.toPlainText().strip()

        if (
            not f_name_input
            or not l_name_input
            or not phone_input
            or not address_input
            or not age_input
        ):
            if not f_name_input:
                self.show_error_window("You Must Enter First Name")
                print("You Must Enter First Name")
            elif not l_name_input:
                self.show_error_window("You Must Enter Last Name")
                print("You Must Enter Last Name")
            elif not phone_input:
                self.show_error_window("You Must Enter Phone Number")
                print("You Must Enter Phone Number")
            elif not address_input:
                self.show_error_window("You Must Enter Address")
                print("You Must Enter Address")
            elif not age_input:
                self.show_error_window("You Must Enter Age")
                print("You Must Enter Age")
            print("Missing Information")
        else:
            conn = sqlite3.connect("medico.db3")
            c = conn.cursor()
            # Search for the patient using first name and phone number
            c.execute(
                "SELECT * FROM patients WHERE f_name=? AND phone=?",
                (f_name_input, phone_input),
            )
            existing_patient = c.fetchone()
            if existing_patient:
                patient_id = existing_patient[0]
                message = f"Patient Already Exists with First Name = {f_name_input} and Phone Number = {phone_input}. Patient ID = {patient_id}"
                self.show_error_window(message)
            else:
                self._go_med_hist()

    def _go_med_hist(self):  # inserting to DB

        # Retrieve patient data from _add_patient_window instance
        f_name = self._add_pat.add_fname_edit.toPlainText()
        l_name = self._add_pat.add_lname_edit.toPlainText()
        phone = self._add_pat.add_phn_edit.toPlainText()
        address = self._add_pat.add_address_edit.toPlainText()
        occupation = self._add_pat.add_occu_edit.toPlainText()
        email = self._add_pat.add_email_edit.toPlainText()
        age = self._add_pat.add_age_edit.toPlainText()
        sex = self._add_pat.add_sex_edit.currentText()
        reference = self._add_pat.add_ref_edit.toPlainText()
        date_of_departure = self._add_pat.add_depart_edit.toPlainText()
        chief_complain = self._add_pat.add_complain_edit.toPlainText()

        # Instantiate _add_med_hist_win with the retrieved patient data
        self._med_hist = add_pat_med._add_med_hist_win(
            f_name,
            l_name,
            phone,
            address,
            occupation,
            email,
            age,
            sex,
            reference,
            date_of_departure,
            chief_complain,
        )
        widget.addWidget(self._med_hist)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        self._med_hist.restart_btn.clicked.connect(self._go_add_pat)
        self._med_hist.patient_btn.clicked.connect(self._go_patient_window)
        self._med_hist.save_pat.clicked.connect(self._go_patient_window)
        self._med_hist.payment_btn.clicked.connect(self._go_make_payment)
        self._med_hist.expense_btn.clicked.connect(self._go_spend_money)
        self._med_hist.appointment_btn.clicked.connect(self._go_appoinment)
        self._med_hist.dentist_btn.clicked.connect(self.get_dentist)

    def _go_pat_det(self):
        f_name = self._patients.fname_srch_edit.toPlainText()
        l_name = self._patients.lname_srch_edit.toPlainText()
        phone = self._patients.phone_srch_edit.toPlainText()
        patient_id = self._patients.patid_srch_edit.toPlainText()
        self._details = pat_detailed._pat_detailed_win(
            f_name, l_name, phone, patient_id
        )
        widget.addWidget(self._details)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        self._details.return_pat.clicked.connect(self._go_patient_window)
        self._details.dash_btn.clicked.connect(self._go_dash)
        self._details.patient_btn.clicked.connect(self._go_patient_window)
        self._details.payment_btn.clicked.connect(self._go_make_payment)
        self._details.expense_btn.clicked.connect(self._go_spend_money)
        self._details.appointment_btn.clicked.connect(self._go_appoinment)
        self._details.dentist_btn.clicked.connect(self.get_dentist)

    def _go_make_payment(self):
        self._make_payment = payments_window._payments_window()
        widget.addWidget(self._make_payment)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        self._make_payment.dash_btn.clicked.connect(self._go_dash)
        self._make_payment.patient_btn.clicked.connect(self._go_patient_window)
        self._make_payment.expense_btn.clicked.connect(self._go_spend_money)
        self._make_payment.pushButton.clicked.connect(self.createpayment)
        self._make_payment.appointment_btn.clicked.connect(self._go_appoinment)
        self._make_payment.dentist_btn.clicked.connect(self.get_dentist)

    def createpayment(self):
        f_name = self._make_payment.fname_srch_edit.toPlainText()
        phone = self._make_payment.phone_srch_edit.toPlainText()
        amount = self._make_payment.payment_edit.toPlainText()
        remarks = self._make_payment.remarks_edit.toPlainText()

        conn = sqlite3.connect("medico.db3")
        cursor = conn.cursor()
        # Retrieve the p_id using the provided first name and phone number
        cursor.execute(
            "SELECT p_id FROM patients WHERE f_name = ? AND phone = ?", (f_name, phone)
        )
        result = cursor.fetchone()
        if result:
            p_id = result[0]
        else:
            # Handle the case where the patient is not found
            print("Patient not found.")
            return

        # Retrieve the last payment_id
        cursor.execute(
            "SELECT MAX(CAST(SUBSTR(payment_id, 5) AS INTEGER)) FROM payment_history"
        )
        result = cursor.fetchone()
        if result[0] is not None:
            last_payment_id = result[0]
        else:
            last_payment_id = 0

        # Increment the last_payment_id
        payment_id = last_payment_id + 1

        # Get the current date
        payment_date = QDate.currentDate().toString(
            "yyyy-MM-dd"
        )  # You need to implement this function

        # Insert the payment record into the payment_history table
        cursor.execute(
            "INSERT INTO payment_history (payment_id, p_id, payment_date, payment_amount, payment_remarks) VALUES (?, ?, ?, ?, ?)",
            (payment_id, p_id, payment_date, int(amount), remarks),
        )

        # Commit the transaction
        conn.commit()

        print("Payment record inserted successfully.")

    def _go_spend_money(self):
        self._spend_money = expense_window._expense_window()
        widget.addWidget(self._spend_money)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        self._spend_money.dash_btn.clicked.connect(self._go_dash)
        self._spend_money.patient_btn.clicked.connect(self._go_patient_window)
        self._spend_money.payment_btn.clicked.connect(self._go_make_payment)
        self._spend_money.expense_btn.clicked.connect(self._go_spend_money)
        self._spend_money.calendar.clicked.connect(self.grab_expense)
        self._spend_money.appointment_btn.clicked.connect(self._go_appoinment)
        self._spend_money.dentist_btn.clicked.connect(self.get_dentist)

    def grab_expense(self):
        dateSelected = self._spend_money.calendar.selectedDate()
        print(dateSelected)
        expense_date = str(dateSelected.toPyDate())
        self._view_expense_window = view_expense._expense_view_window(expense_date)
        widget.addWidget(self._view_expense_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        self._view_expense_window.dash_btn.clicked.connect(self._go_dash)
        self._view_expense_window.patient_btn.clicked.connect(self._go_patient_window)
        self._view_expense_window.payment_btn.clicked.connect(self._go_make_payment)
        self._view_expense_window.expense_btn.clicked.connect(self._go_spend_money)
        # self._view_expense_window.calendar.clicked.connect(self.grab_expense)
        self._view_expense_window.appointment_btn.clicked.connect(self._go_appoinment)
        self._view_expense_window.dentist_btn.clicked.connect(self.get_dentist)

    def get_dentist(self):
        self.dentist_tab = dentist._dentist_window()
        widget.addWidget(self.dentist_tab)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        self.dentist_tab.dentist_btn.clicked.connect(self.get_dentist)
        self.dentist_tab.dash_btn.clicked.connect(self._go_dash)
        self.dentist_tab.patient_btn.clicked.connect(self._go_patient_window)
        self.dentist_tab.payment_btn.clicked.connect(self._go_make_payment)
        self.dentist_tab.expense_btn.clicked.connect(self._go_spend_money)
        self.dentist_tab.appointment_btn.clicked.connect(self._go_appoinment)
        self.dentist_tab.add_dentist_btn.clicked.connect(self.add_new_dentist)

    def add_new_dentist(self):
        self.new_dentist_tab = new_dentist.new_dentist_window()
        widget.addWidget(self.new_dentist_tab)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        self.new_dentist_tab.dash_btn.clicked.connect(self._go_dash)
        self.new_dentist_tab.patient_btn.clicked.connect(self._go_patient_window)
        self.new_dentist_tab.payment_btn.clicked.connect(self._go_make_payment)
        self.new_dentist_tab.expense_btn.clicked.connect(self._go_spend_money)
        self.new_dentist_tab.appointment_btn.clicked.connect(self._go_appoinment)
        self.new_dentist_tab.dentist_btn.clicked.connect(self.get_dentist)


"""     this was for 'only one main.py' file format

class _patient_window(QDialog):
    def __init__(self):
        super(_patient_window, self).__init__()
        loadUi("patients_window.ui", self)
        self.dash_btn.clicked.connect(self._go_dash)

    def _go_dash(self):
        _dash = _main_window()
        widget.addWidget(_dash)
        widget.setCurrentIndex(widget.currentIndex() + 1)

"""

# main
app = QApplication(sys.argv)

widget = QtWidgets.QStackedWidget()
_main = _main_window()

widget.addWidget(_main)


widget.setFixedWidth(1200)
widget.setFixedHeight(600)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")
