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
        square_brush = QtGui.QBrush(QtCore.Qt.black)
        painter.setBrush(square_brush)
        
        # placement and size relative to window size
        M = [self.width() / 4, self.height() / 4]
        r = min(self.width(), self.height()) / 4
        rect = QtCore.QRectF(M[0]-r, M[1]-r, 2*r, 2*r)
        
        painter.drawRect(rect)
        
        painter.setBackground(QtCore.Qt.green)
        
        diceMap = QtGui.QPixmap(self).loadFromData()
        
        
        
if __name__ == "__main__":
    import sys
    # In Spyder kann nur eine Qt-Applikation laufen und sie werden nicht anschliessend geloescht
    if QtCore.QCoreApplication.instance() is not None:
        app = QtCore.QCoreApplication.instance()
    else:
        app = QtWidgets.QApplication(sys.argv)
        
    dice = DiceWidget()
    dice.resize(400,200)
    dice.show()
    sys.exit(app.exec_())    