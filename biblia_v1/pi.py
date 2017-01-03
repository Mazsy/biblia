# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'biblie.ui'
#
# Created: Tue Dec 20 23:13:22 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_NuevaVida(object):
    def setupUi(self, NuevaVida):
        NuevaVida.setObjectName(_fromUtf8("NuevaVida"))
        NuevaVida.resize(800, 600)
        self.centralwidget = QtGui.QWidget(NuevaVida)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.capitulo = QtGui.QLabel(self.centralwidget)
        self.capitulo.setGeometry(QtCore.QRect(20, 130, 68, 22))
        self.capitulo.setObjectName(_fromUtf8("capitulo"))
        self.versiculo_2 = QtGui.QLabel(self.centralwidget)
        self.versiculo_2.setGeometry(QtCore.QRect(20, 180, 68, 22))
        self.versiculo_2.setObjectName(_fromUtf8("versiculo_2"))
        self.libro = QtGui.QLabel(self.centralwidget)
        self.libro.setGeometry(QtCore.QRect(30, 80, 68, 22))
        self.libro.setObjectName(_fromUtf8("libro"))
        self.libro_2 = QtGui.QLineEdit(self.centralwidget)
        self.libro_2.setGeometry(QtCore.QRect(180, 80, 191, 32))
        self.libro_2.setObjectName(_fromUtf8("libro_2"))
        self.capitulo_2 = QtGui.QLineEdit(self.centralwidget)
        self.capitulo_2.setGeometry(QtCore.QRect(180, 120, 113, 32))
        self.capitulo_2.setObjectName(_fromUtf8("capitulo_2"))
        self.versiculo = QtGui.QLineEdit(self.centralwidget)
        self.versiculo.setGeometry(QtCore.QRect(180, 170, 113, 32))
        self.versiculo.setObjectName(_fromUtf8("versiculo"))
        self.btn_Cargar = QtGui.QPushButton(self.centralwidget)
        self.btn_Cargar.setGeometry(QtCore.QRect(180, 230, 100, 32))
        self.btn_Cargar.setObjectName(_fromUtf8("btn_Cargar"))
        self.lista = QtGui.QListWidget(self.centralwidget)
        self.lista.setGeometry(QtCore.QRect(430, 80, 256, 192))
        self.lista.setObjectName(_fromUtf8("lista"))
        NuevaVida.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(NuevaVida)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 32))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        NuevaVida.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(NuevaVida)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        NuevaVida.setStatusBar(self.statusbar)

        self.retranslateUi(NuevaVida)
        QtCore.QMetaObject.connectSlotsByName(NuevaVida)

    def retranslateUi(self, NuevaVida):
        NuevaVida.setWindowTitle(_translate("NuevaVida", "MainWindow", None))
        self.capitulo.setText(_translate("NuevaVida", "capitulo", None))
        self.versiculo_2.setText(_translate("NuevaVida", "versiculo", None))
        self.libro.setText(_translate("NuevaVida", "libro", None))
        self.btn_Cargar.setText(_translate("NuevaVida", "Cargar", None))

