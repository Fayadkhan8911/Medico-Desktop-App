import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget
import pdf_maker
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


class _payments_view_window(QDialog):
    def __init__(self, p_id):
        super(_payments_view_window, self).__init__()
        loadUi("payment_history.ui", self)
        self.p_id = p_id
        self._view_payments_table()
        self.print_btn.clicked.connect(self.print_payments)
        
        def showEvent(self, event):
            #init line chilo super(_add_med_hist_win, self).__init__()
            super(_payments_view_window, self).showEvent(event)
            self.patient_btn.setFocus()

    def print_payments(self):
        _query = " SELECT payment_date,file_name,payment_amount,due, payment_remarks FROM payment_history WHERE p_id = ?"
        prefix = " Payments "
        file_location = "Personal_Payments_pdf/"
        pdf = pdf_maker.pdf_maker_pat_id(_query, prefix, file_location, self.p_id)
        pdf

    def _view_payments_table(self):
        p_id = self.p_id
        print(p_id)
        conn = sqlite3.connect("medico.db3")
        cursor = conn.cursor()
        cursor.execute(
            "SELECT payment_date,file_name,payment_amount,due, payment_remarks FROM payment_history WHERE p_id = ?",
            (p_id,),
        )
        # Fetch all rows
        results = cursor.fetchall()
        
        if not results:
            self.print_btn.setEnabled(False)

        # Print the results
        for row in results:
            print(row)
        conn.close()
        # Clear existing rows
        self.pay_hist_table.setRowCount(0)

        # Set number of rows in the table
        self.pay_hist_table.setRowCount(len(results))

        print("payments individual Showed")
        # self.pay_hist_table.setColumnWidth(0, 120)  # payments Date
        # self.pay_hist_table.setColumnWidth(1, 500)  # file name
        # self.pay_hist_table.setColumnWidth(2, 200)  # amount
        # self.pay_hist_table.setColumnWidth(3, 250)  # due
        # self.pay_hist_table.setColumnWidth(4, 300)  # remarks

        # Populate the table
        for row_index, row_data in enumerate(results):
            for col_index, data in enumerate(row_data):
                item = QtWidgets.QTableWidgetItem(str(data))
                self.pay_hist_table.setItem(row_index, col_index, item)

        self.pay_hist_table.resizeColumnsToContents()

        self.payment_title.setText(f"payments History of Patient: {p_id}")


"""
app = QApplication(sys.argv)

widget = QtWidgets.QStackedWidget()
__view_window = _payments_view_window("2024-02-12")

widget.addWidget(__view_window)


widget.setFixedWidth(800)
widget.setFixedHeight(600)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")
# """
