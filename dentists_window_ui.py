# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dentists_window.ui'
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
        self.side_bar.setGeometry(QtCore.QRect(0, 0, 160, 721))
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
        self.appointment_btn.setStyleSheet("QPushButton{\n"
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
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../Medico_modern/appointmentdownload (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.appointment_btn.setIcon(icon2)
        self.appointment_btn.setObjectName("appointment_btn")
        self.dentist_btn = QtWidgets.QPushButton(self.side_bar)
        self.dentist_btn.setGeometry(QtCore.QRect(10, 580, 140, 40))
        self.dentist_btn.setStyleSheet("\n"
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
"}")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../Medico_modern/dentistimages.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.dentist_btn.setIcon(icon3)
        self.dentist_btn.setObjectName("dentist_btn")
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
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../Medico_modern/billingdownload (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.expense_btn.setIcon(icon4)
        self.expense_btn.setObjectName("expense_btn")
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
        self.payment_btn.setIcon(icon)
        self.payment_btn.setObjectName("payment_btn")
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
        self.dentist_table = QtWidgets.QTableWidget(Dialog)
        self.dentist_table.setGeometry(QtCore.QRect(180, 50, 1061, 491))
        self.dentist_table.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.dentist_table.setStyleSheet("background-color: rgba(255, 255, 255,.85);\n"
"font:  12pt \"Segoe UI \";")
        self.dentist_table.setObjectName("dentist_table")
        self.dentist_table.setColumnCount(8)
        self.dentist_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.dentist_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.dentist_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.dentist_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.dentist_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.dentist_table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.dentist_table.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.dentist_table.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.dentist_table.setHorizontalHeaderItem(7, item)
        self.add_dentist_btn = QtWidgets.QPushButton(Dialog)
        self.add_dentist_btn.setGeometry(QtCore.QRect(1130, 605, 101, 23))
        self.add_dentist_btn.setStyleSheet("QPushButton{\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
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
        self.add_dentist_btn.setObjectName("add_dentist_btn")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 1280, 680))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Images/sam-moghadam-khamseh-I-kDEBUMAaQ-unsplash.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(1135, 610, 100, 25))
        self.label_5.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"border-top-right-radius:10px;\n"
"border-bottom-right-radius:10px;\n"
"color: rgb(255, 255, 255);\n"
"")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.patient_list = QtWidgets.QLabel(Dialog)
        self.patient_list.setGeometry(QtCore.QRect(180, 20, 1061, 31))
        self.patient_list.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"\n"
"font:  14pt \"Segoe UI \";")
        self.patient_list.setObjectName("patient_list")
        self.label.raise_()
        self.side_bar.raise_()
        self.dentist_table.raise_()
        self.label_5.raise_()
        self.add_dentist_btn.raise_()
        self.patient_list.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.dentist_btn, self.add_dentist_btn)
        Dialog.setTabOrder(self.add_dentist_btn, self.dash_btn)
        Dialog.setTabOrder(self.dash_btn, self.patient_btn)
        Dialog.setTabOrder(self.patient_btn, self.payment_btn)
        Dialog.setTabOrder(self.payment_btn, self.expense_btn)
        Dialog.setTabOrder(self.expense_btn, self.appointment_btn)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.patient_btn.setText(_translate("Dialog", "Patients"))
        self.dash_btn.setText(_translate("Dialog", "Dashboard"))
        self.appointment_btn.setText(_translate("Dialog", "Appointments"))
        self.dentist_btn.setText(_translate("Dialog", "Dentists"))
        self.expense_btn.setText(_translate("Dialog", "Expense"))
        self.payment_btn.setText(_translate("Dialog", "Payments"))
        self.label_4.setText(_translate("Dialog", " Medico App "))
        item = self.dentist_table.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Dentist ID"))
        item = self.dentist_table.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "First Name"))
        item = self.dentist_table.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Last Name"))
        item = self.dentist_table.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Email"))
        item = self.dentist_table.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "Phone"))
        item = self.dentist_table.horizontalHeaderItem(5)
        item.setText(_translate("Dialog", "Date of Birth"))
        item = self.dentist_table.horizontalHeaderItem(6)
        item.setText(_translate("Dialog", "Date of Joining"))
        item = self.dentist_table.horizontalHeaderItem(7)
        item.setText(_translate("Dialog", "Date of Leave"))
        self.add_dentist_btn.setText(_translate("Dialog", "Add Dentist"))
        self.patient_list.setText(_translate("Dialog", "Patients List"))
