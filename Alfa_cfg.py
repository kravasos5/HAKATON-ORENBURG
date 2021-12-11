# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Otvetstvenniy(object):
    def setupUi(self, Otvetstvenniy):
        Otvetstvenniy.setObjectName("Otvetstvenniy")
        Otvetstvenniy.resize(1280, 720)
        Otvetstvenniy.setMinimumSize(QtCore.QSize(1280, 720))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        Otvetstvenniy.setFont(font)
        Otvetstvenniy.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(Otvetstvenniy)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-20, -10, 1311, 741))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("дизайн/bg2.jpg"))
        self.label.setObjectName("label")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 3, 1261, 711))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 4, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 0, 0, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(self.widget)
        self.textEdit.setMinimumSize(QtCore.QSize(700, 500))
        self.textEdit.setMaximumSize(QtCore.QSize(700, 500))
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 3, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 55))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAutoFillBackground(False)
        self.label_2.setStyleSheet("color: #2E2E2E;\n"
"")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setWordWrap(False)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.clean = QtWidgets.QPushButton(self.widget)
        self.clean.setMinimumSize(QtCore.QSize(220, 55))
        self.clean.setMaximumSize(QtCore.QSize(220, 55))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.clean.setFont(font)
        self.clean.setStyleSheet("background-color: #3DC4F5;\n"
"color: #2E2E2E;\n"
"border-radius: 20px;")
        self.clean.setObjectName("clean")
        self.horizontalLayout.addWidget(self.clean)
        self.report = QtWidgets.QPushButton(self.widget)
        self.report.setMinimumSize(QtCore.QSize(220, 55))
        self.report.setMaximumSize(QtCore.QSize(220, 55))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.report.setFont(font)
        self.report.setStyleSheet("background-color: #3DC4F5;\n"
"color: #2E2E2E;\n"
"border-radius: 20px;")
        self.report.setObjectName("report")
        self.horizontalLayout.addWidget(self.report)
        self.gridLayout.addLayout(self.horizontalLayout, 5, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 6, 0, 1, 1)
        self.label.raise_()
        self.label_2.raise_()
        self.clean.raise_()
        self.report.raise_()
        self.textEdit.raise_()
        Otvetstvenniy.setCentralWidget(self.centralwidget)

        self.retranslateUi(Otvetstvenniy)
        QtCore.QMetaObject.connectSlotsByName(Otvetstvenniy)

    def retranslateUi(self, Otvetstvenniy):
        _translate = QtCore.QCoreApplication.translate
        Otvetstvenniy.setWindowTitle(_translate("Otvetstvenniy", "Ответственный гражданин"))
        self.label_2.setText(_translate("Otvetstvenniy", "Опишите проблему"))
        self.clean.setText(_translate("Otvetstvenniy", "Стереть все"))
        self.report.setText(_translate("Otvetstvenniy", "Сообщить о проблеме"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Otvetstvenniy = QtWidgets.QMainWindow()
    ui = Ui_Otvetstvenniy()
    ui.setupUi(Otvetstvenniy)
    Otvetstvenniy.show()
    sys.exit(app.exec_())
