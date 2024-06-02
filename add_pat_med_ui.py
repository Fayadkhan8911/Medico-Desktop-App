# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_patients_med_hist_window.ui'
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
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Medico_modern/dashboard.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.dash_btn.setIcon(icon)
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
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../Medico_modern/appointmentdownload (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.appointment_btn.setIcon(icon1)
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
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../Medico_modern/dentistimages.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.dentist_btn.setIcon(icon2)
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
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../Medico_modern/billingdownload (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.payment_btn.setIcon(icon3)
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
        self.expense_btn.setIcon(icon3)
        self.expense_btn.setObjectName("expense_btn")
        self.label_6 = QtWidgets.QLabel(self.side_bar)
        self.label_6.setGeometry(QtCore.QRect(0, 0, 161, 51))
        self.label_6.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";\n"
"font: 75 20pt \"MS Shell Dlg 2\";\n"
"text-decoration: underline;\n"
"font: 22pt \"MS Shell Dlg 2\";\n"
"background-color: rgba(255, 255, 255,0);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.label_6.setObjectName("label_6")
        self.patient_btn = QtWidgets.QPushButton(Dialog)
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
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../Medico_modern/patientdownload .png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.patient_btn.setIcon(icon4)
        self.patient_btn.setObjectName("patient_btn")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(190, 20, 521, 521))
        self.widget.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
"\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"border-top-right-radius:10px;\n"
"border-bottom-right-radius:10px;\n"
"background-color: rgba(0, 0, 0,.5);\n"
"color: rgb(255, 255, 255);")
        self.widget.setObjectName("widget")
        self.q1 = QtWidgets.QLabel(self.widget)
        self.q1.setGeometry(QtCore.QRect(10, 40, 481, 20))
        self.q1.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"\n"
