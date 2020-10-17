# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 16:08:58 2020

@author: luisw
"""

class Player:
    
    keys = ["1er", "2er", "3er", "4er", "5er", "6er", "fullHouse", 
                     "smallStraight", "largeStraight", "2ofKind", "2x2ofKind", 
                     "3ofKind", "4ofKind", "chance", "kniffel"]
    
    def __init__(self, name = "playernumberone"):
        self.points = dict.fromkeys(self.keys, 0)
        self.chosen_cat = dict.fromkeys(self.keys, False)
        self.got_35p = False
        self.name = name
        
        
    def check35p(self):
        if not self.got_35p:
            simples = list(filter(lambda x: x[0][1:] == "er", list(self.points.items())))
            points = 0
            for pair in simples:
                points += pair[1]
            if points >= 63:
                self.got_35p = True
        return

    def score(self):
        return sum(self.points.values())
    
    def unused_cat(self):
        cat_items = list(filter(lambda y: y[1] == False, list(self.chosen_cat.items())))
        return (lambda x: [z[0] for z in x])(cat_items)
    
    #def current_turn(self):
    #    return len(list(filter(lambda y: y[1] == True, list(self.chosen_cat.items())))) + 1
        
                    
        
        
