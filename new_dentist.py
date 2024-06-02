import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QDate

import sqlite3
from new_dentist_ui import Ui_Dialog


class new_dentist_window(QDialog, Ui_Dialog):
    def __init__(self):
        super(new_dentist_window, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.attempt_add_dentist)
        
        
        
    def attempt_add_dentist(self):
        f_name = self.add_fname.toPlainText()
        l_name = self.add_lname.toPlainText()
        phone = self.add_phone.toPlainText()
        dob = self.add_dob.toPlainText()
        email = self.add_email.toPlainText()
        joindate = QDate.currentDate().toString("yyyy-MM-dd")
        
        conn = sqlite3.connect("medico.db3")
        cursor = conn.cursor()
        
        
        # Retrieve the last d_id
        cursor.execute("SELECT MAX(d_id) FROM dentists")
        result = cursor.fetchone()
        if result[0] is not None:
            last_d_id = result[0]
        else:
            last_d_id = 0

        # Increment the last_d_id
        new_d_id = last_d_id + 1

        # Insert the new record into the dentists table
        cursor.execute("INSERT INTO dentists (d_id, d_f_name, d_l_name, d_email, d_phone, d_dob, d_joindate, d_retiredate) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
            (new_d_id, f_name, l_name, email, phone, dob, joindate, ""))
        
    
        conn.commit()
        conn.close()
        print("Doctor Add Successful")
        





""" 

app = QApplication(sys.argv)

widget = QtWidgets.QStackedWidget()
_dentist = new_dentist_window()

widget.addWidget(_dentist)


widget.setFixedWidth(800)
widget.setFixedHeight(600)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")

 """