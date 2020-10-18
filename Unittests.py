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
import Game as f_ga
import Player as f_pl

class DiceRollTest(unittest.TestCase):
    
    def test_roll(self):
        
        
        def legal_dice(l):
            for die in l.all_dice():
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
        
    def test_pick(self):
        
        def legal_dice(l):
            for die in l.all_dice():
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
        dr3 = f_dr.DiceRoll()
        dr3.free_dice = [1,2,3,4,5]
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
    
        
    ca1 = f_ca.Categories([5,4,3,2,1])
    ca2 = f_ca.Categories([1,2,1,1,2])
    ca3 = f_ca.Categories([2,3,1,5,6])
    ca4 = f_ca.Categories([3,4,3,5,4])
    ca5 = f_ca.Categories([6,6,6,6,6])
    ca6 = f_ca.Categories([1,2,3,4,6])
    
    
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
        
        self.assertEqual(self.ca1.fourOfKind(), 0, msg = "falsche Auswertung in FourOfKind")
        self.assertEqual(self.ca2.fourOfKind(), 0, msg = "falsche Auswertung in FourOfKind")
        self.assertEqual(self.ca3.fourOfKind(), 0, msg = "falsche Auswertung in FourOfKind")
        self.assertEqual(self.ca4.fourOfKind(), 0, msg = "falsche Auswertung in FourOfKind")
        self.assertEqual(self.ca5.fourOfKind(), 30, msg = "falsche Auswertung in FourfKind")
        self.assertEqual(self.ca6.fourOfKind(), 0, msg = "falsche Auswertung in FourOfKind")    
    
        
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
        self.assertEqual(self.ca5.twoXtwoOfKind(), 0, msg = "falsche Auswertung in twoXtwoOfKind")
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
        
    def test_keydict(self):
        
        comp = {}
        comp["5er"] = 5
        comp["largeStraight"] = 40
        comp["chance"] = 15
        self.assertEqual(self.ca1.keydict(["5er", "largeStraight", "chance"]), comp, msg = "Fehler in keydict")
    
    def test_points_from_key(self):
        
        self.assertEqual(self.ca1.points_from_key("chance"), 15, msg = "Fehler in points_from_key")
        self.assertEqual(self.ca2.points_from_key("fullHouse"), 25, msg = "Fehler in points_from_key")
        self.assertEqual(self.ca4.points_from_key("2x2ofKind"), 19, msg = "Fehler in points_from_key")
        
        
               
class GameTest(unittest.TestCase):
        
    Anna = f_pl.Player("Anna")
    Betty = f_pl.Player("Betty")
    Claus = f_pl.Player("Claus")
    Doris = f_pl.Player("Doris")
    game = f_ga.Game()
    
        
    def test_check_in(self):
        self.game.players = [self.Anna, self.Betty, self.Claus]
        self.game.check_in("Doris")
        self.assertEqual(len(self.game.players), 4, msg = "Spieler wurde nicht hinzugefügt")
        self.game.check_in("Doris")
        self.assertEqual(len(self.game.players), 4, msg = "selber Name wurde doppelt eingefügt")
        
        
    def test_check_out(self):
        self.game.players = [self.Anna, self.Betty, self.Claus, self.Doris]
        self.game.check_out("Carl")
        self.assertEqual(self.game.players, [self.Anna, self.Betty, self.Claus, self.Doris], msg = "nicht vorhandener Spieler bei check_out")
        self.game.check_out("Betty")
        self.assertEqual(self.game.players, [self.Anna, self.Claus, self.Doris], msg = "Fehler bei korrektem Spieler check_out")
        
        
    def test_next_round(self):
        
        self.game.players = [self.Anna, self.Claus, self.Doris]
        self.game.played_this_round = [self.Anna, self.Claus, self.Doris]
        self.game.round = 13
        self.game.next_round()
        self.assertEqual(self.game.round, 14, msg = "Runde wurde nicht hochgesetzt")
        self.assertEqual(self.game.played_this_round, [], msg = "in neuer Runde existieren Spieler, die bereits spielten")
        
        self.game.played_this_round = [self.Anna, self.Claus]
        self.game.round = 13
        self.game.next_round()
        self.assertEqual(self.game.round, 13, msg = "Runde wurde falsch hochgesetzt")
        self.assertEqual(self.game.played_this_round, [self.Anna, self.Claus], msg = "Trotz selber Runde Spieler aus bereits gespielt gelöscht")
        
        self.game.played_this_round = [self.Anna,self.Claus, self.Doris]
        self.game.round = 15
        self.game.next_round()
        self.assertEqual(self.game.round, 15, msg = "Runde wurde trotzt Spielende hochgesetzt")
        self.assertEqual(self.game.played_this_round, [self.Anna,self.Claus, self.Doris], msg = "trotz Spielende dürfen Spieler nochmal spielen")
        
        
    def test_play_round(self):
        self.game.players = [self.Anna, self.Claus, self.Doris]
        
        self.game.round = 13
        self.game.next_round()
        self.game.play_round("Anna")
        self.assertEqual(self.game.currently_playing, True, msg = "Spiel har Runde nicht gestartet")
        
    
    def test_choose_cat(self):
        
        self.game.players = [self.Anna, self.Claus, self.Doris]
        self.game.played_this_round = []
        self.game.play_round("Anna")
        self.game.chooseCat("chance")
        player = self.game.players[self.game.current_player_ind]
        self.assertEqual(player.chosen_cat["chance"], True, msg = "Kategorie wurde nicht als gewählt gesetzt")
        self.assertNotEqual(player.points["chance"], 0, msg = "Punkte wurden nicht eingetragen")
        self.assertEqual(self.game.currently_playing, False, msg = "Runde des Spieler wurde nicht beednet")
        self.assertEqual(self.game.played_this_round, [self.Anna], msg = "Spieler wurde nicht der Liste bereits gespielt hinzugefügt")
        
        self.game.round = 12
        self.game.played_this_round = [self.Anna, self.Doris]
        self.game.play_round("Claus")
        self.game.chooseCat("chance")
        self.assertEqual(self.game.round, 13, msg = "obwohl alle Spieler dran waren wurde die nächste Runde nicht begonnen")
        
       
    def test_players_left(self):
        self.game.players = [self.Anna, self.Claus, self.Doris]
        self.game.played_this_round = [self.Anna]
        self.assertEqual(self.game.players_left(), [self.Claus, self.Doris], msg = "Fehler in Liste verbleibender Spieler")     
        
        
