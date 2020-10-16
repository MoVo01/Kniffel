# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 21:55:27 2020

@author: luisw
"""


import os
from DiceRoll import DiceRoll, RollError
from PyQt5 import QtCore
from PyQt5.Qt import Qt
from PyQt5.QtGui import QPainter, QPixmap, QCursor, QBrush
from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication

class DiceWidget(QWidget):
    
    statusUpdated = QtCore.pyqtSignal(str)
    
    def __init__(self, parent=None):
        super().__init__(parent)   
        # generate mouse move events (see below)
        #self.setMouseTracking(True)
        
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
        self.newRoll = DiceRoll()
        
    def paintEvent(self, event):
        super().paintEvent(event)
        
        painter = QPainter(self)
        
        
        painter.setPen(Qt.NoPen)
        painter.setBrush(Qt.darkGreen)
        painter.drawRect(event.rect())
        
        
        
        
        for i in range (0,len(self.newRoll.free_dice)):
            if self.newRoll.free_dice[i] == 1:
                painter.drawPixmap(self.width() * ((i+1) / (len(self.newRoll.free_dice)+1)) - (self.dice_width/2), 2 * self.height() / 3 - (self.dice_width/2), self.eins)
            elif self.newRoll.free_dice[i] == 2:
                painter.drawPixmap(self.width() * ((i+1) / (len(self.newRoll.free_dice)+1)) - (self.dice_width/2), 2 * self.height() / 3 - (self.dice_width/2), self.zwei)
            elif self.newRoll.free_dice[i] == 3:
                painter.drawPixmap(self.width() * ((i+1) / (len(self.newRoll.free_dice)+1)) - (self.dice_width/2), 2 * self.height() / 3 - (self.dice_width/2), self.drei)
            elif self.newRoll.free_dice[i] == 4:
                painter.drawPixmap(self.width() * ((i+1) / (len(self.newRoll.free_dice)+1)) - (self.dice_width/2), 2 * self.height() / 3 - (self.dice_width/2), self.vier)
            elif self.newRoll.free_dice[i] == 5:
                painter.drawPixmap(self.width() * ((i+1) / (len(self.newRoll.free_dice)+1)) - (self.dice_width/2), 2 * self.height() / 3 - (self.dice_width/2), self.fuenf)
            elif self.newRoll.free_dice[i] == 6:
                painter.drawPixmap(self.width() * ((i+1) / (len(self.newRoll.free_dice)+1)) - (self.dice_width/2), 2 * self.height() / 3 - (self.dice_width/2), self.sechs)
            else:
                print("Somethings wrong")
          
        for i in range (0,len(self.newRoll.picked_dice)):
            if self.newRoll.picked_dice[i] == 1:
                painter.drawPixmap(self.width() * ((i+1) / (len(self.newRoll.picked_dice)+1)) - (self.dice_width/2), self.height() / 3 - (self.dice_width/2), self.eins)
            elif self.newRoll.picked_dice[i] == 2:
                painter.drawPixmap(self.width() * ((i+1) / (len(self.newRoll.picked_dice)+1)) - (self.dice_width/2), self.height() / 3 - (self.dice_width/2), self.zwei)
            elif self.newRoll.picked_dice[i] == 3:
                painter.drawPixmap(self.width() * ((i+1) / (len(self.newRoll.picked_dice)+1)) - (self.dice_width/2), self.height() / 3 - (self.dice_width/2), self.drei)
            elif self.newRoll.picked_dice[i] == 4:
                painter.drawPixmap(self.width() * ((i+1) / (len(self.newRoll.picked_dice)+1)) - (self.dice_width/2), self.height() / 3 - (self.dice_width/2), self.vier)
            elif self.newRoll.picked_dice[i] == 5:
                painter.drawPixmap(self.width() * ((i+1) / (len(self.newRoll.picked_dice)+1)) - (self.dice_width/2), self.height() / 3 - (self.dice_width/2), self.fuenf)
            elif self.newRoll.picked_dice[i] == 6:
                painter.drawPixmap(self.width() * ((i+1) / (len(self.newRoll.picked_dice)+1)) - (self.dice_width/2), self.height() / 3 - (self.dice_width/2), self.sechs)
            else:
                print("Somethings wrong")
                
        
    def roll(self):
        try:
            self.newRoll.roll()
            self.update()
        except RollError:
            text = "You dont have any rolls left"
            self.statusUpdated.emit(text)
            
    
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            if event.y() >  2 * self.height() / 3 - (self.dice_width/2) and event.y() <  2 * self.height() / 3 + (self.dice_width/2):
                self.newRoll.pick(self.posToIndex(event.pos()))
            elif event.y() > self.height() / 3 - (self.dice_width/2) and event.y() < self.height() / 3 + (self.dice_width/2):
                self.newRoll.remove(self.posToIndex(event.pos()))
            else:
                pass
            self.update()
            
    def posToIndex(self, pos):
        if pos.y() > self.height()/2:
            x = self.width() // pos.x()
            return x
        else:
            x = self.width() // pos.x()
            return x

            
        
if __name__ == "__main__":
    import sys
    if QtCore.QCoreApplication.instance() is not None:
        app = QtCore.QCoreApplication.instance()
    else:
        app = QApplication(sys.argv)
        
    dice = DiceWidget()
    dice.resize(800,600)
    dice.show()
    sys.exit(app.exec_())

