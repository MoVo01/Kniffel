# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 16:39:14 2020

@author: morit
"""


class Categories:
    
    def __init__(self, die_roll):
        self.die_roll = die_roll
        
    def simple(self, num):
        return self.die_roll.count(num)*num
    
    def xOfKind(self, x):
        found = False
        for die in self.die_roll:
            if self.die_roll.count(die) >= x:
                found = True
                break
        if found:
            return sum(self.die_roll)
        else:
            return 0
        
    def kniffel(self):
        if self.die_roll.count(self.die_roll[0]) == 5:
            return 50
        else:
            return 0
        
    def twoX2ofKind(self):
        found = False
        for die1 in self.die_roll:
            if self.die_roll.count(die1) >= 2:
                for die2 in self.die_roll:
                    if die1 != die2 and self.die_roll.count(die2) >= 2:
                        found = True
                        break
                break
        if found:
            return sum(self.die_roll)
        else:
            return 0
        
    def fullHouse(self):
        found = False
        for die1 in self.die_roll:
            if self.die_roll.count(die1) == 3:
                for die2 in self.die_roll:
                    if die1 != die2 and self.die_roll.count(die2) == 2:
                        found = True
                        break
                break
        if found:
            return sum(self.die_roll)
        else:
            return 0
        
    def largeStraight(self):
        if self.die_roll.sort() in [[1,2,3,4,5], [2,3,4,5,6]]:
            return 40
        else:
            return 0
        
    def smallStraight(self):
        
        def sublist(a, b):
            sub = True
            for val in a:
                if a not in b:
                    sub = False
                    break
            return sub
        
        if sublist([1,2,3,4], self.die_roll) or sublist([2,3,4,5], self.die_roll) or sublist([3,4,5,6], self.die_roll):
            return 30
        else:
            return 0
        
    def chance(self):
        return sum(self.die_roll)
    
    
        

        
        