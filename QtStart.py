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
    def __init__(self, parent = None):
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
        else:
            for player in self.game.players_left():
                self.Playerlist.insertItem(-1, player.name)
            
    def update_labels(self):
        player = self.game.player_from_name(self.Playerlist.currentItem().text())
        for key in Player.Player.keys:
            getattr(self, "Label{}".format(key)).setText(str(player.points[key]))
        self.LabelTotalScore.setText(str(player.score()+42))
        self.LabelBonus.setText(str(player.got_35p * 35))
    
    def start_game(self):
        self.CreateNewPlayer.setEnabled(False)
        self.RemovePlayer.setEnabled(False)
        self.NameIn.setEnabled(False)
        self.game.next_round()  
    
    def play(self):
        name = self.Playerlist.currentItem().text()
        self.game.play_round(name)
        self.DiceWidget.newRoll = self.game.diceroll
        self.Playerlist.disable()
        
    def cat_button_clicked(self):
        if self.game.currently_playing:
            cat = self.sender().objectName()[6:]
            print(cat)
            self.game.chooseCat(cat)
            self.sender.disable()
            self.update_labels()
            self.Playerlist.enable()
            self.updatePlayerlist()
            
    def reset():
        pass
            
        
        
        
        
    
if __name__ == "__main__":
    if QtCore.QCoreApplication.instance() is not None:
        app = QtCore.QCoreApplication.instance()
    else:
        app = QtWidgets.QApplication(sys.argv)

    dialog = MyDialog()
    dialog.show()
    sys.exit(app.exec_())