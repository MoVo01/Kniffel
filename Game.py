# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 16:29:53 2020

@author: morit
"""

import DiceRoll, Player

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
        if not self.game_running and not filter(lambda x: x.name == name, self.players):
            self.players.append(Player(name))
            
    def check_out(self, name): ## name muss in liste sein
        del self.players[self.nameindex(name)]
        
    def nameindex(self, name):
        for i in range(len(self.players)):
            if self.players[i].name == name:
                return i
        return -1
    
    def current_player(self):
        return self.players[self.current_player_ind]
        
    def next_round(self):
        if len(self.played_this_round) == len(self.players):
            self.round += 1
            self.played_this_round = []
            return 1
        else:
            return 0
        
    def play_round(self, name):
        self.game_running = True
        index = self.nameindex(name)
        if self.player[index] not in self.played_this_round and not self.currently_playing:
            self.current_player_ind = index
            self.diceroll = DiceRoll()
            return 1
        else:
            return 0
    
    def roll(self):
        if self.diceroll.rolls_left():
            self.diceroll.roll()
            return 1
        else:
            return 0
        
        
    def chooseCat(self, key): ## key aus Player.keys
        pass
        
    def players_left(self):
        left = []
        for player in self.players:
            if player not in self.played_this_round:
                left.append(player)
        return left
        
    
    
    
    def __init__(self, rnd = 1):
        self.players = []
        self.results = []
        self.round = rnd
    
    def check_in(self):
        count_players = int(input("Geben Sie die Spieleranzahl an"))
        for k in range(1, count_players + 1):
            new_one = Player(input("Name: "))
            self.players.append(new_one)
        #return self.players, self.count_players
            
    def round_x(self):
        for k in range(0, len(self.players)):
            print("It's your turn, ",self.players[k].name,"!")
            diceroll = DiceRoll()
            
            roll_again = True
            while diceroll.rolls_left() and roll_again:
                diceroll.roll()
                for i in range(1,5):
                    yes_no = input("If you want to keep rolling die ",i," say yes, else no" )
                    if yes_no == "yes":
                        diceroll.pick(i)
                    else:
                        diceroll.remove(i)
                roll_again = (input("again? yes or no") == "yes")
            
            #which categorie
                        
            self.players[k].check_35p()
            self.players[k].score()        
        self.round += 1    
        
    
    def all_rounds(self):
        x = 1
        while x <= 15:
            self.round_x()
            x += 1
        self.scores = []
        for i in self.players:
            self.scores.append(self.players[i].score())
        return self.scores

        
    def whole_game(self):
        self.check_in()
        self.all_rounds()
        print("Game over!")
        results = {}
        for i in self.players:
            results.setdefault(self.players[i].name, self.scores[i])
        sorted_results = sorted(results.items(), key = lambda x: x[1], reverse = True)
        for r in sorted_results:
            print(r[0], r[1])
            
