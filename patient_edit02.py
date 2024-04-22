import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QCalendarWidget
from PyQt5.QtCore import QDate
import sqlite3


class pat_edit2(QDialog):
    def __init__(
        self,
        f_name,
        l_name,
        phone,
        address,
        occupation,
        email,
        age,
        pat_id,
        reference,
        date_of_departure,
        chief_complain,
    ):
        super(pat_edit2, self).__init__()
        loadUi("patients_custom_02.ui", self)
        self.f_name = f_name
        self.l_name = l_name
        self.phone = phone
        self.address = address
        self.occupation = occupation
        self.email = email
        self.age = age

        self.reference = reference
        self.date_of_departure = date_of_departure
        comp = chief_complain
        self.chief_complain = "\n" + comp
        self.pat_id = pat_id

        self.new_info = [
            self.f_name,
            self.l_name,
            self.age,
            self.phone,
            self.address,
            self.email,
            self.date_of_departure,
            self.reference,
            self.chief_complain,
            self.occupation,
        ]
        # print(self.new_info)
        connect1 = sqlite3.connect("medico.db3")
        cur1 = connect1.cursor()
        cur1.execute("SELECT * FROM Patients WHERE p_id=?", (self.pat_id))
        _q = cur1.fetchone()

        self.old_info = [
            _q[1],
            _q[2],
            _q[3],
            _q[5],
            _q[6],
            _q[7],
            _q[9],
            _q[10],
            _q[11],
            _q[29],
        ]

        for i, F in enumerate(self.new_info):
            if F == "":
                self.new_info[i] = self.old_info[i]

        print(self.old_info)
        print(self.new_info)

        self.save_pat.clicked.connect(self.save_medical_history)

    def save_medical_history(self):
        # Retrieve medical history data
        medhist = self.med_find_edit.toPlainText()

        medical_history = "\n" + medhist
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
        # if self.f_name=='':
        #     cursor.execute("""SELECT * FROM patients WHERE p_id=? """,(self.pat_id))
        #     info=cursor.fetchone()
        #     self.f_name=info[1]

        # else:

        cursor.execute(
            """
        UPDATE patients SET f_name=?, l_name=?, phone=?, address=?, email=?, age=?, reference=?, date_of_departure=?, complain=complain||?, occupation=?, med_find_=med_find_ || ?, 
        blood_diseases=?, smoker=?, bleeding_disorder=?, hepatitis=?, diabetes=?, epilepsy=?, kidney_cardiac_diseases=?, abnormal_bp=?, currently_medicated=?, respiratory_diseases=?, gum_bleed_brush=?, allergies=?, nervous=?, pregnant=?, breastfeeding=?, none_prb_above=? WHERE p_id=?
        """,
            (
                self.new_info[0],
                self.new_info[1],
                self.new_info[3],
                self.new_info[4],
                self.new_info[5],
                self.new_info[2],
                self.new_info[7],
                self.new_info[6],
                self.new_info[8],
                self.new_info[9],
                medical_history,
                *checkbox_values.values(),
                self.pat_id,
            ),
        )
        conn.commit()
        conn.close()
        print("Patient data and medical history saved successfully.")


"""
app = QApplication(sys.argv)

widget = QtWidgets.QStackedWidget()
_patient = pat_edit1()

widget.addWidget(_patient)


widget.setFixedWidth(800)
widget.setFixedHeight(600)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")
# """
