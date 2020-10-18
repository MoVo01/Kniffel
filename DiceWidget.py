# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 21:55:27 2020

@author: luisw
"""


import os
from DiceRoll import DiceRoll, RollError
from PyQt5 import QtCore
from PyQt5.Qt import Qt
from PyQt5.QtGui import QPainter, QPixmap
from PyQt5.QtWidgets import QWidget, QApplication
from Categories import Categories

class DiceWidget(QWidget):
    
    statusUpdated = QtCore.pyqtSignal(str)
    RollSignal = QtCore.pyqtSignal()
    
    def __init__(self, parent=None):
        super().__init__(parent)   
        
        self.dice_width = self.width() / 9
        
        Eins = QPixmap(os.path.join("Würfel", "Eins"))
        Zwei = QPixmap(os.path.join("Würfel", "Zwei"))
        Drei = QPixmap(os.path.join("Würfel", "Drei"))
        Vier = QPixmap(os.path.join("Würfel", "Vier"))
        Fuenf = QPixmap(os.path.join("Würfel", "Fünf"))
        Sechs = QPixmap(os.path.join("Würfel", "Sechs"))
        
        
        self.eins = Eins.scaledToWidth(self.dice_width, Qt.SmoothTransformation)
        self.zwei = Zwei.scaledToWidth(self.dice_width, Qt.SmoothTransformation)
        self.drei = Drei.scaledToWidth(self.dice_width, Qt.SmoothTransformation)
        self.vier = Vier.scaledToWidth(self.dice_width, Qt.SmoothTransformation)
        self.fuenf = Fuenf.scaledToWidth(self.dice_width, Qt.SmoothTransformation)
        self.sechs = Sechs.scaledToWidth(self.dice_width, Qt.SmoothTransformation)
        self.newRoll = None
        
    def set_Roll(self, dr):
        self.newRoll = dr
        self.update()
        
    def paintEvent(self, event):
        super().paintEvent(event)
        
        painter = QPainter(self)
            
        painter.setPen(Qt.NoPen)
        painter.setBrush(Qt.darkGreen)
        painter.drawRect(event.rect())
        
        if self.newRoll:
            
            self.statusUpdated.emit("rolls remaining: {}".format(self.newRoll.rolls_left()))
            
            for i in range (0,len(self.newRoll.free_dice)):
                y1 = 2 * self.height() / 3 - (self.dice_width/2)
                x1 = self.width() * ((i+1) / (len(self.newRoll.free_dice)+1)) - (self.dice_width/2)
                if self.newRoll.free_dice[i] == 1:
                    painter.drawPixmap(x1, y1, self.eins)
                elif self.newRoll.free_dice[i] == 2:
                    painter.drawPixmap(x1, y1, self.zwei)
                elif self.newRoll.free_dice[i] == 3:
                    painter.drawPixmap(x1, y1, self.drei)
                elif self.newRoll.free_dice[i] == 4:
                    painter.drawPixmap(x1, y1, self.vier)
                elif self.newRoll.free_dice[i] == 5:
                    painter.drawPixmap(x1, y1, self.fuenf)
                elif self.newRoll.free_dice[i] == 6:
                    painter.drawPixmap(x1, y1, self.sechs)
                else:
                    print("Somethings wrong")
              
            for i in range (0,len(self.newRoll.picked_dice)):
                x2 = self.width() * ((i+1) / (len(self.newRoll.picked_dice)+1)) - (self.dice_width/2)
                y2 = self.height() / 3 - (self.dice_width/2)
                if self.newRoll.picked_dice[i] == 1:
                    painter.drawPixmap(x2, y2, self.eins)
                elif self.newRoll.picked_dice[i] == 2:
                    painter.drawPixmap(x2, y2, self.zwei)
                elif self.newRoll.picked_dice[i] == 3:
                    painter.drawPixmap(x2, y2, self.drei)
                elif self.newRoll.picked_dice[i] == 4:
                    painter.drawPixmap(x2, y2, self.vier)
                elif self.newRoll.picked_dice[i] == 5:
                    painter.drawPixmap(x2, y2, self.fuenf)
                elif self.newRoll.picked_dice[i] == 6:
                    painter.drawPixmap(x2, y2, self.sechs)
                else:
                    print("Somethings wrong")
                
      
        
    def roll(self):
        if self.newRoll.roll():
            self.RollSignal.emit()
            self.statusUpdated.emit("rolls remaining: {}".format(self.newRoll.rolls_left()))
            self.update()
            
        else:
            text = "You dont have any rolls left!!!"
            self.statusUpdated.emit(text)
            
    
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            index = self.posToIndex(event.pos())
            if index != -1:
                if event.y() >  2 * self.height() / 3 - (self.dice_width/2) and event.y() <  2 * self.height() / 3 + (self.dice_width/2):
                    self.newRoll.pick(index)
                elif event.y() > self.height() / 3 - (self.dice_width/2) and event.y() < self.height() / 3 + (self.dice_width/2):
                    self.newRoll.remove(index)
                else:
                    pass
                self.update()
                
            
    def posToIndex(self, pos):
        if pos.y() > self.height()/2:
            for i in range (0,len(self.newRoll.free_dice)):
                x1 = self.width() * ((i+1) / (len(self.newRoll.free_dice)+1))
                if abs(pos.x() - x1) <= self.dice_width/2:
                    return i
            return -1
        else:
            for i in range (0,len(self.newRoll.picked_dice)):
                x1 = self.width() * ((i+1) / (len(self.newRoll.picked_dice)+1))
                if abs(pos.x() - x1) <= self.dice_width/2:
                    return i
            return -1

            
        
if __name__ == "__main__":
    import sys
    if QtCore.QCoreApplication.instance() is not None:
        app = QtCore.QCoreApplication.instance()
    else:
        app = QApplication(sys.argv)
        
    dice = DiceWidget()
    dice.resize(800,600)
    dice.set_Roll(DiceRoll())
    dice.show()
    sys.exit(app.exec_())

