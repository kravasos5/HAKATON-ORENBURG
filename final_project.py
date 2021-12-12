# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_with_bg.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

massive_problem = []

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
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 3, 1261, 711))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 4, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 0, 0, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(self.layoutWidget)
        self.textEdit.setMinimumSize(QtCore.QSize(700, 500))
        self.textEdit.setMaximumSize(QtCore.QSize(700, 500))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.textEdit.setFont(font)
        self.textEdit.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 3, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
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
        self.clean = QtWidgets.QPushButton(self.layoutWidget)
        self.clean.setMinimumSize(QtCore.QSize(220, 55))
        self.clean.setMaximumSize(QtCore.QSize(220, 55))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.clean.setFont(font)
        self.clean.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.clean.setToolTipDuration(-1)
        self.clean.setStatusTip("")
        self.clean.setStyleSheet("background-color: #3DC4F5;\n"
"color: #2E2E2E;\n"
"border-radius: 20px;")
        self.clean.setObjectName("clean")

        self.clean.clicked.connect(self.steret)

        self.horizontalLayout.addWidget(self.clean)
        self.report = QtWidgets.QPushButton(self.layoutWidget)
        self.report.setMinimumSize(QtCore.QSize(220, 55))
        self.report.setMaximumSize(QtCore.QSize(220, 55))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.report.setFont(font)
        self.report.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.report.setStyleSheet("background-color: #3DC4F5;\n"
"color: #2E2E2E;\n"
"border-radius: 20px;")
        self.report.setObjectName("report")

        self.report.clicked.connect(self.pup)

        self.horizontalLayout.addWidget(self.report)
        self.gridLayout.addLayout(self.horizontalLayout, 5, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 6, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1280, 720))
        self.label.setMinimumSize(QtCore.QSize(1280, 720))
        self.label.setMaximumSize(QtCore.QSize(1280, 720))
        self.label.setText("")
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setPixmap(QtGui.QPixmap("дизайн/bg4.jpg"))
        self.label.setScaledContents(True)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.label.raise_()
        self.layoutWidget.raise_()
        Otvetstvenniy.setCentralWidget(self.centralwidget)
        self.retranslateUi(Otvetstvenniy)
        QtCore.QMetaObject.connectSlotsByName(Otvetstvenniy)

    def pup(self):
        text = self.textEdit.toPlainText()
        massive_texta = text.split(' ')
        problem = ['яма', 'ямы', 'яме', 'яму', 'ямой', 'ям', 'ямам', 'ямами', 'ямах', 'ямки', 'светофор', 'светофора',
                   'светофору', 'светофором', 'светофоре', 'светофоры', 'светофоров','светофорам', 'светофорами',
                   'светофорах', 'мусор', 'мусора', 'мусору', 'мусором', 'мусоре']
        massive_peresecheniy = list(set(massive_texta)&set(problem))
        for i in range(len(massive_texta)):
            if massive_texta[i] in problem:
                print('')

                spasibo = QMessageBox()
                spasibo.setWindowTitle('Спасибо за обращение!')
                spasibo.setText('Благодарим за Ваше обращение. Вскоре проблема будет решена.')
                spasibo.setIcon(QMessageBox.Question)
                spasibo.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                spasibo.setDefaultButton(QMessageBox.Close)
                spasibo.setInformativeText('Вы помогаете сделать город лучше!')
                spasibo.buttonClicked.connect(self.obrashaisa)

                spasibo.exec_()
                if massive_texta[i] in massive_problem:
                    spasibo = QMessageBox()
                    spasibo.setWindowTitle('Спасибо за обращение!')
                    spasibo.setText('Эта проблема уже решается.')
                    spasibo.setIcon(QMessageBox.Question)
                    spasibo.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                    spasibo.setDefaultButton(QMessageBox.Close)
                    spasibo.buttonClicked.connect(self.obrashaisa)

                    spasibo.exec_()
                else:
                    g.append(massive_texta[i])
                break
            elif massive_texta[i] not in problem:
                print('')

                spasibo = QMessageBox()
                spasibo.setWindowTitle('Спасибо за обращение!')
                spasibo.setText('Благодарим за Ваше обращение. Вскоре проблема будет решена.')
                spasibo.setIcon(QMessageBox.Question)
                spasibo.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                spasibo.setDefaultButton(QMessageBox.Close)
                spasibo.setInformativeText('Вы помогаете сделать город лучше!')
                spasibo.buttonClicked.connect(self.obrashaisa)

                spasibo.exec_()
                if massive_texta[i] in massive_problem:
                    spasibo = QMessageBox()
                    spasibo.setWindowTitle('Спасибо за обращение!')
                    spasibo.setText('Благодарим за Ваше обращение. Эта проблема уже решается.')
                    spasibo.setIcon(QMessageBox.Question)
                    spasibo.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                    spasibo.setDefaultButton(QMessageBox.Close)
                    spasibo.setInformativeText('Вы помогаете сделать город лучше!')
                    spasibo.buttonClicked.connect(self.obrashaisa)

                    spasibo.exec_()
                break
        massive_konechniy = massive_problem + massive_peresecheniy
        massive_konechniy = list(set(massive_konechniy))
        print(massive_konechniy)




    def ne_sas(self):
        ne_spasibo = QMessageBox()
        ne_spasibo.setWindowTitle('Ne pup')
        ne_spasibo.setText('Ne pup')
        ne_spasibo.setIcon(QMessageBox.Information)
        ne_spasibo.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        ne_spasibo.setDefaultButton(QMessageBox.Close)
        ne_spasibo.setInformativeText('Ne pup')
        ne_spasibo.buttonClicked.connect(self.obrashaisa)

        ne_spasibo.exec_()


    def sas(self):
        spasibo = QMessageBox()
        spasibo.setWindowTitle('Спасибо за обращение!')
        spasibo.setText('Благодарим за Ваше обращение. Вскоре проблема будет решена.')
        spasibo.setIcon(QMessageBox.Question)
        spasibo.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel)
        spasibo.setDefaultButton(QMessageBox.Close)
        spasibo.setInformativeText('Вы помогаете сделать город лучше!')
        spasibo.buttonClicked.connect(self.obrashaisa)

        spasibo.exec_()



    def obrashaisa(self, btn):
        if btn.text() == 'OK':
            self.textEdit.setText('')
            self.textEdit.setFocus()
        elif btn.text() == 'Cancel':
            print('Спасибо')


    def steret(self):
        self.textEdit.setText('')
        self.textEdit.setFocus()

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
