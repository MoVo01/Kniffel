# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 17:22:48 2020

@author: morit
"""
import random



class DiceRoll:
    
    def __init__(self, free_dice = [0 for i in range(5)]):
        self.picked_dice = []
        self.free_dice = free_dice
        self.count = 1
        if free_dice == [0 for i in range(5)]:
            self.count = 0
            self.roll()
              
    def roll(self):
        if self.count < 3:
            for i in range(len(self.free_dice)):
                self.free_dice[i] = random.randint(1,6)
            self.count += 1
            
    def pick(self, pos):
        self.picked_dice.append(self.free_dice[pos])
        del self.free_dice[pos]
        
    def remove(self, pos):
        self.free_dice.append(self.picked_dice[pos])
        del self.picked_dice[pos]
    
    def all_dice(self):
        return self.free_dice + self.picked_dice
    
    def rolls_left(self):
        return self.count < 3
        