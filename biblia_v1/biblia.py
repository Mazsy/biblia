#!/usr/bin/python
# -*- coding: utf-8 -*-
 
# Aplicacion grafica con sqlite3
# www.pythondiario.com
  
import sys
import sqlite3
from PyQt4 import QtCore, QtGui, uic
 
# Cargar nuestro archivo .ui
form_class = uic.loadUiType("biblie.ui")[0]
 
class MyWindowClass(QtGui.QMainWindow, form_class):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
#        self.btn_Guardar.clicked.connect(self.btn_Guardar_clicked)
        self.btn_Cargar.clicked.connect(self.btn_Cargar_clicked)
    #     self.IniciarBase()


    # def IniciarBase(self):
    #     self.con = sqlite3.connect("/home/maxs/Escritorio/proy_biblia/biblia/bad.sqlite")
    #     self.cursor = self.con.cursor()
    #     cursor.execute(" select text from verse where chapter=3 and verse=2 and book_id = 8;")
    #     self.con.commit()

# # Evento del boton Guardar
#     def btn_Guardar_clicked(self):

#         self.con = sqlite3.connect("/home/maxs/Escritorio/proy_biblia/prueba.bd")
#         self.cursor = self.con.cursor()

#         # Datos
#         self.nombre = str(self.lineEdit.text())
#         self.apellido = str(self.lineEdit_2.text())
#         self.localidad = str(self.lineEdit_3.text())
#         self.datos = (self.nombre, self.apellido, self.localidad)

#         # Inserta los datos en la tabla campos
#         self.cursor.execute("INSERT INTO campos (nombre, apellido, localidad) VALUES (?,?,?)", self.datos)
#         self.con.commit()

#         # Quedan los campos vacios al guardar cliente
#         self.lineEdit.setText("")
#         self.lineEdit_2.setText("")
#         self.lineEdit_3.setText("")

#         self.con.commit()
#         self.con.close()

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
        self.cursor.execute("select text from verse where chapter=? and verse=? and book_id=? ;", (self.capitulo ,self.versiculo, self.libro))

        # Al presionar el boton lo primero es borrar todos los datos
        self.lista.clear()
        print "llegue"
        # Se agregan los elementos al QListWidget
        for i in self.cursor:
            # unicode(i[0].decode('utf-8')) 
            self.nombre = (str(i[0]))
        print self.nombre

        self.lista.addItem(self.nombre )

        self.con.commit()
        self.con.close()
    
  
app = QtGui.QApplication(sys.argv)
MyWindow = MyWindowClass(None)
MyWindow.show()
app.exec_()