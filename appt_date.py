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


class apt_date(QDialog):
    def __init__(self, appt_date):
        super(apt_date, self).__init__()
        loadUi("appointment_date.ui", self)
        self.appt_date = appt_date
        self._view_appt_table()

    def _view_appt_table(self):
        appt_date = self.appt_date
        # print("testing appointment date", appt_date)
        print(type(appt_date))
        conn = sqlite3.connect("medico.db3")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM appointments WHERE visit_date = ?", (appt_date,))
        # Fetch all rows
        results = cursor.fetchall()
        
        if not results:
            self.print_btn.setEnabled(False)
            self.print_btn.setStyleSheet("""
                                        QPushButton {
                                            background-color: lightgray;
                                            font: 14pt "Segoe UI";
                                            color: gray;
                                            border-top-left-radius: 10px;
                                            border-bottom-left-radius: 10px;
                                            border-top-right-radius: 10px;
                                            border-bottom-right-radius: 10px;
                                        }
                                    """)
        
        """ if not results:
            self.print_btn.setEnabled(False) """

        # Print the results
        for row in results:
            print(row)
        conn.close()
        # Clear existing rows
        self.appointment_table.setRowCount(100)

        # Set number of rows in the table
        self.appointment_table.setRowCount(len(results))

        # print("Expense Showed")
        # self.appointment_table.setColumnWidth(0, 120)  # Expense Date
        # self.appointment_table.setColumnWidth(1, 500)  # Expense Description
        # self.appointment_table.setColumnWidth(2, 200)  # Expense Remarks
        # self.appointment_table.setColumnWidth(3, 180)  # Expense Amount

        # Populate the table
        for row_index, row_data in enumerate(results):
            for col_index, data in enumerate(row_data):
                item = QtWidgets.QTableWidgetItem(str(data))
                self.appointment_table.setItem(row_index, col_index, item)
                # print("testing appointment date", appt_date)
        self.appointment_table.resizeColumnsToContents()
        self.visit_date.setText(f"Appointment of Date: {appt_date}")


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
