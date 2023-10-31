import sys
import unittest
from a3 import *


class AllTests(unittest.TestCase):

    def test_push_card_to_deck(self):
        # test that you can't add a card to a full deck, or a card that is already in the deck
        ## Set up
        deck = create_deck()
        card = ("jack", "hearts", 11)
        fake_card = ("test", "hearts", 16)
        ## Execute the thing to test
        full_deck = push_card_to_deck(deck, fake_card)
        removed_card = pop_card(deck)
        card_already_in_deck = push_card_to_deck(deck, card)
        add_card = push_card_to_deck(deck, removed_card)
        ## Evaluate the result for correctness
        assert full_deck is deck, "Deck should be full"
        assert card_already_in_deck is deck, "Card should already be in deck"
        assert add_card is deck, "Card should be added to deck"
        print("push_card_to_deck_test passed")

    def test_create_deck(self):
        deck = create_deck()
        print_deck(deck)
        print("Create deck test passed")

    def test_create_card_node(self):
        card_node = create_card_node("my_payload")
        ## Because this is a unit test for "create_card_node()",
        ##  I'm willing to "break the abstraction" to make sure
        ##  it's correct
        if card_node['payload'] != 'my_payload':
            print("Test failed-- wrong payload")
        if card_node['prev'] is not None:
            print("Test failed-- wrong prev node")
        if card_node['next'] is not None:
            print("Test failed-- wrong next node")
        print("Create card_node test passed")

    def test_card_node_next(self):
        print("Create card_node_next test by-passed")

    def test_create_hand(self):
        hand = create_hand()
        assert hand['first_card'] is None, "First card is not None when it should be"
        assert hand['num_cards_in_hand'] == 0, "num_cards_in_hand is not 0 when it should be"
        print("create_hand_test passed")

    def test_add_1card_to_hand(self):
        ## Set up
        hand = create_hand()
        card = ("jack", "hearts", 10)
        ## Execute the thing to test
        add_card_to_hand(hand, card)
        ## Evaluate the result for correctness
        assert hand['num_cards_in_hand'] == 1, "num_cards_in_hand should be 1"
        assert get_card_from_node(
            hand['first_card']) is card, 'The first card is not the right one'
        print("add_card_to_hand_test passed")

    def test_add_2cards_to_hand(self):
        ## Set up
        hand = create_hand()
        card = ("jack", "hearts", 11)
        card2 = ("queen", "hearts", 12)
        ## Execute the thing to test
        add_card_to_hand(hand, card)
        add_card_to_hand(hand, card2)
        ## Evaluate the result for correctness
        assert hand['num_cards_in_hand'] == 2, "num_cards_in_hand should be 2"
        assert is_card_in_hand(hand, card), "Card 1 is not in hand but should be"
        assert is_card_in_hand(hand, card2), "Card 2 is not in hand but should be"
        assert get_card_from_node(hand['first_card']) is card2, "Card2 is not the first card in the hand, but should be"
        print("add_2card_to_hand_test passed")

    def test_remove_first_card_from_hand(self):
        ## Set up
        hand = create_hand()
        card = ("jack", "hearts", 11)
        card2 = ("queen", "hearts", 12)
        add_card_to_hand(hand, card)
        add_card_to_hand(hand, card2)
        ## Execute the thing to test
        removed_card = remove_card_from_hand(hand, card)
        ## Evaluate the result for correctness
        assert hand['num_cards_in_hand'] == 1, "num_cards_in_hand should be 1"
        assert not is_card_in_hand(hand, card), "Card 1 is in hand but should not be"
        assert is_card_in_hand(hand, card2), "Card 2 is not in hand but should be"
        assert removed_card is card, "Card was not returned but should be"
        assert get_card_from_node(hand['first_card']) is card2, "Card 2 is not the first element but should be"
        print("remove_first_card_from_hand_test passed")

    def test_remove_last_card_from_hand(self):
        ## Set up
        hand = create_hand()
        card = ("jack", "hearts", 11)
        card2 = ("queen", "hearts", 12)
        add_card_to_hand(hand, card)
        add_card_to_hand(hand, card2)
        ## Execute the thing to test
        removed_card = remove_card_from_hand(hand, card2)
        ## Evaluate the result for correctness
        assert hand['num_cards_in_hand'] == 1, "num_cards_in_hand should be 1"
        assert not is_card_in_hand(hand, card2), "Card 2 is in hand but should not be"
        assert is_card_in_hand(hand, card), "Card 1 is not in hand but should be"
        assert removed_card is card2, "Card was not returned but should be"
        assert get_card_from_node(hand['first_card']) is card, "Card 1 is not the first element but should be"
        print("remove_last_card_from_hand_test passed")

    def test_check_full_hand(self):
        # try to add a card to a full hand
        ## Set up
        hand = create_hand()
        # add 5 cards to the hand
        card = ("jack", "hearts", 11)
        card2 = ("queen", "hearts", 12)
        card3 = ("king", "hearts", 13)
        card4 = ("ace", "hearts", 14)
        card5 = ("2", "hearts", 2)
        card6 = ("3", "hearts", 3)
        add_card_to_hand(hand, card)
        add_card_to_hand(hand, card2)
        add_card_to_hand(hand, card3)
        add_card_to_hand(hand, card4)
        add_card_to_hand(hand, card5)
        ## Execute the thing to test
        add_card_to_hand(hand, card6)
        ## Evaluate the result for correctness
        assert hand['num_cards_in_hand'] == 5, "num_cards_in_hand should be 5"
        assert not is_card_in_hand(hand, card6), "Card 6 is should not be in hand"
        print("check_full_hand_test passed")


    # def main(self):
    #     test_create_deck()
    #     test_create_card_node()
    #     test_card_node_next()
    #     test_create_hand()
    #     test_add_1card_to_hand()
    #     test_add_2cards_to_hand()
    #     test_remove_first_card_from_hand()
    #     test_remove_last_card_from_hand()
    #     test_check_full_hand()
    #     test_push_card_to_deck()


if __name__ == '__main__':
    unittest.main()

# terminal command to run main() in a3_test.py:
# python3 a3_test.py
