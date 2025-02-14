# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_patients_window.ui'
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
        self.side_bar.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.side_bar.setObjectName("side_bar")
        self.patient_btn = QtWidgets.QPushButton(self.side_bar)
        self.patient_btn.setGeometry(QtCore.QRect(10, 180, 140, 40))
        self.patient_btn.setStyleSheet("\n"
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
        self.payment_btn.setIcon(icon4)
        self.payment_btn.setObjectName("payment_btn")
        self.label_5 = QtWidgets.QLabel(self.side_bar)
        self.label_5.setGeometry(QtCore.QRect(0, 0, 161, 51))
        self.label_5.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";\n"
"font: 75 20pt \"MS Shell Dlg 2\";\n"
"text-decoration: underline;\n"
"font: 22pt \"MS Shell Dlg 2\";\n"
"background-color: rgba(255, 255, 255,0);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.label_5.setObjectName("label_5")
        self.add_fname = QtWidgets.QLabel(Dialog)
        self.add_fname.setGeometry(QtCore.QRect(180, 20, 101, 30))
        self.add_fname.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"\n"
"font:  14pt \"Segoe UI \";")
        self.add_fname.setObjectName("add_fname")
        self.add_fname_edit = QtWidgets.QTextEdit(Dialog)
        self.add_fname_edit.setGeometry(QtCore.QRect(280, 20, 141, 31))
        self.add_fname_edit.setStyleSheet("QTextEdit:focus{\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"QTextEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"    font: 12pt \"Segoe UI\";\n"
"}\n"
"")
        self.add_fname_edit.setObjectName("add_fname_edit")
        self.add_lname = QtWidgets.QLabel(Dialog)
        self.add_lname.setGeometry(QtCore.QRect(180, 60, 101, 30))
        self.add_lname.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"\n"
"font:  14pt \"Segoe UI \";")
        self.add_lname.setObjectName("add_lname")
        self.add_lname_edit = QtWidgets.QTextEdit(Dialog)
        self.add_lname_edit.setGeometry(QtCore.QRect(280, 60, 141, 31))
        self.add_lname_edit.setStyleSheet("QTextEdit:focus{\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"QTextEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"    font: 12pt \"Segoe UI\";\n"
"}\n"
"")
        self.add_lname_edit.setObjectName("add_lname_edit")
        self.add_phn = QtWidgets.QLabel(Dialog)
        self.add_phn.setGeometry(QtCore.QRect(490, 20, 101, 30))
        self.add_phn.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"\n"
"font:  14pt \"Segoe UI \";")
        self.add_phn.setObjectName("add_phn")
        self.add_phn_edit = QtWidgets.QTextEdit(Dialog)
        self.add_phn_edit.setGeometry(QtCore.QRect(590, 20, 141, 31))
        self.add_phn_edit.setStyleSheet("QTextEdit:focus{\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"QTextEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"    font: 12pt \"Segoe UI\";\n"
"}\n"
"")
        self.add_phn_edit.setObjectName("add_phn_edit")
        self.add_address = QtWidgets.QLabel(Dialog)
        self.add_address.setGeometry(QtCore.QRect(490, 60, 101, 30))
        self.add_address.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"\n"
"font:  14pt \"Segoe UI \";")
        self.add_address.setObjectName("add_address")
        self.add_occu = QtWidgets.QLabel(Dialog)
        self.add_occu.setGeometry(QtCore.QRect(180, 100, 101, 30))
        self.add_occu.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"\n"
"font:  14pt \"Segoe UI \";")
        self.add_occu.setObjectName("add_occu")
        self.add_occu_edit = QtWidgets.QTextEdit(Dialog)
        self.add_occu_edit.setGeometry(QtCore.QRect(280, 100, 141, 31))
        self.add_occu_edit.setStyleSheet("QTextEdit:focus{\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"QTextEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"    font: 12pt \"Segoe UI\";\n"
"}\n"
"")
        self.add_occu_edit.setObjectName("add_occu_edit")
        self.add_email = QtWidgets.QLabel(Dialog)
        self.add_email.setGeometry(QtCore.QRect(490, 100, 101, 30))
        self.add_email.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"\n"
"font:  14pt \"Segoe UI \";")
        self.add_email.setObjectName("add_email")
        self.add_email_edit = QtWidgets.QTextEdit(Dialog)
        self.add_email_edit.setGeometry(QtCore.QRect(590, 100, 141, 31))
        self.add_email_edit.setStyleSheet("QTextEdit:focus{\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"QTextEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"    font: 12pt \"Segoe UI\";\n"
"}\n"
"")
        self.add_email_edit.setObjectName("add_email_edit")
        self.add_ref = QtWidgets.QLabel(Dialog)
        self.add_ref.setGeometry(QtCore.QRect(180, 140, 101, 30))
        self.add_ref.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"\n"
