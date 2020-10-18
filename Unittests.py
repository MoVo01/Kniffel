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
    
    
    # def __init__(self):
    #     ca1 = f_ca.Categories([5,4,3,2,1])
    #     ca2 = f_ca.Categories([1,2,1,1,2])
    #     ca3 = f_ca.Categories([2,3,1,5,6])
    #     ca4 = f_ca.Categories([3,4,3,5,4])
    #     ca5 = f_ca.Categories([6,6,6,6,6])
    #     ca6 = f_ca.Categories([1,2,3,4,6])
    
    
    def test_simple(self):
        
        ca1 = f_ca.Categories([5,4,3,2,1])
        ca2 = f_ca.Categories([1,2,1,1,2])
        ca5 = f_ca.Categories([6,6,6,6,6])
    
        self.assertEqual(ca1.simple(6), 0)
        self.assertEqual(ca1.simple(5), 5)
        self.assertEqual(ca2.simple(1), 3)
        self.assertEqual(ca2.simple(2), 4)
        self.assertEqual(ca5.simple(6), 30)
        
    
    def test_threeOfKind(self):
        
        ca1 = f_ca.Categories([5,4,3,2,1])
        ca2 = f_ca.Categories([1,2,1,1,2])
        ca3 = f_ca.Categories([2,3,1,5,6])
        ca4 = f_ca.Categories([3,4,3,5,4])
        ca5 = f_ca.Categories([6,6,6,6,6])
        ca6 = f_ca.Categories([1,2,3,4,6])
        
        self.assertEqual(ca1.threeOfKind(), 0, msg = "falsche Auswertung in ThreeOfKind")
        self.assertEqual(ca2.threeOfKind(), 7, msg = "falsche Auswertung in ThreeOfKind")
        self.assertEqual(ca3.threeOfKind(), 0, msg = "falsche Auswertung in ThreeOfKind")
        self.assertEqual(ca4.threeOfKind(), 0, msg = "falsche Auswertung in ThreeOfKind")
        self.assertEqual(ca5.threeOfKind(), 30, msg = "falsche Auswertung in ThreeOfKind")
        self.assertEqual(ca6.threeOfKind(), 0, msg = "falsche Auswertung in ThreeOfKind")    
        
        
    def test_fourOfKind(self):
        
        ca1 = f_ca.Categories([5,4,3,2,1])
        ca2 = f_ca.Categories([1,2,1,1,2])
        ca3 = f_ca.Categories([2,3,1,5,6])
        ca4 = f_ca.Categories([3,4,3,5,4])
        ca5 = f_ca.Categories([6,6,6,6,6])
        ca6 = f_ca.Categories([1,2,3,4,6])
        
        self.assertEqual(ca1.fourOfKind(), 0, msg = "falsche Auswertung in FourOfKind")
        self.assertEqual(ca2.fourOfKind(), 0, msg = "falsche Auswertung in FourOfKind")
        self.assertEqual(ca3.fourOfKind(), 0, msg = "falsche Auswertung in FourOfKind")
        self.assertEqual(ca4.fourOfKind(), 0, msg = "falsche Auswertung in FourOfKind")
        self.assertEqual(ca5.fourOfKind(), 30, msg = "falsche Auswertung in FourfKind")
        self.assertEqual(ca6.fourOfKind(), 0, msg = "falsche Auswertung in FourOfKind")    
    
        
    def test_kniffel(self):
        
        ca1 = f_ca.Categories([5,4,3,2,1])
        ca2 = f_ca.Categories([1,2,1,1,2])
        ca3 = f_ca.Categories([2,3,1,5,6])
        ca4 = f_ca.Categories([3,4,3,5,4])
        ca5 = f_ca.Categories([6,6,6,6,6])
        ca6 = f_ca.Categories([1,2,3,4,6])
        
        self.assertEqual(ca1.kniffel(), 0, msg = "falsche Auswertung in kniffel")
        self.assertEqual(ca2.kniffel(), 0, msg = "falsche Auswertung in kniffel")
        self.assertEqual(ca3.kniffel(), 0, msg = "falsche Auswertung in kniffel")
        self.assertEqual(ca4.kniffel(), 0, msg = "falsche Auswertung in kniffel")
        self.assertEqual(ca5.kniffel(), 50, msg = "falsche Auswertung in kniffel")
        self.assertEqual(ca6.kniffel(), 0, msg = "falsche Auswertung in kniffel")
        
        
    def test_twoXtwoOfKind(self):
        
        ca1 = f_ca.Categories([5,4,3,2,1])
        ca2 = f_ca.Categories([1,2,1,1,2])
        ca3 = f_ca.Categories([2,3,1,5,6])
        ca4 = f_ca.Categories([3,4,3,5,4])
        ca5 = f_ca.Categories([6,6,6,6,6])
        ca6 = f_ca.Categories([1,2,3,4,6])
        
        self.assertEqual(ca1.twoXtwoOfKind(), 0, msg = "falsche Auswertung in twoXtwoOfKind")
        self.assertEqual(ca2.twoXtwoOfKind(), 7, msg = "falsche Auswertung in twoXtwoOfKind")
        self.assertEqual(ca3.twoXtwoOfKind(), 0, msg = "falsche Auswertung in twoXtwoOfKind")
        self.assertEqual(ca4.twoXtwoOfKind(), 19, msg = "falsche Auswertung in twoXtwoOfKind")
        self.assertEqual(ca5.twoXtwoOfKind(), 0, msg = "falsche Auswertung in twoXtwoOfKind")
        self.assertEqual(ca6.twoXtwoOfKind(), 0, msg = "falsche Auswertung in twoXtwoOfKind")
        
        
    def test_fullHouse(self):
        
        ca1 = f_ca.Categories([5,4,3,2,1])
        ca2 = f_ca.Categories([1,2,1,1,2])
        ca3 = f_ca.Categories([2,3,1,5,6])
        ca4 = f_ca.Categories([3,4,3,5,4])
        ca5 = f_ca.Categories([6,6,6,6,6])
        ca6 = f_ca.Categories([1,2,3,4,6])
        
        self.assertEqual(ca1.fullHouse(), 0, msg = "falsche Auswertung in FullHouse")
        self.assertEqual(ca2.fullHouse(), 25, msg = "falsche Auswertung in FullHouse")
        self.assertEqual(ca3.fullHouse(), 0, msg = "falsche Auswertung in FullHouse")
        self.assertEqual(ca4.fullHouse(), 0, msg = "falsche Auswertung in FullHouse")
        self.assertEqual(ca5.fullHouse(), 0, msg = "falsche Auswertung in FullHouse")
        self.assertEqual(ca6.fullHouse(), 0, msg = "falsche Auswertung in FullHouse")
        
        
    def test_largeStraight(self):
        
        ca1 = f_ca.Categories([5,4,3,2,1])
        ca2 = f_ca.Categories([1,2,1,1,2])
        ca3 = f_ca.Categories([2,3,1,5,6])
        ca4 = f_ca.Categories([3,4,3,5,4])
        ca5 = f_ca.Categories([6,6,6,6,6])
        ca6 = f_ca.Categories([1,2,3,4,6])
        
        self.assertEqual(ca1.largeStraight(), 40, msg = "falsche Auswertung in LargeStraight")
        self.assertEqual(ca2.largeStraight(), 0, msg = "falsche Auswertung in LargeStraight")
        self.assertEqual(ca3.largeStraight(), 0, msg = "falsche Auswertung in LargeStraight")
        self.assertEqual(ca4.largeStraight(), 0, msg = "falsche Auswertung in LargeStraight")
        self.assertEqual(ca5.largeStraight(), 0, msg = "falsche Auswertung in LargeStraight")
        self.assertEqual(ca6.largeStraight(), 0, msg = "falsche Auswertung in LargeStraight")
        
        
    def test_smallStraight(self):
        
        ca1 = f_ca.Categories([5,4,3,2,1])
        ca2 = f_ca.Categories([1,2,1,1,2])
        ca3 = f_ca.Categories([2,3,1,5,6])
        ca4 = f_ca.Categories([3,4,3,5,4])
        ca5 = f_ca.Categories([6,6,6,6,6])
        ca6 = f_ca.Categories([1,2,3,4,6])
        
        self.assertEqual(ca1.smallStraight(), 30, msg = "falsche Auswertung in SmallStraight")
        self.assertEqual(ca2.smallStraight(), 0, msg = "falsche Auswertung in SmallStraight")
        self.assertEqual(ca3.smallStraight(), 0, msg = "falsche Auswertung in SmallStraight")
        self.assertEqual(ca4.smallStraight(), 0, msg = "falsche Auswertung in SmallStraight")
        self.assertEqual(ca5.smallStraight(), 0, msg = "falsche Auswertung in SmallStraight")
        self.assertEqual(ca6.smallStraight(), 30, msg = "falsche Auswertung in SmallStraight")
        
        
    def test_chance(self):
        
        ca1 = f_ca.Categories([5,4,3,2,1])
        ca2 = f_ca.Categories([1,2,1,1,2])
        ca3 = f_ca.Categories([2,3,1,5,6])
        ca4 = f_ca.Categories([3,4,3,5,4])
        ca5 = f_ca.Categories([6,6,6,6,6])
        ca6 = f_ca.Categories([1,2,3,4,6])
        
        self.assertEqual(ca1.chance(), 15, msg = "falsche Auswertung in Chance")
        self.assertEqual(ca2.chance(), 7, msg = "falsche Auswertung in Chance")
        self.assertEqual(ca3.chance(),17, msg = "falsche Auswertung in Chance")
        self.assertEqual(ca4.chance(),19, msg = "falsche Auswertung in Chance")
        self.assertEqual(ca5.chance(), 30, msg = "falsche Auswertung in Chance")
        self.assertEqual(ca6.chance(), 16, msg = "falsche Auswertung in Chance")
        
    def test_keydict(self):
        
        ca1 = f_ca.Categories([5,4,3,2,1])
        ca2 = f_ca.Categories([1,2,1,1,2])
        ca3 = f_ca.Categories([2,3,1,5,6])
        ca4 = f_ca.Categories([3,4,3,5,4])
        ca5 = f_ca.Categories([6,6,6,6,6])
        ca6 = f_ca.Categories([1,2,3,4,6])
        
        comp = {}
        comp["5er"] = 5
        comp["largeStraight"] = 40
        comp["chance"] = 15
        self.assertEqual(ca1.keydict(["5er", "largeStraight", "chance"]), comp, msg = "Fehler in keydict")
    
    def test_points_from_key(self):
        
        ca1 = f_ca.Categories([5,4,3,2,1])
        ca2 = f_ca.Categories([1,2,1,1,2])
        ca4 = f_ca.Categories([3,4,3,5,4])
        
        self.assertEqual(ca1.points_from_key("chance"), 15, msg = "Fehler in points_from_key")
        self.assertEqual(ca2.points_from_key("fullHouse"), 25, msg = "Fehler in points_from_key")
        self.assertEqual(ca4.points_from_key("2x2ofKind"), 19, msg = "Fehler in points_from_key")
        
        
               
