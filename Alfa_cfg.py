# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'гражданин.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Otvetstvenniy(object):
    def setupUi(self, Otvetstvenniy):
        Otvetstvenniy.setObjectName("Otvetstvenniy")
        Otvetstvenniy.resize(1100, 850)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        Otvetstvenniy.setFont(font)
        Otvetstvenniy.setStyleSheet("\n"
"")
        self.centralwidget = QtWidgets.QWidget(Otvetstvenniy)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 401, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(0, 85, 255);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(450, 100, 250, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("")
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(200, 690, 200, 55))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(0, 255, 0);\n"
"\n"
"color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(680, 690, 220, 55))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(0, 255, 0);\n"
"\n"
"color: rgb(255, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(200, 150, 700, 500))
        self.textEdit.setObjectName("textEdit")
        Otvetstvenniy.setCentralWidget(self.centralwidget)

        self.retranslateUi(Otvetstvenniy)
        QtCore.QMetaObject.connectSlotsByName(Otvetstvenniy)

    def retranslateUi(self, Otvetstvenniy):
        _translate = QtCore.QCoreApplication.translate
        Otvetstvenniy.setWindowTitle(_translate("Otvetstvenniy", "Ответственный гражданин"))
        self.label.setText(_translate("Otvetstvenniy", "Тут должна быть картинка"))
        self.label_2.setText(_translate("Otvetstvenniy", "Опишите проблему"))
        self.pushButton.setText(_translate("Otvetstvenniy", "Стереть все"))
        self.pushButton_2.setText(_translate("Otvetstvenniy", "Сообщить о проблеме"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Otvetstvenniy = QtWidgets.QMainWindow()
    ui = Ui_Otvetstvenniy()
    ui.setupUi(Otvetstvenniy)
    Otvetstvenniy.show()
    sys.exit(app.exec_())
