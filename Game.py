# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 16:29:53 2020

@author: morit
"""

import DiceRoll, Player, Categories

class Game:
    
    def __init__(self):
        self.players = []
        self.game_running = False
        self.round = 0
        self.played_this_round = []
        self.current_player_ind = 0
        self.currently_playing = False
        self.diceroll = None
        
    def check_in(self, name):
        if not self.game_running and not name in filter(lambda x: x.name == name, self.players):
            self.players.append(Player.Player(name))
            
    def check_out(self, name):
        if name in [p.name for p in self.players]:
            del self.players[self.nameindex(name)]
        
    def nameindex(self, name):
        for i in range(len(self.players)):
            if self.players[i].name == name:
                return i
        return -1
    
    def player_from_name(self, name):
        return self.players[self.nameindex(name)]
        
    def next_round(self):
        self.game_running = True
        if len(self.played_this_round) == len(self.players) and self.round < 15:
            self.round += 1
            self.played_this_round = []
            return 1
        else:
            return 0
        
    def play_round(self, name):
        index = self.nameindex(name)
        if self.players[index] not in self.played_this_round and not self.currently_playing:
            #print("play_round if")
            self.current_player_ind = index
            self.currently_playing = True
            self.diceroll = DiceRoll.DiceRoll()       
            return 1
        else:
            return 0
    
    def roll(self):
        if self.diceroll.rolls_left() and self.currently_playing:
            self.diceroll.roll()
            return 1
        else:
            return 0
        
        
    def chooseCat(self, key):  ## key aus Player.keys
        player = self.players[self.current_player_ind]
        if key in player.unused_cat():
            cat = Categories.Categories(self.diceroll.all_dice())
            player.chosen_cat[key] = True
            player.points[key] = cat.points_from_key(key)
            player.check35p()
            self.currently_playing = False
            self.played_this_round.append(player)
            if len(self.players) == len(self.played_this_round):
                self.next_round()     
        
    
    def players_left(self):
        left = []
        for player in self.players:
            if player not in self.played_this_round:
                left.append(player)
        return left
        
  