# to do: implement a betting system
# map out the rules of the game

import random

# global variables
deck_of_cards = range(1, 53)
card_sum = 0

# functions
def shuffle_deck():
	random.shuffle(deck_of_cards)

def new_card():
	return deck_of_cards.pop()

def name(x):
	# conditional to determine the card number
	if x % 13 == 1:
		name = "Ace"
	elif x % 13 == 11:
		name = "Jack"
	elif x % 13 == 12:
		name = "Queen"
	elif x % 13 == 0:
		name = "King"
	elif x % 13 > 1 and x % 13 < 11:
		name = str(x % 13)
	else:
		return False
	return name

def suit(x):
	# conditional to determine the card suit
	if x <= 13:
		suit = "Hearts"
	elif x > 13 and x <= 26:
		suit = "Diamonds"
	elif x > 26 and x <= 39:
		suit = "Clubs"
	elif x > 39 and x <= 52:
		suit = "Spades"
	else:
		return False
	return suit

def value(x):
	# conditional to determine the card value
	if x % 13 == 1:
		if card_sum > 10:
			value = 1
		elif card_sum < 11:
			value = 11
	elif x % 13 == 11:
		value = 10
	elif x % 13 == 12:
		value = 10
	elif x % 13 == 0:
		value = 10
	elif x % 13 > 1 and x % 13 < 11:
		value = x % 13
	else:
		return False
	return value