"font:  14pt \"Segoe UI \";")
        self.add_ref.setObjectName("add_ref")
        self.add_ref_edit = QtWidgets.QTextEdit(Dialog)
        self.add_ref_edit.setGeometry(QtCore.QRect(280, 140, 141, 31))
        self.add_ref_edit.setStyleSheet("QTextEdit:focus{\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"QTextEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"    font: 12pt \"Segoe UI\";\n"
"}\n"
"")
        self.add_ref_edit.setObjectName("add_ref_edit")
        self.add_depart = QtWidgets.QLabel(Dialog)
        self.add_depart.setGeometry(QtCore.QRect(180, 220, 431, 31))
        self.add_depart.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"\n"
"font:  14pt \"Segoe UI \";")
        self.add_depart.setObjectName("add_depart")
        self.add_complain = QtWidgets.QLabel(Dialog)
        self.add_complain.setGeometry(QtCore.QRect(180, 270, 981, 31))
        self.add_complain.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"\n"
"font:  14pt \"Segoe UI \";")
        self.add_complain.setObjectName("add_complain")
        self.add_complain_edit = QtWidgets.QTextEdit(Dialog)
        self.add_complain_edit.setGeometry(QtCore.QRect(180, 300, 981, 171))
        self.add_complain_edit.setStyleSheet("QTextEdit:focus{\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"QTextEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"    font: 12pt \"Segoe UI\";\n"
"}\n"
"")
        self.add_complain_edit.setObjectName("add_complain_edit")
        self.next_btn = QtWidgets.QPushButton(Dialog)
        self.next_btn.setGeometry(QtCore.QRect(925, 525, 241, 30))
        self.next_btn.setStyleSheet("QPushButton{\n"
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
        self.next_btn.setObjectName("next_btn")
        self.add_age = QtWidgets.QLabel(Dialog)
        self.add_age.setGeometry(QtCore.QRect(490, 140, 101, 30))
        self.add_age.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"\n"
"font:  14pt \"Segoe UI \";")
        self.add_age.setObjectName("add_age")
        self.add_age_edit = QtWidgets.QTextEdit(Dialog)
        self.add_age_edit.setGeometry(QtCore.QRect(590, 140, 141, 31))
        self.add_age_edit.setStyleSheet("QTextEdit:focus{\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"QTextEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"    font: 12pt \"Segoe UI\";\n"
"}\n"
"")
        self.add_age_edit.setObjectName("add_age_edit")
        self.add_sex = QtWidgets.QLabel(Dialog)
        self.add_sex.setGeometry(QtCore.QRect(180, 180, 101, 30))
        self.add_sex.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"\n"
"font:  14pt \"Segoe UI \";")
        self.add_sex.setObjectName("add_sex")
        self.add_sex_edit = QtWidgets.QComboBox(Dialog)
        self.add_sex_edit.setGeometry(QtCore.QRect(280, 180, 141, 31))
        self.add_sex_edit.setStyleSheet("#add_sex_edit,\n"
"#add_sex_edit QAbstractItemView {\n"
"    background-color: white;\n"
"background-color: rgb(255, 255, 255);\n"
"    font: 12pt \"Segoe UI\";\n"
"}\n"
"\n"
"#add_sex_edit QAbstractItemView:focus{\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"QTextEdit{\n"
"\n"
"}\n"
"")
        self.add_sex_edit.setObjectName("add_sex_edit")
        self.add_sex_edit.addItem("")
        self.add_sex_edit.addItem("")
        self.add_sex_edit.addItem("")
        self.return_btn = QtWidgets.QPushButton(Dialog)
        self.return_btn.setGeometry(QtCore.QRect(205, 525, 91, 31))
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
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(160, 0, 1280, 720))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Images/daniel-frank-wKbWAMlHgNo-unsplash.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(930, 530, 240, 30))
        self.label_3.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"border-top-right-radius:10px;\n"
"border-bottom-right-radius:10px;\n"
"color: rgb(255, 255, 255);\n"
"")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(210, 530, 90, 30))
        self.label_4.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"border-top-right-radius:10px;\n"
"border-bottom-right-radius:10px;\n"
"color: rgb(255, 255, 255);\n"
"")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.add_pat_id = QtWidgets.QLabel(Dialog)
        self.add_pat_id.setGeometry(QtCore.QRect(490, 180, 101, 30))
        self.add_pat_id.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"\n"
