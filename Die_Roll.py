# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 17:22:48 2020

@author: morit
"""
import random



class Die_roll:
    
    def __init__(self):
        self.picked_dice = []
        self.free_dice = [0 for i in range(5)]
        self.Die_roll()
        self.count = 1
        
        
    def roll(self):
        if self.count <= 3:
            for i in range(len(self.free_dice)):
                self.free_dice[i] = random.randint(1,6)
            self.count += 1
            
    def pick(self, pos):
        self.picked_dice.append(self.free_dice[pos])
        del self.free_dice[pos]
        
    def remove(self, pos):
        self.free_dice.append(self.picked_dice[pos])
        del self.picked_dice[pos]
    
        