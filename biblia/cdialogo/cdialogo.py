#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui, QtCore
 
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

class Segundaventada(QtGui.QWidget):
    def __init__(self, name=None):
        super(Segundaventada, self).__init__()
        self.name = name
        self.initUI()
 
    def initUI(self):

        
        self.ventana2 = QtGui.QLabel(self)
        self.ventana2.setText("Cumplidos los ocho días para circuncidar al niño, le pusieron por nombre JESÚS, el cual le había sido puesto por el ángel antes que fuese concebido")
        self.ventana2.move(30, 20)

        self.setGeometry(300, 300, 250, 180)
        self.setWindowTitle('Versiculo - Iglesia Nueva Vida %s' % self.name)
        self.show()
 
 
class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.children = []
        self.initUI()
        
    def initUI(self):
        reload(sys)
        sys.setdefaultencoding("utf-8")
        
        #etiqueta libro
        self.libro = QtGui.QLabel(self)
        self.libro.setText("Libro")
        self.libro.move(30, 20)
        #caracteres en linea correspondientes al libro
        self.llibro = QtGui.QLineEdit(self)
        self.llibro.move(140, 20)

        #etiqueta capitulo
        self.cap = QtGui.QLabel(self)
        self.cap.setText(_fromUtf8("Capítulo"))
        self.cap.move(30, 60)
        #caracteres en linea correspondientes al capitulo
        self.lcap = QtGui.QLineEdit(self)
        self.lcap.move(140, 60)
        print self.cap

        #etiqueta capitulo
        self.vers = QtGui.QLabel(self)
        self.vers.setText(_fromUtf8("Versículo"))
        self.vers.move(30, 100)
        self.vers.setObjectName(_fromUtf8(str(self.vers)))
        print self.vers
        #caracteres en linea correspondientes al capitulo
        self.lvers = QtGui.QLineEdit(self)
        self.lvers.move(140, 100)
        self.lvers.setObjectName(_fromUtf8("versiculo"))
        print self.lvers

        btn1 = QtGui.QPushButton("Cerrar", self)
        btn1.move(50, 200)
        btn1 = QtGui.QPushButton("Buscar", self)
        btn1.move(170, 200)

        btn1.clicked.connect(self.buttonClicked)
        x, y, w, h = 1200, 500, 390, 450
        self.setGeometry(x, y, w, h)
        self.setWindowTitle('Espada viva - Iglesia Nueva Vida')
        self.show()

    def buttonClicked(self):
        child = Segundaventada(name=self.llibro)
        self.children.append(child)
 
def main():
    app = QtGui.QApplication(sys.argv)
    main_window = MainWindow()
    sys.exit(app.exec_())
 
 
if __name__ == '__main__':
    main()