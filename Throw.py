# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 17:22:48 2020

@author: morit
"""
import random



class Throw:
    
    def __init__(self):
        self.picked_dices = []
        self.free_dices = [0 for i in range(5)]
        self.throw()
        self.count = 1
        
        
    def throw(self):
        if self.count <= 3:
            for i in range(len(self.free_dices)):
                self.free_dices[i] = random.randint(1,6)
            self.count += 1
            
    def pick(self, pos):
        self.picked_dices.append(self.free_dices[pos])
        del self.free_dices[pos]
        
    def remove(self, pos):
        self.free_dices.append(self.picked_dices[pos])
        del self.picked_dices[pos]
    
        