import unittest

from a4 import *


class DeckTestCase(unittest.TestCase):
    def test_create_deck(self):
        # Set up
        deck = create_deck()
        orig_list = deck[:]

        # Run the thing to test
        shuffle(deck)

        # Observe and check that things are as expected
        self.assertNotEqual(orig_list, deck)

    def test_deal(self):
        deck = create_deck()
        hand1 = create_hand()
        hand2 = create_hand()

        deal(deck, hand1, hand2)

        self.assertEqual(len(deck), NUM_CARDS_IN_DECK - 2 * (NUM_CARDS_IN_HAND))
        self.assertEqual(hand1['num_cards_in_hand'], NUM_CARDS_IN_HAND)
        self.assertEqual(hand2['num_cards_in_hand'], NUM_CARDS_IN_HAND)


class GameTestCase(unittest.TestCase):
    def test_is_legal_move(self):
        hand = create_hand()
        add_card_to_hand(hand, ('King', 'of', 'Clubs'))
        add_card_to_hand(hand, (10, 'of', 'Spades'))
        add_card_to_hand(hand, (9, 'of', 'Hearts'))
        add_card_to_hand(hand, ('Queen', 'of', 'Diamonds'))

        result = is_legal_move(hand, ('Ace', 'of', 'Clubs'), (10, 'of', 'Clubs'))

        self.assertTrue(result)

        result = is_legal_move(hand, ('Ace', 'of', 'Clubs'), (10, 'of', 'Diamonds'))
        self.assertFalse(result)

    def test_who_won(self):
        ## How this test is set up might depend how you implement your cards
        ## It can be okay to change it
        lead_card = ('Ace', 'of', 'Clubs', 14)
        followed_card = (9, 'of', 'Clubs', 9)
        trump = 'Hearts'

        result = who_won(lead_card, followed_card, trump)
        self.assertTrue(result)

        result = who_won( (9, 'of', 'Clubs', 9), ('Ace', 'of', 'Diamonds', 14), 'Diamonds')
        self.assertFalse(result)

        result = who_won( (9, 'of', 'Clubs', 9), ('Ace', 'of', 'Diamonds', 14), 'Clubs')
        self.assertTrue(result)




if __name__ == '__main__':
    unittest.main()
