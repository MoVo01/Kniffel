# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 16:31:01 2020

@author: morit
"""

import unittest
import copy


# tested classes
import Die_Roll as f_dr


class DieRollTest(unittest.TestCase):
    
    def test_roll(self):
        
        
        def legal_dices(l):
            for dice in l:
                if not 1 <= dice <= 6:
                    return False
            return True
        
        # sinnvolle Würfel
        dr1 = f_dr.Die_roll()
        self.assertTrue(legal_dices(dr1), msg = "unmoegliche Augenzahl")
        dr1.roll()
        self.assertTrue(legal_dices(dr1), msg = "unmoegliche Augenzahl")
        dr1.roll()
        self.assertTrue(legal_dices(dr1), msg = "unmoegliche Augenzahl")
        
        # ergebnis ändert sich nach drittem wurf nicht mehr
        old_dice = copy.deepcopy(dr1.free_dice)
        dr1.roll()
        self.assertTrue(legal_dices(dr1), msg = "unmoegliche Augenzahl")
        self.assertEqual(dr1.free_dice, old_dice, msg = "mehr als drei Wuerfelaktionen getaetigt")
        dr1.roll()
        self.assertTrue(legal_dices(dr1), msg = "unmoegliche Augenzahl")
        self.assertEqual(dr1.free_dice, old_dice, msg = "mehr als drei Wuerfelaktionen getaetigt")
        
        
        
        
        
        