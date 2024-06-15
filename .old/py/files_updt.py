import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, QtCore
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


class _updt_file_window(QDialog):
    def __init__(self, patient_id, _call_back_go_pat_det_fnc):
        super(_updt_file_window, self).__init__()
        loadUi("gui/files_updt.ui", self)
        
        self.patient_id = patient_id
        self._call_back_go_pat_det_fnc = _call_back_go_pat_det_fnc
        
        self.estd_cost_edit.setTabChangesFocus(True)
        self.discount_edit.setTabChangesFocus(True)
        self.desc_edit.setTabChangesFocus(True)
        
        self.cancel_btn.clicked.connect(self.cancel_update_pat_file)
        
        self.updt_file_btn.clicked.connect(self.make_update_pat_file)
        
    
    def make_update_pat_file(self):
        print(self.patient_id)
        update_estd_cost = self.estd_cost_edit.toPlainText()
        update_discount = self.discount_edit.toPlainText()
        x=self.desc_edit.toPlainText()
        payment_remarks = ''
        
        current_date = QDate.currentDate()
        converted_current_date = current_date.toString("dd-MM-yyyy")
        # Convert to 'yyyy-MM-dd' format
        current_date = current_date.toString("yyyy-MM-dd")
        
        old_x = x
        old_update_estd_cost = update_estd_cost
        old_update_discount = update_discount
        
        file_hist_change_log = "\n\n" + converted_current_date + "\n"
        
        if(x != ''):
            update_desc= "\n"+"\n"+converted_current_date+"\n"+"\n"+x
        else:
            update_desc = x
        
        if(update_estd_cost != ''):
            payment_remarks = payment_remarks + "\nEstimated Cost Update"
            file_hist_change_log += "\nNew Estimated Cost: " + update_estd_cost
        if(update_discount != ''):
            payment_remarks = payment_remarks + "\nDiscount Update"
            file_hist_change_log += "\nNew Discount: " + update_discount
        if(x != ''):
            payment_remarks = payment_remarks + "\nFile Description Update"
            
        
        conn = sqlite3.connect("MEDICO.db3")
        cursor = conn.cursor()    
            
        cursor.execute("SELECT estd_cost, discount FROM patients WHERE p_id = ?", (self.patient_id,))
        result = cursor.fetchone()
        old_estd_cost = round(float(result[0]), 3)
        old_discount = round(float(result[1]), 3)
        
        
        if(update_estd_cost != ''):
            try:
                update_estd_cost = round(float(update_estd_cost), 3)
            except Exception as e:
                print(f"Value error: {e}")
                error_msg = "Value error occured\nError: " + str(e)
                self.show_error_window(error_msg)
                return
                #untested change
        else:
            update_estd_cost = old_estd_cost
            #logical error
            
        if(update_discount != ''):
            update_discount = round(float(update_discount), 3)
        else:
            update_discount = old_discount
            #logical error
        
        if(old_x == '' and old_update_discount == '' and old_update_estd_cost == ''):
            error_msg = "Nothing To Update.\nPlease Close Update Window or Enter Update Values"
            self.show_error_window(error_msg)
            return #untested change
            
            
        self.update_pat_file(update_estd_cost, update_discount, update_desc, payment_remarks, file_hist_change_log)
        
        
        
        
    def update_pat_file(self, update_estd_cost, update_discount, update_desc, payment_remarks, file_hist_change_log):
        
        #update_estd_cost, update_discount, update_desc
        
        try:
            conn = sqlite3.connect("MEDICO.db3")
            cursor = conn.cursor()
            
            
            cursor.execute("SELECT file_name, file_add_date, final_cost, previous_due, file_desc FROM patients WHERE p_id = ?", (self.patient_id,))
            result = cursor.fetchone()
            file_name = str(result[0])
            file_add_date = str(result[1])
            prev_final_cost = round(float(result[2]), 3)
            prev_due = round(float(result[3]), 3)
            file_desc = str(result[4])
            file_desc = file_desc + update_desc
            
            update_final_cost = update_estd_cost - update_discount + prev_due
            
            cost_difference = round(update_final_cost - prev_final_cost, 3)
            
            
            
            
            
            payment_date = QDate.currentDate().toString(
                "yyyy-MM-dd"
            )  # You need to implement this function
            
            
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
            
            
            
            cursor.execute("SELECT * FROM payment_history WHERE p_id = ? AND file_name = ? AND payment_date >= ? ORDER BY payment_date DESC, payment_id DESC", (self.patient_id, file_name, file_add_date))
            result = cursor.fetchone()
            print(f"result:\n{result}")
            
            prev_due = round(float(result[9]), 3)
            print(f"prev_due = {prev_due}")
            print("printed file name and patient id")
            final_due = round((prev_due + cost_difference), 3)
            
            
            
            cursor.execute("""UPDATE patients SET estd_cost = ?, discount = ?, final_cost = ?, file_desc=file_desc||? WHERE p_id = ?""", (update_estd_cost, update_discount, update_final_cost, update_desc, self.patient_id))
            conn.commit()
            
            print("Patient table update done")
            
            
            cursor.execute("""INSERT INTO payment_history (payment_id, p_id, payment_date, payment_amount, payment_remarks, file_name, estd_cost, discount, final_cost, due) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", (payment_id, self.patient_id, payment_date, "0", payment_remarks, file_name, update_estd_cost, update_discount, update_final_cost, final_due))
            conn.commit()
            
            print("payment_history update done")
            
            cursor.execute("""UPDATE files_hist SET file_desc=file_desc||?, estd_cost = ?, discount = ?, final_cost = ?, change_log = change_log||? WHERE patient_id = ? AND file_name = ?""", (update_desc, update_estd_cost, update_discount, update_final_cost, file_hist_change_log, self.patient_id, file_name))
            conn.commit()
            
            
            msg = "File updated successfully."
            # #"\nRemaining Due: " + str(final_due)
            if(update_estd_cost != 0):
                msg = msg + "\nEstimated Cost: " + str(update_estd_cost) + " taka"
            if(update_discount != 0):
                msg = msg + "\nDiscount: " + str(update_discount) + " taka"
            if(update_estd_cost != 0 or update_discount != 0):
                msg = msg + "\nFinal Cost: " + str(update_final_cost) + " taka" + "\nRemaining Due: " + str(final_due) + " taka"
            
                
            self.show_error_window(msg)
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

        
        
    def show_error_window(self, message):
        error_window = value_error._error_window(message)  # Adjusted to use the error module
        error_window.exec_()
    
    
    
    def cancel_update_pat_file(self):
        print("Update file cancelled")
        self.close()


"""
app = QApplication(sys.argv)

widget = QtWidgets.QStackedWidget()
_app = _updt_file_window()

widget.addWidget(_app)


widget.setFixedWidth(740)
widget.setFixedHeight(636)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")
# """