import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget

from PyQt5.QtGui import QPixmap

from PyQt5.QtCore import QDate
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

from files_main_ui import Ui_Dialog

class _files_view_window(QDialog, Ui_Dialog):
    def __init__(self, p_id):
        super(_files_view_window, self).__init__()
        self.setupUi(self)
        self.p_id = p_id
        self._view_files_table()
        

    def _view_files_table(self):
        p_id = self.p_id
        print(p_id)
        conn = sqlite3.connect("medico.db3")
        cursor = conn.cursor()
        cursor.execute(
            "SELECT file_add_date , file_name,estd_cost,discount,final_cost,file_desc FROM files_hist WHERE patient_id = ?",
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
        self.files_table.setRowCount(0)

        # Set number of rows in the table
        self.files_table.setRowCount(len(results))

        print("files Showed")
        # self.files_table.setColumnWidth(0, 120)  # files Date
        # self.pay_hist_table.setColumnWidth(1, 500)  # file name
        # self.pay_hist_table.setColumnWidth(2, 200)  # amount
        # self.pay_hist_table.setColumnWidth(3, 250)  # due
        # self.pay_hist_table.setColumnWidth(4, 300)  # remarks

        # Populate the table
        for row_index, row_data in enumerate(results):
            for col_index, data in enumerate(row_data):
                
                if col_index == 0:
                    # Convert the date string to QDate and then to the desired format
                    date = QDate.fromString(data, "yyyy-MM-dd")
                    formatted_date = date.toString("dd-MM-yyyy")
                    item = QtWidgets.QTableWidgetItem(formatted_date)
                else:
                    item = QtWidgets.QTableWidgetItem(str(data))
                self.files_table.setItem(row_index, col_index, item)

        self.files_table.resizeColumnsToContents()

        self.files_list.setText(f"File List of {p_id}")


"""
app = QApplication(sys.argv)

widget = QtWidgets.QStackedWidget()
__view_window = _files_view_window("2024-02-12")

widget.addWidget(__view_window)


widget.setFixedWidth(800)
widget.setFixedHeight(600)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")
# """
