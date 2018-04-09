# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'packet.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import os
class Ui_Dialog(object):
    def do(self):
	os.system("sudo python snif.py > sniffed-packets.txt")

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(640, 402)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(190, 30, 341, 31))
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(180, 80, 311, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.capture = QtWidgets.QPushButton(Dialog)
        self.capture.setGeometry(QtCore.QRect(180, 160, 271, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.capture.setFont(font)
        self.capture.setObjectName("capture")
	self.capture.clicked.connect(self.do)
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(180, 260, 271, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Packet  sniffer"))
        self.label.setText(_translate("Dialog", "Welcome to packet capture "))
        self.label_2.setText(_translate("Dialog", "Please Select a option to continue"))
        self.capture.setText(_translate("Dialog", "Capture Packets"))
        self.pushButton_2.setText(_translate("Dialog", "Display Packets"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

