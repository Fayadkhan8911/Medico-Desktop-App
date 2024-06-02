# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'appointment_date.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1280, 680)
        Dialog.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.side_bar = QtWidgets.QWidget(Dialog)
        self.side_bar.setGeometry(QtCore.QRect(0, 0, 160, 681))
        self.side_bar.setStyleSheet("\n"
"background-color: rgba(170, 170, 255,.5);\n"
"")
        self.side_bar.setObjectName("side_bar")
        self.patient_btn = QtWidgets.QPushButton(self.side_bar)
        self.patient_btn.setGeometry(QtCore.QRect(10, 180, 140, 40))
        self.patient_btn.setStyleSheet("QPushButton{\n"
"\n"
"\n"
"font:  14pt \"Segoe UI \";\n"
"background-color: rgb(255, 255, 255);\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"border-top-right-radius:10px;\n"
"border-bottom-right-radius:10px;}\n"
"QPushButton:hover{\n"
"    background-color: rgb(161, 161, 161);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:focus{\n"
"    background-color: rgb(161, 161, 161);\n"
"    color: rgb(255, 255, 255);\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Medico_modern/patientdownload .png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.patient_btn.setIcon(icon)
        self.patient_btn.setObjectName("patient_btn")
        self.dash_btn = QtWidgets.QPushButton(self.side_bar)
        self.dash_btn.setGeometry(QtCore.QRect(10, 80, 140, 40))
        self.dash_btn.setStyleSheet("QPushButton{\n"
"\n"
"\n"
"font:  14pt \"Segoe UI \";\n"
"background-color: rgb(255, 255, 255);\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"border-top-right-radius:10px;\n"
"border-bottom-right-radius:10px;}\n"
"QPushButton:hover{\n"
"    background-color: rgb(161, 161, 161);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:focus{\n"
"    background-color: rgb(161, 161, 161);\n"
"    color: rgb(255, 255, 255);\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../Medico_modern/dashboard.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.dash_btn.setIcon(icon1)
        self.dash_btn.setObjectName("dash_btn")
        self.appointment_btn = QtWidgets.QPushButton(self.side_bar)
        self.appointment_btn.setGeometry(QtCore.QRect(10, 480, 140, 40))
        self.appointment_btn.setStyleSheet("\n"
"QPushButton{\n"
"\n"
"\n"
"font:  14pt \"Segoe UI \";\n"
"background-color: rgb(255, 255, 255);\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"border-top-right-radius:10px;\n"
"border-bottom-right-radius:10px;\n"
"\n"
"    background-color: rgb(0, 0, 0);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(161, 161, 161);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:focus{\n"
"    background-color: rgb(0, 0, 0);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../Medico_modern/appointmentdownload (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.appointment_btn.setIcon(icon2)
        self.appointment_btn.setObjectName("appointment_btn")
        self.dentist_btn = QtWidgets.QPushButton(self.side_bar)
        self.dentist_btn.setGeometry(QtCore.QRect(10, 580, 140, 40))
        self.dentist_btn.setStyleSheet("QPushButton{\n"
"\n"
"\n"
"font:  14pt \"Segoe UI \";\n"
"background-color: rgb(255, 255, 255);\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"border-top-right-radius:10px;\n"
"border-bottom-right-radius:10px;}\n"
"QPushButton:hover{\n"
"    background-color: rgb(161, 161, 161);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:focus{\n"
"    background-color: rgb(161, 161, 161);\n"
"    color: rgb(255, 255, 255);\n"
"}")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../Medico_modern/dentistimages.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.dentist_btn.setIcon(icon3)
        self.dentist_btn.setObjectName("dentist_btn")
        self.payment_btn = QtWidgets.QPushButton(self.side_bar)
        self.payment_btn.setGeometry(QtCore.QRect(10, 280, 140, 40))
        self.payment_btn.setStyleSheet("QPushButton{\n"
"\n"
"\n"
"font:  14pt \"Segoe UI \";\n"
"background-color: rgb(255, 255, 255);\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"border-top-right-radius:10px;\n"
"border-bottom-right-radius:10px;}\n"
"QPushButton:hover{\n"
"    background-color: rgb(161, 161, 161);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:focus{\n"
"    background-color: rgb(161, 161, 161);\n"
"    color: rgb(255, 255, 255);\n"
"}")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../Medico_modern/billingdownload (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.payment_btn.setIcon(icon4)
        self.payment_btn.setObjectName("payment_btn")
        self.expense_btn = QtWidgets.QPushButton(self.side_bar)
        self.expense_btn.setGeometry(QtCore.QRect(10, 380, 140, 40))
        self.expense_btn.setStyleSheet("QPushButton{\n"
"\n"
"\n"
"font:  14pt \"Segoe UI \";\n"
"background-color: rgb(255, 255, 255);\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"border-top-right-radius:10px;\n"
"border-bottom-right-radius:10px;}\n"
"QPushButton:hover{\n"
"    background-color: rgb(161, 161, 161);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:focus{\n"
"    background-color: rgb(161, 161, 161);\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.expense_btn.setIcon(icon4)
        self.expense_btn.setObjectName("expense_btn")
        self.label_4 = QtWidgets.QLabel(self.side_bar)
        self.label_4.setGeometry(QtCore.QRect(0, 0, 161, 51))
        self.label_4.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";\n"
"font: 75 20pt \"MS Shell Dlg 2\";\n"
"text-decoration: underline;\n"
"font: 22pt \"MS Shell Dlg 2\";\n"
"background-color: rgba(255, 255, 255,0);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.label_4.setObjectName("label_4")
        self.appointment_table = QtWidgets.QTableWidget(Dialog)
        self.appointment_table.setGeometry(QtCore.QRect(200, 60, 1051, 561))
        self.appointment_table.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.appointment_table.setStyleSheet("background-color: rgba(255, 255, 255,.85);\n"
"font:  12pt \"Segoe UI \";")
        self.appointment_table.setObjectName("appointment_table")
        self.appointment_table.setColumnCount(8)
        self.appointment_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.appointment_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.appointment_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.appointment_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.appointment_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.appointment_table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.appointment_table.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.appointment_table.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.appointment_table.setHorizontalHeaderItem(7, item)
        self.visit_date = QtWidgets.QLabel(Dialog)
        self.visit_date.setGeometry(QtCore.QRect(200, 30, 901, 31))
        self.visit_date.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"\n"
"font:  14pt \"Segoe UI \";")
        self.visit_date.setObjectName("visit_date")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 1281, 680))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Images/jonathan-borba-W9YEY6G8LVM-unsplash.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.return_btn = QtWidgets.QPushButton(Dialog)
        self.return_btn.setGeometry(QtCore.QRect(200, 630, 75, 30))
        self.return_btn.setStyleSheet("QPushButton{\n"
"\n"
"\n"
"font:  14pt \"Segoe UI \";\n"
"background-color: rgb(255, 255, 255);\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"border-top-right-radius:10px;\n"
"border-bottom-right-radius:10px;}\n"
"QPushButton:hover{\n"
"    background-color: rgb(161, 161, 161);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:focus{\n"
"    background-color: rgb(161, 161, 161);\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.return_btn.setObjectName("return_btn")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(210, 640, 75, 30))
        self.label_2.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"border-top-right-radius:10px;\n"
"border-bottom-right-radius:10px;\n"
"color: rgb(255, 255, 255);\n"
"")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.print_btn = QtWidgets.QPushButton(Dialog)
        self.print_btn.setGeometry(QtCore.QRect(1176, 630, 75, 30))
        self.print_btn.setStyleSheet("QPushButton{\n"
"    background-color: rgb(255, 0, 0);\n"
"\n"
"font:  14pt \"Segoe UI \";\n"
"    color: rgb(255, 255, 255);\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"border-top-right-radius:10px;\n"
"border-bottom-right-radius:10px;}\n"
"QPushButton:hover{\n"
"    background-color: rgb(255, 0, 0);\n"
"    background-color: rgb(255, 85, 0);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:focus{\n"
"    background-color: rgb(255, 0, 0);\n"
"    background-color: rgb(255, 85, 0);\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.print_btn.setObjectName("print_btn")
        self.label.raise_()
        self.side_bar.raise_()
        self.appointment_table.raise_()
        self.visit_date.raise_()
        self.label_2.raise_()
        self.return_btn.raise_()
        self.print_btn.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.appointment_btn, self.dentist_btn)
        Dialog.setTabOrder(self.dentist_btn, self.return_btn)
        Dialog.setTabOrder(self.return_btn, self.print_btn)
        Dialog.setTabOrder(self.print_btn, self.dash_btn)
        Dialog.setTabOrder(self.dash_btn, self.patient_btn)
        Dialog.setTabOrder(self.patient_btn, self.payment_btn)
        Dialog.setTabOrder(self.payment_btn, self.expense_btn)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.patient_btn.setText(_translate("Dialog", "Patients"))
        self.dash_btn.setText(_translate("Dialog", "Dashboard"))
        self.appointment_btn.setText(_translate("Dialog", "Appointments"))
        self.dentist_btn.setText(_translate("Dialog", "Dentists"))
        self.payment_btn.setText(_translate("Dialog", "Payments"))
        self.expense_btn.setText(_translate("Dialog", "Expense"))
        self.label_4.setText(_translate("Dialog", " Medico App "))
        item = self.appointment_table.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Date Registered"))
        item = self.appointment_table.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "First Name"))
        item = self.appointment_table.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Phone"))
        item = self.appointment_table.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Visit time"))
        item = self.appointment_table.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "Visit Date"))
        item = self.appointment_table.horizontalHeaderItem(5)
        item.setText(_translate("Dialog", "Dentist Name"))
        item = self.appointment_table.horizontalHeaderItem(6)
        item.setText(_translate("Dialog", "Status"))
        item = self.appointment_table.horizontalHeaderItem(7)
        item.setText(_translate("Dialog", "Patient ID"))
        self.visit_date.setText(_translate("Dialog", "Appointment Table"))
        self.return_btn.setText(_translate("Dialog", "Return"))
        self.print_btn.setText(_translate("Dialog", "Print"))
