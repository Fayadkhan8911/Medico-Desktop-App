import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QPushButton
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QDate

import sqlite3


class _pat_detailed_win(QDialog):
    def __init__(self, f_name=None, l_name=None, phone=None, patient_id=None):
        super(_pat_detailed_win, self).__init__()
        loadUi("gui/patients_window_detailed.ui", self)        
        self.f_name = f_name
        self.l_name = l_name
        self.phone = phone
        self.patient_id = patient_id
        self.search_patient()
        self.f_name_labl.setFocus()
        self.buttons = self.findChildren(QPushButton)
        for button in self.buttons:
            button.pressed.connect(self.on_button_pressed)
        
    def keyPressEvent(self, event):
        if event.modifiers() == Qt.ControlModifier and event.key() == Qt.Key_C:
            # Loop through the buttons to find the focused one
            for button in self.buttons:
                if button.hasFocus():
                    # Copy the button text to the clipboard
                    QApplication.clipboard().setText(button.text())
                    break  # Stop searching after finding the focused button
        else:
            # Pass the event to the base class for default handling
            super().keyPressEvent(event)
            
    def on_button_pressed(self):
        # Set the focus to the button that was pressed
        button = self.sender()
        if button:
            button.setFocus()




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
            
            reg_date = QDate.fromString(result[8], "yyyy-MM-dd").toString("dd-MM-yyyy")
            
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
                    if result[7] is not None:
                        self.updt_email.setText(str(result[7]))
                    self.updt_reg_dt.setText(reg_date)
                    if result[9] is not None:
                        self.updt_depart.setText(str(result[9]))
                    if result[10] is not None:
                        self.updt_refr.setText(str(result[10]))
                    if result[11] is not None:
                        self.updt_comp.setText(str(result[11]))
                    self.updt_q1.setText("  "+str(result[12]))
                    self.updt_q2.setText("  "+str(result[13]))
                    self.updt_q3.setText("  "+str(result[14]))
                    self.updt_q4.setText("  "+str(result[15]))
                    self.updt_q5.setText("  "+str(result[16]))
                    self.updt_q6.setText("  "+str(result[17]))
                    self.updt_q7.setText("  "+str(result[18]))
                    self.updt_q8.setText("  "+str(result[19]))
                    self.updt_q9.setText("  "+str(result[20]))
                    self.updt_q10.setText("  "+str(result[21]))
                    self.updt_q11.setText("  "+str(result[22]))
                    self.updt_q12.setText("  "+str(result[23]))
                    self.updt_q13.setText("  "+str(result[24]))
                    self.updt_q14.setText("  "+str(result[25]))
                    self.updt_q15.setText("  "+str(result[26]))
                    self.updt_q16.setText("  "+str(result[27]))
                    self.updt_med_findings.setText(" "+str(result[28]))
                    if result[29] is not None:
                        self.updt_occu.setText(str(result[29]))
                    if result[30] is not None:
                        self.updt_file_name.setText(str(result[30]))
                    if result[30] is None:
                        self.updt_file_btn.setEnabled(False)
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
