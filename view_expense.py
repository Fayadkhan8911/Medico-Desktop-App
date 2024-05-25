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
        print(expense_date)
        conn = sqlite3.connect("medico.db3")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM expense WHERE expense_date = ?", (expense_date,))
        # Fetch all rows
        results = cursor.fetchall()

        # Print the results
        # for row in results:
        #     print(row)
        # conn.close()
        # Clear existing rows
        self.expenseTable.setRowCount(100)

        # Set number of rows in the table
        self.expenseTable.setRowCount(len(results))

        print("Expense Showed")
        # self.expenseTable.setColumnWidth(0, 120)  # Expense Date
        # self.expenseTable.setColumnWidth(1, 500)  # Expense Description
        # self.expenseTable.setColumnWidth(2, 200)  # Expense Remarks
        # self.expenseTable.setColumnWidth(3, 180)  # Expense Amount

        # Populate the table
        for row_index, row_data in enumerate(results):
            for col_index, data in enumerate(row_data):
                item = QtWidgets.QTableWidgetItem(str(data))
                self.expenseTable.setItem(row_index, col_index, item)

        self.expenseTable.resizeColumnsToContents()
        self.expenseTable.resizeRowsToContents()
        self.expense_title.setText(f"Expense History of Date: {expense_date}")


"""
app = QApplication(sys.argv)

widget = QtWidgets.QStackedWidget()
__view_window = _expense_view_window("2024-02-12")

widget.addWidget(__view_window)


widget.setFixedWidth(800)
widget.setFixedHeight(600)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")
# """
