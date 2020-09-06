# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 16:39:14 2020

@author: morit
"""


class Categories:
    
    def __init__(self, dice):
        self.dice = dice
        
    def simple(self, num):
        return self.dice.count(num)*num
    
    def threeOfKind(self):
        return self.xOfKind(3)
    def fourOfKind(self):
        return self.xOfKind(4)
    
    def xOfKind(self, x):
        found = False
        for die in self.dice:
            if self.dice.count(die) >= x:
                found = True
                break
        if found:
            return sum(self.dice)
        else:
            return 0
        
    def kniffel(self):
        if self.dice.count(self.dice[0]) == 5:
            return 50
        else:
            return 0
        
    def twoXtwoOfKind(self):
        found = False
        for die1 in self.dice:
            if self.dice.count(die1) >= 2:
                for die2 in self.dice:
                    if die1 != die2 and self.dice.count(die2) >= 2:
                        found = True
                        break
        if found:
            return sum(self.dice)
        else:
            return 0
        
    def fullHouse(self):
        found = False
        for die1 in self.dice:
            if self.dice.count(die1) == 3:
                for die2 in self.dice:
                    if die1 != die2 and self.dice.count(die2) == 2:
                        found = True
                        break
        if found:
            return 25
        else:
            return 0
        
    def largeStraight(self):
        if self.dice.sort() in [[1,2,3,4,5], [2,3,4,5,6]]:
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
        
        if sublist([1,2,3,4], self.dice) or sublist([2,3,4,5], self.dice) or sublist([3,4,5,6], self.dice):
            return 30
        else:
            return 0
        
    def chance(self):
        return sum(self.dice)
    
    
        

        
        