"\n"
"\n"
"font:  12pt \"Segoe UI \";")
        self.q1.setObjectName("q1")
        self.q1_y_check = QtWidgets.QCheckBox(self.widget)
        self.q1_y_check.setGeometry(QtCore.QRect(500, 40, 16, 20))
        self.q1_y_check.setStyleSheet("QCheckBox{\n"
"    background-color: rgba(0, 0, 0,0);\n"
"}\n"
"QCheckBox:focus{\n"
"    background-color: rgb(161, 161, 161);\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.q1_y_check.setText("")
        self.q1_y_check.setObjectName("q1_y_check")
        self.q2 = QtWidgets.QLabel(self.widget)
        self.q2.setGeometry(QtCore.QRect(10, 70, 481, 20))
        self.q2.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"\n"
"\n"
"\n"
"font:  12pt \"Segoe UI \";")
        self.q2.setObjectName("q2")
        self.q2_y_check = QtWidgets.QCheckBox(self.widget)
        self.q2_y_check.setGeometry(QtCore.QRect(500, 70, 16, 20))
        self.q2_y_check.setStyleSheet("QCheckBox{\n"
"    background-color: rgba(0, 0, 0,0);\n"
"}\n"
"QCheckBox:focus{\n"
"    background-color: rgb(161, 161, 161);\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.q2_y_check.setText("")
        self.q2_y_check.setObjectName("q2_y_check")
        self.q3 = QtWidgets.QLabel(self.widget)
        self.q3.setGeometry(QtCore.QRect(10, 100, 481, 20))
        self.q3.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"\n"
"\n"
"\n"
"font:  12pt \"Segoe UI \";")
        self.q3.setObjectName("q3")
        self.q3_y_check = QtWidgets.QCheckBox(self.widget)
        self.q3_y_check.setGeometry(QtCore.QRect(500, 100, 16, 20))
        self.q3_y_check.setStyleSheet("QCheckBox{\n"
"    background-color: rgba(0, 0, 0,0);\n"
"}\n"
"QCheckBox:focus{\n"
"    background-color: rgb(161, 161, 161);\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.q3_y_check.setText("")
        self.q3_y_check.setObjectName("q3_y_check")
        self.q4 = QtWidgets.QLabel(self.widget)
        self.q4.setGeometry(QtCore.QRect(10, 130, 481, 20))
        self.q4.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"\n"
"\n"
"\n"
"font:  12pt \"Segoe UI \";")
        self.q4.setObjectName("q4")
        self.q4_y_check = QtWidgets.QCheckBox(self.widget)
        self.q4_y_check.setGeometry(QtCore.QRect(500, 130, 16, 20))
        self.q4_y_check.setStyleSheet("QCheckBox{\n"
"    background-color: rgba(0, 0, 0,0);\n"
"}\n"
"QCheckBox:focus{\n"
"    background-color: rgb(161, 161, 161);\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.q4_y_check.setText("")
        self.q4_y_check.setObjectName("q4_y_check")
        self.q5 = QtWidgets.QLabel(self.widget)
        self.q5.setGeometry(QtCore.QRect(10, 160, 481, 20))
        self.q5.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"\n"
"\n"
"\n"
"font:  12pt \"Segoe UI \";")
        self.q5.setObjectName("q5")
        self.q5_y_check = QtWidgets.QCheckBox(self.widget)
        self.q5_y_check.setGeometry(QtCore.QRect(500, 160, 16, 20))
        self.q5_y_check.setStyleSheet("QCheckBox{\n"
"    background-color: rgba(0, 0, 0,0);\n"
"}\n"
"QCheckBox:focus{\n"
"    background-color: rgb(161, 161, 161);\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.q5_y_check.setText("")
        self.q5_y_check.setObjectName("q5_y_check")
        self.q6 = QtWidgets.QLabel(self.widget)
        self.q6.setGeometry(QtCore.QRect(10, 190, 481, 20))
        self.q6.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"\n"
"\n"
"\n"
"font:  12pt \"Segoe UI \";")
        self.q6.setObjectName("q6")
        self.q6_y_check = QtWidgets.QCheckBox(self.widget)
        self.q6_y_check.setGeometry(QtCore.QRect(500, 190, 16, 20))
        self.q6_y_check.setStyleSheet("QCheckBox{\n"
"    background-color: rgba(0, 0, 0,0);\n"
"}\n"
"QCheckBox:focus{\n"
"    background-color: rgb(161, 161, 161);\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.q6_y_check.setText("")
        self.q6_y_check.setObjectName("q6_y_check")
        self.q7 = QtWidgets.QLabel(self.widget)
        self.q7.setGeometry(QtCore.QRect(10, 220, 481, 20))
        self.q7.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"\n"
"\n"
"\n"
"font:  12pt \"Segoe UI \";")
        self.q7.setObjectName("q7")
        self.q7_y_check = QtWidgets.QCheckBox(self.widget)
        self.q7_y_check.setGeometry(QtCore.QRect(500, 220, 16, 20))
        self.q7_y_check.setStyleSheet("QCheckBox{\n"
"    background-color: rgba(0, 0, 0,0);\n"
"}\n"
"QCheckBox:focus{\n"
"    background-color: rgb(161, 161, 161);\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.q7_y_check.setText("")
        self.q7_y_check.setObjectName("q7_y_check")
        self.q8 = QtWidgets.QLabel(self.widget)
        self.q8.setGeometry(QtCore.QRect(10, 250, 481, 20))
        self.q8.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"\n"
"\n"
"\n"
"font:  12pt \"Segoe UI \";")
        self.q8.setObjectName("q8")
        self.q8_y_check = QtWidgets.QCheckBox(self.widget)
        self.q8_y_check.setGeometry(QtCore.QRect(500, 250, 16, 20))
        self.q8_y_check.setStyleSheet("QCheckBox{\n"
"    background-color: rgba(0, 0, 0,0);\n"
"}\n"
"QCheckBox:focus{\n"
"    background-color: rgb(161, 161, 161);\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.q8_y_check.setText("")
        self.q8_y_check.setObjectName("q8_y_check")
        self.q9 = QtWidgets.QLabel(self.widget)
        self.q9.setGeometry(QtCore.QRect(10, 280, 481, 20))
        self.q9.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"\n"
"\n"
"\n"
"font:  12pt \"Segoe UI \";")
        self.q9.setObjectName("q9")
        self.q9_y_check = QtWidgets.QCheckBox(self.widget)
        self.q9_y_check.setGeometry(QtCore.QRect(500, 280, 16, 20))
        self.q9_y_check.setStyleSheet("QCheckBox{\n"
"    background-color: rgba(0, 0, 0,0);\n"
"}\n"
"QCheckBox:focus{\n"
"    background-color: rgb(161, 161, 161);\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.q9_y_check.setText("")
        self.q9_y_check.setObjectName("q9_y_check")
        self.q10 = QtWidgets.QLabel(self.widget)
        self.q10.setGeometry(QtCore.QRect(10, 310, 481, 20))
        self.q10.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"\n"
"\n"
"\n"
"font:  12pt \"Segoe UI \";")
        self.q10.setObjectName("q10")
        self.q10_y_check = QtWidgets.QCheckBox(self.widget)
        self.q10_y_check.setGeometry(QtCore.QRect(500, 310, 16, 20))
        self.q10_y_check.setStyleSheet("QCheckBox{\n"
"    background-color: rgba(0, 0, 0,0);\n"
"}\n"
"QCheckBox:focus{\n"
"    background-color: rgb(161, 161, 161);\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.q10_y_check.setText("")
        self.q10_y_check.setObjectName("q10_y_check")
        self.q11 = QtWidgets.QLabel(self.widget)
        self.q11.setGeometry(QtCore.QRect(10, 340, 481, 20))
        self.q11.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"\n"
"\n"
"\n"
"font:  12pt \"Segoe UI \";")
        self.q11.setObjectName("q11")
        self.q11_y_check = QtWidgets.QCheckBox(self.widget)
        self.q11_y_check.setGeometry(QtCore.QRect(500, 340, 16, 20))
        self.q11_y_check.setStyleSheet("QCheckBox{\n"
"    background-color: rgba(0, 0, 0,0);\n"
"}\n"
"QCheckBox:focus{\n"
"    background-color: rgb(161, 161, 161);\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.q11_y_check.setText("")
        self.q11_y_check.setObjectName("q11_y_check")
        self.q12 = QtWidgets.QLabel(self.widget)
        self.q12.setGeometry(QtCore.QRect(10, 370, 481, 20))
        self.q12.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"\n"
"\n"
"\n"
"font:  12pt \"Segoe UI \";")
        self.q12.setObjectName("q12")
        self.q12_y_check = QtWidgets.QCheckBox(self.widget)
        self.q12_y_check.setGeometry(QtCore.QRect(500, 370, 16, 20))
        self.q12_y_check.setStyleSheet("QCheckBox{\n"
"    background-color: rgba(0, 0, 0,0);\n"
"}\n"
"QCheckBox:focus{\n"
"    background-color: rgb(161, 161, 161);\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.q12_y_check.setText("")
        self.q12_y_check.setObjectName("q12_y_check")
        self.q13 = QtWidgets.QLabel(self.widget)
        self.q13.setGeometry(QtCore.QRect(10, 400, 481, 20))
        self.q13.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"\n"
"\n"
"\n"
"font:  12pt \"Segoe UI \";")
        self.q13.setObjectName("q13")
        self.q13_y_check = QtWidgets.QCheckBox(self.widget)
        self.q13_y_check.setGeometry(QtCore.QRect(500, 400, 16, 20))
        self.q13_y_check.setStyleSheet("QCheckBox{\n"
"    background-color: rgba(0, 0, 0,0);\n"
"}\n"
"QCheckBox:focus{\n"
"    background-color: rgb(161, 161, 161);\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.q13_y_check.setText("")
        self.q13_y_check.setObjectName("q13_y_check")
        self.q14 = QtWidgets.QLabel(self.widget)
        self.q14.setGeometry(QtCore.QRect(10, 430, 481, 20))
        self.q14.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"\n"
"\n"
"\n"
"font:  12pt \"Segoe UI \";")
        self.q14.setObjectName("q14")
        self.q14_y_check = QtWidgets.QCheckBox(self.widget)
        self.q14_y_check.setGeometry(QtCore.QRect(500, 430, 16, 20))
        self.q14_y_check.setStyleSheet("QCheckBox{\n"
"    background-color: rgba(0, 0, 0,0);\n"
"}\n"
"QCheckBox:focus{\n"
"    background-color: rgb(161, 161, 161);\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.q14_y_check.setText("")
        self.q14_y_check.setObjectName("q14_y_check")
        self.q15 = QtWidgets.QLabel(self.widget)
        self.q15.setGeometry(QtCore.QRect(10, 460, 481, 20))
        self.q15.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"\n"
"\n"
"\n"
"font:  12pt \"Segoe UI \";")
        self.q15.setObjectName("q15")
        self.q15_y_check = QtWidgets.QCheckBox(self.widget)
        self.q15_y_check.setGeometry(QtCore.QRect(500, 460, 16, 20))
        self.q15_y_check.setStyleSheet("QCheckBox{\n"
"    background-color: rgba(0, 0, 0,0);\n"
"}\n"
"QCheckBox:focus{\n"
"    background-color: rgb(161, 161, 161);\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.q15_y_check.setText("")
        self.q15_y_check.setObjectName("q15_y_check")
        self.q16 = QtWidgets.QLabel(self.widget)
        self.q16.setGeometry(QtCore.QRect(10, 490, 481, 20))
        self.q16.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"\n"
"\n"
"\n"
"font:  12pt \"Segoe UI \";")
        self.q16.setObjectName("q16")
        self.q16_y_check = QtWidgets.QCheckBox(self.widget)
        self.q16_y_check.setGeometry(QtCore.QRect(500, 490, 16, 20))
        self.q16_y_check.setStyleSheet("QCheckBox{\n"
"    background-color: rgba(0, 0, 0,0);\n"
"}\n"
"QCheckBox:focus{\n"
"    background-color: rgb(161, 161, 161);\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.q16_y_check.setText("")
        self.q16_y_check.setObjectName("q16_y_check")
        self.findings_label_2 = QtWidgets.QLabel(self.widget)
        self.findings_label_2.setGeometry(QtCore.QRect(0, 0, 521, 31))
        self.findings_label_2.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"\n"
"font:  14pt \"Segoe UI \";")
        self.findings_label_2.setObjectName("findings_label_2")
        self.widget_2 = QtWidgets.QWidget(Dialog)
        self.widget_2.setGeometry(QtCore.QRect(740, 20, 421, 381))
        self.widget_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.widget_2.setObjectName("widget_2")
        self.findings_label = QtWidgets.QLabel(self.widget_2)
        self.findings_label.setGeometry(QtCore.QRect(0, 0, 351, 31))
        self.findings_label.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"\n"
