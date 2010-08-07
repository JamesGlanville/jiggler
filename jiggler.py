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
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)

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
		xbox = QtGui.QTextEdit()
		ybox = QtGui.QTextEdit()
		zbox = QtGui.QTextEdit()
		slider = QtGui.QSlider(QtCore.Qt.Horizontal, self)

		grid = QtGui.QGridLayout()
		grid.setSpacing(10)
		grid.addWidget(zerox,1,1)
		grid.addWidget(zeroy,2,1)
		grid.addWidget(zeroz,3,1)
		grid.addWidget(xbox,1,2)
		grid.addWidget(ybox,2,2)
		grid.addWidget(zbox,3,2)
		grid.addWidget(slider,1,3,1,10)
#		xbox.setGeometry(50, 10, 60, 35)
		#self.connect(slider, QtCore.SIGNAL('valueChanged(int)'), xbox,
		#QtCore.SLOT('display(int)'))
		self.setLayout(grid)

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
