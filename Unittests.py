# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 16:31:01 2020

@author: morit
"""

import unittest
import copy


# tested classes
import Die_Roll as f_dr


class ThrowTest(unittest.TestCase):
    
    def test_throw(self):
        
        
        def legal_dices(l):
            for dice in l:
                if not 1 <= dice <= 6:
                    return False
            return True
        
        dr1 = f_dr.Die_roll()
        self.assertTrue(legal_dices(dr1))
        dr1.roll()
        self.assertTrue(legal_dices(dr1))
        dr1.roll()
        self.assertTrue(legal_dices(dr1))
        old_dice
        
        