"font:  14pt \"Segoe UI \";")
        self.findings_label.setObjectName("findings_label")
        self.med_find_edit = QtWidgets.QTextEdit(self.widget_2)
        self.med_find_edit.setGeometry(QtCore.QRect(0, 40, 421, 341))
        self.med_find_edit.setStyleSheet("QTextEdit:focus{\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"QTextEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"    font: 12pt \"Segoe UI\";\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"")
        self.med_find_edit.setObjectName("med_find_edit")
        self.med_find_edit.raise_()
        self.findings_label.raise_()
        self.save_pat = QtWidgets.QPushButton(Dialog)
        self.save_pat.setGeometry(QtCore.QRect(990, 530, 191, 41))
        self.save_pat.setStyleSheet("QPushButton{\n"
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
        self.save_pat.setObjectName("save_pat")
        self.restart_btn = QtWidgets.QPushButton(Dialog)
        self.restart_btn.setGeometry(QtCore.QRect(190, 560, 101, 31))
        self.restart_btn.setStyleSheet("QPushButton{\n"
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
        self.restart_btn.setObjectName("restart_btn")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, -20, 1280, 720))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Images/daniel-frank-wKbWAMlHgNo-unsplash.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(195, 565, 100, 30))
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
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(995, 535, 190, 40))
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
        self.label.raise_()
        self.side_bar.raise_()
        self.patient_btn.raise_()
        self.widget.raise_()
        self.widget_2.raise_()
        self.label_4.raise_()
        self.restart_btn.raise_()
        self.label_5.raise_()
        self.save_pat.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.patient_btn, self.payment_btn)
        Dialog.setTabOrder(self.payment_btn, self.expense_btn)
        Dialog.setTabOrder(self.expense_btn, self.appointment_btn)
        Dialog.setTabOrder(self.appointment_btn, self.dentist_btn)
        Dialog.setTabOrder(self.dentist_btn, self.q1_y_check)
        Dialog.setTabOrder(self.q1_y_check, self.q2_y_check)
        Dialog.setTabOrder(self.q2_y_check, self.q3_y_check)
        Dialog.setTabOrder(self.q3_y_check, self.q4_y_check)
        Dialog.setTabOrder(self.q4_y_check, self.q5_y_check)
        Dialog.setTabOrder(self.q5_y_check, self.q6_y_check)
        Dialog.setTabOrder(self.q6_y_check, self.q7_y_check)
        Dialog.setTabOrder(self.q7_y_check, self.q8_y_check)
        Dialog.setTabOrder(self.q8_y_check, self.q9_y_check)
        Dialog.setTabOrder(self.q9_y_check, self.q10_y_check)
        Dialog.setTabOrder(self.q10_y_check, self.q11_y_check)
        Dialog.setTabOrder(self.q11_y_check, self.q12_y_check)
        Dialog.setTabOrder(self.q12_y_check, self.q13_y_check)
        Dialog.setTabOrder(self.q13_y_check, self.q14_y_check)
        Dialog.setTabOrder(self.q14_y_check, self.q15_y_check)
        Dialog.setTabOrder(self.q15_y_check, self.q16_y_check)
        Dialog.setTabOrder(self.q16_y_check, self.med_find_edit)
        Dialog.setTabOrder(self.med_find_edit, self.save_pat)
        Dialog.setTabOrder(self.save_pat, self.restart_btn)
        Dialog.setTabOrder(self.restart_btn, self.dash_btn)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.dash_btn.setText(_translate("Dialog", "Dashboard"))
        self.appointment_btn.setText(_translate("Dialog", "Appointments"))
        self.dentist_btn.setText(_translate("Dialog", "Dentists"))
        self.payment_btn.setText(_translate("Dialog", "Payments"))
        self.expense_btn.setText(_translate("Dialog", "Expense"))
        self.label_6.setText(_translate("Dialog", " Medico App "))
        self.patient_btn.setText(_translate("Dialog", "Patients"))
        self.q1.setText(_translate("Dialog", "  1.Blood diasease ?"))
        self.q2.setText(_translate("Dialog", "  2.Do You Smoke ?"))
        self.q3.setText(_translate("Dialog", "  3.Bleeding disorder ?"))
        self.q4.setText(_translate("Dialog", "  4.Do you have Hepatitis ?"))
        self.q5.setText(_translate("Dialog", "  5.Do you have Diabetes ?"))
        self.q6.setText(_translate("Dialog", "  6.Do you Epilepsy ?"))
        self.q7.setText(_translate("Dialog", "  7.Do you have any cardiac or kidney diaseases ?"))
        self.q8.setText(_translate("Dialog", "  8.Do you have any abnormal blood pressure ?"))
        self.q9.setText(_translate("Dialog", "  9.Are you currently on any medications ?"))
        self.q10.setText(_translate("Dialog", "  10.Do you have any respitory diasease/ asthma ?"))
        self.q11.setText(_translate("Dialog", "  11.Do your gums bleed when you brush your teeth ?"))
        self.q12.setText(_translate("Dialog", "  12.Allergies (penicillin, aspirin,local anesthesia , codeine ,others ?"))
        self.q13.setText(_translate("Dialog", "  13.Do your consider yourself to be a nervous person ?"))
        self.q14.setText(_translate("Dialog", "  14.(Female) Currently Pregnant ?"))
        self.q15.setText(_translate("Dialog", "  15.(Female) Currently breastfeeding ?"))
        self.q16.setText(_translate("Dialog", "  16.Do you have any other chronic diasease not stated above ?"))
        self.findings_label_2.setText(_translate("Dialog", "  Medical History"))
        self.findings_label.setText(_translate("Dialog", "  Medical Findings"))
        self.save_pat.setText(_translate("Dialog", "Save and add patient"))
        self.restart_btn.setText(_translate("Dialog", "Restart "))
