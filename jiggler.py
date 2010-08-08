#!/usr/bin/python

import sys
from PyQt4 import QtGui, QtCore

def zero(axis):
	print "zeroing ",axis

class Jiggler(QtGui.QWidget):
	def zerox(self):
		zero("x")	
	def zeroy(self):
		zero("y")	
	def zeroz(self):
		zero("z")	
	def setspeed(self,name):
		print name
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)
		xspeed=40
		self.setGeometry(0, 0, 450, 300)
		self.setWindowTitle('Jiggler')

		quit = QtGui.QPushButton('Close', self)
		quit.setGeometry(370, 250, 60, 35)

		zerox = QtGui.QPushButton('Zero X',self)
		zerox.setGeometry(10, 10, 60, 35)
		zeroy = QtGui.QPushButton('Zero Y',self)
		zeroy.setGeometry(10, 45, 60, 35)
		zeroz = QtGui.QPushButton('Zero Z',self)
		zeroz.setGeometry(10, 80, 60, 35)
		xbox = QtGui.QTextEdit(str(xspeed),self)
		ybox = QtGui.QTextEdit()
		zbox = QtGui.QTextEdit()
		slider = QtGui.QSlider(QtCore.Qt.Horizontal, self)

		xbox.setGeometry(80, 15, 40, 30)
		slider.setGeometry(120,15,150,150)
		self.connect(slider, QtCore.SIGNAL('valueChanged(int)'), self,
		QtCore.SLOT('setspeed(int,"char")'))
		#self.setLayout(grid)

		self.connect(quit, QtCore.SIGNAL('clicked()'), \
			QtGui.qApp, QtCore.SLOT('quit()'))

		self.connect(zerox, QtCore.SIGNAL('clicked()'), \
			self.zerox)
		self.connect(zeroy, QtCore.SIGNAL('clicked()'), \
			self.zeroy)
		self.connect(zeroz, QtCore.SIGNAL('clicked()'), \
			self.zeroz)
			



app = QtGui.QApplication(sys.argv)
qb = Jiggler()
qb.show()
sys.exit(app.exec_())