class GameTest(unittest.TestCase):
        
        
    def test_check_in(self):
        game = f_ga.Game()
        game.players = ["Anna", "Betty", "Claus"]
        game.check_in("Doris")
        self.assertEqual(game.players, ["Anna", "Betty", "Claus", "Doris"], msg = "Spieler wurde nicht hinzugefügt")
        game.check_in("Doris")
        self.assertEqual(game.players, ["Anna", "Betty", "Claus", "Doris"], msg = "selber Name wurde doppelt eingefügt")
        
        
    def test_check_out(self):
        game = f_ga.Game()
        game.players = ["Anna", "Betty", "Claus", "Doris"]
        game.check_out("Carl")
        self.assertEqual(game.players, ["Anna", "Betty", "Claus", "Doris"], msg = "nicht vorhandener Spieler bei check_out")
        game.check_out("Betty")
        self.assertEqual(game.players, ["Anna", "Claus", "Doris"], msg = "Fehler bei korrektem Spieler check_out")
        
        
    def test_next_round(self):
        game = f_ga.Game()
        
        game.players = ["Anna", "Claus", "Doris"]
        game.played_this_round = ["Anna", "Claus", "Doris"]
        game.round = 13
        game.next_round()
        self.assertEqual(game.round, 14, msg = "Runde wurde nicht hochgesetzt")
        self.assertEqual(game.played_this_round, [], msg = "in neuer Runde existieren Spieler, die bereits spielten")
        
        game.played_this_round = ["Anna","Claus"]
        game.round = 13
        game.next_round()
        self.assertEqual(game.round, 13, msg = "Runde wurde falsch hochgesetzt")
        self.assertEqual(game.played_this_round, ["Anna","Claus"], msg = "Trotz selber Runde Spieler aus bereits gespielt gelöscht")
        
        game.played_this_round = ["Anna","Claus","Doris"]
        game.round = 15
        game.next_round()
        self.assertEqual(game.round, 15, msg = "Runde wurde trotzt Spielende hochgesetzt")
        self.assertEqual(game.played_this_round, ["Anna","Claus","Doris"], msg = "trotz Spielende dürfen Spieler nochmal spielen")
        
        
    def test_play_round(self):
        game = f_ga.Game()
        
        game.round = 13
        game.next_round()
        self.play_round("Anna")
        self.assertEqual(game.currently_playing, True, msg = "Spiel har Runde nicht gestartet")
        
    
    def test_choose_cat(self):
        game = f_ga.Game()
        
        game.players = ["Anna", "Claus", "Doris"]
        game.played_this_round = []
        game.play_round("Anna")
        game.chooseCat("chance")
        player = game.players[game.current_player_ind]
        self.assertEqual(player.chosen_cat["chance"], True, msg = "Kategorie wurde nicht als gewählt gesetzt")
        self.assertNotEquals(player.points["chance"], 0, msg = "Punkte wurden nicht eingetragen")
        self.assertEqual(game.currently_playing, False, msg = "Runde des Spieler wurde nicht beednet")
        self.assertEqual(game.played_this_round, ["Anna"], msg = "Spieler wurde nicht der Liste bereits gespielt hinzugefügt")
        
        game.round = 12
        game.played_this_round = ["Anna", "Doris"]
        game.play_round("Claus")
        game.chooseCat("chance")
        self.assertEqual(game.round, 13, msg = "obwohl alle Spieler dran waren wurde die nächste Runde nicht begonnen")
        
       
    def test_players_left(self):
        game = f_ga.Game()
        game.players = ["Anna", "Claus", "Doris"]
        game.played_this_round = ["Anna"]
        self.assertEqual(game.players_left(), ["Claus","Doris"], msg = "Fehler in Liste verbleibender Spieler")        


if __name__ == "__main__":
    
    suite1 = unittest.defaultTestLoader.loadTestsFromTestCase(DiceRollTest)
    res1 = unittest.TextTestRunner(resultclass = unittest.TextTestResult).run(suite1)
    ## RollError wird in test logischerweise gecalled, was zu einem Fehlschlag führt
    
    
    suite2 = unittest.defaultTestLoader.loadTestsFromTestCase(CategoriesTest)
    res2 = unittest.TextTestRunner(resultclass = unittest.TextTestResult).run(suite2)
    
    
    suite3 = unittest.defaultTestLoader.loadTestsFromTestCase(GameTest)
    res3 = unittest.TextTestRunner(resultclass = unittest.TextTestResult).run(suite3)
    
    
    
    
    
    
    