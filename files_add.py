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


class _add_file_window(QDialog):
    def __init__(self, patient_id, addfile_popup_callback_fnc):
        super(_add_file_window, self).__init__()
        loadUi("files_add.ui", self)
        self.patient_id = patient_id
        self.addfile_popup_callback_fnc = addfile_popup_callback_fnc
        #self.add_file_btn.clicked.connect(self.addfile_popup_callback_fnc)
        self.add_file_btn.clicked.connect(self.add_new_pat_file)
        self.cancel_btn.clicked.connect(self.cancel_new_pat_file)
        
    def add_new_pat_file(self):
        print(f"Patient ID = {self.patient_id}")
        
        file_name = self.fname_srch_edit.toPlainText()
        file_desc = self.file_desc_edit.toPlainText()
        estimated_cost = self.estd_cost_edit.toPlainText()
        discount = self.discount_edit.toPlainText()
        
        try:
            calc_estimated_cost = float(estimated_cost)
            calc_discount = float(discount)
            final_cost = calc_estimated_cost - calc_discount
        except Exception as e:
            print(f"Value error: {e}")
            error_msg = "Value error occured\nError: " + str(e)
            self.show_error_window(error_msg)
            return
        
        try:
            conn = sqlite3.connect("MEDICO.db3")
            cursor = conn.cursor()

            cursor.execute("""UPDATE patients SET file_name = ?, file_desc = ?, estd_cost = ?, discount = ?, final_cost = ? WHERE p_id = ?""", (file_name, file_desc, estimated_cost, discount, final_cost, self.patient_id))
            conn.commit()
            msg = "File added successfully.\nFile Name: " + str(file_name) + "\nEstimated Cost: " + str(calc_estimated_cost) + "\nDiscount: " + str(calc_discount) + " taka\nFinal Cost: " + str(final_cost)
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
        self.addfile_popup_callback_fnc()
        
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
