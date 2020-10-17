# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 21:56:15 2020

@author: luisw
"""


import sys
from PyQt5 import QtCore, QtWidgets, uic
import Game, Player



Ui_MainWindow, WindowBaseClass = uic.loadUiType("GUI.ui")

class MyDialog(WindowBaseClass, Ui_MainWindow):
    def __init__(self, parent=None):
        WindowBaseClass.__init__(self, parent)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        
        self.game = Game.Game()
        
    def create_new_player(self):
        if str(self.NameIn.text()) != "":
            self.game.check_in(str(self.NameIn.text()))
            self.updatePlayerlist()
            self.NameIn.clear()
            
    def remove_player(self):
        self.game.check_out(self.Playerlist.currentItem().text())
        self.updatePlayerlist()
        
    def updatePlayerlist(self):
        self.Playerlist.clear()
        if not self.game.game_running:
            for player in self.game.players:
                self.Playerlist.insertItem(-1, player.name)
        else: #übrige Speiler dieser Runde
            pass
            
    
    def reset():
        pass
            
    def update_labels(self):
        player = self.game.player_from_name(self.Playerlist.CurrentItem().text())
        for key in Player.keys:
            getattr(self, "Label{}".format(key)).setText(player.points[key])
            
        
        
        
        
    
if __name__ == "__main__":
    if QtCore.QCoreApplication.instance() is not None:
        app = QtCore.QCoreApplication.instance()
    else:
        app = QtWidgets.QApplication(sys.argv)

    dialog = MyDialog()
    dialog.show()
    sys.exit(app.exec_())