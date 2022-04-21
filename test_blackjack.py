from mimetypes import init
import unittest
import random
from blackjack import Blackjack

class TestBlackJack(unittest.TestCase):


    def test_shuffle(self):

        shuffler = Blackjack()
        shuffler.card_shuffle()
        shuffler_length = len(shuffler.deck_of_cards)
        
        # print(shuffler)
        # print(shuffler.deck_of_cards)
        # print(shuffler_length)

        self.assertEqual(shuffler_length, 52)
    

    def test_player_cards(self):
        shuffler = Blackjack()
        shuffler.card_shuffle()
        shuffler.pdealer()
        shuffler_player = len(shuffler.pcards)

        self.assertEqual(shuffler_player, 2)

    def test_dealer_cards(self):
        shuffler = Blackjack()
        shuffler.card_shuffle()
        shuffler.ddealer()
        shuffler_dealer = len(shuffler.dcards)

        self.assertEqual(shuffler_dealer, 2)
        self.assertTrue(shuffler_dealer)

    
    def test_player_action_hit(self):
        shuffler = Blackjack()
        
        self.assertTrue(shuffler.player_action1)
    
    def test_player_action_stand(self):
        shuffler = Blackjack()

        self.assertTrue(shuffler.player_action2)
       
    def test_dealer_sum(self):
        shuffler = Blackjack()
        shuffler.totaldealer()

        

program = TestBlackJack()

program.test_shuffle()