class PlayerTest(unittest.TestCase):
    
    pl = f_pl.Player()
    
    def test_check35p(self):
        self.pl.points["6er"] = 30
        self.pl.points["5er"] = 20
        self.pl.points["4er"] = 12
        self.pl.check35p()
        self.assertEqual(self.pl.got_35p, False, msg = "Fehler in check35p")
        self.pl.points["1er"] = 1
        self.pl.check35p()
        self.assertEqual(self.pl.got_35p, True, msg = "Fehler in check35p")
        self.pl.points["2er"] = 10
        self.pl.check35p()
        self.assertEqual(self.pl.got_35p, True, msg = "Fehler in check35p")
        
        
    def test_score(self):
        self.pl.points["6er"] = 30
        self.pl.points["5er"] = 20
        self.pl.points["4er"] = 12
        self.pl.points["1er"] = 1
        self.pl.points["2er"] = 10
        self.pl.check35p()
        
        self.assertEqual(self.pl.score(), 108, msg = "Fehler in score")
        
        self.pl.points["kniffel"] = 50
        self.pl.points["chance"] = 42
        
        self.assertEqual(self.pl.score(), 200, msg = "Fehler in score")
        
        
    def test_unused_cat(self):
        self.pl.chosen_cat["1er"] = True
        self.assertEqual(self.pl.unused_cat(), ["2er", "3er", "4er", "5er", "6er", "fullHouse", 
                     "smallStraight", "largeStraight", "2ofKind", "2x2ofKind", 
                     "3ofKind", "4ofKind", "chance", "kniffel"], msg = "Fehler in unused cat")
        self.pl.chosen_cat["kniffel"] = True
        self.assertEqual(self.pl.unused_cat(), ["2er", "3er", "4er", "5er", "6er", "fullHouse", 
                     "smallStraight", "largeStraight", "2ofKind", "2x2ofKind", 
                     "3ofKind", "4ofKind", "chance"], msg = "Fehler in unused cat")




if __name__ == "__main__":
    
    suite1 = unittest.defaultTestLoader.loadTestsFromTestCase(DiceRollTest)
    res1 = unittest.TextTestRunner(resultclass = unittest.TextTestResult).run(suite1)
    ## RollError wird in test logischerweise gecalled, was zu einem Fehlschlag führt
    
    
    suite2 = unittest.defaultTestLoader.loadTestsFromTestCase(CategoriesTest)
    res2 = unittest.TextTestRunner(resultclass = unittest.TextTestResult).run(suite2)
    
    
    suite3 = unittest.defaultTestLoader.loadTestsFromTestCase(GameTest)
    res3 = unittest.TextTestRunner(resultclass = unittest.TextTestResult).run(suite3)
    
    suite4 = unittest.defaultTestLoader.loadTestsFromTestCase(PlayerTest)
    res4 = unittest.TextTestRunner(resultclass = unittest.TextTestResult).run(suite4)
    
    
    
    
    
    
    