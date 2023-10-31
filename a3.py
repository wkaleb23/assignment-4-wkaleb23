import random

## These constants have been defined as a starting point.
## You may find yourself wanting to define things a little differently for your
##  implementation. That's fine.
NUM_CARDS_IN_HAND = 5
NUM_CARDS_IN_DECK = 24

# Changed this so that it would be easier to create a deck
SUIT_NAMES = ["Clubs", "Spades", "Hearts", "Diamonds"]
SUIT_COLORS = ["Black", "Black", "Red", "Red"]
FACES = ["Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace"]
NUMBERED = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]


## card is a tuple of (name, suit, color, value)
## deck is a list structured as a stack
## card_node is a dict of {next_card, prev_card, payload}
## hand is a linked list, represented by a dict of {first_card, num_cards_in_hand}

# ----------------------------------------
#  Deck functions
# ---------------------------------------
#  Assume that the value of cards are:
#  Nine=9; Ten=10; Jack=11; and so on, up to Ace=14.

# shuffles the deck, returns a pointer to the deck
# added this function to help in create a deck
def shuffle_deck(deck):
    for i in range(0, 7):
        random.shuffle(deck)
    return deck


# determines if the specified card is in the deck, returns 0 if the card is not in the deck, 1 otherwise
# added this to help for deck functions (we don't want to duplicate cards)
def is_card_in_deck(deck, card):
    for i in range(0, len(deck)):
        if deck[i] == card:
            return 1
    return 0


# Creates the deck, initializing any fields necessary.
# Returns a deck.
def create_deck():
    deck = []
    for s in range(0, 4):
        suit = SUIT_NAMES[s]
        suit_color = SUIT_COLORS[s]
        for i in range(0, 13):
            card = (FACES[i], suit, suit_color, NUMBERED[i])
            deck.append(card)
    deck = shuffle_deck(deck)
    return deck


# Adds a card to the top of the deck.
# Returns a pointer to the deck.
# added checks to see if deck is full or if card is already in deck
def push_card_to_deck(deck, card):
    if is_card_in_deck(deck, card) == 1:
        print("Card is already in deck")
        return deck
    # check that the deck is not full
    if len(deck) == NUM_CARDS_IN_DECK:
        print("Deck is full")
        return deck
    # add the card to the top of the deck
    deck.append(card)
    # return a pointer to the deck
    return deck


# Shows the top card, but does not remove it from the stack.
# Returns a pointer to the top card.
def peek_card(deck):
    return deck[-1]


# Removes the top card from the deck and returns it.
# Returns a pointer to the top card in the deck.
def pop_card(deck):
    return deck.pop(0)


# Determines if the deck is empty.
# Returns 0 if the Deck has any cards; 1 otherwise.
def is_deck_empty(deck):
    if len(deck) == 0:
        return 1
    else:
        return 0


## Prints the provided deck
def print_deck(deck):
    print(deck)


# ----------------------------------------
# Hand functions
# ----------------------------------------

## A Hand is a linked list, so we define Card_Nodes before
## defining the Hand
def create_card_node(card):
    card_node = {'next': None, 'prev': None, 'payload': card}
    return card_node


def get_next_card_node(card_node):
    return card_node['next']


def get_prev_card_node(card_node):
    return card_node['prev']


def get_card_from_node(card_node):
    return card_node['payload']


# Creates a Hand and initializes any necessary fields.
# Returns a new empty hand
def create_hand():
    hand = {'first_card': None, 'num_cards_in_hand': 0}
    return hand


# Adds a card to the hand.
# Added checks to see if hand is full
def add_card_to_hand(hand, card):
    # Only add a card if the hand is not full
    if hand['num_cards_in_hand'] == NUM_CARDS_IN_HAND:
        print("Hand is full")
    else:
        hand['num_cards_in_hand'] += 1
        card_node = create_card_node(card)
        if hand['first_card'] is None:
            # if the hand is empty, add the card to the hand
            hand['first_card'] = card_node
        else:
            # if the hand is not empty, add the card to the beginning of the hand
            card_node['next'] = hand['first_card']
            hand['first_card']['prev'] = card_node
            hand['first_card'] = card_node


# Removes a card from the hand via card value
# Returns the card (not a card_node) that was removed from the hand
# Returns None if the specified card is not in the hand
def remove_card_from_hand(hand, card):
    card_node = hand['first_card']
    # loop through all cards through linked list
    while card_node is not None:
        if card_node['payload'] == card:
            hand['num_cards_in_hand'] -= 1
            if card_node['prev'] is not None:
                card_node['prev']['next'] = card_node['next']
            if card_node['next'] is not None:
                card_node['next']['prev'] = card_node['prev']
            if card_node == hand['first_card']:
                hand['first_card'] = card_node['next']
            return get_card_from_node(card_node)
        card_node = card_node['next']
    return None


# determines if the specified card is in the hand, returns 0 if the card is not in the hand, 1 otherwise
# added this function since it existed in tests
def is_card_in_hand(hand, card):
    card_node = hand['first_card']
    # loop through all cards through linked list
    while card_node is not None:
        if card_node['payload'] == card:
            return 1
        card_node = card_node['next']
    return 0


# Removes a card from the hand via index
# Returns the card, not a card_node
# Returns None if index is < 0 or greater than the length of the hand/list.
def get_card_from_hand(hand, index):
    card_node = hand['first_card']
    if index < 0 or index > hand['num_cards_in_hand']:
        return None
    for i in range(0, index):
        card_node = card_node['next']
    return get_card_from_node(card_node)


# Determines if there are any cards in the hand.
# Return 0 if the hand is empty; 1 otherwise.
def is_hand_empty(hand):
    if hand['num_cards_in_hand'] == 0:
        return 0
    else:
        return 1


# Prints a single card
def print_card(card):
    print(card)


# Prints an entire hand
def print_hand(hand):
    card_node = hand['first_card']
    while card_node is not None:
        print_card(get_card_from_node(card_node))
        card_node = card_node['next']
