import random

# global variables
deck_of_cards = range(1, 53)

#TO DO: going to keep track in case of Aces, will append to list and clear at the end of round.
#playerpulled = []
#dealerpulled = []

playersum = 0
dealersum = 0
dhiddencard = ""

# randomizes the list - KEEP
def shuffle_deck():
	random.shuffle(deck_of_cards)

# pulls a new card from the deck
def draw():
	return deck_of_cards.pop()

# determines the card name & suit - KEEP
def name_suit(x):
	if x % 13 == 1:
		name = "an Ace"
	elif x % 13 == 11:
		name = "a Jack"
	elif x % 13 == 12:
		name = "a Queen"
	elif x % 13 == 0:
		name = "a King"
	elif x % 13 > 1 and x % 13 < 11:
		if x % 13 == 8:
			name = "an " + str(x % 13)
		else:
			name = "a " + str(x % 13)
	else:
		return False

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

	return name + " of " + suit 

# determines the value of the card - KEEP
def value(x):
	global dealersum
	global playersum

	if x % 13 == 1:
		if dealersum > 10:
			value = 1
		elif dealersum < 11:
			value = 11
		if playersum == True:
			def pchoice():
				pchoice = raw_input("choose value: 1 or 11")
				if pchoice == 1:
					value = 1
				elif pchoice == 11:
					value = 11
				else:
					pchoice()
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

def initial_deal():
	global dealersum
	global playersum
	global dhiddencard

	pcard1 = draw()
	pcard2 = draw()
	dcard1 = draw()
	dcard2 = draw()

	playersum = value(pcard1) + value(pcard2)
	dealersum = value(dcard1) + value(dcard2)
	dealervisiblesum = value(dcard1)
	dhiddencard = name_suit(dcard2)

	# player hand
	print "You have been dealt " + name_suit(pcard1) + " and " + name_suit(pcard2) + " for a sum of " + str(playersum) + "."

	# dealer hand
	print "The dealer has drawn " + name_suit(dcard1)

	if dealersum == 21 and playersum == 21:
		print "and " + name_suit(dcard2)
		print "Dealer has a final sum of " + str(dealersum)
		print "You have a final sum of " + str(playersum)
		print "Push"
	elif dealersum == 21 and playersum != 21:
		print "and " + name_suit(dcard2)
		print "Dealer has a final sum of " + str(dealersum)
		print "You have a final sum of " + str(playersum)
		print "Dealer has blackjack"
	elif dealersum != 21 and playersum == 21:
		print "and " + name_suit(dcard2)
		print "Dealer has a final sum of " + str(dealersum)
		print "You have a final sum of " + str(playersum)
		print "You have blackjack!"
	elif dealersum != 21 and playersum != 21:
		print "The dealer's second card is hidden"
		print "Dealer has a visible sum of " + str(dealervisiblesum)
		nextdeal()
	else:
		return False

# defines the players hand before moving forward
def nextdeal():
	global dealersum
	global playersum
	global dhiddencard
	
	if playersum < 21:
		hit_or_stay = raw_input("Do you want to hit or stay? (hit/stay) ").lower()
		if playersum == 21:
			print "Your card sum is 21."
			stay()
		else:
			if hit_or_stay == "stay":
				stay()
			elif hit_or_stay == "hit":
				drawncard = draw()
				cardvalue = value(drawncard) 
				playersum += cardvalue
				print "You have drawn " + name_suit(drawncard)
				print "Which brings the card sum to " + str(playersum)
				nextdeal()
			else:
				print "That is not a valid answer."
				nextdeal()
	elif playersum > 21:
		print "The dealer's hidden card was a " + dhiddencard
		print "Dealer has a final sum of " + str(dealersum)
		print "Dealer wins"
	else:
		stay()


# if player chooses to stay - KEEP
def stay():
	global playersum
	global dealersum
	global dhiddencard

	if dealersum < 17:
		print "The dealer's hidden card was a " + dhiddencard + " bringing their sum to " + str(dealersum) 
		dealerhand()
	elif dealerhand > 16:
		if dealersum == playersum:
			print "The dealer's hidden card was a " + dhiddencard
			print "Dealer has a final sum of " + str(dealersum)
			print "You have a final sum of " + str(playersum)
			print "Push"
		elif dealersum > playersum and dealersum < 22:
			print "The dealer's hidden card was a " + dhiddencard
			print "Dealer has a final sum of " + str(dealersum)
			print "You have a final sum of " + str(playersum)
			print "Dealer wins"
		elif dealersum > 21:
			print "The dealer's hidden card was a " + dhiddencard
			print "Dealer has a final sum of " + str(dealersum)
			print "You have a final sum of " + str(playersum)
			print "You won!"
		elif dealersum < playersum:
			print "The dealer's hidden card was a " + dhiddencard
			print "Dealer has a final sum of " + str(dealersum)
			print "You have a final sum of " + str(playersum)
			print "You won!"
	else:
		return False

# dealer hand - KEEP
def dealerhand():
	global playersum
	global dealersum

	if playersum < 22 and dealersum < 17:
		drawncard = draw()
		cardvalue = value(drawncard) 
		dealersum += cardvalue
		print "The dealer has drawn " + name_suit(drawncard)
		print "Which brings their card sum to " + str(dealersum)
		dealerhand()
	elif dealersum > 16 and dealersum <= 21 and playersum < 22:
		if dealersum == 21:
			if playersum == 21:
				print "You have a final sum of " + str(playersum)
				print "Push"
			else:
				print "You have a final sum of " + str(playersum)
				print "Dealer wins"
		elif dealersum == playersum:
			print "You have a final sum of " + str(playersum)
			print "Push"
		elif dealersum > playersum:
			print "You have a final sum of " + str(playersum)
			print "Dealer wins"
		elif dealersum < playersum:
			print "You have a final sum of " + str(playersum)
			print "You won!"
	elif playersum > 21:
		print "You have a final sum of " + str(playersum)
		print "Dealer wins"
	elif dealersum > 21 and playersum < 22:
		print "You have a final sum of " + str(playersum)
		print "You won!"
	else:
		return False

shuffle_deck()
initial_deal()
