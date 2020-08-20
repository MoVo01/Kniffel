# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 16:31:01 2020

@author: morit
"""

import unittest
import copy


# tested classes
import DieRoll as f_dr


class DieRollTest(unittest.TestCase):
    
    def test_roll(self):
        
        
        def legal_dices(l):
            for die in l:
                if not 1 <= die <= 6:
                    return False
            return True
        
        # sinnvolle würfel
        dr1 = f_dr.DieRoll()
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
        
    def test_pick(self):
        
        def legal_dices(l):
            for die in l:
                if not 1 <= die <= 6:
                    return False
            return True
        
        # würfel auswählen
        dr2 = f_dr.DieRoll()
        old_dice = copy.deepcopy(dr2.free_dice)
        dr2.pick(3)
        del old_dice[3]
        self.assertEqual(dr2.free_dice, old_dice, msg = "falscher Wuerfel geloescht")
        dr2.pick(1)
        del old_dice[1]
        self.assertEqual(dr2.free_dice, old_dice, msg = "falscher Wuerfel geloescht")
        
        # nur ein teil der würfel werfen
        old_dice = copy.deepcopy(dr2.free_dice)
        dr2.roll()
        self.assertTrue(legal_dices(dr2), msg = "unmoegliche Augenzahl")
        self.assertEqual(len(dr2.free_dice), len(old_dice), msg = "falsche Anzal Wuerfel erneut geworfen")
        dr2.roll()
        self.assertTrue(legal_dices(dr2), msg = "unmoegliche Augenzahl")
        self.assertEqual(len(dr2.free_dice), len(old_dice), msg = "falsche Anzal Wuerfel erneut geworfen")
        old_dice2 = copy.deepcopy(dr2.free_dice)
        dr2.roll()
        self.assertTrue(legal_dices(dr2), msg = "unmoegliche Augenzahl")
        self.assertEqual(dr2.free_dice, old_dice2, msg = "mehr als drei Wuerfelaktionen getaetigt")
        self.assertEqual(len(dr2.free_dice), len(old_dice), msg = "falsche Anzal Wuerfel erneut geworfen")
        dr2.roll()
        self.assertTrue(legal_dices(dr2), msg = "unmoegliche Augenzahl")
        self.assertEqual(dr2.free_dice, old_dice2, msg = "mehr als drei Wuerfelaktionen getaetigt")
        self.assertEqual(len(dr2.free_dice), len(old_dice), msg = "falsche Anzal Wuerfel erneut geworfen")
        
    def test_remove(self):
        
        # würfel auswählen
        dr3 = f_dr.DieRoll([1,2,3,4,5])
        dr3.pick(1)
        self.assertEqual(dr3.free_dice, [1, 3, 4, 5])
        self.assertEqual(dr3.picked_dice, [2])
        dr3.pick(0)
        self.assertEqual(dr3.free_dice, [3, 4, 5])
        self.assertEqual(dr3.picked_dice, [2, 1])
        
        # würfel zurücklegen
        dr3.remove(1)
        self.assertEqual(dr3.free_dice, [3, 4, 5, 1])
        self.assertEqual(dr3.picked_dice, [2])
        dr3.remove(0)
        self.assertEqual(dr3.free_dice, [3, 4, 5, 1, 2])
        self.assertEqual(dr3.picked_dice, [])
        
                
        
        