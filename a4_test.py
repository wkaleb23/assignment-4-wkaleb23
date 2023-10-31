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
        shuffle(deck)
        hand1 = create_hand()
        hand2 = create_hand()
        deal(deck, hand1, hand2)
        self.assertEqual(len(deck), NUM_CARDS_IN_DECK - 2 * (NUM_CARDS_IN_HAND))
        self.assertEqual(hand1['num_cards_in_hand'], NUM_CARDS_IN_HAND)
        self.assertEqual(hand2['num_cards_in_hand'], NUM_CARDS_IN_HAND)


class GameTestCase(unittest.TestCase):

    def test_is_legal_move(self):
        hand = create_hand()
        add_card_to_hand(hand, ('King', 'Clubs', 'Black', 13))
        add_card_to_hand(hand, ('Ten', 'Spades', 'Black', 10))
        add_card_to_hand(hand, ('Nine', 'Hearts', 'Red', 9))
        add_card_to_hand(hand, ('Queen', 'Clubs', 'Black', 12))
        result = is_legal_move(hand, ('Ace', 'Clubs', 'Black', 14), ('King', 'Clubs', 'Black', 13))
        self.assertTrue(result)
        # result = is_legal_move(hand, ('Ace', 'Clubs', 'Black', 14), ('Ten', 'Clubs', 'Black', 10))
        # self.assertFalse(result)
        result = is_legal_move(hand, ('Ace', 'Clubs', 'Black', 14), ('Queen', 'Diamonds', 'Red', 12))
        self.assertFalse(result)
        result = is_legal_move(hand, ('Queen', 'Diamonds', 'Red', 12), ('Queen', 'Clubs', 'Black', 12))
        self.assertTrue(result)

    def test_who_won(self):
        # Given two cards that are played in a hand, which one wins?
        # If the suits are the same, the higher card value wins.
        # If the suits are not the same, player 1 wins, unless player 2 played trump.
        # write tests to validate this
        # result = who_won(Ace of Clubs, Nine of Clubs, Hearts)
        result = who_won(('Ace', 'Clubs', 'Black', 14), ('Nine', 'Clubs', 'Black', 9), 'Hearts')
        self.assertTrue(result)
        # result = who_won( Nine of Clubs, Ace of Diamonds, Diamonds)
        result = who_won(('Nine', 'Clubs', 'Black', 9), ('Ace', 'Diamonds', 'Red', 14), 'Diamonds')
        self.assertFalse(result)
        # result = who_won( NIne of Clubs, Ace of Diamonds, Clubs)
        result = who_won(('Nine', 'Clubs', 'Black', 9), ('Ace', 'Diamonds', 'Red', 14), 'Clubs')
        self.assertTrue(result)

    # write unit test for return_hand_to_deck
    def test_return_hand_to_deck(self):
        deck = create_deck()
        hand1 = create_hand()
        hand2 = create_hand()
        deal(deck, hand1, hand2)
        return_hand_to_deck(hand1, deck)
        self.assertEqual(len(deck), NUM_CARDS_IN_DECK - NUM_CARDS_IN_HAND)
        self.assertEqual(hand1['num_cards_in_hand'], 0)
        return_hand_to_deck(hand2, deck)
        self.assertEqual(len(deck), NUM_CARDS_IN_DECK)
        self.assertEqual(hand2['num_cards_in_hand'], 0)

    # write unit test for sort_hand
    # The sort order should be: all cards of the given trump suit should
    # be the "highest", and A high down to 9;
    # The other suits can be in random order, but the card values must go
    # from high to low.
    def test_sort_hand(self):
        # create 3 hands, one with all the same suit, one with all the same value, and one with a mix of suits and values
        hand1 = create_hand()
        hand2 = create_hand()
        hand3 = create_hand()
        add_card_to_hand(hand1, ('Jack', 'Clubs', 'Black', 11))
        add_card_to_hand(hand1, ('Ten', 'Clubs', 'Black', 10))
        add_card_to_hand(hand1, ('King', 'Clubs', 'Black', 13))
        add_card_to_hand(hand1, ('Queen', 'Clubs', 'Black', 12))
        add_card_to_hand(hand1, ('Ace', 'Clubs', 'Black', 14))
        add_card_to_hand(hand2, ('Ace', 'Hearts', 'Red', 14))
        add_card_to_hand(hand2, ('Ace', 'Diamonds', 'Red', 14))
        add_card_to_hand(hand2, ('Ace', 'Clubs', 'Black', 14))
        add_card_to_hand(hand2, ('Ace', 'Spades', 'Black', 14))
        add_card_to_hand(hand3, ('Queen', 'Hearts', 'Red', 12))
        add_card_to_hand(hand3, ('Jack', 'Diamonds', 'Red', 11))
        add_card_to_hand(hand3, ('Ten', 'Clubs', 'Black', 10))
        add_card_to_hand(hand3, ('Ace', 'Clubs', 'Black', 14))
        add_card_to_hand(hand3, ('King', 'Spades', 'Black', 13))
        # sort the hands
        hand1 = sort_hand(hand1, 'Clubs')
        hand2 = sort_hand(hand2, 'Clubs')
        hand3 = sort_hand(hand3, 'Clubs')
        # check that the hands are sorted correctly
        self.assertEqual(get_card_from_node(get_card_from_hand(hand1, 0)), ('Ace', 'Clubs', 'Black', 14))
        self.assertEqual(get_card_from_node(get_card_from_hand(hand1, 1)), ('King', 'Clubs', 'Black', 13))
        self.assertEqual(get_card_from_node(get_card_from_hand(hand2, 0)), ('Ace', 'Clubs', 'Black', 14))
        self.assertEqual(get_card_from_node(get_card_from_hand(hand3, 0)), ('Ace', 'Clubs', 'Black', 14))
        self.assertEqual(get_card_from_node(get_card_from_hand(hand3, 1)), ('Ten', 'Clubs', 'Black', 10))

    # write unit test for take_player1_turn
    def test_take_player1_turn(self):
        # create a hand
        hand = create_hand()
        add_card_to_hand(hand, ('Jack', 'Clubs', 'Black', 11))
        add_card_to_hand(hand, ('Ten', 'Clubs', 'Black', 10))
        add_card_to_hand(hand, ('King', 'Clubs', 'Black', 13))
        add_card_to_hand(hand, ('Queen', 'Clubs', 'Black', 12))
        add_card_to_hand(hand, ('Ace', 'Clubs', 'Black', 14))
        # take a turn
        card = take_player1_turn(hand, 'Clubs')
        # check that the card is (Ace, Clubs, Black, 14)
        self.assertEqual(card, ('Ace', 'Clubs', 'Black', 14))
    # write unit test for take_player2_turn
    def test_take_player2_turn(self):
        # create a hand
        hand = create_hand()
        add_card_to_hand(hand, ('Jack', 'Clubs', 'Black', 11))
        add_card_to_hand(hand, ('Ten', 'Clubs', 'Black', 10))
        add_card_to_hand(hand, ('King', 'Clubs', 'Black', 13))
        add_card_to_hand(hand, ('Queen', 'Clubs', 'Black', 12))
        add_card_to_hand(hand, ('Ace', 'Clubs', 'Black', 14))
        # take a turn
        card = take_player2_turn(hand, 'Clubs')
        # check that the card is (Ace, Clubs, Black, 14)
        self.assertEqual(card, ('Ace', 'Clubs', 'Black', 14))

if __name__ == '__main__':
    unittest.main()