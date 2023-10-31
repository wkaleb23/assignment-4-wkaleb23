from a3 import *
# ----------------------------------------
# Game functions
# ----------------------------------------
# Shuffle the deck.
# Put them in a random order.
# Please note: this should not create a new deck or cards in a different order;
# It should move the existing cards around in the existing deck.

def shuffle(deck):
    for i in range(0, 7):
        random.shuffle(deck)
    return deck


# Given a deck (assume that it is already shuffled),
# take the top card from the deck and alternately give
# it to player 1 and player 2, until they both have
# NUM_DECKS_IN_HAND.
def deal(deck, p1_hand, p2_hand):
    # deal the cards to the players
    for i in range(0, NUM_CARDS_IN_HAND):
        card1 = pop_card(deck)
        card2 = pop_card(deck)
        add_card_to_hand(p1_hand, card1)
        add_card_to_hand(p2_hand, card2)
    return deck, p1_hand, p2_hand

# Given a lead card, a players hand, and the card the player wants
# to play, is it legal?
# If the player has a card of the same suit as the lead_card, they
# must play a card of the same suit.
# If the player does not have a card of the same suit, they can
# play any card.
def is_legal_move(hand, lead_card, played_card):
    # loop through the hand
    if get_card_suit(lead_card) == get_card_suit(played_card):
        return True
    else:
        current_card = get_card_from_hand(hand, 0)
        while current_card is not None:
            card = get_card_from_node(current_card)
            # check if the player has a card of the same suit as the lead card
            if get_card_suit(card) == get_card_suit(lead_card):
                # the player has a card of the same suit as the lead card
                # check if the played card is of the same suit as the lead card
                return False
            # check the next card in the hand
            current_card = current_card['next']
    return True

# Given two cards that are played in a hand, which one wins?
# If the suits are the same, the higher card value wins.
# If the suits are not the same, player 1 wins, unless player 2 played trump.
# Returns True if the person who lead won, False if the person who followed won.
def who_won(lead_card, followed_card, trump):
    # If the suits are the same, the higher card value wins.
    if get_card_suit(lead_card) == get_card_suit(followed_card):
        # the suits are the same
        if lead_card[3] > followed_card[3]:
            # the lead card has a higher value
            return True
        else:
            # the followed card has a higher value
            return False
    # If the suits are not the same, player 1 wins, unless player 2 played trump.
    else:
        if get_card_suit(followed_card) == trump:
            # player 2 played trump
            return False
        else:
            # player 1 wins
            return True


# Take all the cards out of a given hand, and put them
# back into the deck.
def return_hand_to_deck(hand, deck):
    # loop through the hand and get first card, then add it to the deck
    while hand['first_card'] is not None:
        card = remove_first_card_from_hand(hand)
        push_card_to_deck(deck, card)

# Sort the given hand in descending order of power.
# For full credit, implement your own sort algorithm (e.g. Selection Sort).
# Using Python's built-in "sort()" functionality will earn you max 25% credit
#
# The sort order should be: all cards of the given trump suit should
# be the "highest", and A high down to 9;
# The other suits can be in random order, but the card values must go
# from high to low.
def sort_hand(hand, trump):
    # loop through the hand and order the cards
    ordered_list = []
    for i in range(0, hand['num_cards_in_hand']):
        card = remove_first_card_from_hand(hand)
        # loop through the ordered list and insert the card in the correct position
        if len(ordered_list) == 0:
            ordered_list.append(card)
            continue
        else:
            for j in range(0, len(ordered_list)):
                ordered_card_current = ordered_list[j]
                # use who_won to determine if the card is higher or lower than the current card
                if who_won(card, ordered_card_current, trump) == True:
                    # the card is higher than the current card
                    ordered_list.insert(j, card)
                    break
                else:
                    # the card is lower than the current card
                    if j == len(ordered_list) - 1:
                        # the card is lower than all the cards in the ordered list
                        ordered_list.append(card)
                        break
                    else:
                        continue
    new_hand = create_hand()
    # add the cards back to the hand in reverse order
    t = len(ordered_list) - 1
    for i in range(0, len(ordered_list)):
        card = ordered_list[t]
        add_card_to_hand(new_hand, card)
        t -= 1
    hand = new_hand
    return hand

# Given the player1 hand, play a card.
# Player 1 is always the computer.
# This function should choose a card from the hand,
# remove it from the hand, print out a message
# saying what card was played, and return the played card.
# I recommend beginning with choosing the card in a very simple
# manner: just remove/return the first card in the hand, regardless
# if it's a "good" card or not.
def take_player1_turn(hand, trump):
    hand = sort_hand(hand, trump)
    card = remove_first_card_from_hand(hand)
    print("Player 1 played: ")
    print_card(card)
    return card

# Given the player2 hand, play a card.
# Player 2 is always a human.
# This function should prompt the user to choose a card to play.
# It probably should print out the cards that are available to play.
# Once the human player chooses,
# remove it from the hand, print a message
# saying what card was played, and return the played card.
# This function does not have to enforce that a valid card is chosen.
def take_player2_turn(hand, trump):
    hand = sort_hand(hand, trump)
    print("Player 2's hand: ")
    print_hand(hand)
    # prompt the user to choose a card to play
    card_number = input("Choose a card to play: ")
    card_number = int(card_number)
    card = get_card_from_hand(hand, card_number - 1)
    card = get_card_from_node(card)
    card = remove_card_from_hand(hand, card)
    print("Player 2 played: ")
    print_card(card)
    return card

## Helper function to return the Suit of a given card
def get_card_suit(card):
    # card is a tuple of (name, suit, color, value)
    return card[1]