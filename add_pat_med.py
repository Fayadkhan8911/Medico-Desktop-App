import sys
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog, QApplication
import sqlite3
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (
    QApplication,
    QDialog,
    QVBoxLayout,
    QPushButton,
    QStackedWidget,
    QLabel,
)
from PyQt5.QtCore import QDate
import requests


class _add_med_hist_win(QDialog):
    def __init__(
        self,
        f_name,
        l_name,
        phone,
        address,
        occupation,
        email,
        age,
        sex,
        pat_id,
        reference,
        date_of_departure,
        chief_complain,
    ):
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
        self.pat_id = pat_id

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
        checkbox_values = {
            key: "yes" if value else "no" for key, value in checkbox_states.items()
        }

        reg_date = QDate.currentDate().toString("yyyy-MM-dd")

        # Insert patient data, medical history, and checkbox values into the database
        conn = sqlite3.connect("medico.db3")
        cursor = conn.cursor()
        # Fetch the last patient ID
        # cursor.execute("SELECT MAX(p_id) FROM patients")
        # last_p_id = cursor.fetchone()[0]
        # if last_p_id is None:
        #     last_p_id = 0

        # # Increment the last patient ID
        # new_p_id = last_p_id + 1
        cursor.execute(
            """
            INSERT INTO patients (p_id, f_name, l_name, phone, address, email, age, sex, reference, date_of_departure, complain, occupation, med_find_, 
            blood_diseases, smoker, bleeding_disorder, hepatitis, diabetes, epilepsy, kidney_cardiac_diseases, abnormal_bp, currently_medicated, respiratory_diseases, gum_bleed_brush, allergies, nervous, pregnant, breastfeeding, none_prb_above, reg_date)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
            (
                self.pat_id,
                self.f_name,
                self.l_name,
                self.phone,
                self.address,
                self.email,
                self.age,
                self.sex,
                self.reference,
                self.date_of_departure,
                self.chief_complain,
                self.occupation,
                medical_history,
                *checkbox_values.values(),
                reg_date,
            ),
        )
        conn.commit()
        conn.close()
        print("Patient data and medical history saved successfully.")
        
        
        message = (
            "New Patient Added."
            + "\n"
            + "Registration Date: "
            + str(QDate.currentDate().toString("yyyy-MM-dd"))
            + "\n"
            + "Patient ID: "
            + self.pat_id
            + "\n"
            + "First Name: "
            + self.f_name
            + "\n"
            + "Last Name: "
            + self.l_name
            + "\n"
            + "Phone Number: "
            + str(self.phone)
            + "\n"
            + "Age: "
            + str(self.age)
            + "\n"
            + "Sex: "
            + self.sex
            + "\n"
            + "Address: "
            + self.address
            + "\n"
            + "Email: "
            + self.email
            + "\n"
            + "Departure Date: "
            + self.date_of_departure
            + "\n"
            + "Reference: "
            + self.reference
            + "\n"
            + "Complain "
            + self.chief_complain
            + "\n"
        )
        # # Send the message to your channel using the bot
        # url = f"https://api.telegram.org/bot6966315301:AAF79OPk17hjJ_dN75FOXnt_VmrFNePY7Hs/sendMessage"
        # params = {"chat_id": -1002137636697, "text": message}
        # response = requests.post(url, params=params)

        # # Check if the message was sent successfully
        # if response.status_code == 200:
        #     print("Message sent successfully!")
        # else:
        #     print(f"Failed to send message. Status code: {response.status_code}")
        #     print(response.text)  # Print the error response if any

        # Clear the variables
        self.f_name = ""
        self.l_name = ""
        self.phone = ""
        self.address = ""
        self.occupation = ""
        self.email = ""
        self.age = ""
        self.sex = ""
        self.reference = ""
        self.date_of_departure = ""
        self.chief_complain = ""

        # Clear input fields
        self.med_find_edit.clear()

        # Clear checkboxes
        self.q1_y_check.setChecked(False)
        self.q2_y_check.setChecked(False)
        self.q3_y_check.setChecked(False)
        self.q4_y_check.setChecked(False)
        self.q5_y_check.setChecked(False)
        self.q6_y_check.setChecked(False)
        self.q7_y_check.setChecked(False)
        self.q8_y_check.setChecked(False)
        self.q9_y_check.setChecked(False)
        self.q10_y_check.setChecked(False)
        self.q11_y_check.setChecked(False)
        self.q12_y_check.setChecked(False)
        self.q13_y_check.setChecked(False)
        self.q14_y_check.setChecked(False)
        self.q15_y_check.setChecked(False)
        self.q16_y_check.setChecked(False)


""" 
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = _add_med_hist_win()
    window.show()
    sys.exit(app.exec_())

 """


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
