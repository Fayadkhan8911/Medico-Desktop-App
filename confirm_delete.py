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
from confirm_delete_ui import Ui_Dialog

class _warning_window(QDialog, Ui_Dialog):
    def __init__(self, f_name, l_name, phone, dlt_callback_function):
        super(_warning_window, self).__init__()
        self.setupUi(self)
        self.f_name = f_name
        self.l_name = l_name
        self.phone = phone
        
        self.dlt_callback_function = dlt_callback_function  # Store the callback function
        self.cnf_no_btn.clicked.connect(self.close_warning)
        self.cnf_yes_btn.clicked.connect(self.delete_patient)

    
    
    def close_warning(self):
        print("Why close me?")
        self.close()
        
        
    def delete_patient(self):
        print(f"f_name = {self.f_name} l_name = {self.l_name} phone = {self.phone}")
        
        def update_countdown():
            nonlocal count
            if count > 0:
                self.warning_label.setText(f"Entry deleted successfully.\nThe window will close in {count} seconds")
                count -= 1
            else:
                timer.stop()  # Stop the timer when countdown reaches 0
                self.close()  # Close the window
                self.dlt_callback_function()
                
                
                
        
        try:
            conn = sqlite3.connect("MEDICO.db3")
            cursor = conn.cursor()

            cursor.execute(
                "DELETE FROM patients WHERE f_name = ? AND phone = ?", (self.f_name, self.phone)
            )
            conn.commit()

            count = 3
            timer = QTimer(self)
            timer.timeout.connect(update_countdown)
            timer.start(1000)  # Start timer with 1-second interval

        #except sqlite3.Error as e:
        #    self.warning_label.setText(f"There has been an error: {e}")
        #    print(f"There has been an error: {e}")
            
        except Exception as e:
            self.warning_label.setText(f"There has been an error: {e}")
            print(f"There has been an error: {e}")

        finally:
            if conn:
                conn.close()
        




"""
app = QApplication(sys.argv)

widget = QtWidgets.QStackedWidget()
_patient = _warning_window()

widget.addWidget(_patient)


widget.setFixedWidth(550)
widget.setFixedHeight(250)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")
# """
