# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 21:55:27 2020

@author: luisw
"""


import os
from DieRoll import DiceRoll
from PyQt5 import QtCore
from PyQt5.Qt import Qt
from PyQt5.QtGui import QPainter, QPixmap, QCursor, QBrush
from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication

class DiceWidget(QWidget):
    
    def __init__(self, parent=None):
        super().__init__(parent)   
        # generate mouse move events (see below)
        #self.setMouseTracking(True)
        
        self.dice_width = 20
        
        Eins = QPixmap(os.path.join("Würfel", "Eins"))
        Zwei = QPixmap(os.path.join("Würfel", "Zwei"))
        Drei = QPixmap(os.path.join("Würfel", "Drei"))
        Vier = QPixmap(os.path.join("Würfel", "Vier"))
        Fuenf = QPixmap(os.path.join("Würfel", "Fünf"))
        Sechs = QPixmap(os.path.join("Würfel", "Sechs"))
        
        
        self.eins= Eins
        #self.eins = Eins.scaledToWidth(self.dice_width, Qt.SmoothTransformation)
        self.zwei = Zwei.scaledToWidth(self.dice_width, Qt.SmoothTransformation)
        self.drei = Drei.scaledToWidth(self.dice_width, Qt.SmoothTransformation)
        self.vier = Vier.scaledToWidth(self.dice_width, Qt.SmoothTransformation)
        self.fuenf = Fuenf.scaledToWidth(self.dice_width, Qt.SmoothTransformation)
        self.sechs = Sechs.scaledToWidth(self.dice_width, Qt.SmoothTransformation)
        
    def paintEvent(self, event):
        super().paintEvent(event)
        
        painter = QPainter(self)
        
        
        painter.setPen(Qt.NoPen)
        painter.setBrush(Qt.darkGreen)
        painter.drawRect(event.rect())
        
        
        newRoll = DiceRoll()
        
        #newRoll.pick(1)
        #newRoll.pick(3)
        painter.drawPixmap(100, 100, self.eins)
        
        for i in range (0,len(newRoll.free_dice)):
            if newRoll.free_dice[i] == 1:
                painter.drawPixmap(self.width() * ((i+1) / (len(newRoll.free_dice)+1)),2 * self.height() / 3, self.eins)
            elif newRoll.free_dice[i] == 2:
                painter.drawPixmap(self.width() * ((i+1) / (len(newRoll.free_dice)+1)),2 * self.height() / 3, self.zwei)
            elif newRoll.free_dice[i] == 3:
                painter.drawPixmap(self.width() * ((i+1) / (len(newRoll.free_dice)+1)),2 * self.height() / 3, self.drei)
            elif newRoll.free_dice[i] == 4:
                painter.drawPixmap(self.width() * ((i+1) / (len(newRoll.free_dice)+1)),2 * self.height() / 3, self.vier)
            elif newRoll.free_dice[i] == 5:
                painter.drawPixmap(self.width() * ((i+1) / (len(newRoll.free_dice)+1)),2 * self.height() / 3, self.fuenf)
            elif newRoll.free_dice[i] == 6:
                painter.drawPixmap(self.width() * ((i+1) / (len(newRoll.free_dice)+1)),2 * self.height() / 3, self.sechs)
            else:
                print("SOmethings wrong")
          
        for i in range (0,len(newRoll.picked_dice)):
            if newRoll.picked_dice[i] == 1:
                painter.drawPixmap(self.width() * ((i+1) / (len(newRoll.picked_dice)+1)),self.height() / 3, self.eins)
            elif newRoll.picked_dice[i] == 2:
                painter.drawPixmap(self.width() * ((i+1) / (len(newRoll.picked_dice)+1)),self.height() / 3, self.zwei)
            elif newRoll.picked_dice[i] == 3:
                painter.drawPixmap(self.width() * ((i+1) / (len(newRoll.picked_dice)+1)),self.height() / 3, self.drei)
            elif newRoll.picked_dice[i] == 4:
                painter.drawPixmap(self.width() * ((i+1) / (len(newRoll.picked_dice)+1)),self.height() / 3, self.vier)
            elif newRoll.picked_dice[i] == 5:
                painter.drawPixmap(self.width() * ((i+1) / (len(newRoll.picked_dice)+1)),self.height() / 3, self.fuenf)
            elif newRoll.picked_dice[i] == 6:
                painter.drawPixmap(self.width() * ((i+1) / (len(newRoll.picked_dice)+1)),self.height() / 3, self.sechs)
            else:
                print("SOmethings wrong")
                
            
        
if __name__ == "__main__":
    import sys
    # In Spyder kann nur eine Qt-Applikation laufen und sie werden nicht anschliessend geloescht
    if QtCore.QCoreApplication.instance() is not None:
        app = QtCore.QCoreApplication.instance()
    else:
        app = QApplication(sys.argv)
        
    dice = DiceWidget()
    dice.resize(800,600)
    dice.show()
    sys.exit(app.exec_())

