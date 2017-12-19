#!/usr/bin/python
# -*- coding: UTF-8 -*-
#coding=utf-8



import sys
from PyQt4 import QtGui

app = QtGui.QApplication(sys.argv)
widget = QtGui.QWidget()
widget.resize(250, 150)
widget.setWindowTitle('PyQt for the')
widget.show()
sys.exit(app.exec_())

