import sys
from a3 import *


def create_deck_test():
    deck = create_deck()
    print_deck(deck)
    print("Create deck test passed")


def create_card_node_test():
    card_node = create_card_node("my_payload")
    ## Because this is a unit test for "create_card_node()",
    ##  I'm willing to "break the abstraction" to make sure
    ##  it's correct
    if (card_node['payload'] != 'my_payload'):
        print("Test failed-- wrong payload")
    if card_node['prev'] is not None:
        print("Test failed-- wrong prev node")
    if card_node['next'] is not None:
        print("Test failed-- wrong next node")

    print("Create card_node test passed")


def card_node_next_test():
    print("Create card_node_next test by-passed")


def create_hand_test():
    hand = create_hand()
    assert hand['first_card'] is None, "First card is not None when it should be"
    assert hand['num_cards_in_hand'] == 0, "num_cards_in_hand is not 0 when it should be"
    print("create_hand_test passed")


def add_1card_to_hand_test():
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


def add_2cards_to_hand_test():
    ## Set up
    hand = create_hand()
    card = ("Jack", "Hearts", "Red", 11)
    card2 = ("Queen", "Hearts", "Red", 12)

    ## Execute the thing to test
    add_card_to_hand(hand, card)
    add_card_to_hand(hand, card2)

    ## Evaluate the result for correctness
    assert hand['num_cards_in_hand'] == 2, "num_cards_in_hand should be 2"
    assert is_card_in_hand(hand, card), "Card 1 is not in hand but should be"
    assert is_card_in_hand(hand, card2), "Card 2 is not in hand but should be"
    assert get_card_from_node(hand['first_card']) is card2, "Card2 is not the first card in the hand, but should be"
    print("add_2card_to_hand_test passed")


def remove_first_card_from_hand_test():
    ## Set up
    hand = create_hand()
    card = ("Jack", "Hearts", "Red", 11)
    card2 = ("Queen", "Hearts", "Red", 12)
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


# also checking that we can remove a card from the middle or end of hand
def remove_any_card_from_hand_test():
    ## Set up
    hand = create_hand()
    card = ("Jack", "Hearts", "Red", 11)
    card2 = ("Queen", "Hearts", "Red", 12)
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


# Added tests for checking that we can't go over the full hand limit
def check_full_hand_test():
    # try to add a card to a full hand
    ## Set up
    hand = create_hand()
    # add 5 cards to the hand
    card = ("Jack", "Hearts", "Red", 11)
    card2 = ("Queen", "Hearts", "Red", 12)
    card3 = ("Kind", "Hearts", "Red", 13)
    card4 = ("Ace", "Hearts", "Red", 14)
    card5 = ("Two", "Hearts", "Red", 2)
    card6 = ("Three", "Hearts", "Red", 3)
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


# Adding tests for some of the basic deck functions
def deck_functions_test():
    # test the functions peek_card, pop_card, is_deck_empty
    ## Set up
    deck = create_deck()

    ## Execute the thing to test
    top_card_peek = peek_card(deck)
    top_card_pop = pop_card(deck)
    is_empty = is_deck_empty(deck)

    ## Evaluate the result for correctness
    assert top_card_peek == top_card_pop, "Top card should be the same"
    assert is_empty == 0, "Deck should not be empty"

    print("deck_functions_test passed")


# adding tests for the exceptions in the push_card_to_deck
def push_card_to_deck_test():
    # test that you can't add a card to a full deck, or a card that is already in the deck
    ## Set up
    deck = create_deck()
    card = ("Jack", "Hearts", "Red", 11)
    fake_card = ("Test", "Hearts", "Red", 12)

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


# Add to main the new tests
def main():
    create_deck_test()
    create_card_node_test()
    card_node_next_test()
    create_hand_test()
    add_1card_to_hand_test()
    add_2cards_to_hand_test()
    remove_first_card_from_hand_test()
    remove_any_card_from_hand_test()
    check_full_hand_test()
    push_card_to_deck_test()


if __name__ == '__main__':
    sys.exit(main())
