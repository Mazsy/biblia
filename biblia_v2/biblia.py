#!/usr/bin/python
# -*- coding: utf-8 -*-
 
# Aplicacion grafica con sqlite3
# www.pythondiario.com
  
import sys
import sqlite3
from PyQt4 import QtCore, QtGui, uic
import pi_ui

class MyWindowClass(QtGui.QMainWindow, pi_ui.Ui_NuevaVida):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.btn_Cargar.clicked.connect(self.btn_Cargar_clicked)

# Evento del boton Caragar
    def btn_Cargar_clicked(self):
        import sys
        reload(sys)
        sys.setdefaultencoding("utf-8")

        self.con = sqlite3.connect("/home/maxs/Escritorio/proy_biblia/biblia/bad.sqlite")
        self.cursor = self.con.cursor()

#         # Datos
        self.libro = str(self.libro_2.text())
        self.capitulo = str(self.capitulo_2.text())
        self.versiculo = str(self.versiculo.text())
        print self.libro
        print self.capitulo
        print self.versiculo
   
        # Se cargan los datos indicados de la tabla
        self.cursor.execute(" select verse.text, book.name, verse.chapter, verse.verse " 
        					"from verse inner join book where chapter=? and verse=?" 
        					"and book.name=? and verse.book_id = book.id ;", (self.capitulo ,self.versiculo, self.libro))

        # Al presionar el boton lo primero es borrar todos los datos
        self.lista.clear()
        print "llegue"
        # Se agregan los elementos al QListWidget
        for i in self.cursor:
            self.nombre = (str(i[0]))
        self.lista.addItem(self.nombre )
        self.con.commit()
        self.con.close()

def main():
    app = QtGui.QApplication(sys.argv)
    MyWindow = MyWindowClass(None)
    MyWindow.show()
    app.exec_()

if __name__ == "__main__":
    main()