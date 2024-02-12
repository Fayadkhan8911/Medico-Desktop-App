import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QMainWindow,
    QPushButton,
    QMessageBox,
    QVBoxLayout,
    QSizePolicy,
    QTableWidget,
)

import sqlite3


class _expense_view_window(QDialog):
    def __init__(self, expense_date):
        super(_expense_view_window, self).__init__()
        loadUi("view_expense.ui", self)
        self.expense_date = expense_date
        self._view_expense_table()
        
        
    def _view_expense_table(self):
        expense_date = self.expense_date
        conn = sqlite3.connect("medico.db3")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM expense WHERE expense_date = ?", (expense_date,))
        # Fetch all rows
        results = cursor.fetchall()

        # Print the results
        for row in results:
            print(row)
        conn.close()
        
        print("Expense Showed")
        self.expenseTable.setColumnWidth(0, 120)  # Expense Date
        self.expenseTable.setColumnWidth(1, 140)  # Expense Amount
        self.expenseTable.setColumnWidth(2, 180)  # Expense Description
        self.expenseTable.setColumnWidth(3, 180)  # Expense Remarks
        
        tablerow=0
        for row in results:
            self.expenseTable.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.expenseTable.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.expenseTable.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))
            tablerow+=1



"""
app = QApplication(sys.argv)

widget = QtWidgets.QStackedWidget()
__view_window = _expense_view_window()

widget.addWidget(__view_window)


widget.setFixedWidth(800)
widget.setFixedHeight(600)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")
# """
