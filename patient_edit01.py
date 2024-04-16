import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QCalendarWidget
from PyQt5.QtCore import QDate
import sqlite3


class pat_edit1(QDialog):
    def __init__(self, fname=None, lname=None, phone=None, pat_id=None):
        super(pat_edit1, self).__init__()
        loadUi("patients_custom_01.ui", self)
        self.fname = fname
        self.lname = lname
        self.phone = phone
        self.pat_id = pat_id
        # self.search_patient()

        # Connect to the database
        conn = sqlite3.connect("medico.db3")
        c = conn.cursor()

        # Get the values from the text boxes
        first_name = self.fname
        last_name = self.lname
        phone_number = self.phone
        patient_id = self.pat_id

        # Build the SQL query based on the provided values
        if (first_name and phone_number) or patient_id:
            if first_name and phone_number:
                c.execute(
                    "SELECT * FROM patients WHERE f_name=? AND phone=?",
                    (first_name, phone_number),
                )
            elif patient_id:
                c.execute("SELECT * FROM patients WHERE p_id=?", (patient_id,))

            # Fetch the results
            result = c.fetchone()

            # Display the details of the found patient
            print("Patient Found:")
            for row in result:
                self.updt_pat_id.setText(str(result[0]))
                self.old_fname.setText(result[1])
                self.old_lname.setText(result[2])
                self.old_age.setText(result[3])
                self.gender.setText(result[4])
                self.old_phone.setText(result[5])
                self.old_address.setText(result[6])
                if result[7] is not None:
                    self.old_email.setText(result[7])
                self.reg_date.setText(result[8])
                if result[9] is not None:
                    self.old_depart.setText(result[9])
                if result[10] is not None:
                    self.old_ref.setText(result[10])
                if result[11] is not None:
                    self.old_comp.setText(result[11])

                # self.updt_q1.setText("  " +(result[12])
                # self.updt_q2.setText("  " +(result[13])
                # self.updt_q3.setText("  " +(result[14])
                # self.updt_q4.setText("  " +(result[15])
                # self.updt_q5.setText("  " +(result[16])
                # self.updt_q6.setText("  " +(result[17])
                # self.updt_q7.setText("  " +(result[18])
                # self.updt_q8.setText("  " +(result[19])
                # self.updt_q9.setText("  " +(result[20])
                # self.updt_q10.setText("  " +(result[21])
                # self.updt_q11.setText("  " +(result[22])
                # self.updt_q12.setText("  " +(result[23])
                # self.updt_q13.setText("  " +(result[24])
                # self.updt_q14.setText("  " +(result[25])
                # self.updt_q15.setText("  " +(result[26])
                # self.updt_q16.setText("  " +(result[27])
                # self.updt_med_findings.setText(" " +(result[28])

                if result[29] is not None:
                    self.old_job.setText(result[29])

                # if result[30] is not None:
                #     self.updt_file_name.setText(result[30])
                # if result[30] is None:
                #     self.updt_file_btn.setEnabled(False)

            print(result)

        # Close the connection
        conn.close()

    def proceed_to_medical_history(self):

        # Retrieve patient data
        f_name = self.add_fname_edit.toPlainText()  # Change text() to toPlainText()
        l_name = self.add_lname_edit.toPlainText()
        phone = self.add_phn_edit.toPlainText()
        occupation = self.add_occu_edit.toPlainText()
        email = self.add_email_edit.toPlainText()
        age = self.add_age_edit.toPlainText()
        sex = self.add_sex_edit.currentText()
        reference = self.add_ref_edit.toPlainText()
        date_of_departure = self.add_depart_edit.toPlainText()
        chief_complain = self.add_complain_edit.toPlainText()
        address = self.address_combo.currentText()


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
