# -*- coding: utf-8 -*-
"""Interfaz de la aplicación"""
import os, sys

# Importamos los módulos de QT
from PyQt4 import QtCore, QtGui, uic

class Main(QtGui.QDialog):
	"""Ventana principal de la aplicación"""
	def __init__(self):
		QtGui.QDialog.__init__(self)
		# Cargamos la interfaz desde el archivo .ui
		uifile = os.path.join(os.path.abspath(os.path.dirname(__file__)),'MB.ui')
		uic.loadUi(uifile,self)

def main():
	app = QtGui.QApplication(sys.argv)
	window = Main()
	window.show()
	sys.exit(app.exec_())

if __name__ == "__main__":
	main()