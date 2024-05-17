import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (
    QDialog,
    QApplication,
    QWidget,
    QTableWidget,
    QTableWidgetItem,
    QPushButton,
)
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QCalendarWidget
from PyQt5.QtCore import QDate
import sqlite3
import re
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
import appointment_individual
import confirm_delete
import files_add
import files_updt
import patient_edit01
import patient_edit02
import pdf_maker
import view_payments
import view_files

# import sys


class _main_window(QDialog):
    def __init__(self):
        super(_main_window, self).__init__()
        loadUi("main_window.ui", self)

        self.patient_btn.clicked.connect(self._go_patient_window)
        self.payment_btn.clicked.connect(self._go_make_payment)
        self.expense_btn.clicked.connect(self._go_spend_money)
        self.appointment_btn.clicked.connect(self._go_appointment)
        self.dentist_btn.clicked.connect(self.get_dentist)
        # self.add_patient_btn.clicked.connect(self._go_add_pat)
        current_day = QDate.currentDate()
        self.formatted_date = current_day.toString("dd-MM-yyyy")
        print(self.formatted_date)
        self.load_appointment_table()
        self.load_expense_table()
        self.load_payment_table()
        # self.show_expenses()
        # Get the current date
        self.print_appt.clicked.connect(self.print_present_appointments)
        self.print_pay.clicked.connect(self.print_present_payments)
        self.print_expense.clicked.connect(self.print_present_expence)

    def print_present_expence(self):
        _query = "SELECT expense_description, expense_remarks , expense_cost FROM expense WHERE expense_date = ?"
        prefix = " Expences "
        file_location = "expence_pdf/"
        pdf = pdf_maker.pdf_maker(_query, prefix, file_location)
        pdf

    def print_present_appointments(self):
        _query = "SELECT visitor_name,visitor_phone,visit_time,dentist_name,p_id,status FROM appointments WHERE visit_date=? "
        suffix = "__Appointments "
        file_location = "Appointments_PDF/"
        pdf = pdf_maker.pdf_maker(_query, suffix, file_location)
        pdf

    def print_present_payments(self):
        _query = "SELECT payment_history.p_id, patients.f_name, patients.phone,payment_history.payment_amount FROM payment_history INNER JOIN patients on payment_history.p_id = patients.p_id WHERE payment_date=? "
        prefix = " Payments "
        file_location = "Payments_pdf/"
        pdf = pdf_maker.pdf_maker(_query, prefix, file_location)
        pdf

    current_date = QDate.currentDate()

    # Convert to 'yyyy-MM-dd' format
    formatted_date = current_date.toString("dd-MM-yyyy")

    def load_payment_table(self):

        _connect = sqlite3.connect("MEDICO.db3")
        _cur = _connect.cursor()
        # _query = ("SELECT * FROM appointments WHERE appnt_date = ?",(self.current_date,),)
        self.payment_table.setColumnWidth(1, 125)
        self.payment_table.setColumnWidth(0, 125)

        # data = _cur.fetchall()  # Fetch data
        tablerow = 0
        self.payment_table.setRowCount(50)
        # cursor.execute("SELECT * FROM appointments WHERE appnt_date = ?", (self.current_date,))

        _cur.execute(
            "SELECT patients.p_id, patients.f_name, patients.phone, payment_history.payment_amount FROM patients JOIN  payment_history ON patients.p_id=payment_history.p_id WHERE payment_history.payment_date=?",
            (self.formatted_date,),
        )
        results = _cur.fetchall()
        # _query = ("SELECT * FROM appointments WHERE appnt_date = ?",(self.current_date,),)
        self.payment_table.setColumnWidth(0, 150)
        self.payment_table.setColumnWidth(1, 150)
        self.payment_table.setColumnWidth(2, 100)
        # self.payment_table.setColumnWidth(3, 150)
        # data = _cur.fetchall()  # Fetch data
        _tablerow = 0
        self.payment_table.setRowCount(50)
        # cursor.execute("SELECT * FROM appointments WHERE appnt_date = ?", (self.current_date,))
        print(self.formatted_date + " from expense")
        for row_index, row_data in enumerate(results):
            for col_index, data in enumerate(row_data):
                item = QtWidgets.QTableWidgetItem(str(data))
                self.payment_table.setItem(row_index, col_index, item)

            _tablerow += 1
            pass

    def load_expense_table(self):
        _connect = sqlite3.connect("MEDICO.db3")
        _cur = _connect.cursor()
        _cur.execute(
            "SELECT expense_description, expense_remarks , expense_cost FROM expense WHERE expense_date = ?",
            (self.formatted_date,),
        )
        results = _cur.fetchall()
        # _query = ("SELECT * FROM appointments WHERE appnt_date = ?",(self.current_date,),)
        self.expense_table.setColumnWidth(0, 150)
        self.expense_table.setColumnWidth(1, 150)
        self.expense_table.setColumnWidth(2, 100)
        # self.expense_table.setColumnWidth(3, 150)
        # data = _cur.fetchall()  # Fetch data
        _tablerow = 0
        self.expense_table.setRowCount(50)
        # cursor.execute("SELECT * FROM appointments WHERE appnt_date = ?", (self.current_date,))
        # print(self.formatted_date + " from expense")
        for row_index, row_data in enumerate(results):
            for col_index, data in enumerate(row_data):
                item = QtWidgets.QTableWidgetItem(str(data))
                self.expense_table.setItem(row_index, col_index, item)

            _tablerow += 1
            pass

    def load_appointment_table(self):
        _connect = sqlite3.connect("MEDICO.db3")
        _cur = _connect.cursor()
        # _query = ("SELECT * FROM appointments WHERE appnt_date = ?",(self.current_date,),)
        self.appointment_table.setColumnWidth(0, 150)
        self.appointment_table.setColumnWidth(1, 150)
        self.appointment_table.setColumnWidth(2, 100)
        self.appointment_table.setColumnWidth(3, 150)
        # data = _cur.fetchall()  # Fetch data
        _tablerow = 0
        self.appointment_table.setRowCount(50)
        # cursor.execute("SELECT * FROM appointments WHERE appnt_date = ?", (self.current_date,))

        for col in _cur.execute(
            "SELECT visitor_name, visitor_phone, visit_time,dentist_name,p_id,status FROM appointments WHERE visit_date=? ORDER BY visit_time ",
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
            self.appointment_table.setItem(
                _tablerow, 3, QtWidgets.QTableWidgetItem(col[3])
            )
            self.appointment_table.setItem(
                _tablerow, 4, QtWidgets.QTableWidgetItem(col[4])
            )
            self.appointment_table.setItem(
                _tablerow, 5, QtWidgets.QTableWidgetItem(col[5])
            )

            _tablerow += 1
            pass

    def _go_appointment(self):
        self._appointment = appoinment.appointment_window(
            self._go_appointment_callback_fnc
        )
        widget.addWidget(self._appointment)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        self._appointment.dash_btn.clicked.connect(self._go_dash)
        self._appointment.patient_btn.clicked.connect(self._go_patient_window)
        # self._appointment.search_btn.clicked.connect(self._go_pat_det)

        self._appointment.payment_btn.clicked.connect(self._go_make_payment)
        self._appointment.expense_btn.clicked.connect(self._go_spend_money)
        self._appointment.dentist_btn.clicked.connect(self.get_dentist)
        self._appointment.appointment_btn.clicked.connect(self._go_appointment)
        self._appointment.search_btn.clicked.connect(self.valid_pat)

    def appointment_individual(self):
        v_name = self._appointment.search_name_edit.toPlainText()
        v_phone = self._appointment.search_phone_edit.toPlainText()
        p_id = self._appointment.search_pat_id_edit.toPlainText()

        self._indi_app = appointment_individual.appointment_individual(
            v_name, v_phone, p_id
        )
        widget.addWidget(self._indi_app)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        # self._indi_app.load_table(v_name,0 v_phone)
        print(v_name)
        self._indi_app.dash_btn.clicked.connect(self._go_dash)
        self._indi_app.patient_btn.clicked.connect(self._go_patient_window)
        # self._indi_app.search_btn.clicked.connect(self._go_pat_det)

        self._indi_app.payment_btn.clicked.connect(self._go_make_payment)
        self._indi_app.expense_btn.clicked.connect(self._go_spend_money)
        self._indi_app.dentist_btn.clicked.connect(self.get_dentist)
        self._indi_app.appointment_btn.clicked.connect(self._go_appointment)
        self._indi_app.return_btn.clicked.connect(self._go_appointment)

    def valid_pat(self):  # for  patient details

        f_name = self._appointment.search_name_edit.toPlainText()
        # l_name = self._appointment.lname_srch_edit.toPlainText()
        phone = self._appointment.search_phone_edit.toPlainText()
        patient_id = self._appointment.search_pat_id_edit.toPlainText()

        if patient_id:

            conn = sqlite3.connect("medico.db3")
            c = conn.cursor()
            c.execute("SELECT * FROM appointments WHERE p_id=?", (patient_id,))
            result = c.fetchone()
            conn.close()

            if result:
                self.appointment_individual()
            else:
                self.show_error_window("No patient found with Patient ID")
                print("No patient found with Patient ID")

        elif f_name and phone:
            conn = sqlite3.connect("medico.db3")
            c = conn.cursor()
            c.execute(
                "SELECT * FROM appointments WHERE visitor_name=? AND visitor_phone=?",
                (f_name, phone),
            )
            result = c.fetchone()
            conn.close()
            if result:
                self.appointment_individual()
            else:
                self.show_error_window(
                    "No patient found with First Name and Phone Number."
                )
                print("No patient found with First Name and Phone Number.")

        else:
            self.show_error_window(
                "Please provide either First Name and Phone Number or Patient ID"
            )
            print("Please provide either first name and phone number or patient ID")

    def checkvalid_appnt(self):
        # CHECK0
        vname_input = self._appointment.vname_edit.toPlainText().strip()
        phone_input = self._appointment.phone_edit.toPlainText().strip()
        # date_input = self._appointment.add_address_edit.toPlainText().strip()
        # time_input = self._appointment.add_age_edit.toPlainText().strip()
        dentist_input = self._appointment.add_pat_id_edit.toPlainText().strip()

        if not vname_input or not phone_input or len(phone_input) != 11:
            if not vname_input:
                self.show_error_window("You Must Enter Visitor Name")
                print("You Must Enter Visitor Name")
            elif not phone_input:
                self.show_error_window("You Must Enter Visitor Phone number")
                print("You Must Enter Visitor Phone number")
            elif len(phone_input) != 11:
                self.show_error_window("You Must Enter a valid Phone Number")
                print("You Must Enter a valid Phone Number")

            print("Missing Information")

        else:
            pass

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
        self._patients.appointment_btn.clicked.connect(self._go_appointment)
        self._patients.dentist_btn.clicked.connect(self.get_dentist)

    def show_error_window(self, message):
        error_window = error._error_window(message)  # Adjusted to use the error module
        error_window.exec_()

    def makemegotopat(self):  # for  patient details

        f_name = self._patients.fname_srch_edit.toPlainText()
        l_name = self._patients.lname_srch_edit.toPlainText()
        phone = self._patients.phone_srch_edit.toPlainText()
        patient_id = self._patients.patid_srch_edit.toPlainText()

        if patient_id:

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

        elif f_name and phone:
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
        self._add_pat.next_btn.clicked.connect(self.checkvalid)
        self._add_pat.return_btn.clicked.connect(self._go_patient_window)
        self._add_pat.payment_btn.clicked.connect(self._go_make_payment)
        self._add_pat.expense_btn.clicked.connect(self._go_spend_money)
        self._add_pat.appointment_btn.clicked.connect(self._go_appointment)
        self._add_pat.dentist_btn.clicked.connect(self.get_dentist)

    def checkvalid(self):
        # CHECK
        f_name_input = self._add_pat.add_fname_edit.toPlainText().strip()
        l_name_input = self._add_pat.add_lname_edit.toPlainText().strip()
        phone_input = self._add_pat.add_phn_edit.toPlainText().strip()
        # address_input = self._add_pat.add_address_edit.toPlainText().strip()
        age_input = self._add_pat.add_age_edit.toPlainText().strip()
        pat_id_input = self._add_pat.add_pat_id_edit.toPlainText().strip()

        if (
            not f_name_input
            or not l_name_input
            or not phone_input
            # or not address_input
            or not age_input
            or not pat_id_input
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
            # elif not address_input:
            #     self.show_error_window("You Must Enter Address")
            #     print("You Must Enter Address")
            elif not age_input:
                self.show_error_window("You Must Enter Age")
                print("You Must Enter Age")
            elif not pat_id_input:
                self.show_error_window("You Must Enter a new valid Patient ID")
                print("You Must Enter Pat ID")

            print("Missing Information")

        else:
            conn = sqlite3.connect("medico.db3")
            c = conn.cursor()
            # Search for the patient using first name , phone number
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

    def convert_date_format(self, date_str):
        # Use regex to match yyyy-mm-dd format
        match = re.match(r"(\d{4})-(\d{2})-(\d{2})", date_str)
        if match:
            year, month, day = match.groups()
            return f"{day}-{month}-{year}"
        else:
            return "Invalid date format"

    def _go_med_hist(self):  # inserting to DB

        # if self._add_pat.date_edit.setVisible(True):

        #     print("yes visible")
        #     date = self._add_pat.date_edit.date().toPyDate()
        #     date_of_departure = self.convert_date_format(str(date))

        # else:
        #     print("not visible")
        #     # self._add_pat.date_edit.setVisible(False)
        #     date_of_departure = ""
        # Retrieve patient data from _add_patient_window instance
        f_name = self._add_pat.add_fname_edit.toPlainText()
        l_name = self._add_pat.add_lname_edit.toPlainText()
        phone = self._add_pat.add_phn_edit.toPlainText()
        address = self._add_pat.address_combo.currentText()
        occupation = self._add_pat.add_occu_edit.toPlainText()
        email = self._add_pat.add_email_edit.toPlainText()
        age = self._add_pat.add_age_edit.toPlainText()
        sex = self._add_pat.add_sex_edit.currentText()
        reference = self._add_pat.add_ref_edit.toPlainText()
        date_of_departure = self._add_pat.add_depart_edit.toPlainText()
        chief_complain = self._add_pat.add_complain_edit.toPlainText()
        pat_id = self._add_pat.add_pat_id_edit.toPlainText()

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
            pat_id,
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
        self._med_hist.appointment_btn.clicked.connect(self._go_appointment)
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
        self._details.appointment_btn.clicked.connect(self._go_appointment)
        self._details.dentist_btn.clicked.connect(self.get_dentist)
        self._details.delete_pat.clicked.connect(self._confirm_delete)
        self._details.new_file_btn.clicked.connect(self._new_patient_file)
        self._details.updt_file_btn.clicked.connect(self._update_existing_file)
        self._details.customize_btn.clicked.connect(self.pat_custom1)
        self._details.pay_hist_btn.clicked.connect(self.grab_pay_hist)
        self._details.files_hist_btn.clicked.connect(self.grab_file_hist)

    def grab_file_hist(self):
        patient_id = self._patients.patid_srch_edit.toPlainText()

        self._view_file_window = view_files._files_view_window(patient_id)
        widget.addWidget(self._view_file_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        self._view_file_window.dash_btn.clicked.connect(self._go_dash)
        self._view_file_window.patient_btn.clicked.connect(self._go_patient_window)
        # self._view_file_window.file_btn.clicked.connect(self._go_make_file)
        self._view_file_window.expense_btn.clicked.connect(self._go_spend_money)
        # self._view_file_window.calendar.clicked.connect(self.grab_expense)
        self._view_file_window.appointment_btn.clicked.connect(self._go_appointment)
        self._view_file_window.return_btn.clicked.connect(self._go_pat_det)
        self._view_file_window.dentist_btn.clicked.connect(self.get_dentist)
        # self._view_file_window.print_btn.clicked.connect(self.print_pat_pay_hist)

    def grab_pay_hist(self):
        patient_id = self._patients.patid_srch_edit.toPlainText()

        self._view_payment_window = view_payments._payments_view_window(patient_id)
        widget.addWidget(self._view_payment_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        self._view_payment_window.dash_btn.clicked.connect(self._go_dash)
        self._view_payment_window.patient_btn.clicked.connect(self._go_patient_window)
        self._view_payment_window.payment_btn.clicked.connect(self._go_make_payment)
        self._view_payment_window.expense_btn.clicked.connect(self._go_spend_money)
        # self._view_payment_window.calendar.clicked.connect(self.grab_expense)
        self._view_payment_window.appointment_btn.clicked.connect(self._go_appointment)
        self._view_payment_window.return_btn.clicked.connect(self._go_pat_det)
        self._view_payment_window.dentist_btn.clicked.connect(self.get_dentist)
        self._view_payment_window.print_btn.clicked.connect(self.print_pat_pay_hist)

    def print_pat_pay_hist(self):
        patient_id = self._patients.patid_srch_edit.toPlainText()
        _query = "SELECT payment_date,file_name,payment_amount,due, payment_remarks FROM payment_history WHERE p_id = ? "
        suffix = "_Payments "
        file_location = "Payments_PDF/"
        pdf = pdf_maker.pdf_maker_pat_id(_query, suffix, file_location, patient_id)
        pdf

    def pat_custom1(self):
        f_name = self._patients.fname_srch_edit.toPlainText()
        l_name = self._patients.lname_srch_edit.toPlainText()
        phone = self._patients.phone_srch_edit.toPlainText()
        patient_id = self._patients.patid_srch_edit.toPlainText()
        self.pat_cus1 = patient_edit01.pat_edit1(f_name, l_name, phone, patient_id)
        widget.addWidget(self.pat_cus1)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        self.pat_cus1.return_btn.clicked.connect(self._go_pat_det)
        self.pat_cus1.next_btn.clicked.connect(self.pat_custom2)

    def pat_custom2(self):
        f_name = self.pat_cus1.add_fname_edit.toPlainText()
        l_name = self.pat_cus1.add_lname_edit.toPlainText()
        phone = self.pat_cus1.add_phn_edit.toPlainText()
        address = self.pat_cus1.address_combo.currentText()
        occupation = self.pat_cus1.add_occu_edit.toPlainText()
        email = self.pat_cus1.add_email_edit.toPlainText()
        age = self.pat_cus1.add_age_edit.toPlainText()

        reference = self.pat_cus1.add_ref_edit.toPlainText()
        date_of_departure = self.pat_cus1.add_depart_edit.toPlainText()
        chief_complain = self.pat_cus1.add_complain_edit.toPlainText()
        pat_id = self._patients.patid_srch_edit.toPlainText()
        self._med_hist = patient_edit02.pat_edit2(
            f_name,
            l_name,
            phone,
            address,
            occupation,
            email,
            age,
            pat_id,
            reference,
            date_of_departure,
            chief_complain,
        )
        widget.addWidget(self._med_hist)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        self._med_hist.return_btn.clicked.connect(self.pat_custom1)
        self._med_hist.patient_btn.clicked.connect(self._go_patient_window)
        self._med_hist.save_pat.clicked.connect(self._go_patient_window)
        self._med_hist.payment_btn.clicked.connect(self._go_make_payment)
        self._med_hist.expense_btn.clicked.connect(self._go_spend_money)
        self._med_hist.appointment_btn.clicked.connect(self._go_appointment)
        self._med_hist.dentist_btn.clicked.connect(self.get_dentist)

    def _update_existing_file(self):
        self.patient_id = self._patients.patid_srch_edit.toPlainText()
        self.updatefile_popup = files_updt._updt_file_window(
            self.patient_id, self._call_back_go_pat_det_fnc
        )
        self.updatefile_popup.show()

    def _new_patient_file(self):
        self.patient_id = self._patients.patid_srch_edit.toPlainText()
        self.addfile_popup = files_add._add_file_window(
            self.patient_id, self._call_back_go_pat_det_fnc
        )
        self.addfile_popup.show()

    def _call_back_go_pat_det_fnc(self):
        self._go_pat_det()

    def _confirm_delete(self):
        f_name = self._details.updt_f_name.text()
        l_name = self._details.updt_l_name.text()
        phone = self._details.updt_phn.text()
        print(f"f_name = {f_name} l_name = {l_name} phone = {phone}")
        self.show_warning_window(f_name, l_name, phone)

    def show_warning_window(self, f_name, l_name, phone):
        self.f_name = f_name
        self.l_name = l_name
        self.phone = phone
        self.warning_window = confirm_delete._warning_window(
            f_name, l_name, phone, self.pat_dlt_callback_fnc
        )

        self.warning_window.show()

    def pat_dlt_callback_fnc(self):
        self._go_patient_window()

    def _go_appointment_callback_fnc(self):
        self._go_appointment()

    def _call_back_go_make_payment(self):
        self._go_make_payment()

    def _go_make_payment(self):
        self._make_payment = payments_window._payments_window(
            self._call_back_go_make_payment
        )
        widget.addWidget(self._make_payment)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        self._make_payment.dash_btn.clicked.connect(self._go_dash)
        self._make_payment.patient_btn.clicked.connect(self._go_patient_window)
        self._make_payment.expense_btn.clicked.connect(self._go_spend_money)
        self._make_payment.appointment_btn.clicked.connect(self._go_appointment)
        self._make_payment.dentist_btn.clicked.connect(self.get_dentist)

    """ 

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
            try:
                amount = int(amount)
            except Exception as e:
                print("Enter Valid Amount")
                return
        else:
            # Handle the case where the patient is not found
            print("Patient not found.")
            return

        # Retrieve the last payment_id
        cursor.execute("SELECT MAX(CAST(payment_id AS INTEGER)) FROM payment_history")
        result = cursor.fetchone()
        print(f"paymentresult = {result}")
        if result[0] is not None:
            last_payment_id = result[0]
            print(f"last payment id: {last_payment_id}")
        else:
            last_payment_id = 0
            print(f"last payment id: {last_payment_id}")

        # Increment the last_payment_id
        payment_id = last_payment_id + 1
        print(f"payment id: {payment_id}")

        # Get the current date
        payment_date = QDate.currentDate().toString(
            "yyyy-MM-dd"
        )  # You need to implement this function

        # Insert the payment record into the payment_history table
        cursor.execute(
            "INSERT INTO payment_history (payment_id, p_id, payment_date, payment_amount, payment_remarks) VALUES (?, ?, ?, ?, ?)",
            (payment_id, p_id, payment_date, amount, remarks),
        )

        # Commit the transaction
        conn.commit()

        print("Payment record inserted successfully.")
        self._go_make_payment()
        
     """

    def expense_back(self):
        self._go_spend_money()

    def _go_spend_money(self):
        self._spend_money = expense_window._expense_window(self.expense_back)
        widget.addWidget(self._spend_money)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        self._spend_money.dash_btn.clicked.connect(self._go_dash)
        self._spend_money.patient_btn.clicked.connect(self._go_patient_window)
        self._spend_money.payment_btn.clicked.connect(self._go_make_payment)
        self._spend_money.expense_btn.clicked.connect(self._go_spend_money)
        self._spend_money.calendar.clicked.connect(self.grab_expense)
        self._spend_money.appointment_btn.clicked.connect(self._go_appointment)
        self._spend_money.dentist_btn.clicked.connect(self.get_dentist)

    def grab_expense(self):
        dateSelected = self._spend_money.calendar.selectedDate().toString("dd-MM-yyyy")
        print(dateSelected)
        expense_date = dateSelected
        self._view_expense_window = view_expense._expense_view_window(expense_date)
        widget.addWidget(self._view_expense_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        self._view_expense_window.dash_btn.clicked.connect(self._go_dash)
        self._view_expense_window.patient_btn.clicked.connect(self._go_patient_window)
        self._view_expense_window.payment_btn.clicked.connect(self._go_make_payment)
        self._view_expense_window.expense_btn.clicked.connect(self._go_spend_money)
        # self._view_expense_window.calendar.clicked.connect(self.grab_expense)
        self._view_expense_window.appointment_btn.clicked.connect(self._go_appointment)
        self._view_expense_window.return_btn.clicked.connect(self._go_spend_money)
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
        self.dentist_tab.appointment_btn.clicked.connect(self._go_appointment)
        self.dentist_tab.add_dentist_btn.clicked.connect(self.add_new_dentist)

    def add_new_dentist(self):
        self.new_dentist_tab = new_dentist.new_dentist_window()
        widget.addWidget(self.new_dentist_tab)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        self.new_dentist_tab.dash_btn.clicked.connect(self._go_dash)
        self.new_dentist_tab.patient_btn.clicked.connect(self._go_patient_window)
        self.new_dentist_tab.payment_btn.clicked.connect(self._go_make_payment)
        self.new_dentist_tab.expense_btn.clicked.connect(self._go_spend_money)
        self.new_dentist_tab.appointment_btn.clicked.connect(self._go_appointment)
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


widget.setFixedWidth(1280)
widget.setFixedHeight(680)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")
