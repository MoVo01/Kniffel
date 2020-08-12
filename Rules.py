# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 16:39:14 2020

@author: morit
"""


class Rules:
    
    def __init__(self, throw):
        self.throw = throw
        
    def simple(self, num):
        return self.throw.count(num)*num
    
    def xOfKind(self, x):
        found = False
        for dice in self.throw:
            if self.throw.count(dice) >= x:
                found = True
                break
        if found:
            return sum(self.throw)
        else:
            return 0
        
    def kniffel(self):
        if self.throw.count(self.throw[0]) == 5:
            return 50
        else:
            return 0
        
    def twoX2ofKind(self):
        found = False
        for dice1 in self.throw:
            if self.throw.count(dice1) >= 2:
                for dice2 in self.throw:
                    if dice1 != dice2 and self.throw.count(dice2) >= 2:
                        found = True
                        break
                break
        if found:
            return sum(self.throw)
        else:
            return 0
        
    def fullHouse(self):
        found = False
        for dice1 in self.throw:
            if self.throw.count(dice1) == 3:
                for dice2 in self.throw:
                    if dice1 != dice2 and self.throw.count(dice2) == 2:
                        found = True
                        break
                break
        if found:
            return sum(self.throw)
        else:
            return 0
        
    def largeStraight(self):
        if self.throw.sort() in [[1,2,3,4,5], [2,3,4,5,6]]:
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
        if sublist([1,2,3,4], self.throw) or sublist([2,3,4,5], self.throw) or sublist([3,4,5,6], self.throw):
            return 30
        else:
            return 0
        
    def chance(self):
        return sum(self.throw)
    
    
        

        
        