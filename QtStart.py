# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 21:56:15 2020

@author: luisw
"""


import sys
from PyQt5 import QtCore, QtWidgets, uic
from DiceWidget import DiceWidget


Ui_MainWindow, WindowBaseClass = uic.loadUiType("GUI.ui")

class MyDialog(WindowBaseClass, Ui_MainWindow):
    def __init__(self, parent=None):
        WindowBaseClass.__init__(self, parent)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
    
if __name__ == "__main__":
    if QtCore.QCoreApplication.instance() is not None:
        app = QtCore.QCoreApplication.instance()
    else:
        app = QtWidgets.QApplication(sys.argv)

    dialog = MyDialog()
    dialog.show()
    sys.exit(app.exec_())