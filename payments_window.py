import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QDate


import value_error

import sqlite3


class _payments_window(QDialog):
    def __init__(self, _call_back_go_make_payment):
        super(_payments_window, self).__init__()
        loadUi("payments_window.ui", self)
        self._call_back_go_make_payment = _call_back_go_make_payment
        # kaj sheshe use self._call_back_go_make_payment()
        self.makepayment_btn.clicked.connect(self.createpayment)

    def createpayment(self):
        self.f_name = self.fname_srch_edit.toPlainText()
        self.phone = self.phone_srch_edit.toPlainText()
        self.amount = self.payment_edit.toPlainText()
        self.remarks = self.remarks_edit.toPlainText()
        self.patient_id = self.patid_srch_edit.toPlainText()

        if self.patient_id != "":
            self.pay_with_patient_id()

        elif self.f_name != "" and self.phone != "":
            self.pay_with_name_and_phone()

        else:
            error_msg = "Please fill atleast one of the following:\n1. Patient ID\n2. Both First Name and Phone"
            self.show_error_window(error_msg)
            return

    def pay_with_patient_id(self):
        conn = sqlite3.connect("medico.db3")
        cursor = conn.cursor()
        # Retrieve the p_id using the provided first name and phone number
        cursor.execute(
            "SELECT f_name, l_name, file_add_date, file_name, estd_cost, discount, final_cost FROM patients WHERE p_id = ?",
            (self.patient_id,),
        )
        result = cursor.fetchone()
        if result:
            f_name = result[0]
            l_name = result[1]
            file_add_date = result[2]
            file_name = result[3]
            estimated_cost = result[4]
            discount = result[5]
            final_cost = result[6]
            print(f_name)

            cursor.execute(
                "SELECT * FROM payment_history WHERE p_id = ? AND payment_date >= ? ORDER BY payment_date DESC, payment_id DESC",
                (self.patient_id, file_add_date),
            )

            result = cursor.fetchone()
            print(f"result:\n{result}")
            prev_due = round(float(result[9]), 3)
            print(f"prev_due = {prev_due}")
            print("printed file name and patient id")

            error_msg = (
                "Patient Found:"
                + "\nPatient ID: "
                + str(self.patient_id)
                + "\nPatient Name: "
                + str(f_name)
                + " "
                + str(l_name)
                + "\nCurrent Due: "
                + str(prev_due)
            )
            self.show_error_window(error_msg)

            if prev_due <= 0.0:
                error_msg = "No Due Left!"
                self.show_error_window(error_msg)
                return

            try:
                self.amount = round(float(self.amount), 3)
            except Exception as e:
                error_msg = "Enter Valid Amount\nError: " + str(e)
                self.show_error_window(error_msg)
                return
        else:
            # Handle the case where the patient is not found
            error_msg = "Patient Not Found"
            self.show_error_window(error_msg)
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
            "dd-MM-yyyy"
        )  # You need to implement this function

        if self.remarks == "":
            error_msg = "Please Input Payment Remarks."
            self.show_error_window(error_msg)
            return

        current_due = round(float(prev_due - self.amount), 3)

        # Insert the payment record into the payment_history table
        cursor.execute(
            "INSERT INTO payment_history (payment_id, p_id, payment_date, payment_amount, payment_remarks, file_name, estd_cost, discount, final_cost, due) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (
                payment_id,
                self.patient_id,
                payment_date,
                self.amount,
                self.remarks,
                file_name,
                estimated_cost,
                discount,
                final_cost,
                current_due,
            ),
        )

        # Commit the transaction
        conn.commit()

        error_msg = (
            "Payment Record Insert Successfull.\n"
            + "Patient ID: "
            + str(self.patient_id)
            + "\nPatient Name: "
            + str(f_name)
            + " "
            + str(l_name)
            + "\nPrevious Due: "
            + str(prev_due)
            + "\nPayment Amount: "
            + str(self.amount)
            + "\nCurrent Due: "
            + str(current_due)
        )
        self.show_error_window(error_msg)

        print("Payment record inserted successfully.")
        self._call_back_go_make_payment()

    def pay_with_name_and_phone(self):
        conn = sqlite3.connect("medico.db3")
        cursor = conn.cursor()
        # Retrieve the p_id using the provided first name and phone number
        cursor.execute(
            "SELECT p_id, l_name, file_add_date, file_name, estd_cost, discount, final_cost FROM patients WHERE f_name = ? AND phone = ?",
            (self.f_name, self.phone),
        )
        result = cursor.fetchone()
        if result:
            f_name = self.f_name
            phone = self.phone
            patient_id = result[0]
            l_name = result[1]
            file_add_date = result[2]
            file_name = result[3]
            estimated_cost = result[4]
            discount = result[5]
            final_cost = result[6]
            print(patient_id)

            cursor.execute(
                "SELECT * FROM payment_history WHERE p_id = ? AND payment_date >= ? ORDER BY payment_date DESC, payment_id DESC",
                (patient_id, file_add_date),
            )

            result = cursor.fetchone()
            print(f"result:\n{result}")
            prev_due = round(float(result[9]), 3)
            print(f"prev_due = {prev_due}")
            print("printed file name and patient id")

            error_msg = (
                "Patient Found:"
                + "\nPatient ID: "
                + str(patient_id)
                + "\nPatient Name: "
                + str(f_name)
                + " "
                + str(l_name)
                + "\nCurrent Due: "
                + str(prev_due)
            )
            self.show_error_window(error_msg)

            if prev_due <= 0.0:
                error_msg = "No Due Left!"
                self.show_error_window(error_msg)
                return

            try:
                self.amount = round(float(self.amount), 3)
            except Exception as e:
                error_msg = "Enter Valid Amount\nError: " + str(e)
                self.show_error_window(error_msg)
                return
        else:
            # Handle the case where the patient is not found
            error_msg = "Patient Not Found"
            self.show_error_window(error_msg)
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

        if self.remarks == "":
            error_msg = "Please Input Payment Remarks."
            self.show_error_window(error_msg)
            return

        current_due = round(float(prev_due - self.amount), 3)

        # Insert the payment record into the payment_history table
        cursor.execute(
            "INSERT INTO payment_history (payment_id, p_id, payment_date, payment_amount, payment_remarks, file_name, estd_cost, discount, final_cost, due) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (
                payment_id,
                patient_id,
                payment_date,
                self.amount,
                self.remarks,
                file_name,
                estimated_cost,
                discount,
                final_cost,
                current_due,
            ),
        )

        # Commit the transaction
        conn.commit()

        error_msg = (
            "Payment Record Insert Successfull.\n"
            + "Patient ID: "
            + str(patient_id)
            + "\nPatient Name: "
            + str(f_name)
            + " "
            + str(l_name)
            + "\nPrevious Due: "
            + str(prev_due)
            + "\nPayment Amount: "
            + str(self.amount)
            + "\nCurrent Due: "
            + str(current_due)
        )
        self.show_error_window(error_msg)

        print("Payment record inserted successfully.")
        self._call_back_go_make_payment()

    def show_error_window(self, message):
        error_window = value_error._error_window(
            message
        )  # Adjusted to use the error module
        error_window.exec_()

        """ 

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
            self._call_back_go_make_payment()
        
        
         """


"""
app = QApplication(sys.argv)

widget = QtWidgets.QStackedWidget()
_payment = _payments_window()

widget.addWidget(_payment)


widget.setFixedWidth(800)
widget.setFixedHeight(600)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")
# """
