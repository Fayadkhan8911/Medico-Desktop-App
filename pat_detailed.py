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
                for row in result:
                    self.updt_pat_id.setText(str(result[0]))
                    self.updt_f_name.setText(str(result[1]))
                    self.updt_l_name.setText(str(result[2]))
                    self.updt_age.setText(str(result[3]))
                    self.updt_gender.setText(str(result[4]))
                    self.updt_phn.setText(str(result[5]))
                    self.updt_addr.setText(str(result[6]))
                    self.updt_email.setText(str(result[7]))
                    self.updt_reg_dt.setText(str(result[8]))
                    self.updt_depart.setText(str(result[9]))
                    self.updr_refr.setText(str(result[10]))
                    self.updt_comp.setText(str(result[11]))
                    self.updt_q1.setText(str(result[12]))
                    self.updt_q2.setText(str(result[13]))
                    self.updt_q3.setText(str(result[14]))
                    self.updt_q4.setText(str(result[15]))
                    self.updt_q5.setText(str(result[16]))
                    self.updt_q6.setText(str(result[17]))
                    self.updt_q7.setText(str(result[18]))
                    self.updt_q8.setText(str(result[19]))
                    self.updt_q9.setText(str(result[20]))
                    self.updt_q10.setText(str(result[21]))
                    self.updt_q11.setText(str(result[22]))
                    self.updt_q12.setText(str(result[23]))
                    self.updt_q13.setText(str(result[24]))
                    self.updt_q14.setText(str(result[25]))
                    self.updt_q15.setText(str(result[26]))
                    self.updt_q16.setText(str(result[27]))
                    self.updt_med_findings.setText(str(result[28]))
                    self.updt_occu.setText(str(result[29]))
                print(result)
            else:
                print("Patient not found")
        else:
            print("Please provide either first name and phone number or patient ID")
         
        # Close the connection
        conn.close()




        
"""         
        
        pat_patient_id = result[0]
        pat_first_name = result[1]
        pat_last_name = result[2]
        pat_age = result[3]
        pat_gender = result[4]
        pat_phone = result[5]
        pat_address = result[6]
        pat_email = result[7]
        pat_reg_date = result[8]
        pat_date_of_depart = result[9]
        pat_reference = result[10]
        pat_complain = result[11]
        pat_blood_diseases = result[12]
        pat_smoker = result[13]
        pat_bleeding_disorder = result[14]
        pat_hepatitis = result[15]
        pat_diabetes = result[16]
        pat_epilepsy = result[17]
        pat_kidney_cardiac_diseases = result[18]
        pat_abnormal_bp = result[19]
        pat_currently_medicated = result[20]
        pat_respiratory_diseases = result[21]
        pat_gum_bleed_brush = result[22]
        pat_allergies = result[23]
        pat_nervous = result[24]
        pat_pregnant = result[25]
        pat_breast_feeding = result[26]
        pat_none_prb_above = result[27]
        pat_med_find = result[28]
        
 """
        
        
    
    
    
    
    
    
    

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
