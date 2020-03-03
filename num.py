# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'num.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 40, 131, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 100, 131, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEditfirstnumb = QtWidgets.QLineEdit(Dialog)
        self.lineEditfirstnumb.setGeometry(QtCore.QRect(180, 40, 113, 20))
        self.lineEditfirstnumb.setObjectName("lineEditfirstnumb")
        self.lineEdit_2secondnumb = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2secondnumb.setGeometry(QtCore.QRect(180, 100, 113, 20))
        self.lineEdit_2secondnumb.setObjectName("lineEdit_2secondnumb")
        self.pushButtonaddnumb = QtWidgets.QPushButton(Dialog)
        self.pushButtonaddnumb.setGeometry(QtCore.QRect(110, 170, 111, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonaddnumb.setFont(font)
        self.pushButtonaddnumb.setObjectName("pushButtonaddnumb")
        self.labelresponse = QtWidgets.QLabel(Dialog)
        self.labelresponse.setGeometry(QtCore.QRect(60, 230, 261, 20))
        self.labelresponse.setObjectName("labelresponse")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "ENTER FIRST NUMBER"))
        self.label_2.setText(_translate("Dialog", "ENTER SECOND NUMBER"))
        self.pushButtonaddnumb.setText(_translate("Dialog", "ADD"))
        self.labelresponse.setText(_translate("Dialog", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
