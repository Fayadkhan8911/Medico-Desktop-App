import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QCalendarWidget, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QDate

import sqlite3

import error_for_expense

import pytz
from PyQt5.QtCore import QTimeZone


class _expense_window(QDialog):
    def __init__(self):
        super(_expense_window, self).__init__()
        loadUi("expense_window.ui", self)
        
        self.calendar = self.findChild(QCalendarWidget, "calendarWidget")
        self.label = self.findChild(QLabel, "select_date")
        
        """ 
        timezone = pytz.timezone('Asia/Dhaka') 

        qt_timezone = QTimeZone(timezone.zone)

        self.calendar.setTimeZone(qt_timezone) 
         """
        
        self.add_expense_btn.clicked.connect(self._make_expense)
        
        self.calendar.selectionChanged.connect(self.grab_expense)
        
    def _make_expense(self):
        #medical_history = self.med_find_edit.toPlainText()
        expense_description = self.expense_desc_edit.toPlainText()
        expense_remarks = self.expense_remark_edit.toPlainText()
        expense_amount = self.expense_amount_edit.toPlainText()
        expense_date = QDate.currentDate().toString("yyyy-MM-dd")
        
        if expense_amount:
        
            try:
                expense_amount = int(expense_amount)
                # Now you can use expense_amount for calculations
                print("Expense amount:", expense_amount)
                if not expense_description:
                    self.show_error_window("Please fill in expense description.")
                    print("Must fill expense description")
                else:
                    conn = sqlite3.connect("medico.db3")
                    cursor = conn.cursor()
                    cursor.execute("INSERT INTO expense (expense_amount, expense_description, expense_remarks, expense_date) VALUES (?, ?, ?, ?)",
                      (expense_amount, expense_description, expense_remarks, expense_date))
                    conn.commit()
                    conn.close()
                    print("Expense Added")
                    
            except ValueError:
                self.show_error_window("Invalid Amount Input. Please Use Number Only.")
                print("Wrong Expense Amount Datatype")
                
        else:
            self.show_error_window("Amount Must Be Filled.")
            print("Amount Must Be Filled.")

        
        #self.show_error_window("No patient found with First Name and Phone Number.")
        
    
    def grab_expense(self):
        dateSelected = self.calendar.selectedDate()
        expense_date = str(dateSelected.toPyDate())
        conn = sqlite3.connect("medico.db3")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM expense WHERE expense_date = ?", (expense_date,))
        # Fetch all rows
        results = cursor.fetchall()

        # Print the results
        for row in results:
            print(row)
        conn.commit()
        conn.close()
        print("Expense Showed")

        
    def show_error_window(self, message):
        error_window = error_for_expense._error_window(message)  # Adjusted to use the error module
        error_window.exec_()


"""
app = QApplication(sys.argv)

widget = QtWidgets.QStackedWidget()
_expense = _expense_window()

widget.addWidget(_expense)


widget.setFixedWidth(800)
widget.setFixedHeight(600)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")
# """
