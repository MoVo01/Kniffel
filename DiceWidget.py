# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 21:55:27 2020

@author: luisw
"""


from PyQt5 import QtCore, QtGui, QtWidgets

class DiceWidget(QtWidgets.QWidget):
    
    def __init__(self, parent=None):
        super().__init__(parent)   
        # generate mouse move events (see below)
        #self.setMouseTracking(True)
    
    def paintEvent(self, event):
        super().paintEvent(event)
        
        painter = QtGui.QPainter(self)
        painter.setRenderHints(QtGui.QPainter.Antialiasing)
        
        painter.setPen(QtCore.Qt.NoPen) # no boundary
        circle_brush = QtGui.QBrush(QtCore.Qt.black)
        painter.setBrush(circle_brush)
        
        
        
        
if __name__ == "__main__":
    import sys
    # In Spyder kann nur eine Qt-Applikation laufen und sie werden nicht anschliessend geloescht
    if QtCore.QCoreApplication.instance() is not None:
        app = QtCore.QCoreApplication.instance()
    else:
        app = QtWidgets.QApplication(sys.argv)