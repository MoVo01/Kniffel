# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 16:31:01 2020

@author: morit
"""

import unittest
import copy


# tested classes
import DiceRoll as f_dr
import Categories as f_ca

class DiceRollTest(unittest.TestCase):
    
    def test_roll(self):
        
        
        def legal_dice(l):
            for die in l:
                if not 1 <= die <= 6:
                    return False
            return True
        
        # sinnvolle würfel
        dr1 = f_dr.DiceRoll()
        self.assertTrue(legal_dice(dr1), msg = "unmoegliche Augenzahl")
        dr1.roll()
        self.assertTrue(legal_dice(dr1), msg = "unmoegliche Augenzahl")
        dr1.roll()
        self.assertTrue(legal_dice(dr1), msg = "unmoegliche Augenzahl")
        
        # ergebnis ändert sich nach drittem wurf nicht mehr
        old_dice = copy.deepcopy(dr1.free_dice)
        dr1.roll()
        self.assertTrue(legal_dice(dr1), msg = "unmoegliche Augenzahl")
        self.assertEqual(dr1.free_dice, old_dice, msg = "mehr als drei Wuerfelaktionen getaetigt")
        dr1.roll()
        self.assertTrue(legal_dice(dr1), msg = "unmoegliche Augenzahl")
        self.assertEqual(dr1.free_dice, old_dice, msg = "mehr als drei Wuerfelaktionen getaetigt")
        
    def test_pick(self):
        
        def legal_dice(l):
            for die in l:
                if not 1 <= die <= 6:
                    return False
            return True
        
        # würfel auswählen
        dr2 = f_dr.DiceRoll()
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
        self.assertTrue(legal_dice(dr2), msg = "unmoegliche Augenzahl")
        self.assertEqual(len(dr2.free_dice), len(old_dice), msg = "falsche Anzal Wuerfel erneut geworfen")
        dr2.roll()
        self.assertTrue(legal_dice(dr2), msg = "unmoegliche Augenzahl")
        self.assertEqual(len(dr2.free_dice), len(old_dice), msg = "falsche Anzal Wuerfel erneut geworfen")
        old_dice2 = copy.deepcopy(dr2.free_dice)
        dr2.roll()
        self.assertTrue(legal_dice(dr2), msg = "unmoegliche Augenzahl")
        self.assertEqual(dr2.free_dice, old_dice2, msg = "mehr als drei Wuerfelaktionen getaetigt")
        self.assertEqual(len(dr2.free_dice), len(old_dice), msg = "falsche Anzal Wuerfel erneut geworfen")
        dr2.roll()
        self.assertTrue(legal_dice(dr2), msg = "unmoegliche Augenzahl")
        self.assertEqual(dr2.free_dice, old_dice2, msg = "mehr als drei Wuerfelaktionen getaetigt")
        self.assertEqual(len(dr2.free_dice), len(old_dice), msg = "falsche Anzal Wuerfel erneut geworfen")
        
    def test_remove(self):
        
        # würfel auswählen
        dr3 = f_dr.DiceRoll([1,2,3,4,5])
        dr3.pick(1)
        self.assertEqual(dr3.free_dice, [1, 3, 4, 5], msg = "falscher Wuerfel geloescht")
        self.assertEqual(dr3.picked_dice, [2], msg = "falscher Wuerfel ausgewaehlt")
        dr3.pick(0)
        self.assertEqual(dr3.free_dice, [3, 4, 5], msg = "falscher Wuerfel geloescht")
        self.assertEqual(dr3.picked_dice, [2, 1], msg = "falscher Wuerfel ausgewaehlt")
        
        # würfel zurücklegen
        dr3.remove(1)
        self.assertEqual(dr3.free_dice, [3, 4, 5, 1], msg = "Wuerfel nicht richtig hinzugefuegt")
        self.assertEqual(dr3.picked_dice, [2], msg = "falscher Wuerfel ausgewaehlt")
        dr3.remove(0)
        self.assertEqual(dr3.free_dice, [3, 4, 5, 1, 2], msg = "Wuerfel nicht richtig hinzugefuegt")
        self.assertEqual(dr3.picked_dice, [], msg = "falscher Wuerfel ausgewaehlt")
        
                
class CategoriesTest(unittest.TestCase):
    
    
    def __init__(self):
        super(self.__class__, self).__init__()
        self.ca1 = f_ca.Categories([5,4,3,2,1])
        self.ca2 = f_ca.Categories([1,2,1,1,2])
        self.ca3 = f_ca.Categories([2,3,1,5,6])
        self.ca4 = f_ca.Categories([3,4,3,5,4])
        self.ca5 = f_ca.Categories([6,6,6,6,6])
        self.ca6 = f_ca.Categories([1,2,3,4,6])
    
    
    def test_simple(self):
    
        self.assertEqual(self.ca1.simple(6), 0)
        self.assertEqual(self.ca1.simple(5), 5)
        self.assertEqual(self.ca2.simple(1), 3)
        self.assertEqual(self.ca2.simple(2), 4)
        self.assertEqual(self.ca5.simple(6), 30)
        
    
    def test_threeOfKind(self):
        
        self.assertEqual(self.ca1.threeOfKind(), 0, msg = "falsche Auswertung in ThreeOfKind")
        self.assertEqual(self.ca2.threeOfKind(), 7, msg = "falsche Auswertung in ThreeOfKind")
        self.assertEqual(self.ca3.threeOfKind(), 0, msg = "falsche Auswertung in ThreeOfKind")
        self.assertEqual(self.ca4.threeOfKind(), 0, msg = "falsche Auswertung in ThreeOfKind")
        self.assertEqual(self.ca5.threeOfKind(), 30, msg = "falsche Auswertung in ThreeOfKind")
        self.assertEqual(self.ca6.threeOfKind(), 0, msg = "falsche Auswertung in ThreeOfKind")    
        
        
    def test_fourOfKind(self):
        
        self.assertEqual(self.ca1.threeOfKind(), 0, msg = "falsche Auswertung in FourOfKind")
        self.assertEqual(self.ca2.threeOfKind(), 0, msg = "falsche Auswertung in FourOfKind")
        self.assertEqual(self.ca3.threeOfKind(), 0, msg = "falsche Auswertung in FourOfKind")
        self.assertEqual(self.ca4.threeOfKind(), 0, msg = "falsche Auswertung in FourOfKind")
        self.assertEqual(self.ca5.threeOfKind(), 30, msg = "falsche Auswertung in FourfKind")
        self.assertEqual(self.ca6.threeOfKind(), 0, msg = "falsche Auswertung in FourOfKind")    
    
        
    def test_kniffel(self):
        
        self.assertEqual(self.ca1.kniffel(), 0, msg = "falsche Auswertung in kniffel")
        self.assertEqual(self.ca2.kniffel(), 0, msg = "falsche Auswertung in kniffel")
        self.assertEqual(self.ca3.kniffel(), 0, msg = "falsche Auswertung in kniffel")
        self.assertEqual(self.ca4.kniffel(), 0, msg = "falsche Auswertung in kniffel")
        self.assertEqual(self.ca5.kniffel(), 50, msg = "falsche Auswertung in kniffel")
        self.assertEqual(self.ca6.kniffel(), 0, msg = "falsche Auswertung in kniffel")
        
        
    def test_twoXtwoOfKind(self):
        
        self.assertEqual(self.ca1.twoXtwoOfKind(), 0, msg = "falsche Auswertung in twoXtwoOfKind")
        self.assertEqual(self.ca2.twoXtwoOfKind(), 7, msg = "falsche Auswertung in twoXtwoOfKind")
        self.assertEqual(self.ca3.twoXtwoOfKind(), 0, msg = "falsche Auswertung in twoXtwoOfKind")
        self.assertEqual(self.ca4.twoXtwoOfKind(), 19, msg = "falsche Auswertung in twoXtwoOfKind")
        self.assertEqual(self.ca5.twoXtwoOfKind(), 30, msg = "falsche Auswertung in twoXtwoOfKind")
        self.assertEqual(self.ca6.twoXtwoOfKind(), 0, msg = "falsche Auswertung in twoXtwoOfKind")
        
        
    def test_fullHouse(self):
        
        self.assertEqual(self.ca1.fullHouse(), 0, msg = "falsche Auswertung in FullHouse")
        self.assertEqual(self.ca2.fullHouse(), 25, msg = "falsche Auswertung in FullHouse")
        self.assertEqual(self.ca3.fullHouse(), 0, msg = "falsche Auswertung in FullHouse")
        self.assertEqual(self.ca4.fullHouse(), 0, msg = "falsche Auswertung in FullHouse")
        self.assertEqual(self.ca5.fullHouse(), 0, msg = "falsche Auswertung in FullHouse")
        self.assertEqual(self.ca6.fullHouse(), 0, msg = "falsche Auswertung in FullHouse")
        
        
    def test_largeStraight(self):
        
        self.assertEqual(self.ca1.largeStraight(), 40, msg = "falsche Auswertung in LargeStraight")
        self.assertEqual(self.ca2.largeStraight(), 0, msg = "falsche Auswertung in LargeStraight")
        self.assertEqual(self.ca3.largeStraight(), 0, msg = "falsche Auswertung in LargeStraight")
        self.assertEqual(self.ca4.largeStraight(), 0, msg = "falsche Auswertung in LargeStraight")
        self.assertEqual(self.ca5.largeStraight(), 0, msg = "falsche Auswertung in LargeStraight")
        self.assertEqual(self.ca6.largeStraight(), 0, msg = "falsche Auswertung in LargeStraight")
        
        
    def test_smallStraight(self):
        
        self.assertEqual(self.ca1.smallStraight(), 30, msg = "falsche Auswertung in SmallStraight")
        self.assertEqual(self.ca2.smallStraight(), 0, msg = "falsche Auswertung in SmallStraight")
        self.assertEqual(self.ca3.smallStraight(), 0, msg = "falsche Auswertung in SmallStraight")
        self.assertEqual(self.ca4.smallStraight(), 0, msg = "falsche Auswertung in SmallStraight")
        self.assertEqual(self.ca5.smallStraight(), 0, msg = "falsche Auswertung in SmallStraight")
        self.assertEqual(self.ca6.smallStraight(), 30, msg = "falsche Auswertung in SmallStraight")
        
        
    def test_chance(self):
        
        self.assertEqual(self.ca1.chance(), 15, msg = "falsche Auswertung in Chance")
        self.assertEqual(self.ca2.chance(), 7, msg = "falsche Auswertung in Chance")
        self.assertEqual(self.ca3.chance(),17, msg = "falsche Auswertung in Chance")
        self.assertEqual(self.ca4.chance(),19, msg = "falsche Auswertung in Chance")
        self.assertEqual(self.ca5.chance(), 30, msg = "falsche Auswertung in Chance")
        self.assertEqual(self.ca6.chance(), 16, msg = "falsche Auswertung in Chance")