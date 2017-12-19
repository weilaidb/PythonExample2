#!/usr/bin/python
# -*- coding: UTF-8 -*-
#coding=utf-8


import sys
import sqlite3
from PyQt4 import QtGui
from PyQt4 import QtCore

#self define
from icon import *







##main start
app = QtGui.QApplication(sys.argv)
# icon = Icon()
# icon.show()
widget = QtGui.QWidget()
widget.resize(600, 400)
widget.setWindowTitle('AutoTest')
widget.setWindowIcon(QtGui.QIcon('icons/att.png'))
widget.setToolTip('This is a <b>Auto Test</b> widget')
QtGui.QToolTip.setFont(QtGui.QFont('OldEnglish', 10))

#####################################################
quitbtn=QtGui.QPushButton('Close',widget)
quitbtn.setGeometry(10,10,60,35)
messageboxbtn=QtGui.QPushButton('MessageBox',widget)
messageboxbtn.setGeometry(10,55,100,35)

widget.show()


def method_name():
    qb = MessageBox()
    qb.show()
    return qb

qb = method_name()
sys.exit(app.exec_())

