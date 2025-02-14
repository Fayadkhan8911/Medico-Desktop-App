# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'payments_window.ui'
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
"\n"
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
        self.payment_btn.setStyleSheet("\n"
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
"QPushButton:focus{\n"
"    background-color: rgb(0, 0, 0);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"")
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
        self.fname_srch = QtWidgets.QLabel(Dialog)
        self.fname_srch.setGeometry(QtCore.QRect(190, 30, 101, 31))
        self.fname_srch.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
"font: 16pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"\n"
"\n"
"border-top-right-radius:20px;\n"
"border-bottom-right-radius:20px;")
        self.fname_srch.setObjectName("fname_srch")
        self.fname_srch_edit = QtWidgets.QTextEdit(Dialog)
        self.fname_srch_edit.setGeometry(QtCore.QRect(290, 30, 141, 31))
        self.fname_srch_edit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.fname_srch_edit.setObjectName("fname_srch_edit")
        self.phn_srch = QtWidgets.QLabel(Dialog)
        self.phn_srch.setGeometry(QtCore.QRect(470, 30, 100, 31))
        self.phn_srch.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
"font: 16pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"\n"
"\n"
"border-top-right-radius:20px;\n"
"border-bottom-right-radius:20px;")
        self.phn_srch.setObjectName("phn_srch")
        self.phone_srch_edit = QtWidgets.QTextEdit(Dialog)
        self.phone_srch_edit.setGeometry(QtCore.QRect(570, 30, 141, 31))
        self.phone_srch_edit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.phone_srch_edit.setObjectName("phone_srch_edit")
        self.patid_srch = QtWidgets.QLabel(Dialog)
        self.patid_srch.setGeometry(QtCore.QRect(190, 80, 101, 31))
        self.patid_srch.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
"font: 16pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"\n"
"\n"
"border-top-right-radius:20px;\n"
"border-bottom-right-radius:20px;")
        self.patid_srch.setObjectName("patid_srch")
        self.patid_srch_edit = QtWidgets.QTextEdit(Dialog)
        self.patid_srch_edit.setGeometry(QtCore.QRect(290, 80, 141, 31))
        self.patid_srch_edit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.patid_srch_edit.setObjectName("patid_srch_edit")
        self.payment = QtWidgets.QLabel(Dialog)
        self.payment.setGeometry(QtCore.QRect(190, 130, 181, 31))
        self.payment.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
"font: 16pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"\n"
"\n"
"border-top-right-radius:20px;\n"
"border-bottom-right-radius:20px;")
        self.payment.setObjectName("payment")
        self.payment_edit = QtWidgets.QTextEdit(Dialog)
        self.payment_edit.setGeometry(QtCore.QRect(371, 130, 141, 31))
        self.payment_edit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.payment_edit.setObjectName("payment_edit")
        self.remarks = QtWidgets.QLabel(Dialog)
        self.remarks.setGeometry(QtCore.QRect(190, 180, 101, 31))
        self.remarks.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
"font: 16pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"\n"
"\n"
"border-top-right-radius:20px;\n"
"border-bottom-right-radius:20px;")
        self.remarks.setObjectName("remarks")
        self.remarks_edit = QtWidgets.QTextEdit(Dialog)
        self.remarks_edit.setGeometry(QtCore.QRect(290, 180, 471, 31))
        self.remarks_edit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.remarks_edit.setObjectName("remarks_edit")
        self.makepayment_btn = QtWidgets.QPushButton(Dialog)
        self.makepayment_btn.setGeometry(QtCore.QRect(190, 245, 191, 41))
        self.makepayment_btn.setStyleSheet("QPushButton{\n"
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
        self.makepayment_btn.setObjectName("makepayment_btn")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 1280, 680))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Images/Designer.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(195, 250, 190, 40))
        self.label_2.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
"border-color: rgb(0, 0, 0);\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"border-top-right-radius:10px;\n"
"border-bottom-right-radius:10px;\n"
"border-bottom-color: rgb(0, 0, 0);\n"
"selection-color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.select_date = QtWidgets.QLabel(Dialog)
        self.select_date.setGeometry(QtCore.QRect(190, 390, 371, 31))
        self.select_date.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"\n"
"font:  14pt \"Segoe UI \";")
        self.select_date.setObjectName("select_date")
        self.calendarWidget = QtWidgets.QCalendarWidget(Dialog)
        self.calendarWidget.setGeometry(QtCore.QRect(190, 420, 371, 211))
        self.calendarWidget.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.calendarWidget.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgba(0, 0, 0,.9);\n"
"")
        self.calendarWidget.setObjectName("calendarWidget")
        self.label.raise_()
        self.side_bar.raise_()
        self.fname_srch.raise_()
        self.fname_srch_edit.raise_()
        self.phn_srch.raise_()
        self.phone_srch_edit.raise_()
        self.patid_srch.raise_()
        self.patid_srch_edit.raise_()
        self.payment.raise_()
        self.payment_edit.raise_()
        self.remarks.raise_()
        self.remarks_edit.raise_()
        self.label_2.raise_()
        self.makepayment_btn.raise_()
        self.select_date.raise_()
        self.calendarWidget.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.fname_srch_edit, self.phone_srch_edit)
        Dialog.setTabOrder(self.phone_srch_edit, self.patid_srch_edit)
        Dialog.setTabOrder(self.patid_srch_edit, self.payment_edit)
        Dialog.setTabOrder(self.payment_edit, self.remarks_edit)
        Dialog.setTabOrder(self.remarks_edit, self.makepayment_btn)
        Dialog.setTabOrder(self.makepayment_btn, self.dash_btn)
        Dialog.setTabOrder(self.dash_btn, self.patient_btn)
        Dialog.setTabOrder(self.patient_btn, self.payment_btn)
        Dialog.setTabOrder(self.payment_btn, self.expense_btn)
        Dialog.setTabOrder(self.expense_btn, self.appointment_btn)
        Dialog.setTabOrder(self.appointment_btn, self.dentist_btn)

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
        self.fname_srch.setText(_translate("Dialog", "First Name"))
        self.phn_srch.setText(_translate("Dialog", "Phone"))
        self.patid_srch.setText(_translate("Dialog", "Patient ID"))
        self.payment.setText(_translate("Dialog", "Payment Amount:"))
        self.remarks.setText(_translate("Dialog", "Remarks"))
        self.makepayment_btn.setText(_translate("Dialog", "Add Payment"))
        self.select_date.setText(_translate("Dialog", "Select a date to see expenses of that day:"))
