import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget
from PyQt5.QtGui import QPixmap

import sqlite3


class _pat_detailed_win(QDialog):
    def __init__(self, f_name=None, l_name=None, phone=None, patient_id=None):
        super(_pat_detailed_win, self).__init__()
        loadUi("patients_window_detailed.ui", self)
        self.f_name = f_name
        self.l_name = l_name
        self.phone = phone
        self.patient_id = patient_id
        self.search_patient()



    def search_patient(self):
        # Connect to the database
        conn = sqlite3.connect('medico.db3')
        c = conn.cursor()
        
        # Get the values from the text boxes
        first_name = self.f_name
        last_name = self.l_name
        phone_number = self.phone
        patient_id = self.patient_id
        
        # Build the SQL query based on the provided values
        if (first_name and phone_number) or patient_id:
            if first_name and phone_number:
                c.execute("SELECT * FROM patients WHERE f_name=? AND phone=?", (first_name, phone_number))
            elif patient_id:
                c.execute("SELECT * FROM patients WHERE p_id=?", (patient_id,))
            
            # Fetch the results
            result = c.fetchone()
            
            
            
            if result:
                # Display the details of the found patient
                print("Patient Found:")
                print(result)
            else:
                print("Patient not found")
        else:
            print("Please provide either first name and phone number or patient ID")
        
        # Close the connection
        conn.close()

        
        
    
    
    
    
    
    
    

"""
app = QApplication(sys.argv)

widget = QtWidgets.QStackedWidget()
_patient = _pat_detailed_win()

widget.addWidget(_patient)


widget.setFixedWidth(800)
widget.setFixedHeight(600)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")
# """
