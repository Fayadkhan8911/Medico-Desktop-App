import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QCalendarWidget

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


class _payment_view_window(QDialog):
    def __init__(self, payment_date):
        super(_payment_view_window, self).__init__()
        loadUi("view_payment.ui", self)
        self.payment_date = payment_date
        self._view_payment_table()
        self.calendar = self.findChild(QCalendarWidget, "calendarWidget")

    def _view_payment_table(self):
        payment_date = self.payment_date
        print(payment_date)
        conn = sqlite3.connect("medico.db3")
        cursor = conn.cursor()
        cursor.execute("SELECT payment_date, p_id, file_name, payment_amount, due FROM payment_history WHERE payment_date = ?", (payment_date,))
        # Fetch all rows
        results = cursor.fetchall()
        

        # Print the results
        for row in results:
            print(row)
        conn.close()
        # Clear existing rows
        self.paymentTable.setRowCount(100)

        # Set number of rows in the table
        self.paymentTable.setRowCount(len(results))

        print("Payment of date Showed")
        # self.expenseTable.setColumnWidth(0, 120)  # Expense Date
        # self.expenseTable.setColumnWidth(1, 500)  # Expense Description
        # self.expenseTable.setColumnWidth(2, 200)  # Expense Remarks
        # self.expenseTable.setColumnWidth(3, 180)  # Expense Amount

        # Populate the table
        for row_index, row_data in enumerate(results):
            for col_index, data in enumerate(row_data):
                item = QtWidgets.QTableWidgetItem(str(data))
                self.paymentTable.setItem(row_index, col_index, item)

        self.paymentTable.resizeColumnsToContents()
        self.payment_title.setText(f"Payment History of Date: {payment_date}")


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
