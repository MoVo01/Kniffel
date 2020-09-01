# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 16:29:53 2020

@author: morit
"""

import DieRoll, Player, Categories

class Game:
    
    def __init__(self, round=1):
        self.players=[]
        self.results=[]
        self.round=round
    
    def check_in(self):
        count_players = input("Geben Sie die Spieleranzahl an")
        int(count_players)
        for k in range(1,count_players+1):
            new_one=Player(input("Name"))
            self.players.append(new_one)
        return self.players, self.count_players
            
    def round_x(self):
        for k in range(0,self.count_players):
            print("It's your turn, ",self.players[k].name,"!")
            roll_round_x=DieRoll()
            
            h=True
            while roll_round_x <= 3 and h==True:
                roll_round_x.roll()
                for i in range(1,5):
                    yes_no=input("If you want to keep roll ",i," say yes, else no" )
                    if yes_no=="yes":
                        roll_round_x.pick(i)
                    else:
                        roll_round_x.remove(i)
                again=input("again? yes or no")
                if again=="no":
                   h=False
            
            #which categorie
                        
            self.players[k].check_35p()
            self.players[k].score()        
        self.round+=1    
        
    
    def all_rounds(self):
        x=1
        while x<=15:
            self.round_x()
            x+=1
        self.scores=[]
        for i in self.players:
            self.scores.append(self.players[i].score())
        return self.scores

        
    def whole_game(self):
        self.check_in()
        self.all_rounds()
        print("Game over!")
        results={}
        for i in self.players:
            results.setdefault(self.players[i].name,self.scores[i])
        sorted_results=sorted(results.items(),key=lambda x: x[1], reverse=True)
        for r in sorted_results:
            print(r[0], r[i])