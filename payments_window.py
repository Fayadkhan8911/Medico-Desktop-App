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
        #kaj sheshe use self._call_back_go_make_payment()
        self.makepayment_btn.clicked.connect(self.createpayment)


    def createpayment(self):
        self.f_name = self.fname_srch_edit.toPlainText()
        self.phone = self.phone_srch_edit.toPlainText()
        self.amount = self.payment_edit.toPlainText()
        self.remarks = self.remarks_edit.toPlainText()
        self.patient_id = self.patid_srch_edit.toPlainText()
        
        if(self.patient_id != ''):
            self.pay_with_patient_id()
            
        elif(self.f_name != '' and self.phone != ''):
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
            "SELECT f_name FROM patients WHERE p_id = ?", (self.patient_id,)
        )
        result = cursor.fetchone()
        if result:
            f_name = result[0]
            print(f_name)
            try:
                amount = int(amount)
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
        
        cursor.execute(
            
        )

        # Insert the payment record into the payment_history table
        cursor.execute(
            "INSERT INTO payment_history (payment_id, p_id, payment_date, payment_amount, payment_remarks) VALUES (?, ?, ?, ?, ?)",
            (payment_id, self.patient_id, payment_date, amount, self.remarks),
        )

        # Commit the transaction
        conn.commit()

        print("Payment record inserted successfully.")
        self._call_back_go_make_payment()
            
    def pay_with_name_and_phone(self):
        print()
    
        
    def show_error_window(self, message):
        error_window = value_error._error_window(message)  # Adjusted to use the error module
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
