
from globals import config
from game_functionalities import functionalities





# Initializes player's chips (starting with 100 chips by default)
chips = functionalities.Chips()


while True:		# Central loop of the game

	config.playing = True

	# Creates and initializes a full shufled deck
	deck = functionalities.Deck()
	deck.shuffle()

	# Takes a bet from the player
	chips.bet = functionalities.take_bet(chips)

	# Initializes both the dealer's and the player's hand
	dealer_hand = functionalities.Hand()
	player_hand = functionalities.Hand()

	# Deals two cards to both the player and the dealer and displays them
	dealer_hand.add_card(deck.deal())
	dealer_hand.add_card(deck.deal())

	player_hand.add_card(deck.deal())
	player_hand.add_card(deck.deal())

	functionalities.show_some(player_hand, dealer_hand)


	# Start with a player's hand
	while config.playing:

		functionalities.hit_or_stand(deck, player_hand)

		functionalities.show_some(player_hand, dealer_hand)
		print("New player's hand value is {}".format(player_hand.value))

		# If player's hand exceeds 21, this hand ends with the player losing
		if player_hand.value > 21:
			break


	# If Player hasn't busted, play dealer's hand until dealer reaches 17
	while True:

		functionalities.hit(deck, dealer_hand)

		# Prints the dealer's hand value excluding the hidden card
		dealer_hand_value_without = dealer_hand.value - config.values[dealer_hand.cards[0].rank]
		print("New dealer's hand value is {}".format(dealer_hand_value_without))

		if dealer_hand_value_without >= 17:
			break

	# Show all hands, including dealer's first
	functionalities.show_all(player_hand, dealer_hand)


	# Run different winning scenarios
	if player_hand.value > 21:
		functionalities.player_busts(chips)
	elif dealer_hand.value > 21:
		functionalities.dealer_busts(chips)
	else:
		if player_hand.value > dealer_hand.value:
			functionalities.player_wins(chips)
		else:
			functionalities.dealer_wins(chips)


	# Asks the player if he wishes to play again
	player_choice = input("Do you want play again: ")

	while True:
		if player_choice == "yes":
			break
		elif player_choice == "no":
			break
		else:
			print("Wrong input, please type your choice again")
			continue

	if player_choice == "yes":
		continue	# Place a new bet and play again
	else:
		break 	# Exit the game
