# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 16:29:53 2020

@author: morit
"""

import DiceRoll, Player, Categories

class Game:
    
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
            