"font:  14pt \"Segoe UI \";")
        self.add_pat_id.setObjectName("add_pat_id")
        self.add_pat_id_edit = QtWidgets.QTextEdit(Dialog)
        self.add_pat_id_edit.setGeometry(QtCore.QRect(590, 180, 141, 31))
        self.add_pat_id_edit.setStyleSheet("QTextEdit:focus{\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"QTextEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"    font: 12pt \"Segoe UI\";\n"
"}\n"
"")
        self.add_pat_id_edit.setObjectName("add_pat_id_edit")
        self.address_combo = QtWidgets.QComboBox(Dialog)
        self.address_combo.setGeometry(QtCore.QRect(590, 60, 141, 30))
        self.address_combo.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"    font: 12pt \"Segoe UI\";")
        self.address_combo.setObjectName("address_combo")
        self.address_combo.addItem("")
        self.address_combo.addItem("")
        self.address_combo.addItem("")
        self.address_combo.addItem("")
        self.address_combo.addItem("")
        self.address_combo.addItem("")
        self.address_combo.addItem("")
        self.address_combo.addItem("")
        self.address_combo.addItem("")
        self.address_combo.addItem("")
        self.address_combo.addItem("")
        self.address_combo.addItem("")
        self.address_combo.addItem("")
        self.address_combo.addItem("")
        self.address_combo.addItem("")
        self.address_combo.addItem("")
        self.address_combo.addItem("")
        self.address_combo.addItem("")
        self.address_combo.addItem("")
        self.address_combo.addItem("")
        self.address_combo.addItem("")
        self.address_combo.addItem("")
        self.address_combo.addItem("")
        self.address_combo.addItem("")
        self.address_combo.addItem("")
        self.address_combo.addItem("")
        self.address_combo.addItem("")
        self.address_combo.addItem("")
        self.address_combo.addItem("")
        self.address_combo.addItem("")
        self.address_combo.addItem("")
        self.address_combo.addItem("")
        self.address_combo.addItem("")
        self.address_combo.addItem("")
        self.address_combo.addItem("")
        self.address_combo.addItem("")
        self.address_combo.addItem("")
        self.address_combo.addItem("")
        self.address_combo.addItem("")
        self.address_combo.addItem("")
        self.address_combo.addItem("")
        self.address_combo.addItem("")
        self.address_combo.addItem("")
        self.address_combo.addItem("")
        self.address_combo.addItem("")
        self.address_combo.addItem("")
        self.address_combo.addItem("")
        self.address_combo.addItem("")
        self.address_combo.addItem("")
        self.address_combo.addItem("")
        self.address_combo.addItem("")
        self.address_combo.addItem("")
        self.address_combo.addItem("")
        self.address_combo.addItem("")
        self.address_combo.addItem("")
        self.address_combo.addItem("")
        self.address_combo.addItem("")
        self.address_combo.addItem("")
        self.address_combo.addItem("")
        self.address_combo.addItem("")
        self.address_combo.addItem("")
        self.address_combo.addItem("")
        self.address_combo.addItem("")
        self.address_combo.addItem("")
        self.address_combo.addItem("")
        self.address_combo.addItem("")
        self.address_combo.addItem("")
        self.address_combo.addItem("")
        self.address_combo.addItem("")
        self.address_combo.addItem("")
        self.address_combo.addItem("")
        self.address_combo.addItem("")
        self.address_combo.addItem("")
        self.add_depart_edit = QtWidgets.QTextEdit(Dialog)
        self.add_depart_edit.setGeometry(QtCore.QRect(590, 220, 141, 31))
        self.add_depart_edit.setStyleSheet("QTextEdit:focus{\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"QTextEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"    font: 12pt \"Segoe UI\";\n"
"}\n"
"")
        self.add_depart_edit.setObjectName("add_depart_edit")
        self.label.raise_()
        self.side_bar.raise_()
        self.add_fname.raise_()
        self.add_fname_edit.raise_()
        self.add_lname.raise_()
        self.add_lname_edit.raise_()
        self.add_phn.raise_()
        self.add_phn_edit.raise_()
        self.add_address.raise_()
        self.add_occu.raise_()
        self.add_occu_edit.raise_()
        self.add_email.raise_()
        self.add_email_edit.raise_()
        self.add_ref.raise_()
        self.add_ref_edit.raise_()
        self.add_depart.raise_()
        self.add_complain.raise_()
        self.add_complain_edit.raise_()
        self.add_age.raise_()
        self.add_age_edit.raise_()
        self.add_sex.raise_()
        self.add_sex_edit.raise_()
        self.label_3.raise_()
        self.next_btn.raise_()
        self.label_4.raise_()
        self.return_btn.raise_()
        self.add_pat_id.raise_()
        self.add_pat_id_edit.raise_()
        self.address_combo.raise_()
        self.add_depart_edit.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.add_fname_edit, self.add_lname_edit)
        Dialog.setTabOrder(self.add_lname_edit, self.add_occu_edit)
        Dialog.setTabOrder(self.add_occu_edit, self.add_ref_edit)
        Dialog.setTabOrder(self.add_ref_edit, self.add_sex_edit)
        Dialog.setTabOrder(self.add_sex_edit, self.add_phn_edit)
        Dialog.setTabOrder(self.add_phn_edit, self.address_combo)
        Dialog.setTabOrder(self.address_combo, self.add_email_edit)
        Dialog.setTabOrder(self.add_email_edit, self.add_age_edit)
        Dialog.setTabOrder(self.add_age_edit, self.add_pat_id_edit)
        Dialog.setTabOrder(self.add_pat_id_edit, self.add_depart_edit)
        Dialog.setTabOrder(self.add_depart_edit, self.add_complain_edit)
        Dialog.setTabOrder(self.add_complain_edit, self.next_btn)
        Dialog.setTabOrder(self.next_btn, self.return_btn)
        Dialog.setTabOrder(self.return_btn, self.dash_btn)
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
        self.expense_btn.setText(_translate("Dialog", "Expense"))
        self.payment_btn.setText(_translate("Dialog", "Payments"))
        self.label_5.setText(_translate("Dialog", " Medico App "))
        self.add_fname.setText(_translate("Dialog", "First Name"))
        self.add_lname.setText(_translate("Dialog", "Last Name"))
        self.add_phn.setText(_translate("Dialog", "Phone"))
        self.add_address.setText(_translate("Dialog", "Address"))
        self.add_occu.setText(_translate("Dialog", "Occupation"))
        self.add_email.setText(_translate("Dialog", "Email"))
        self.add_ref.setText(_translate("Dialog", "Reference"))
        self.add_depart.setText(_translate("Dialog", "If from abroad, date of departure (mm/dd/yyyy):"))
        self.add_complain.setText(_translate("Dialog", "Chief Complain"))
        self.next_btn.setText(_translate("Dialog", "Proceed To Medical History"))
        self.add_age.setText(_translate("Dialog", "Age"))
        self.add_sex.setText(_translate("Dialog", "Sex"))
        self.add_sex_edit.setItemText(0, _translate("Dialog", "Male"))
        self.add_sex_edit.setItemText(1, _translate("Dialog", "Female"))
        self.add_sex_edit.setItemText(2, _translate("Dialog", "Others"))
        self.return_btn.setText(_translate("Dialog", "Return"))
        self.add_pat_id.setText(_translate("Dialog", "Patient ID"))
        self.address_combo.setItemText(0, _translate("Dialog", "..."))
        self.address_combo.setItemText(1, _translate("Dialog", "Abdullahpur"))
        self.address_combo.setItemText(2, _translate("Dialog", "Adabor"))
        self.address_combo.setItemText(3, _translate("Dialog", "Agargaon"))
        self.address_combo.setItemText(4, _translate("Dialog", "Ahmadbag"))
        self.address_combo.setItemText(5, _translate("Dialog", "Badda"))
        self.address_combo.setItemText(6, _translate("Dialog", "Baganbari"))
        self.address_combo.setItemText(7, _translate("Dialog", "Banani"))
        self.address_combo.setItemText(8, _translate("Dialog", "Baridhara"))
        self.address_combo.setItemText(9, _translate("Dialog", "Basaboo"))
        self.address_combo.setItemText(10, _translate("Dialog", "Bashundhara"))
        self.address_combo.setItemText(11, _translate("Dialog", "Banasree"))
        self.address_combo.setItemText(12, _translate("Dialog", "Bawnia"))
        self.address_combo.setItemText(13, _translate("Dialog", "Beraid"))
        self.address_combo.setItemText(14, _translate("Dialog", "Bochila"))
        self.address_combo.setItemText(15, _translate("Dialog", "BRAC Bank"))
        self.address_combo.setItemText(16, _translate("Dialog", "Cantonment area"))
        self.address_combo.setItemText(17, _translate("Dialog", "Dakkhin Gao"))
        self.address_combo.setItemText(18, _translate("Dialog", "Dakshinkhan"))
        self.address_combo.setItemText(19, _translate("Dialog", "Dania"))
        self.address_combo.setItemText(20, _translate("Dialog", "Demra"))
        self.address_combo.setItemText(21, _translate("Dialog", "Dhanmondi"))
        self.address_combo.setItemText(22, _translate("Dialog", "Farmgate"))
        self.address_combo.setItemText(23, _translate("Dialog", "Gabtali"))
        self.address_combo.setItemText(24, _translate("Dialog", "Goran"))
        self.address_combo.setItemText(25, _translate("Dialog", "Gulshan"))
        self.address_combo.setItemText(26, _translate("Dialog", "Hazaribagh"))
        self.address_combo.setItemText(27, _translate("Dialog", "Islampur"))
        self.address_combo.setItemText(28, _translate("Dialog", "Jurain"))
        self.address_combo.setItemText(29, _translate("Dialog", "Kadamtala"))
        self.address_combo.setItemText(30, _translate("Dialog", "Kafrul"))
        self.address_combo.setItemText(31, _translate("Dialog", "Kakrail"))
        self.address_combo.setItemText(32, _translate("Dialog", "Kamalapur"))
        self.address_combo.setItemText(33, _translate("Dialog", "Kamrangirchar"))
        self.address_combo.setItemText(34, _translate("Dialog", "Kazipara"))
        self.address_combo.setItemText(35, _translate("Dialog", "Khilgaon"))
        self.address_combo.setItemText(36, _translate("Dialog", "Khilkhet"))
        self.address_combo.setItemText(37, _translate("Dialog", "Kotwali"))
        self.address_combo.setItemText(38, _translate("Dialog", "Lalbagh"))
        self.address_combo.setItemText(39, _translate("Dialog", "Madartek"))
        self.address_combo.setItemText(40, _translate("Dialog", "Manda"))
        self.address_combo.setItemText(41, _translate("Dialog", "Manikdi"))
        self.address_combo.setItemText(42, _translate("Dialog", "Matuail"))
        self.address_combo.setItemText(43, _translate("Dialog", "Mayakanon"))
        self.address_combo.setItemText(44, _translate("Dialog", "Mohakhali"))
        self.address_combo.setItemText(45, _translate("Dialog", "Mohammadpur"))
        self.address_combo.setItemText(46, _translate("Dialog", "Motijheel"))
        self.address_combo.setItemText(47, _translate("Dialog", "Mirpur"))
        self.address_combo.setItemText(48, _translate("Dialog", "Mugda"))
        self.address_combo.setItemText(49, _translate("Dialog", "Nandipara"))
        self.address_combo.setItemText(50, _translate("Dialog", "Niketan, Gulshan"))
        self.address_combo.setItemText(51, _translate("Dialog", "Nimtoli"))
        self.address_combo.setItemText(52, _translate("Dialog", "Outter Dhaka"))
        self.address_combo.setItemText(53, _translate("Dialog", "Pallabi"))
        self.address_combo.setItemText(54, _translate("Dialog", "Paltan"))
        self.address_combo.setItemText(55, _translate("Dialog", "Paribagh"))
        self.address_combo.setItemText(56, _translate("Dialog", "Rajarbag"))
        self.address_combo.setItemText(57, _translate("Dialog", "Ramna"))
        self.address_combo.setItemText(58, _translate("Dialog", "Rampura"))
        self.address_combo.setItemText(59, _translate("Dialog", "Sabujbag"))
        self.address_combo.setItemText(60, _translate("Dialog", "Sadarghat"))
        self.address_combo.setItemText(61, _translate("Dialog", "Satarkul"))
        self.address_combo.setItemText(62, _translate("Dialog", "Segunbagicha"))
        self.address_combo.setItemText(63, _translate("Dialog", "Shahbagh"))
        self.address_combo.setItemText(64, _translate("Dialog", "Sher-e-Bangla Nagar"))
        self.address_combo.setItemText(65, _translate("Dialog", "Shyampur"))
        self.address_combo.setItemText(66, _translate("Dialog", "Sutrapur"))
        self.address_combo.setItemText(67, _translate("Dialog", "Tejgaon"))
        self.address_combo.setItemText(68, _translate("Dialog", "UCBL Bank"))
        self.address_combo.setItemText(69, _translate("Dialog", "Uttara"))
        self.address_combo.setItemText(70, _translate("Dialog", "Uttarkhan"))
        self.address_combo.setItemText(71, _translate("Dialog", "Vatara"))
        self.address_combo.setItemText(72, _translate("Dialog", "Wari"))
