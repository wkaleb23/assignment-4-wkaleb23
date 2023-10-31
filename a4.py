from a3 import *

#----------------------------------------
# Game functions
#----------------------------------------

# Shuffle the deck.
# Put them in a random order.
# Please note: this should not create a new deck or cards in a different order;
# It should move the existing cards around in the existing deck.
def shuffle(deck):
	pass

# Given a deck (assume that it is already shuffled),
# take the top card from the deck and alternately give
# it to player 1 and player 2, until they both have
# NUM_DECKS_IN_HAND.
def deal(deck, p1_hand, p2_hand):
	pass

# Given a lead card, a players hand, and the card the player wants
# to play, is it legal?
# If the player has a card of the same suit as the lead_card, they
# must play a card of the same suit.
# If the player does not have a card of the same suit, they can
# play any card.
def is_legal_move(hand, lead_card, played_card):
	pass

# Given two cards that are played in a hand, which one wins?
# If the suits are the same, the higher card value wins.
# If the suits are not the same, player 1 wins, unless player 2 played trump.
# Returns True if the person who lead won, False if the person who followed won.
def who_won(lead_card, followed_card, trump):
	pass

# Take all the cards out of a given hand, and put them
# back into the deck.
def return_hand_to_deck(hand, deck):
	pass

# Sort the given hand in descending order of power.
# For full credit, implement your own sort algorithm (e.g. Selection Sort).
# Using Python's built-in "sort()" functionality will earn you max 25% credit
#
# The sort order should be: all cards of the given trump suit should
# be the "highest", and A high down to 9;
# The other suits can be in random order, but the card values must go
# from high to low.
def sort_hand(hand, trump):
	pass

# Given the player1 hand, play a card.
# Player 1 is always the computer.
# This function should choose a card from the hand,
# remove it from the hand, print out a message
# saying what card was played, and return the played card.
# I recommend beginning with choosing the card in a very simple
# manner: just remove/return the first card in the hand, regardless
# if it's a "good" card or not.
def take_player1_turn(hand, trump):
	pass

# Given the player2 hand, play a card.
# Player 2 is always a human.
# This function should prompt the user to choose a card to play.
# It probably should print out the cards that are available to play.
# Once the human player chooses,
# remove it from the hand, print a message
# saying what card was played, and return the played card.
# This function does not have to enforce that a valid card is chosen.
def take_player2_turn(hand, trump):
	pass

## Helper function to return the Suit of a given card
def get_card_suit(card):
	pass