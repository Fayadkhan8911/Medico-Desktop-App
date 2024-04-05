import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer
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
        
        if(update_estd_cost == '' and update_discount == ''):
            error_msg = "Nothing to update"
            self.show_error_window(error_msg)
            return
        
        elif(update_estd_cost != '' and update_discount == ''):
            try:
                calc_estimated_cost = float(update_estd_cost)
            except Exception as e:
                print(f"Value error: {e}")
                error_msg = "Value error occured\nError: " + str(e)
                self.show_error_window(error_msg)
                return
            self.update_estd_cost_only(calc_estimated_cost)
            
        elif(update_estd_cost == '' and update_discount != ''):
            try:
                calc_discount = float(update_discount)
            except Exception as e:
                print(f"Value error: {e}")
                error_msg = "Value error occured\nError: " + str(e)
                self.show_error_window(error_msg)
                return
            self.update_discount_only(calc_discount)
            
        elif(update_estd_cost != '' and update_discount != ''):
            try:
                calc_estimated_cost = float(update_estd_cost)
                calc_discount = float(update_discount)
                final_cost = calc_estimated_cost - calc_discount
            except Exception as e:
                print(f"Value error: {e}")
                error_msg = "Value error occured\nError: " + str(e)
                self.show_error_window(error_msg)
                return
            self.update_both(calc_estimated_cost, calc_discount, final_cost)
                
            
    def update_estd_cost_only(self, calc_estimated_cost):
            
        try:
            conn = sqlite3.connect("MEDICO.db3")
            cursor = conn.cursor()
            cursor.execute("SELECT discount FROM patients WHERE p_id = ?", (self.patient_id,))
            result = cursor.fetchone()
            fetched_disc = float(result[0])
            final_cost = calc_estimated_cost - fetched_disc
            cursor.execute("""UPDATE patients SET estd_cost = ?, final_cost = ? WHERE p_id = ?""", (calc_estimated_cost, final_cost, self.patient_id))
            conn.commit()
            msg = "File updated successfully.\nEstimated Cost: " + str(calc_estimated_cost) + "\nFinal Cost: " + str(final_cost)
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
            cursor.execute("SELECT estd_cost FROM patients WHERE p_id = ?", (self.patient_id,))
            result = cursor.fetchone()
            fetched_estd_cost = float(result[0])
            final_cost = fetched_estd_cost - calc_discount
            cursor.execute("""UPDATE patients SET discount = ?, final_cost = ? WHERE p_id = ?""", (calc_discount, final_cost, self.patient_id))
            conn.commit()
            msg = "File updated successfully.\nDiscount: " + str(calc_discount) + " taka\nFinal Cost: " + str(final_cost)
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
            cursor.execute("""UPDATE patients SET estd_cost = ?, discount = ?, final_cost = ? WHERE p_id = ?""", (calc_estimated_cost, calc_discount, final_cost, self.patient_id))
            conn.commit()
            msg = "File added successfully.\nEstimated Cost: " + str(calc_estimated_cost) + "\nDiscount: " + str(calc_discount) + " taka\nFinal Cost: " + str(final_cost)
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
