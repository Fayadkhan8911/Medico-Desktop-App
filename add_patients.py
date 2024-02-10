""" import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget
from PyQt5.QtGui import QPixmap

import sqlite3


class _add_patient_window(QDialog):
    def __init__(self):
        super(_add_patient_window, self).__init__()
        loadUi("add_patients_window.ui", self)


 """


import sys
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog, QApplication
from add_pat_med import _add_med_hist_win  # Importing the medical history window
from PyQt5.QtWidgets import QDialog, QApplication, QStackedWidget  # Import QStackedWidget

# Assuming 'widget' is an instance of QStackedWidget


class _add_patient_window(QDialog):
    def __init__(self):
        super(_add_patient_window, self).__init__()
        loadUi("add_patients_window.ui", self)
        self.next_btn.clicked.connect(self.proceed_to_medical_history)



    def proceed_to_medical_history(self):
        # Retrieve patient data
        f_name = self.add_fname_edit.toPlainText()  # Change text() to toPlainText()
        l_name = self.add_lname_edit.toPlainText()
        phone = self.add_phn_edit.toPlainText()
        address = self.add_address_edit.toPlainText()
        occupation = self.add_occu_edit.toPlainText()
        email = self.add_email_edit.toPlainText()
        age = self.add_age_edit.toPlainText()
        sex = self.add_sex_edit.currentText()
        reference = self.add_ref_edit.toPlainText()
        date_of_departure = self.add_depart_edit.toPlainText()
        chief_complain = self.add_complain_edit.toPlainText()

        # Open the medical history window after saving patient data
        self.medical_history_window = _add_med_hist_win(
            f_name, l_name, phone, address, occupation, email, age, sex, reference, date_of_departure, chief_complain
        )
        #self.medical_history_window.exec_()
        widget = QStackedWidget()
        widget.addWidget(self.medical_history_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        
        
    
""" 
if __name__ == "__main__":
    app = QApplication(sys.argv)
    add_patient_window = _add_patient_window()  # Correct instantiation
    add_patient_window.show()
    sys.exit(app.exec_())
 """

"""
app = QApplication(sys.argv)

widget = QtWidgets.QStackedWidget()
_patient = _add_patient_window()

widget.addWidget(_patient)


widget.setFixedWidth(800)
widget.setFixedHeight(600)
# widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")


#"""
