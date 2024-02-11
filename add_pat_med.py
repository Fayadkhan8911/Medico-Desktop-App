""" import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget
from PyQt5.QtGui import QPixmap

import sqlite3


class _add_med_hist_win(QDialog):
    def __init__(self):
        super(_add_med_hist_win, self).__init__()
        loadUi("add_patients_med_hist_window.ui", self)
 """


import sys
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog, QApplication
import sqlite3
from PyQt5.QtWidgets import QDialog, QApplication, QStackedWidget  # Import QStackedWidget
import _mysql_connector

class _add_med_hist_win(QDialog):
    def __init__(self, f_name, l_name, phone, address, occupation, email, age, sex, reference, date_of_departure, chief_complain):
        super(_add_med_hist_win, self).__init__()
        loadUi("add_patients_med_hist_window.ui", self)
        self.f_name = f_name
        self.l_name = l_name
        self.phone = phone
        self.address = address
        self.occupation = occupation
        self.email = email
        self.age = age
        self.sex = sex
        self.reference = reference
        self.date_of_departure = date_of_departure
        self.chief_complain = chief_complain

        self.save_pat.clicked.connect(self.save_medical_history)

    def save_medical_history(self):
        # Retrieve medical history data
        medical_history = self.med_find_edit.toPlainText()

        # Retrieve checkbox states
        checkbox_states = {
            "q1": self.q1_y_check.isChecked(),
            "q2": self.q2_y_check.isChecked(),
            "q3": self.q3_y_check.isChecked(),
            "q4": self.q4_y_check.isChecked(),
            "q5": self.q5_y_check.isChecked(),
            "q6": self.q6_y_check.isChecked(),
            "q7": self.q7_y_check.isChecked(),
            "q8": self.q8_y_check.isChecked(),
            "q9": self.q9_y_check.isChecked(),
            "q10": self.q10_y_check.isChecked(),
            "q11": self.q11_y_check.isChecked(),
            "q12": self.q12_y_check.isChecked(),
            "q13": self.q13_y_check.isChecked(),
            "q14": self.q14_y_check.isChecked(),
            "q15": self.q15_y_check.isChecked(),
            "q16": self.q16_y_check.isChecked(),
        }

        # Convert checkbox states to 'yes' or 'no'
        checkbox_values = {key: 'yes' if value else 'no' for key, value in checkbox_states.items()}

        # Insert patient data, medical history, and checkbox values into the database
        conn = sqlite3.connect("medico.db3")
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO patients (f_name, l_name, phone, address, email, age, sex, reference, date_of_departure, complain, med_find_, 
            blood_diseases, smoker, bleeding_disorder, hepatitis, diabetes, epilepsy, kidney_cardiac_diseases, abnormal_bp, currently_medicated, respiratory_diseases, gum_bleed_brush, nervous, allergies, pregnant, breastfeeding, none_prb_above, reg_date)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, DATE('now'))
        """, (
            self.f_name, self.l_name, self.phone, self.address, self.email, self.age, self.sex, self.reference, self.date_of_departure,
            self.chief_complain, medical_history, *checkbox_values.values()
        ))
        conn.commit()
        conn.close()
        print("Patient data and medical history saved successfully.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = _add_med_hist_win()
    window.show()
    sys.exit(app.exec_())





"""
app = QApplication(sys.argv)

widget = QtWidgets.QStackedWidget()
_patient = _add_med_hist_win()

widget.addWidget(_patient)


widget.setFixedWidth(800)
widget.setFixedHeight(600)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")
# """
