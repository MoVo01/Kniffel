# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 21:56:15 2020

@author: luisw
"""


import sys
from PyQt5 import QtCore, QtWidgets, uic
import Game, Player



Ui_MainWindow, WindowBaseClass = uic.loadUiType("Kniffel.ui")

class MyDialog(WindowBaseClass, Ui_MainWindow):
    def __init__(self, parent = None):
        WindowBaseClass.__init__(self, parent)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.DiceRoll.setVisible(False)
        self.Play.setEnabled(False) 
        self.StartGame.setEnabled(False)
        self.DiceWidget.set_dicewidth(self.DiceWidget.width() / 9)
        self.game = Game.Game()
        
    def create_new_player(self):
        if str(self.NameIn.text()) != "":
            self.game.check_in(str(self.NameIn.text()))
            self.updatePlayerlist()
            self.NameIn.clear()
            self.StartGame.setEnabled(True)
            
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
        self.Playerlist.setCurrentRow(0)
            
    def update_labels(self):
        if self.Playerlist.currentItem():
            player = self.game.player_from_name(self.Playerlist.currentItem().text())
            for key in Player.Player.keys:
                getattr(self, "Label{}".format(key)).setText(str(player.points[key]))
            self.LabelTotalScore.setText(str(player.score()))
            self.LabelBonus.setText(str(player.got_35p * 35))
        
    def update_buttons(self):
        if self.Playerlist.currentItem():
            player = self.game.player_from_name(self.Playerlist.currentItem().text())
            for key in Player.Player.keys:
                getattr(self, "Button{}".format(key)).setEnabled(not player.chosen_cat[key])
    
    def start_game(self):
        self.CreateNewPlayer.setEnabled(False)
        self.RemovePlayer.setEnabled(False)
        self.NameIn.setEnabled(False)
        self.StartGame.setEnabled(False)
        self.Play.setEnabled(True)
        self.game.next_round()  
        self.Turn.setText("Turn: {}".format(self.game.round))
    
    def play(self):
        if self.game.round == 15 and not self.game.players_left():
            self.Play.setEnabled(False)
            self.game.played_this_round = []
            self.updatePlayerlist()
        elif self.game.round <= 15:
            name = self.Playerlist.currentItem().text()
            self.game.play_round(name)
            self.DiceWidget.set_Roll(self.game.diceroll)
            self.Playerlist.setEnabled(False)
            self.Play.setEnabled(False)
            self.DiceRoll.setVisible(True)
            
        
    def cat_button_clicked(self):
        if self.game.currently_playing:
            cat = self.sender().objectName()[6:]
            self.game.chooseCat(cat)
            self.DiceRoll.setVisible(False)
            self.Play.setEnabled(True)
            self.Playerlist.setEnabled(True)
            self.update_labels()
            self.update_buttons()
            self.updatePlayerlist()
            self.DiceWidget.set_Roll(None)
            self.update_score_list()
            
    def list_player_selected(self):
        self.update_labels()
        self.update_buttons()
          
    def reset(self):
        self.game = Game.Game()
        self.CreateNewPlayer.setEnabled(True)
        self.RemovePlayer.setEnabled(True)
        self.NameIn.setEnabled(True)
        self.StartGame.setEnabled(True)
        self.Play.setEnabled(True)
        self.Turn.setText("")
        self.updatePlayerlist()
        self.update_labels()
        self.update_buttons()
        self.ScoreComparison.setRowCount(0)
        self.DiceWidget.set_Roll(None)
        
    def create_score_list(self):
        self.ScoreComparison.setRowCount(len(self.game.players))
        i = 0
        for player in self.game.players:
            self.ScoreComparison.setItem(i, 0, QtWidgets.QTableWidgetItem(player.name))
            self.ScoreComparison.setItem(i, 1, QtWidgets.QTableWidgetItem("0"))
            i += 1
        
    def update_score_list(self):
        i = 0  
        self.game.players.sort(key = lambda x: x.score(), reverse = True)
        for player in self.game.players:
            self.ScoreComparison.setItem(i, 1, QtWidgets.QTableWidgetItem(str(player.score())))
            i += 1
        #self.ScoreComparison.sortItems(1, 1)
        self.Turn.setText("Turn: {}".format(self.game.round))
              
        
           
if __name__ == "__main__":
    if QtCore.QCoreApplication.instance() is not None:
        app = QtCore.QCoreApplication.instance()
    else:
        app = QtWidgets.QApplication(sys.argv)

    dialog = MyDialog()
    dialog.show()
    sys.exit(app.exec_())