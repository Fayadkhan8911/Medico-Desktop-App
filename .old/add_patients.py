import sys
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtWidgets import (
    QDialog,
    QApplication,
    QStackedWidget,
)  # Import QStackedWidget
from add_pat_med import _add_med_hist_win


class _add_patient_window(QDialog):
    def __init__(self):
        super(_add_patient_window, self).__init__()
        loadUi("gui/add_patients_window.ui", self)
        
        self.add_fname_edit.setTabChangesFocus(True)
        self.add_lname_edit.setTabChangesFocus(True)
        self.add_occu_edit.setTabChangesFocus(True)
        self.add_ref_edit.setTabChangesFocus(True)
        self.add_phn_edit.setTabChangesFocus(True)
        self.add_email_edit.setTabChangesFocus(True)
        self.add_age_edit.setTabChangesFocus(True)
        self.add_pat_id_edit.setTabChangesFocus(True)
        self.add_depart_edit.setTabChangesFocus(True)
        self.add_complain_edit.setTabChangesFocus(True)
        
        self.patient_btn.setFocus()
        
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

        # self.next_btn.clicked.connect(self.checkifnull)

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
