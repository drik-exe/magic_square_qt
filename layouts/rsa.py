# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rsa.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.encrypt = QtWidgets.QPushButton(self.centralwidget)
        self.encrypt.setGeometry(QtCore.QRect(530, 50, 121, 41))
        self.encrypt.setObjectName("encrypt")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 30, 191, 21))
        self.label_4.setObjectName("label_4")
        self.decrypt = QtWidgets.QPushButton(self.centralwidget)
        self.decrypt.setGeometry(QtCore.QRect(530, 120, 121, 41))
        self.decrypt.setObjectName("decrypt")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(310, 40, 181, 21))
        self.label_5.setObjectName("label_5")
        self.mes = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.mes.setGeometry(QtCore.QRect(30, 60, 261, 41))
        self.mes.setObjectName("mes")
        self.dec_mes = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.dec_mes.setGeometry(QtCore.QRect(310, 60, 211, 41))
        self.dec_mes.setObjectName("dec_mes")
        self.open_key = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.open_key.setGeometry(QtCore.QRect(30, 130, 491, 161))
        self.open_key.setObjectName("open_key")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(30, 110, 191, 21))
        self.label_6.setObjectName("label_6")
        self.save = QtWidgets.QPushButton(self.centralwidget)
        self.save.setGeometry(QtCore.QRect(680, 50, 121, 41))
        self.save.setObjectName("save")
        self.open = QtWidgets.QPushButton(self.centralwidget)
        self.open.setGeometry(QtCore.QRect(680, 120, 121, 41))
        self.open.setObjectName("open")
        self.closed_key = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.closed_key.setGeometry(QtCore.QRect(30, 330, 861, 251))
        self.closed_key.setObjectName("closed_key")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(30, 300, 191, 21))
        self.label_7.setObjectName("label_7")
        self.generate = QtWidgets.QPushButton(self.centralwidget)
        self.generate.setGeometry(QtCore.QRect(530, 190, 271, 41))
        self.generate.setObjectName("generate")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.encrypt.setText(_translate("MainWindow", "Зашифровать"))
        self.label_4.setText(_translate("MainWindow", "Сообщение для шифрования"))
        self.decrypt.setText(_translate("MainWindow", "Дешифровать"))
        self.label_5.setText(_translate("MainWindow", "Зашифрованное сообщение"))
        self.label_6.setText(_translate("MainWindow", "Открытый ключ"))
        self.save.setText(_translate("MainWindow", "Сохранить"))
        self.open.setText(_translate("MainWindow", "Открыть"))
        self.label_7.setText(_translate("MainWindow", "Закрытый ключ"))
        self.generate.setText(_translate("MainWindow", "Сгенерировать ключи"))
