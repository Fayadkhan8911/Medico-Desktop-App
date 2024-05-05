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


class _updt_file_window(QDialog):
    def __init__(self, patient_id, _call_back_go_pat_det_fnc):
        super(_updt_file_window, self).__init__()
        loadUi("files_updt.ui", self)
        
        self.patient_id = patient_id
        self._call_back_go_pat_det_fnc = _call_back_go_pat_det_fnc
        
        self.cancel_btn.clicked.connect(self.cancel_update_pat_file)
        
        self.updt_file_btn.clicked.connect(self.make_update_pat_file)
        
    
    def make_update_pat_file(self):
        print(self.patient_id)
        update_estd_cost = self.estd_cost_edit.toPlainText()
        update_discount = self.discount_edit.toPlainText()
        x=self.desc_edit.toPlainText()
        if(x != ''):
            current_date = QDate.currentDate()
            # Convert to 'yyyy-MM-dd' format
            current_date = current_date.toString("dd-MM-yyyy")
            self.desc= "\n"+"\n"+current_date+"\n"+"\n"+x
        else:
            self.desc = x
        
        if(update_estd_cost == '' and update_discount == '' and x == ''):
            error_msg = "Nothing to update"
            self.show_error_window(error_msg)
            return
        
        elif(update_estd_cost != '' and update_discount == ''):
            try:
                calc_estimated_cost = round(float(update_estd_cost), 3)
            except Exception as e:
                print(f"Value error: {e}")
                error_msg = "Value error occured\nError: " + str(e)
                self.show_error_window(error_msg)
                return
            self.update_estd_cost_only(calc_estimated_cost)
            
        elif(update_estd_cost == '' and update_discount != ''):
            try:
                calc_discount = round(float(update_discount), 3)
            except Exception as e:
                print(f"Value error: {e}")
                error_msg = "Value error occured\nError: " + str(e)
                self.show_error_window(error_msg)
                return
            self.update_discount_only(calc_discount)
            
        elif(update_estd_cost != '' and update_discount != ''):
            try:
                calc_estimated_cost = round(float(update_estd_cost), 3)
                calc_discount = round(float(update_discount), 3)
                final_cost = round((calc_estimated_cost - calc_discount), 3)
            except Exception as e:
                print(f"Value error: {e}")
                error_msg = "Value error occured\nError: " + str(e)
                self.show_error_window(error_msg)
                return
            self.update_both(calc_estimated_cost, calc_discount, final_cost)
        elif(x != ''):
            self.update_only_desc()
        
                
            
    def update_estd_cost_only(self, calc_estimated_cost):
            
        try:
            conn = sqlite3.connect("MEDICO.db3")
            cursor = conn.cursor()
            cursor.execute("SELECT discount, file_name, file_add_date FROM patients WHERE p_id = ?", (self.patient_id,))
            result = cursor.fetchone()
            fetched_disc = round(float(result[0]), 3)
            file_name = str(result[1])
            print(f"file_name = {file_name}")
            file_add_date = result[2]
            print(f"file_add_date = {file_add_date}")
            final_cost = round((calc_estimated_cost - fetched_disc), 3)
            cursor.execute("SELECT estd_cost FROM patients WHERE p_id = ?", (self.patient_id,))
            result = cursor.fetchone()
            fetched_estd_cost = round(float(result[0]), 3)
            #i have patient id = self.patient_id, estimated cost = calc_estimated_cost, final cost = final_cost
            #discount = fetched_disc, filename = file_name
            
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
            
            payment_date = QDate.currentDate().toString(
                "yyyy-MM-dd"
            )  # You need to implement this function
            
            estd_cost_change_amount = round((calc_estimated_cost - fetched_estd_cost), 3)
            print(f"cost changed: {estd_cost_change_amount}")
            
            cursor.execute("SELECT * FROM payment_history WHERE p_id = ? AND payment_date >= ? ORDER BY payment_date DESC, payment_id DESC", (self.patient_id, file_add_date))
            result = cursor.fetchone()
            print(f"result:\n{result}")
            
            prev_due = round(float(result[9]), 3)
            print(f"prev_due = {prev_due}")
            print("printed file name and patient id")
            final_due = round((prev_due + estd_cost_change_amount), 3)
            
            print(f"prvious due = {prev_due}\nEstimated Cost Change = {estd_cost_change_amount}\nFinal Due = {final_due}")
            
            cursor.execute("""UPDATE patients SET estd_cost = ?, final_cost = ?, file_desc=file_desc||? WHERE p_id = ?""", (calc_estimated_cost, final_cost, self.desc, self.patient_id))
            conn.commit()
            
            print("patients table update done")
            
            cursor.execute("""INSERT INTO payment_history (payment_id, p_id, payment_date, payment_amount, payment_remarks, file_name, estd_cost, discount, final_cost, due) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", (payment_id, self.patient_id, payment_date, "0", "Update file", file_name, calc_estimated_cost, fetched_disc, final_cost, final_due))
            conn.commit()
            
            print("payment_history update done")
            
            msg = "File updated successfully.\nUpdated Estimated Cost: " + str(calc_estimated_cost) + "\nFinal Cost: " + str(final_cost) + "\nRemaining Due: " + str(final_due)
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
        
        
        
    def update_discount_only(self, calc_discount):
        try:
            conn = sqlite3.connect("MEDICO.db3")
            cursor = conn.cursor()
            cursor.execute("SELECT estd_cost, discount, file_name, file_add_date FROM patients WHERE p_id = ?", (self.patient_id,))
            result = cursor.fetchone()
            initial_estd_cost = round(float(result[0]), 3)
            initial_discount = round(float(result[1]), 3)
            file_name = str(result[2])
            file_add_date = result[3]
            
            
            discount_change = round((calc_discount - initial_discount), 3)
            
            cursor.execute("SELECT * FROM payment_history WHERE p_id = ? AND payment_date >= ? ORDER BY payment_date DESC, payment_id DESC", (self.patient_id, file_add_date))
            result = cursor.fetchone()
            print(f"result:\n{result}")
            prev_due = float(result[9])
            print("prev due worked")
            new_due = round((prev_due - discount_change), 3)
            print("new due worked")
            
            cursor.execute("SELECT estd_cost FROM patients WHERE p_id = ?", (self.patient_id,))
            result = cursor.fetchone()
            print(f"result:\n{result}")
            fetched_estd_cost = float(result[0])
            print(f"fetched_estd_cost = {fetched_estd_cost}")
            final_cost = round((fetched_estd_cost - calc_discount), 3)
            print(f"final_cost = {final_cost}")
            cursor.execute("""UPDATE patients SET discount = ?, final_cost = ?, file_desc=file_desc||? WHERE p_id = ?""", (calc_discount, final_cost, self.desc, self.patient_id))
            conn.commit()
            
            print("File update in patient table done")
            
            
            #lets add transaction in payment_history
            #
            #
            #
            
            
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
            
            
            
            cursor.execute("""INSERT INTO payment_history (payment_id, p_id, payment_date, payment_amount, payment_remarks, file_name, estd_cost, discount, final_cost, due) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", (payment_id, self.patient_id, payment_date, "0", "Discount Change", file_name, initial_estd_cost, calc_discount, final_cost, new_due))
            conn.commit()
            
            print("payment_history update done")
            
            
            
            
            
            msg = "File updated successfully.\nDiscount: " + str(calc_discount) + " taka\nFinal Cost: " + str(final_cost) + "\nRemaining Due: " + str(new_due)
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
        
        
        
    def update_both(self, calc_estimated_cost, calc_discount, final_cost):
        try:
            conn = sqlite3.connect("MEDICO.db3")
            cursor = conn.cursor()
            
            #new estd cost = calc_estimated_cost
            #new discount = calc_discount
            #final cost = final_cost
            
            cursor.execute("SELECT estd_cost, discount, file_name, file_add_date FROM patients WHERE p_id = ?", (self.patient_id,))
            result = cursor.fetchone()
            initial_estd_cost = round(float(result[0]), 3)
            initial_discount = round(float(result[1]), 3)
            file_name = str(result[2])
            file_add_date = result[3]
            
            total_amount_change = round(((calc_estimated_cost - initial_estd_cost) - (calc_discount - initial_discount)),3)
            
            
            
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
            
            
            
            cursor.execute("SELECT * FROM payment_history WHERE p_id = ? AND payment_date >= ? ORDER BY payment_date DESC, payment_id DESC", (self.patient_id, file_add_date))
            result = cursor.fetchone()
            print(f"result:\n{result}")
            
            prev_due = round(float(result[9]), 3)
            print(f"prev_due = {prev_due}")
            print("printed file name and patient id")
            final_due = round((prev_due + total_amount_change), 3)
            
            
            
            cursor.execute("""UPDATE patients SET estd_cost = ?, discount = ?, final_cost = ?, file_desc=file_desc||? WHERE p_id = ?""", (calc_estimated_cost, calc_discount, final_cost, self.desc, self.patient_id))
            conn.commit()
            
            print("Patient table update done")
            
            
            cursor.execute("""INSERT INTO payment_history (payment_id, p_id, payment_date, payment_amount, payment_remarks, file_name, estd_cost, discount, final_cost, due) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", (payment_id, self.patient_id, payment_date, "0", "Estimated Cost and Discount Change", file_name, calc_estimated_cost, calc_discount, final_cost, final_due))
            conn.commit()
            
            print("payment_history update done")
            
            
            
            msg = "File updated successfully.\nEstimated Cost: " + str(calc_estimated_cost) + "\nDiscount: " + str(calc_discount) + " taka\nFinal Cost: " + str(final_cost) + "\nRemaining Due: " + str(final_due)
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
        
    def update_only_desc(self):
        try:
            patient_id = self.patient_id
            conn = sqlite3.connect("MEDICO.db3")
            cursor = conn.cursor()
            cursor.execute("""UPDATE patients SET file_desc=file_desc||? WHERE p_id = ?""", (self.desc, patient_id))
            conn.commit()
            print("Only Description Update")
            
            cursor.execute("SELECT file_desc FROM patients WHERE p_id = ?", (patient_id,))
            current_description = cursor.fetchone()
            current_description = str(current_description[0])
            msg = "File updated successfully.\nCurrent Description: \n" + current_description
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