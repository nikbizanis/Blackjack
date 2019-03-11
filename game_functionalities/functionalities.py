
# Contains the main classes and functionalities of the blackjack game
from globals import config
import random




class Card:

	def __init__(self, rank, suit):
		self.suit = suit
		self.rank = rank


	def __str__(self):
		return "{} of {}".format(self.rank, self.suit)


	def value(self):
	# Takes a card as input and computes its numerical value for the game
		return config.values[self.rank]



class Deck:

	def __init__(self):
	# Start with an empty deck list and populate it

		self.deck = []

		for suit in config.suits:
			for rank in config.ranks:
				card = Card(rank, suit)
				self.deck.append(card)


	def __str__(self):
	# Method to print the deck when requested
		return "[%s]" % ", ".join(map(str, self.deck))


	def shuffle(self):
		random.shuffle(self.deck)


	def deal(self):
	# Deals a card from the deck
		return self.deck.pop()



class Hand:

	def __init__(self):

		self.cards = []  	# Start with an empty list as we did in the Deck class
		self.value = 0
		self.aces = 0    	# Add an attribute to keep track of aces


	def __str__(self):
	# Method to print the hand when requested

		return "[%s]" % ", ".join(map(str, self.cards))


	def add_card(self, card):
	# Adds a card to the hand and updates the hand's value

		self.cards.append(card)
		self.value += card.value()

		if card.rank == "Ace":
			self.aces += 1


	def adjust_for_ace(self):
		# Ace may count for 1 or 11 points, in order to avoid busting

		if (self.value > 21) and (self.aces > 0):
			self.value -= 10
			self.aces -= 1



class Chips:

	def __init__(self):
	# Player starts with 100 chips by default

		self.total = 100
		self.bet = 0


	def return_total(self):

		return self.total


	def reduce_amount(self):

		self.total -= self.bet
		print("New chips total is {}\n".format(self.total))


	def increase_amount(self):

		self.total += self.bet
		print("New chips total is {}\n".format(self.total))




def take_bet(chips):

    # Prompts the user to take a bet and performs the necessary checks
	while True:
		try:
			bet = input("Please place a bet: ")
			bet = int(bet)
		except ValueError:
			print("You must provide an integer number")
			continue

		# Checks if player has adequate funds to place this bet
		if (chips.return_total() - bet) < 0:
			print("You don't have enough chips to place this bet. Please place a lower bet")
			continue
		else:
			break

	return bet



def show_some(player_hand, dealer_hand):
# Displays all of the dealer's cards except the first and all of the player's cards

	print("Dealer Cards:")
	for card in dealer_hand.cards[1:]:
		print(card)

	print("\nPlayer Cards:")
	for card in player_hand.cards:
		print(card)



def show_all(player_hand, dealer_hand):
# Displays all of the cards at the end of a hand

	print("Dealer Cards:")
	for card in dealer_hand.cards:
		print(card)

	print("\nPlayer Cards:")
	for card in player_hand.cards:
		print(card)



def hit(deck, hand):
# It deals one card off the deck and adds it at the current hand. Then computes the new value of the hand

	hand.add_card(deck.deck.pop())

	hand.adjust_for_ace()




def hit_or_stand(deck, player_hand):
# Prompts the player to hit or stand and takes his hit if applicable

	#global config.playing  	# To control an upcoming while loop in the main body of the game

	# Asks the player if they wish to hit or stand and take his input
	player_choice = input("Do you want to hit or stand: ")

	while True:
		if player_choice == "hit":
			break
		elif player_choice == "stand":
			break
		else:
			print("Wrong input, please type your choice again")
			continue

	if player_choice == "hit":
		hit(deck, player_hand)
	else:
		print("Player stands. Dealer's turn: ")
		config.playing = False



def player_busts(chips):
# If a player is bust it informs the players and settles the game

	print("The player is bust!")

	dealer_wins(chips)



def dealer_busts(chips):
# If the dealer is bust it informs the players and settles the game

	print("The dealer is bust!")

	player_wins(chips)



def player_wins(chips):
# Settles the bets in case the player won the hand

	chips.increase_amount()



def dealer_wins(chips):
# Settles the bets in case the player won the hand

	chips.reduce_amount()
