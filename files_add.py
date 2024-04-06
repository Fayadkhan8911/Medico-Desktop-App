import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer, QDate
from PyQt5.QtWidgets import QStackedWidget
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QMainWindow,
    QPushButton,
    QMessageBox,
    QVBoxLayout,
    QSizePolicy,
)

import sqlite3
import value_error


class _add_file_window(QDialog):
    def __init__(self, patient_id, _call_back_go_pat_det_fnc):
        super(_add_file_window, self).__init__()
        loadUi("files_add.ui", self)
        self.patient_id = patient_id
        self._call_back_go_pat_det_fnc = _call_back_go_pat_det_fnc
        #self.add_file_btn.clicked.connect(self.addfile_popup_callback_fnc)
        self.add_file_btn.clicked.connect(self.add_new_pat_file)
        self.cancel_btn.clicked.connect(self.cancel_new_pat_file)
        
    def add_new_pat_file(self):
        
        file_name = self.fname_srch_edit.toPlainText()
        file_desc = self.file_desc_edit.toPlainText()
        estimated_cost = self.estd_cost_edit.toPlainText()
        discount = self.discount_edit.toPlainText()
        
        if(discount != ''):
            discount = discount
        else:
            discount = 0.0
        
        file_add_date = QDate.currentDate().toString("yyyy-MM-dd")
        
        if(file_name == '' or file_desc == '' or estimated_cost == ''):
            error_msg = "Please Fill ALL of the Field Stated Below:\nFile Name\nFile Description\nEstimated Cost"
            self.show_error_window(error_msg)
            return
        
        try:
            calc_estimated_cost = round(float(estimated_cost), 3)
            calc_discount = round(float(discount), 3)
            final_cost = round((calc_estimated_cost - calc_discount), 3)
        except Exception as e:
            print(f"Value error: {e}")
            error_msg = "Value error occured\nError: " + str(e)
            self.show_error_window(error_msg)
            return
        
        try:
            conn = sqlite3.connect("MEDICO.db3")
            cursor = conn.cursor()

            cursor.execute("""UPDATE patients SET file_name = ?, file_desc = ?, estd_cost = ?, discount = ?, final_cost = ?, file_add_date = ? WHERE p_id = ?""", (file_name, file_desc, calc_estimated_cost, calc_discount, final_cost, file_add_date, self.patient_id))
            conn.commit()
            msg = "File added successfully.\nFile Name: " + str(file_name) + "\nEstimated Cost: " + str(calc_estimated_cost) + "\nDiscount: " + str(calc_discount) + " taka\nFinal Cost: " + str(final_cost) + "\nFile Add Date: " + file_add_date
            self.show_error_window(msg)
            
            #now add it in payment history
            
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
            
            cursor.execute("""INSERT INTO payment_history (payment_id, p_id, payment_date, payment_amount, payment_remarks, file_name, estd_cost, discount, final_cost, due) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",(payment_id, self.patient_id, file_add_date, "0", "New File Add", file_name, calc_estimated_cost, calc_discount, final_cost, final_cost))
            conn.commit()
            
            
            
        except Exception as e:
            print(f"There has been an error: {e}")
            msg = "An error occured: " + str(e)
            self.show_error_window(msg)
            return

        finally:
            if conn:
                conn.close()
        
        self.close()
        self._call_back_go_pat_det_fnc()
        
    def cancel_new_pat_file(self):
        print("Add file cancelled")
        self.close()
        
        
    def show_error_window(self, message):
        error_window = value_error._error_window(message)  # Adjusted to use the error module
        error_window.exec_()


"""
app = QApplication(sys.argv)

widget = QtWidgets.QStackedWidget()
_app = _add_file_window()

widget.addWidget(_app)


widget.setFixedWidth(740)
widget.setFixedHeight(636)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")
# """
