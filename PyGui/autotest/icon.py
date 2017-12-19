# -*- coding: UTF-8 -*-
#coding=utf-8

import  sys
from PyQt4 import QtGui,QtCore;

class Icon(QtGui.QWidget):
    def __index__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)
        self.setGeometry(300,300,250,150)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QtGui.QIcon('icons/web.png'))



class MessageBox(QtGui.QWidget):
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self,parent)
        self.setGeometry(300,300,250,150)
        self.setWindowTitle('message box')

        def closeEvent(self, event):
            print('close event')
            reply = QtGui.QMessageBox.question(self, 'Message',
                                               "Are you sure to quit?", QtGui.QMessageBox.Yes,
                                               QtGui.QMessageBox.No)
            if reply == QtGui.QMessageBox.Yes:
                event.accept()
            else:
                event.ignore()



class Calendar(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self)
        self.setGeometry(300,300,350,300)
        self.setWindowTitle('Calendar')
        self.cal = QtGui.QCalendarWidget(self)
        self.cal.setGridVisible(True)
        self.connect(self.cal, QtCore.SIGNAL('selectionChanged()'),
                                             self.showDate)
        self.label = QtGui.QLabel(self)
        date = self.cal.selectedDate()
        self.label.setText(str(date.toPyDate()))
        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(self.cal)
        vbox.addWidget(self.label)
        self.setLayout(vbox)

    def showDate(self):
        date = self.cal.selectedDate()
        self.label.setText(str(date.toPyDate()))



#[MessageBox]
# app = QtGui.QApplication(sys.argv)
# qb = MessageBox()
# qb.show()
# sys.exit(app.exec_())

#[Calendar]
app = QtGui.QApplication(sys.argv)
w = Calendar()
w.show()
sys.exit(app.exec_())

