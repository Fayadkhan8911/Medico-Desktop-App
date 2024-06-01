import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget
from PyQt5.QtGui import QPixmap

import sqlite3


class _dentist_window(QDialog):
    def __init__(self):
        super(_dentist_window, self).__init__()
        loadUi("gui/dentists_window.ui", self)
        self.dentist_table.setColumnWidth(6, 200)

        self.dentist_table.setColumnWidth(7, 200)

        self.load_table()

    def load_table(self):

        # data = _cur.fetchall()  # Fetch data
        _tablerow = 0
        self.dentist_table.setRowCount(50)
        conn = sqlite3.connect("medico.db3")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM dentists")
        # Fetch all rows
        results = cursor.fetchall()

        for col in results:
            item = str(col[0])
            self.dentist_table.setItem(_tablerow, 0, QtWidgets.QTableWidgetItem(item))
            self.dentist_table.setItem(_tablerow, 1, QtWidgets.QTableWidgetItem(col[1]))
            self.dentist_table.setItem(_tablerow, 2, QtWidgets.QTableWidgetItem(col[2]))
            self.dentist_table.setItem(_tablerow, 3, QtWidgets.QTableWidgetItem(col[3]))
            self.dentist_table.setItem(_tablerow, 4, QtWidgets.QTableWidgetItem(col[4]))
            self.dentist_table.setItem(_tablerow, 5, QtWidgets.QTableWidgetItem(col[5]))
            self.dentist_table.setItem(_tablerow, 6, QtWidgets.QTableWidgetItem(col[6]))
            self.dentist_table.setItem(_tablerow, 7, QtWidgets.QTableWidgetItem(col[7]))
            # self.dentist_table.setItem(_tablerow, 5, QtWidgets.QTableWidgetItem(col[2]))6
            _tablerow += 1
            pass


"""
app = QApplication(sys.argv)

widget = QtWidgets.QStackedWidget()
_patient = _dentist_window()

widget.addWidget(_patient)


widget.setFixedWidth(800)
widget.setFixedHeight(600)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")
# """
